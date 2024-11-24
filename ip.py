#!/usr/bin/env python3

from rich.console import Console
from rich.table import Table
import requests

def fetch_ip_info():
    # URL for the API
    url = "http://ifconfig.co/json"

    # Making a request to the URL
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extracting the required fields
        ip_info = {
            "IP": data.get('ip', 'Not available'),
            "ASN": data.get('asn', 'Not available'),
            "asn_org": data.get('asn_org', 'Not available')
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
