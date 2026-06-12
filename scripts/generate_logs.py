from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
events = [
    "User login successful",
    "User login failed",
    "Disk usage high",
    "Service started",
    "Service stopped",
    "Connection timeout",
    "Permission denied",
    "System reboot",
    "Memory usage high",
    "Backup completed"
]

def generate_logs(n=200):
    logs = []
    start_time = datetime.now() - timedelta(days=7)

    for i in range(n):
        timestamp = start_time + timedelta(minutes=random.randint(1, 10080))
        level = random.choices(log_levels, weights=[50, 25, 15, 10])[0]
        event = random.choice(events)
        user = fake.user_name()
        ip = fake.ipv4()
        line = f"{timestamp.strftime('%Y-%m-%d %H:%M:%S')} {level} [{user}] [{ip}] {event}"
        logs.append(line)

    logs.sort()
    return logs

with open("../Logs/system.log", "w") as f:
    for line in generate_logs(200):
        f.write(line + "\n")

print("✅ system.log generated successfully!")