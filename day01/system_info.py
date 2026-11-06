import platform
import socket
import os
import getpass
from datetime import datetime

def get_system_info():
    hostname = socket.gethostname()
    operating_system = platform.system()
    os_version = platform.release()
    cpu_count = os.cpu_count()
    username = getpass.getuser()
    current_time = datetime.now()
    python_version = platform.python_version()
    machine_architecture = platform.machine()

    print("===== System Information =====")
    print(f"Hostname: {hostname}")
    print(f"Operating System: {operating_system}")
    print(f"OS Version: {os_version}")
    print(f"CPU Count: {cpu_count}")
    print(f"Username: {username}")
    print(f"Current Time: {current_time}")
    print(f"Python Version: {python_version}")
    print(f"Machine Architecture: {machine_architecture}")
    print("==============================")

if __name__ == "__main__":
    get_system_info()



