# This program will contineously monitor the computer and will write into 
# network_network monitor if the CPU or memory usage is above 30%
# To create this as a script that runs in the backgound modify the crontab file in Linux
import time
from datetime import datetime
import psutil
THRESHOLD = 30
def simple_network():
    while True:
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('network_monitor.txt', 'a') as file:
            if cpu > THRESHOLD and memory > THRESHOLD:
                file.write(f"CPU usage is {cpu}, Memory usage is {memory}, {timestamp}\n")
            elif cpu > THRESHOLD:
                file.write(f"CPU usage is {cpu}, {timestamp}\n")
            elif memory > THRESHOLD:
                file.write(f"Memory usage is {memory}, {timestamp}\n")
        time.sleep(300)
simple_network()