import hashlib

def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
        return hashlib.sha256(file_data).hexdigest()


file_path = "important_file.txt"

original_hash = calculate_hash(file_path)

print("Monitoring file for changes...\n")

while True:
    current_hash = calculate_hash(file_path)

    if current_hash != original_hash:
        print("WARNING: File has been modified!")
        break
