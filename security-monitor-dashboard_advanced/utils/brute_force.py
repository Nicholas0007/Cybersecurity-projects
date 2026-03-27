def detect_brute_force(log_file, threshold=3):
    attempts = {}

    with open(log_file, "r") as file:
        for line in file:
            ip, status = line.strip().split()

            if status == "FAILED":
                attempts[ip] = attempts.get(ip, 0) + 1

    alerts = []

    for ip, count in attempts.items():
        if count >= threshold:
            alerts.append((ip, count))

    return alerts
