import os
import re
import subprocess
import time
import csv

# Where the CSV data gets stored
path = 'home/paul/speedtest/speedtest.csv'

# Call the command-line version of Speedtest. Must first install it, following instructions here https://pypi.org/project/speedtest-cli/
response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

# Collect and parse speed data
ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

# Clean and format data a little
ping[0] = str(ping[0]).replace(',', '.')
download[0] = str(download[0]).replace(',', '.')
upload[0] = str(upload[0]).replace(',', '.')
timestamp = str(time.strftime('%m/%d/%y')) + ' ' + str(time.strftime('%H:%M'))

# Store the data in a CSV file at location 'path'
with open(path, 'a') as f:
    fWriter = csv.writer(f)
    if f.tell() == 0:
        fWriter.writerow(['Date','Time','Ping (ms)','Download (Mbit/s)','Upload (Mbit/s)'])
    fWriter.writerow([timestamp, ping[0], download[0], upload[0]])
