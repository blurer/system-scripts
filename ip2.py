#!/usr/bin/env python3

from rich.console import Console
from rich.table import Table
import requests
import subprocess

def get_tailscale_ip():
    # Run the tailscale command and capture the output
    result = subprocess.run(["tailscale", "ip", "-4"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        return result.stdout.decode().strip()
    else:
        return "Unavailable"

def fetch_ip_info():
    # URL for the API
    url = "http://ifconfig.co/json"

    # Making a request to the URL
    response = requests.get(url)

    # Getting the Tailscale IP
    tailscale_ip = get_tailscale_ip()

    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extracting the required fields
        ip_info = {
            "Public IP": data.get('ip', 'Not available'),
            "ASN": data.get('asn', 'Not available'),
            "ASN Org": data.get('asn_org', 'Not available'),
            "Tailscale IP": tailscale_ip
        }

        # Creating a console object
        console = Console()

        # Creating a table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Field", style="dim", width=12)
        table.add_column("Value")

        # Adding rows to the table
        for key, value in ip_info.items():
            table.add_row(key, value)

        # Print the table to the console
        console.print(table)
    else:
        print("Failed to retrieve data")

if __name__ == "__main__":
    fetch_ip_info()

