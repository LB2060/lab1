import re
import csv
from collections import defaultdict


input_file = 'server_logs.txt'  
output_text_file = 'failed_attempts.txt'  # Mətn faylı üçün
output_csv_file = 'failed_attempts.csv'  # CSV faylı üçün

failed_attempts = defaultdict(int)
log_details = []

with open(input_file, 'r') as f:
    for line in f:
        
        match = re.match(r'(\d+\.\d+\.\d+\.\d+) .*? \[(.*?)\] "(.*?) HTTP/1.1" (\d+)', line)
        if match:
            ip, timestamp, method, status = match.groups()
            if status == '401':  
                failed_attempts[ip] += 1
            log_details.append((ip, timestamp, method.split()[0], status))


with open(output_text_file, 'w') as f:
    for ip, count in failed_attempts.items():
        f.write(f"{ip} - {count} uğursuz cəhd\n")


with open(output_csv_file, 'w', newline='') as csvfile:
    fieldnames = ['IP ünvanı', 'Tarix', 'HTTP metodu', 'Uğursuz cəhdlər']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ip, timestamp, method, status in log_details:
        writer.writerow({
            'IP ünvanı': ip,
            'Tarix': timestamp,
            'HTTP metodu': method,
            'Uğursuz cəhdlər': failed_attempts.get(ip, 0)
        })

print("Fayllar uğurla yaradıldı!")
