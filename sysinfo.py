#!/usr/bin/env python3

from rich.console import Console
from rich.table import Table
import subprocess
import re

# Function to run shell commands and capture their output
def run_command(command):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True, shell=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return None

# Gather system information
def get_system_info():
    info = {}

    # CPU model
    info['cpu_model'] = run_command("cat /proc/cpuinfo | grep 'model name' | head -1 | cut -d':' -f2 | xargs")

    # Number of cores and threads
    cores = int(run_command("lscpu | grep 'Core(s) per socket:' | awk '{print $4}'"))
    threads_per_core = int(run_command("lscpu | grep 'Thread(s) per core:' | awk '{print $4}'"))
    total_threads = cores * threads_per_core
    info['cores_threads'] = f"{cores}c / {total_threads}t"

    # System memory
    mem_info = run_command("free -h | grep Mem")
    if mem_info:
        mem_info_parts = mem_info.split()
        info['system_memory'] = f"{mem_info_parts[2]} / {mem_info_parts[3]} / {mem_info_parts[1]}"
    
    # Disk storage
    disk_storage = run_command("df -h / | grep /")
    if disk_storage:
        disk_storage_parts = disk_storage.split()
        info['disk_storage'] = f"{disk_storage_parts[2]} / {disk_storage_parts[3]} / {disk_storage_parts[1]}"

    # Uptime
    info['uptime'] = run_command("uptime -p")

    # OS
    # OS name
    info['os_name'] = run_command("grep PRETTY_NAME /etc/os-release | cut -d'=' -f2 | tr -d '\"'")

    return info

# Print the system information in a table
def print_system_info(info):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Item", style="dim", width=20)
    table.add_column("Value")

    for key, value in info.items():
        table.add_row(key, value)

    console.print(table)

if __name__ == "__main__":
    system_info = get_system_info()
    if system_info:
        print_system_info(system_info)
    else:
        print("Failed to retrieve system information")

