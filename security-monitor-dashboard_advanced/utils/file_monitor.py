import hashlib

def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        return hashlib.sha256(file.read()).hexdigest()


def check_file_integrity(file_path, original_hash):
    current_hash = calculate_hash(file_path)
    return current_hash != original_hash
