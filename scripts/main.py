import os
import subprocess
import sys
from datetime import datetime

# ---- PATHS ----
OUTPUT_PATH = "../output/"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def show_menu():
    clear()
    print("=" * 50)
    print("   📊 LOG ANALYSIS — MAIN MENU")
    print("=" * 50)
    print()
    print("  🖥️  WINDOWS")
    print("  [1] Retrieve Windows logs")
    print("  [2] Run Windows analysis (once)")
    print("  [3] Run Windows analysis (automatic)")
    print()
    print("  🐧  LINUX")
    print("  [4] Run Linux analysis (once)")
    print("  [5] Run Linux analysis (automatic)")
    print()
    print("  📄  REPORTS")
    print("  [6] Open latest report")
    print("  [7] List all reports")
    print("  [8] Open a specific report")
    print()
    print("  🛠️  UTILITIES")
    print("  [9] Generate fake logs (test)")
    print("  [10] Clear old reports")
    print()
    print("  [0] Quit")
    print()
    print("=" * 50)

def get_reports():
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    reports = sorted([
        f for f in os.listdir(OUTPUT_PATH) if f.endswith(".html")
    ])
    return reports

def open_report(path):
    full_path = os.path.abspath(path)
    if os.name == "nt":
        os.startfile(full_path)
    else:
        subprocess.run(["xdg-open", full_path])

def main():
    while True:
        show_menu()
        choice = input("  👉 Your choice: ").strip()

        # ---- WINDOWS ----
        if choice == "1":
            print("\n📥 Retrieving Windows logs...")
            subprocess.run(["python", "get_windows_logs.py"])
            input("\n  Press Enter to continue...")

        elif choice == "2":
            print("\n🔄 Running Windows analysis (once)...")
            subprocess.run(["python", "analyse_windows.py", "--once"])
            input("\n  Press Enter to continue...")

        elif choice == "3":
            print("\n⏰ Running Windows analysis (automatic, Ctrl+C to stop)...")
            try:
                subprocess.run(["python", "analyse_windows.py"])
            except KeyboardInterrupt:
                print("\n⛔ Automation stopped.")
            input("\n  Press Enter to continue...")

        # ---- LINUX ----
        elif choice == "4":
            print("\n🔄 Running Linux analysis (once)...")
            subprocess.run(["python", "analyse_linux.py", "--once"])
            input("\n  Press Enter to continue...")

        elif choice == "5":
            print("\n⏰ Running Linux analysis (automatic, Ctrl+C to stop)...")
            try:
                subprocess.run(["python", "analyse_linux.py"])
            except KeyboardInterrupt:
                print("\n⛔ Automation stopped.")
            input("\n  Press Enter to continue...")

        # ---- REPORTS ----
        elif choice == "6":
            reports = get_reports()
            if reports:
                latest = reports[-1]
                print(f"\n📄 Opening: {latest}")
                open_report(f"{OUTPUT_PATH}{latest}")
            else:
                print("\n❌ No reports found in output/")
            input("\n  Press Enter to continue...")

        elif choice == "7":
            reports = get_reports()
            print()
            if reports:
                print(f"  📁 {len(reports)} report(s) found:\n")
                for i, r in enumerate(reports, 1):
                    print(f"  [{i}] {r}")
            else:
                print("  ❌ No reports found.")
            input("\n  Press Enter to continue...")

        elif choice == "8":
            reports = get_reports()
            if not reports:
                print("\n❌ No reports found.")
            else:
                print(f"\n  📁 Available reports:\n")
                for i, r in enumerate(reports, 1):
                    print(f"  [{i}] {r}")
                print()
                try:
                    num = int(input("  👉 Report number to open: "))
                    if 1 <= num <= len(reports):
                        open_report(f"{OUTPUT_PATH}{reports[num-1]}")
                        print(f"✅ Opening {reports[num-1]}")
                    else:
                        print("❌ Invalid number.")
                except ValueError:
                    print("❌ Enter a valid number.")
            input("\n  Press Enter to continue...")

        # ---- UTILITIES ----
        elif choice == "9":
            print("\n🛠️  Generating fake logs...")
            subprocess.run(["python", "generate_logs.py"])
            input("\n  Press Enter to continue...")

        elif choice == "10":
            reports = get_reports()
            if not reports:
                print("\n❌ No reports to delete.")
            else:
                confirm = input(f"\n  ⚠️  Delete {len(reports)} report(s)? (yes/no): ").strip().lower()
                if confirm == "yes":
                    for r in reports:
                        os.remove(f"{OUTPUT_PATH}{r}")
                    print(f"✅ {len(reports)} report(s) deleted.")
                else:
                    print("❌ Cancelled.")
            input("\n  Press Enter to continue...")

        # ---- QUIT ----
        elif choice == "0":
            clear()
            print("  👋 Goodbye!")
            sys.exit()

        else:
            print("\n❌ Invalid choice, try again.")
            input("\n  Press Enter to continue...")

if __name__ == "__main__":
    main()