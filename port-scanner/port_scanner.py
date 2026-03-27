import socket
from datetime import datetime

target = input("Enter target IP address: ")

start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

print(f"\nScanning target: {target}")
print(f"Port range: {start_port} - {end_port}")

start_time = datetime.now()

print("\nScanning...\n")

for port in range(start_port, end_port + 1):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(0.5)

    result = scanner.connect_ex((target, port))

    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown Service"

        print(f"Port {port} is OPEN ({service})")

    scanner.close()

end_time = datetime.now()

print("\nScan completed")
print(f"Start time: {start_time}")
print(f"End time: {end_time}")

