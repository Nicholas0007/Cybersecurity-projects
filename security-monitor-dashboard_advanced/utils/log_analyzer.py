def count_failed_logins(log_file):
    count = 0

    with open(log_file, "r") as file:
        for line in file:
            if "FAILED" in line:
                count += 1

    return count
