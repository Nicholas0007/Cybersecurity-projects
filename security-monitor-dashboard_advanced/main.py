from utils.log_analyzer import count_failed_logins
from utils.brute_force import detect_brute_force
from utils.file_monitor import calculate_hash, check_file_integrity

log_file = "logs.txt"
file_to_monitor = "important_file.txt"

# Initial file hash
original_hash = calculate_hash(file_to_monitor)

print("\n Security Monitoring Dashboard\n")

# Log analysis
failed_logins = count_failed_logins(log_file)
print(f"Total Failed Logins: {failed_logins}")

# Brute force detection
alerts = detect_brute_force(log_file)

if alerts:
    print("\n Brute Force Alerts:")
    for ip, count in alerts:
        print(f"IP: {ip} | Attempts: {count}")
else:
    print("\nNo brute-force attacks detected.")

# File integrity check
import time

print("\nMonitoring file for changes...\n")

while True:
    if check_file_integrity(file_to_monitor, original_hash):
        print("\n🚨 WARNING: File has been modified!")
        break

    time.sleep(2)

