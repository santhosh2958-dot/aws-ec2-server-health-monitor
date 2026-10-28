# AWS EC2 Server Health Monitor

## Project Overview

A beginner-friendly Python project that monitors basic health information on an Ubuntu server running on AWS EC2.

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Python 3
- Linux Cron
- Git and GitHub

## Features

- Identifies the server hostname
- Checks disk usage
- Reads memory information from Linux
- Displays the one-minute CPU load average
- Reports disk health using a configurable threshold
- Saves health reports to a text file
- Supports automatic execution through Linux Cron

## Project Structure

```text
server-health-monitor/
├── health_monitor.py
├── README.md
└── .gitignore
```

## Run the Project

Activate the Python virtual environment from the main learning project:

```bash
source ~/Python-Linux-AWS-DevOps/.venv/bin/activate
```

Navigate to the project directory:

```bash
cd ~/Python-Linux-AWS-DevOps/05-Projects/server-health-monitor
```

Run the monitor:

```bash
python health_monitor.py
```

The program displays the server health report and saves it to `health_report.txt`.

## Automated Monitoring

Linux Cron can execute the script every five minutes.

Check the scheduled jobs:

```bash
crontab -l
```

## Learning Outcomes

This project demonstrates Python scripting, Linux system information, conditional logic, file handling, scheduled jobs, and basic DevOps automation.

## Limitations

This is a learning project, not production-grade monitoring. CPU load average is not CPU usage percentage, and the current health status is based on disk usage only.
