# 🔍 Threat detection

def detect_threat(log):

    if "FAILED LOGIN" in log:
        return "[ALERT] Brute force attempt"

    if "LOGIN SUCCESS - admin" in log:
        return "[ALERT] Admin compromise"

    if "confidential" in log:
        return "[ALERT] Sensitive data access"

    return None
