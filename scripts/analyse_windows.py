import re
import sys
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os
import schedule
import time
import subprocess

# ---- PATHS ----
LOGS_PATH = "../Logs/system.log"
DATA_PATH = "../data/"
OUTPUT_PATH = "../output/"

os.makedirs(DATA_PATH, exist_ok=True)
os.makedirs(OUTPUT_PATH, exist_ok=True)

# ---- EXTRACTION ----
def extract_logs(filepath=LOGS_PATH):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) \[(.+?)\] \[(.+?)\] (.+)'
    records = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                timestamp, level, source, log_type, event = match.groups()
                records.append({
                    "timestamp": timestamp,
                    "level": level,
                    "source": source,
                    "log_type": log_type,
                    "event": event
                })
    return records

# ---- PROCESSING ----
def process_logs(records):
    df = pd.DataFrame(records)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["date"] = df["timestamp"].dt.date
    df["hour"] = df["timestamp"].dt.hour
    return df

# ---- VISUALIZATIONS ----
def generate_charts(df):

    # 1. Bar chart — error frequency by source
    plt.figure(figsize=(10, 5))
    errors = df[df["level"].isin(["ERROR", "CRITICAL"])]
    if not errors.empty:
        errors.groupby("log_type")["level"].count().plot(kind="bar", color="tomato")
    plt.title("Error Frequency by Source (System / Application / Security)")
    plt.xlabel("Source")
    plt.ylabel("Number of Errors")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig(f"{DATA_PATH}chart_errors.png")
    plt.close()
    print("✅ chart_errors.png saved")

    # 2. Time series — activity by hour and source
    plt.figure(figsize=(12, 5))
    for log_type in df["log_type"].unique():
        subset = df[df["log_type"] == log_type]
        subset.groupby("hour").size().plot(kind="line", marker="o", label=log_type)
    plt.title("Activity by Hour and Source")
    plt.xlabel("Hour")
    plt.ylabel("Number of Events")
    plt.legend()
    plt.tight_layout()
    plt.savefig(f"{DATA_PATH}chart_logins.png")
    plt.close()
    print("✅ chart_logins.png saved")

    # 3. Pie chart — log level distribution
    plt.figure(figsize=(7, 7))
    df["level"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=140)
    plt.title("Log Level Distribution")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(f"{DATA_PATH}chart_distribution.png")
    plt.close()
    print("✅ chart_distribution.png saved")

# ---- HTML REPORT ----
def generate_report(df, report_path):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total = len(df)
    errors = len(df[df["level"].isin(["ERROR", "CRITICAL"])])
    warnings = len(df[df["level"] == "WARNING"])
    infos = len(df[df["level"] == "INFO"])

    stats_by_source = df.groupby("log_type")["level"].count().reset_index()
    stats_by_source.columns = ["Source", "Total"]
    rows_source = ""
    for _, row in stats_by_source.iterrows():
        rows_source += f"<tr><td>{row['Source']}</td><td>{row['Total']}</td></tr>"

    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Log Analysis Report - {now}</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }}
            h1 {{ color: #2c3e50; }}
            h2 {{ color: #34495e; border-bottom: 2px solid #ddd; padding-bottom: 5px; }}
            h3 {{ color: #555; }}
            .stats {{ display: flex; gap: 20px; margin: 20px 0; flex-wrap: wrap; }}
            .card {{ background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); min-width: 150px; text-align: center; }}
            .card h3 {{ margin: 0; font-size: 2em; color: #e74c3c; }}
            .card p {{ margin: 5px 0 0; color: #777; }}
            table {{ border-collapse: collapse; width: 50%; background: white; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            th {{ background: #2c3e50; color: white; padding: 10px; }}
            td {{ padding: 10px; border-bottom: 1px solid #eee; text-align: center; }}
            img {{ max-width: 100%; border-radius: 8px; margin: 10px 0; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        </style>
    </head>
    <body>
        <h1>📊 Windows Log Analysis Report</h1>
        <p>Generated on: <strong>{now}</strong></p>

        <h2>📈 General Statistics</h2>
        <div class="stats">
            <div class="card"><h3>{total}</h3><p>Total Events</p></div>
            <div class="card"><h3>{errors}</h3><p>Errors / Critical</p></div>
            <div class="card"><h3>{warnings}</h3><p>Warnings</p></div>
            <div class="card"><h3>{infos}</h3><p>Info</p></div>
        </div>

        <h2>📁 Breakdown by Source</h2>
        <table>
            <tr><th>Source</th><th>Total Events</th></tr>
            {rows_source}
        </table>

        <h2>📊 Visualizations</h2>
        <h3>1. Error Frequency by Source</h3>
        <img src="../data/chart_errors.png" alt="Errors">
        <h3>2. Activity by Hour and Source</h3>
        <img src="../data/chart_logins.png" alt="Activity">
        <h3>3. Log Level Distribution</h3>
        <img src="../data/chart_distribution.png" alt="Distribution">

    </body>
    </html>
    """

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {report_path} generated!")

# ---- AUTOMATION ----
def run_analysis():
    print(f"\n🔄 Analysis started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # 1. Retrieve Windows logs
    print("📥 Retrieving Windows logs...")
    subprocess.run(["python", "get_windows_logs.py"], check=True)

    # 2. Extraction and processing
    records = extract_logs()
    df = process_logs(records)
    print(f"✅ {len(df)} lines extracted")

    # 3. Charts
    generate_charts(df)

    # 4. Report with timestamp in filename
    timestamp_str = datetime.now().strftime("%Y-%m-%d_%H-%M")
    report_path = f"{OUTPUT_PATH}rapport_{timestamp_str}.html"
    generate_report(df, report_path)

    print("🎉 Analysis complete!")

# ---- MAIN ----
if __name__ == "__main__":
    if "--once" in sys.argv:
        run_analysis()
    else:
        run_analysis()
        print("\n⏰ Automation enabled — analysis every 2 minutes (Ctrl+C to quit)")
        schedule.every(2).minutes.do(run_analysis)
        while True:
            schedule.run_pending()
            time.sleep(1)