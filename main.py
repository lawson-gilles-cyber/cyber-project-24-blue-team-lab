# Blue Team Lab Simulation

from attack.attacker import simulate_attack
from defense.detector import detect_threat
from defense.responder import respond
from defense.logger import log_event

# Step 1: Simulate attack
logs = simulate_attack()

print("=== Blue Team Simulation ===\n")

# Step 2: Analyze logs
for log in logs:
    alert = detect_threat(log)

    if alert:
        print(alert)

        # Step 3: Respond to threat
        action = respond(alert)
        print(action)

        # Step 4: Log response
        log_event(alert, action)
