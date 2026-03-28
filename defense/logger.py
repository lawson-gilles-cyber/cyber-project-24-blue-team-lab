# 📘 Event logger for incident tracking

from datetime import datetime

def log_event(alert, action):
    """
    Save detected alert and response action to a report file
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"{timestamp} | {alert} | {action}"

    # Save to incident report file
    with open("reports/incident_report.txt", "a") as file:
        file.write(log_entry + "\n")
