#!b. 5-dən çox uğursuz giriş cəhdi olan hər hansı IP ünvanlarını müəyyən edin və onları JSON faylında saxlayın.
import re
import json
from collections import defaultdict

FAILED_STATUS = [401]
failed_attempts = defaultdict(int)

# Log faylı oxumaq
with open("server_logs.txt", "r") as file:
    server_file = file.readlines()
    

# Regex pattern
log_pattern = re.compile(r'(?P<ip>\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b).*"POST /login HTTP/1\.1" (?P<status>\d{3})')

# Log faylını emal etmək
for log in server_file:
    match = log_pattern.search(log)
    if match:
        ip = match.group("ip")
        status = int(match.group("status"))
        if status in FAILED_STATUS:
            failed_attempts[ip] += 1


# 5-dən çox uğursuz cəhd olan IP-lər
blocked_ips = {ip: attempts for ip, attempts in failed_attempts.items() if attempts > 3}

# JSON faylında saxlamaq
output_file = "blocked_ips.json"
with open(output_file, "w") as json_file:
    json.dump(blocked_ips, json_file, indent=4)

print("uygunsuzluq qeyde alindi")