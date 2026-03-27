failed_attempts = {}

threshold = 5

with open("login_attempts.txt", "r") as file:
    for line in file:
        parts = line.strip().split(" ")
        ip = parts[0]
        status = parts[1]

        if status == "FAILED":
            if ip in failed_attempts:
                failed_attempts[ip] += 1
            else:
                failed_attempts[ip] = 1

print("\nBrute Force Detection Report\n")

for ip, count in failed_attempts.items():
    if count >= threshold:
        print(f"ALERT: Possible brute-force attack detected from {ip}")
        print(f"Failed attempts: {count}\n")


## python brute_force_detector.py
