import re


with open("server_logs.txt", "r") as file:
    server_file = file.read()

#!a. Regex-dən istifadə edərək verilmiş veb server log faylından IP ünvanlarını, tarixləri və HTTP metodlarını çıxarın.
    
log_pattern = re.compile(
    r'(?P<ip>\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b)'  # IP ünvanı
    r'.*\[(?P<date>\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2} \+\d{4})\]'  # Tarix
    r'.*\"(?P<method>POST|GET|PUT|DELETE|HEAD|OPTIONS|PATCH) [^\s]+ HTTP/\d\.\d\"'  # HTTP metodu
)

matches = log_pattern.finditer(server_file)

for match in matches:
    ip = match.group("ip")
    date = match.group("date")
    method = match.group("method")
    print(f"IP: {ip}, Date: {date}, HTTP Method: {method}")

