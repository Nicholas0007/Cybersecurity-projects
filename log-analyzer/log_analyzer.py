failed_attempts = {}

with open("auth_log.txt", "r") as file:
    for line in file:
        if "Failed login" in line:
            parts = line.strip().split(" ")
            ip = parts[-1]

            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print("Suspicious Activity Report")

for ip, count in failed_attempts.items():
    if count >= 2:
        print(f"IP: {ip} | Failed Attempts: {count}")
