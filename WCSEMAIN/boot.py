import colorama
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

import os
import sys
import time
import random
import subprocess
import platform

# Directory for command scripts
COMMANDS_DIR = os.path.join("COM")

def loading_spinner(duration=3):
    """Simulates a loading spinner for the given duration."""
    spinner = ["|", "/", "-", "\\"]
    end_time = time.time() + duration
    while time.time() < end_time:
        for symbol in spinner:
            sys.stdout.write(f"\r{Style.BRIGHT}[{symbol}] Loading...")
            sys.stdout.flush()
            time.sleep(0.1)

def clear_console():
    """Clears the console based on the operating system."""
    if platform.system() == "Windows":
        os.system("cls")
    else:  # Assumes Linux or macOS
        os.system("clear")




def boot_sequence():
    """Runs the boot sequence with fake services and displays ASCII art."""
    # Fake boot sequence messages with statuses
    services = [
        {"name": "Mounting /VFS", "display_name": "Mounted /VFS", "status": "ok"},
        {"name": "Starting Network Manager", "display_name": "Started Network Manager", "status": "ok"},
        {"name": "Loading Kernel Modules", "display_name": "Loaded Kernel Modules", "status": "ok"},
        {"name": "Initializing RAM", "display_name": "Initialized RAM", "status": "ok"},
        {"name": "Starting User Authentication", "display_name": "Started User Authentication", "status": "ok"},
	{"name": "Starting Colorama", "display_name": "Started Colorama", "status": "ok"},
	{"name": "Launching WSCE", "display_name": "Started {Fore.CYAN}WSCE{Style.RESET_ALL}", "status": "ok"},
    ]

    # Display the boot sequence messages
    for service in services:
        loading_spinner()
        time.sleep(random.uniform(1, 3))  # Random wait to make it feel realistic

        if service["status"] == "ok":
            print(f"\r{Style.BRIGHT}[{Fore.GREEN}OK{Style.RESET_ALL}{Style.BRIGHT}] {service['display_name']}")
        elif service["status"] == "fail":
            print(f"\r{Style.BRIGHT}[{Fore.RED}FAILED{Style.RESET_ALL}{Style.BRIGHT}] {service['display_name']}")
        time.sleep(1)  # Pause before the next service loads

    # Clear the console
    clear_console()

    current_os = platform.system()
    if current_os == "Windows":
        os.system("python WSCECLI.py")
    elif current_os == "Linux" or current_os == "Darwin":
        os.system("python3 WSCECLI.py")


if __name__ == "__main__":
    boot_sequence()

