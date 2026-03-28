# 🛡️ Response engine

def respond(alert):

    if "Brute force" in alert:
        return "[ACTION] Block IP"

    if "Admin compromise" in alert:
        return "[ACTION] Lock account"

    if "Sensitive data" in alert:
        return "[ACTION] Alert SOC"

    return "[ACTION] Monitor"
