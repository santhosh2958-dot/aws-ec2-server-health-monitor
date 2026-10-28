import os
import shutil
from datetime import datetime

# Step 1: Get server information
server_name = os.uname().nodename

# Step 2: Get disk usage
disk = shutil.disk_usage("/")

disk_total = disk.total / (1024 ** 3)
disk_used = disk.used / (1024 ** 3)
disk_percent = (disk.used / disk.total) * 100

# Step 3: Get memory usage from Linux
with open("/proc/meminfo") as file:
    memory_data = file.readlines()

memory_total = int(memory_data[0].split()[1])
memory_available = int(memory_data[2].split()[1])

memory_percent = (
    (memory_total - memory_available) / memory_total
) * 100

# Step 4: Get CPU load average
cpu_load = os.getloadavg()[0]

# Step 5: Decide disk health
if disk_percent >= 80:
    status = "WARNING"
else:
    status = "HEALTHY"

# Step 6: Display report
report = f"""
===== AWS EC2 SERVER HEALTH REPORT =====

Date: {datetime.now()}
Server: {server_name}

Disk Total: {disk_total:.2f} GB
Disk Used: {disk_used:.2f} GB
Disk Usage: {disk_percent:.2f}%

Memory Usage: {memory_percent:.2f}%
CPU Load Average (1 min): {cpu_load:.2f}

Disk Status: {status}
=======================================
"""

print(report)

# Step 7: Save report to a file
with open("health_report.txt", "a") as file:
    file.write(report + "\n")

print("Report saved to health_report.txt")
