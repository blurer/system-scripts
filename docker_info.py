#!/usr/bin/env python3

import subprocess
from rich.console import Console
from rich.table import Table

def get_docker_containers():
    try:
        result = subprocess.run(["docker", "ps", "-a", "--format", "{{.Names}}\t{{.Status}}\t{{.Ports}}\t{{.Networks}}"], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"
    except FileNotFoundError:
        return "Docker is not installed or not found in PATH."

def parse_docker_output(output):
    lines = output.strip().split('\n')
    containers = []
    for line in lines:
        parts = line.split('\t')
        if len(parts) == 4:
            containers.append(parts)
    return containers

def display_containers(containers):
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Name", style="dim", width=12)
    table.add_column("Status")
    table.add_column("Ports")
    table.add_column("Networks")

    for container in containers:
        table.add_row(*container)

    console.print(table)

def main():
    output = get_docker_containers()
    if output.startswith("Error:") or output.startswith("Docker is not installed"):
        print(output)
    else:
        containers = parse_docker_output(output)
        if containers:
            display_containers(containers)
        else:
            print("No Docker containers found.")

if __name__ == "__main__":
    main()
