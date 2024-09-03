import colorama
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

import os
import subprocess
import configparser
import platform
import shutil
import psutil
import requests
import socket
from collections import deque
import json
import sys

COMMANDS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "COM")
BASE_DIR = os.path.join(os.getcwd(), "vfs")

commands = {}

# Simulated memory management
memory_blocks = deque()
MAX_MEMORY_BLOCKS = 100  # Define a maximum number of memory blocks
BLOCK_SIZE = 1024        # Size of each block in bytes

# Simulated CPU time slicing
cpu_slices = deque()
TIME_SLICE_DURATION = 5  # Duration of each CPU time slice in seconds

# User management simulation
users = {
    "admin": {"password": "admin", "permissions": {"all": True}},
    "user": {"password": "user", "permissions": {"basic": True}}
}
current_user = None

def clear_screen():
    """Clears the terminal screen."""
    # ANSI escape sequence to clear the screen and move the cursor to the top-left corner
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def authenticate_user():
    """Authenticate user for login."""
    global current_user
    print(f"{Style.BRIGHT}Enter username: ", end="")
    username = input().strip()
    if username in users:
        print(f"{Style.BRIGHT}Enter password: ", end="")
        password = input().strip()
        if users[username]["password"] == password:
            current_user = username
            clear_screen()
            print(f"{Style.BRIGHT}{Fore.GREEN}Logged in as {username}.")
        else:
            print("{Style.BRIGHT}{Fore.RED}Invalid password.")
            current_user = None
    else:
        print("User does not exist.")
        current_user = None

def check_permission(command):
    """Check if the current user has permission to run a specific command."""
    if current_user == "admin":
        return True
    if command in commands:
        return users[current_user].get("permissions", {}).get("all", False) or \
               users[current_user].get("permissions", {}).get("basic", False)
    return False

def display_credits():
    clear_screen()
    """Displays the credits once when the CLI starts."""
    credits = """
░▒▓█▓▒  ▒▓█▓▒  ▒▓█▓▒  ▒▓███████▓▒  ▒▓██████▓▒  ▒▓████████▓▒░
░▒▓█▓▒  ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒░       ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒░
░▒▓█▓▒  ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒░       ▒▓█▓▒        ▒▓█▓▒░
░▒▓█▓▒  ▒▓█▓▒  ▒▓█▓▒  ▒▓██████▓▒  ▒▓█▓▒        ▒▓██████▓▒░
░▒▓█▓▒  ▒▓█▓▒  ▒▓█▓▒       ░▒▓█▓▒ ▒▓█▓▒        ▒▓█▓▒░
░▒▓█▓▒  ▒▓█▓▒  ▒▓█▓▒       ░▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒░
 ░▒▓█████████████▓▒  ▒▓███████▓▒  ▒▓██████▓▒   ▒▓████████▓▒░




 ░▒▓██████▓▒  ▒▓███████▓▒  ▒▓█▓▒  ▒▓██████▓▒   ▒▓███████▓▒░             ░▒▓███████▓▒ ▒▓████████▓▒ ▒▓███████▓▒  ▒▓█▓▒  ▒▓█▓▒░
░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░                   ░▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒       ░▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░
░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░                   ░▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒       ░▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░
░▒▓█▓▒  ▒▓█▓▒ ▒▓███████▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░             ░▒▓██████▓▒  ▒▓█▓▒  ▒▓█▓▒  ▒▓██████▓▒  ▒▓████████▓▒░
░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░            ░▒▓█▓▒░       ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒░             ░▒▓█▓▒░
░▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓█▓▒░            ░▒▓█▓▒░       ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒░             ░▒▓█▓▒░
 ░▒▓██████▓▒  ▒▓█▓▒  ▒▓█▓▒ ▒▓█▓▒  ▒▓██████▓▒  ▒▓█▓▒  ▒▓█▓▒░            ░▒▓████████▓▒ ▒▓████████▓▒ ▒▓████████▓▒░      ░▒▓█▓▒░



"""
    print(f"{Style.BRIGHT}{Fore.CYAN}{credits}{Style.RESET_ALL}")


def load_commands():
    """Loads all available commands from .inf files in the COM directory."""
    global commands
    commands = {}
    for root, dirs, files in os.walk(COMMANDS_DIR):
        for file in files:
            if file.endswith(".inf"):
                inf_path = os.path.join(root, file)
                config = configparser.ConfigParser()
                config.read(inf_path)

                if "WSCE" in config:
                    command_name = config["WSCE"].get("commandname", "").strip()
                    command_desc = config["WSCE"].get("commanddesc", "No description available").strip()
                    script_name = file.replace(".inf", ".py")
                    script_path = os.path.join(root, script_name)

                    if os.path.exists(script_path):
                        # Normalize paths for the current OS
                        script_path = os.path.normpath(script_path)
                        commands[command_name] = {"path": script_path, "desc": command_desc}
                    else:
                        print(f"{Style.BRIGHT}{Fore.RED}Script '{script_path}' not found for command '{command_name}'.")

def run_command(command):
    """Runs the Python script associated with the given command."""
    if command in commands:
        interpreter = "python3" if platform.system() == "Linux" else "python"
        subprocess.run([interpreter, commands[command]["path"]])
    else:
        print(f"{Style.BRIGHT}{Fore.RED}Command '{command}' not found. Check your .inf configuration and try again.")
        
def relabel(old_name, new_name):
    """Rename a file or directory."""
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"Renamed '{old_name}' to '{new_name}'.")
    else:
        print(f"'{old_name}' does not exist.")

def duplicate(source, destination):
    """Copy a file or directory."""
    if os.path.exists(source):
        if os.path.isdir(source):
            shutil.copytree(source, destination)
            print(f"Copied directory '{source}' to '{destination}'.")
        else:
            shutil.copy2(source, destination)
            print(f"Copied file '{source}' to '{destination}'.")
    else:
        print(f"'{source}' does not exist.")

def shift(source, destination):
    """Move a file or directory."""
    if os.path.exists(source):
        shutil.move(source, destination)
        print(f"Moved '{source}' to '{destination}'.")
    else:
        print(f"'{source}' does not exist.")

def change_directory(directory):
    global BASE_DIR

    # Get the current directory
    current_dir = os.getcwd()

    # Resolve the new directory path
    new_dir = os.path.normpath(os.path.join(current_dir, directory))
    
    # Prevent navigation out of the BASE_DIR
    if os.path.commonpath([new_dir, BASE_DIR]) != BASE_DIR:
        print("Cannot navigate outside of the vfs directory.")
        return
    
    if os.path.isdir(new_dir):
        os.chdir(new_dir)
        print(f"Changed directory to: {os.getcwd()}")
    else:
        print(f"Directory '{directory}' does not exist.")

def list_directory():
    """Handles the custom 'show' command to list directory contents."""
    contents = os.listdir()
    for item in contents:
        print(item)

def requestping(host):
    """Simulates a ping command using the system's ping utility."""
    system = platform.system().lower()
    
    if system == 'windows':
        cmd = ['ping', '-n', '4', host]
    else:
        cmd = ['ping', '-c', '4', host]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(f"{Style.BRIGHT}{result.stdout}")
    except Exception as e:
        print(f"{Style.BRIGHT}{Fore.RED}An error occurred: {e}")

def notepad(filename):
    """A simple text editor for creating and editing text files."""

    file_path = os.path.join(os.getcwd(), filename)

    # Load existing content if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
    else:
        print(f"{Style.BRIGHT}Creating new file: {filename}{Style.RESET_ALL}")
        lines = [""]
    
    current_line = 0

    while True:
        clear_screen()
        print(f"{Style.BRIGHT}Text Editor - Use 'save' to save and exit{Style.RESET_ALL}")
        print(f"{Style.BRIGHT}-------------------------------------------------{Style.RESET_ALL}")
        # Display all lines in the file with line numbers
        for i, line in enumerate(lines):
            if i == current_line:
                print(f"{Style.BRIGHT}> {i + 1}: {line}{Style.RESET_ALL}", end="")  # Highlight current line
            else:
                print(f"{Style.BRIGHT}  {i + 1}: {line}{Style.RESET_ALL}", end="")

        # Get user input for line editing or navigation
        command = input(f"{Style.BRIGHT}\nEnter command or text: {Style.RESET_ALL}").strip()

        if command.lower() == "save":
            break
        elif command.lower().startswith("add "):
            # Add text to the end of the current line
            lines[current_line] += command[4:] + "\n"
        elif command.lower() == "new":
            lines.insert(current_line + 1, "")
            current_line += 1
        elif command.lower().startswith("edit "):
            # Edit the current line
            lines[current_line] = command[5:] + "\n"
        elif command.lower() == "del":
            if len(lines) > 0:
                lines.pop(current_line)
                if current_line >= len(lines):
                    current_line = len(lines) - 1
        elif command.lower() == "up":
            if current_line > 0:
                current_line -= 1
        elif command.lower() == "down":
            if current_line < len(lines) - 1:
                current_line += 1
        else:
            # Treat input as text to be added to the current line
            lines[current_line] += command + "\n"

    # Save the file before exiting
    with open(file_path, "w") as file:
        file.writelines(lines)
    
    print(f"{Style.BRIGHT}File saved: {file_path}{Style.RESET_ALL}")

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

    
def memory():
    """Simulate memory allocation and deallocation."""
    global memory_blocks

    print(f"{Style.BRIGHT}Memory Manager - Commands:{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}- 'alloc' : Allocate a memory block.{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}- 'free'  : Free the last allocated memory block.{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}- 'status': Show current memory allocation status.{Style.RESET_ALL}")

    while True:
        command = input("Memory> ").strip().lower()

        if command == "alloc":
            if len(memory_blocks) < MAX_MEMORY_BLOCKS:
                memory_blocks.append(BLOCK_SIZE)
                print(f"{Style.BRIGHT}Allocated a memory block of size {BLOCK_SIZE} bytes.{Style.RESET_ALL}")
            else:
                print(f"{Style.BRIGHT}Memory limit reached.{Style.RESET_ALL}")
        elif command == "free":
            if memory_blocks:
                memory_blocks.pop()
                print(f"{Style.BRIGHT}Freed the last allocated memory block.{Style.RESET_ALL}")
            else:
                print(f"{Style.BRIGHT}No memory blocks to free.{Style.RESET_ALL}")
        elif command == "status":
            print(f"{Style.BRIGHT}Total blocks allocated: {len(memory_blocks)}{Style.RESET_ALL}")
            print(f"{Style.BRIGHT}Available blocks: {MAX_MEMORY_BLOCKS - len(memory_blocks)}{Style.RESET_ALL}")
        elif command == "exit":
            break
        else:
            print(f"{Style.BRIGHT}Unknown command.{Style.RESET_ALL}")

def cpu():
    """Simulate CPU time slicing."""
    global cpu_slices

    print(f"{Style.BRIGHT}CPU Scheduler - Commands:{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}- 'add <name>' : Add a task to the scheduler.{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}- 'status'     : Show current CPU time slices.{Style.RESET_ALL}")
    print(f"{Style.BRIGHT}- 'run'        : Run tasks with CPU time slicing.{Style.RESET_ALL}")

    while True:
        command = input(f"{Style.BRIGHT}CPU> ").strip().lower()

        if command.startswith("add "):
            task_name = command[4:].strip()
            cpu_slices.append(task_name)
            print(f"{Style.BRIGHT}Added task: {task_name}")
        elif command == "status":
            print(f"{Style.BRIGHT}Current tasks: {list(cpu_slices)}")
        elif command == "run":
            print(f"{Style.BRIGHT}Running tasks with time slicing...")
            while cpu_slices:
                task = cpu_slices.popleft()
                print(f"{Style.BRIGHT}Running task: {task}")
                time.sleep(TIME_SLICE_DURATION)
        elif command == "exit":
            break
        else:
            print(f"{Style.BRIGHT}{Fore.RED}Unknown command.{Style.RESET_ALL}")

    """Display the current CPU usage."""
    cpu_percent = psutil.cpu_percent(interval=1)
    print(" ")
    print(f"{Style.BRIGHT}CPU Usage: {cpu_percent}%")
    print(" ")

def portscan(host, port):
    """Check if a specific port on a given host is open."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(" ")
        print(f"{Style.BRIGHT}{Fore.GREEN}Port {port} on {host} is open.")
        print(" ")
    else:
        print(" ")
        print(f"{Style.BRIGHT}{Fore.RED}Port {port} on {host} is closed.")
        print(" ")
    sock.close()

def httphead(url):
    """Fetch and display HTTP headers from a given URL."""
    try:
        response = requests.head(url)
        print(" ")
        print(f"{Style.BRIGHT}HTTP Headers for {url}:")
        for key, value in response.headers.items():
            print(f"{Style.BRIGHT}{key}: {value}")
        print(" ")
    except requests.RequestException as e:
        print(" ")
        print(f"{Style.BRIGHT}{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
        print(" ")

def display_help():
    """Displays the help information for all available commands, including built-ins."""
    print(" ")
    print(f"{Style.BRIGHT}Available commands:")
    print(f"{Style.BRIGHT}exit -{Fore.YELLOW} Exits the CLI")
    print(f"{Style.BRIGHT}help -{Fore.YELLOW} Displays this help information")
    print(f"{Style.BRIGHT}nav {Fore.YELLOW}<directory> - Changes the current directory")
    print(f"{Style.BRIGHT}show - {Fore.YELLOW}Lists the contents of the current directory")
    print(f"{Style.BRIGHT}aurora {Fore.YELLOW}<filename> - Opens a text editor to create/edit a .txt file")
    print(f"{Style.BRIGHT}request - {Fore.YELLOW}Pings a specified IP address or domain") 
    print(f"{Style.BRIGHT}relabel <old_name> <new_name> - {Fore.YELLOW}Renames a file or directory")
    print(f"{Style.BRIGHT}duplicate <source> <destination> - {Fore.YELLOW}Copies a file or directory to another location")
    print(f"{Style.BRIGHT}shift <source> <destination> - {Fore.YELLOW}Moves a file or directory to another location")
    print(f"{Style.BRIGHT}httphead <URL> - {Fore.YELLOW}Fetches HTTP headers from a given URL.")
    print(f"{Style.BRIGHT}portscan <host> <port> - {Fore.YELLOW}Checks if a specific port on a host is open.")
    print(f"{Style.BRIGHT}memory - {Fore.YELLOW}Launches the memory manager")
    print(f"{Style.BRIGHT}cpu - {Fore.YELLOW}Launches the cpu manager")
    print(f"{Style.BRIGHT}clear - {Fore.YELLOW}Clears the screen")
    # Dynamically loaded commands
    if commands:
        for cmd, info in commands.items():
            print(f"{Style.BRIGHT}{cmd} - {Fore.YELLOW}{info['desc']}{Style.RESET_ALL}")
    else:
        print(f"{Style.BRIGHT}{Fore.YELLOW}No additional commands available.{Style.RESET_ALL}")
    print(" ")

def cli():
    """Basic CLI loop to accept commands."""
    display_credits()  # Display credits at the start

    authenticate_user()
    if not current_user:
        return

    load_commands()    # Load all commands at startup
    os.chdir(BASE_DIR)
    while True:
        UNDERLINE = '\033[4m'
        command = input(f"{Style.BRIGHT}|{UNDERLINE} {current_user}@{Fore.CYAN}WSCE {Style.RESET_ALL}{Style.BRIGHT}|{Style.RESET_ALL} ").strip().lower()
        
        if command == "exit":
            clear_screen()
            break
        elif command == "help":
            display_help()
        elif command.startswith("request "):
            host = command[8:].strip()
            requestping(host)
        elif command.startswith("nav "):
            directory = command[4:].strip()
            change_directory(directory)
        elif command == "show":
            list_directory()
        elif command.startswith("aurora "):
            filename = command[8:].strip()
            if not filename.endswith(".txt"):
                filename += ".txt"
            notepad(filename)
        elif command.startswith("relabel "):
            parts = command[8:].split(maxsplit=1)
            if len(parts) == 2:
                relabel(parts[0].strip(), parts[1].strip())
            else:
                print(f"{Style.BRIGHT}Usage: relabel <old_name> <new_name>")
        elif command.startswith("duplicate "):
            parts = command[10:].split(maxsplit=1)
            if len(parts) == 2:
                duplicate(parts[0].strip(), parts[1].strip())
            else:
                print("Usage: {Style.BRIGHT}duplicate <source> <destination>")
        elif command.startswith("shift "):
            parts = command[6:].split(maxsplit=1)
            if len(parts) == 2:
                shift(parts[0].strip(), parts[1].strip())
            else:
                print("{Style.BRIGHT}Usage: shift <source> <destination>")
        elif command == "memory":
            memory()
        elif command == "cpu":
            cpu()
        elif command.startswith("portscan "):
            parts = command[9:].split(maxsplit=1)
            if len(parts) == 2:
                host, port = parts[0].strip(), int(parts[1].strip())
                portscan(host, port)
            else:
                print("{Style.BRIGHT}Usage: portscan <host> <port>")
        elif command.startswith("httphead "):
            url = command[9:].strip()
            httphead(url)
        elif command == "clear":
            clear_screen()
        elif command:
            run_command(command)

if __name__ == "__main__":
    cli()
