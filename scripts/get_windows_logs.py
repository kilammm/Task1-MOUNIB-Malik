import win32evtlog
import pandas as pd
import os

def get_logs_from_source(log_type, max_events=200):
    server = "localhost"
    try:
        hand = win32evtlog.OpenEventLog(server, log_type)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

        records = []
        while len(records) < max_events:
            events = win32evtlog.ReadEventLog(hand, flags, 0)
            if not events:
                break
            for event in events:
                records.append({
                    "timestamp": event.TimeGenerated.Format(),
                    "level": str(event.EventType),
                    "source": event.SourceName,
                    "log_type": log_type,
                    "event_id": event.EventID,
                    "event": str(event.StringInserts)
                })
                if len(records) >= max_events:
                    break

        win32evtlog.CloseEventLog(hand)
        print(f"✅ {len(records)} events retrieved from [{log_type}]")
        return records

    except Exception as e:
        print(f"❌ Unable to read [{log_type}] : {e}")
        return []

def save_logs(all_records):
    os.makedirs("../Logs", exist_ok=True)
    output_path = "../Logs/system.log"

    df = pd.DataFrame(all_records)

    type_map = {
        "1": "ERROR",
        "2": "WARNING",
        "4": "INFO",
        "8": "SUCCESS",
        "16": "CRITICAL"
    }
    df["level"] = df["level"].map(type_map).fillna("INFO")
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    with open(output_path, "w", encoding="utf-8") as f:
        for _, row in df.iterrows():
            line = (
                f"{row['timestamp'].strftime('%Y-%m-%d %H:%M:%S')} "
                f"{row['level']} "
                f"[{row['source']}] "
                f"[{row['log_type']}] "
                f"{row['event']}\n"
            )
            f.write(line)

    print(f"\n📁 system.log saved in Logs/ with {len(df)} events")

    print("\n📊 Summary by source:")
    print(df.groupby("log_type")["level"].count().rename("total"))

    print("\n📊 Summary by level:")
    print(df["level"].value_counts())

    return df

if __name__ == "__main__":
    print("🔄 Retrieving Windows logs...\n")

    all_records = []
    all_records += get_logs_from_source("System", max_events=200)
    all_records += get_logs_from_source("Application", max_events=200)
    all_records += get_logs_from_source("Security", max_events=200)

    if all_records:
        df = save_logs(all_records)
        print("\n✅ Done! Logs ready for analysis.")
    else:
        print("❌ No logs retrieved.")