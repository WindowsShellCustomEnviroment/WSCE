import os
import subprocess
import configparser
import platform

# Directory where commands and their .inf files are located
COMMANDS_DIR = os.path.join("COM")

# Dictionary to store commands and their corresponding script paths and descriptions
commands = {}

def display_credits():
    """Displays the credits once when the CLI starts."""
    credits = """
----------------------------------
|                                |
|        Welcome to WSCE         |
|                                |
| Developed By: Orion - 2024     |
|                                |
----------------------------------
"""
    print(credits)

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
                        print(f"Script '{script_path}' not found for command '{command_name}'.")

def run_command(command):
    """Runs the Python script associated with the given command."""
    if command in commands:
        interpreter = "python3" if platform.system() == "Linux" else "python"
        subprocess.run([interpreter, commands[command]["path"]])
    else:
        print(f"Command '{command}' not found. Check your .inf configuration and try again.")

def display_help():
    """Displays the help information for all available commands."""
    if commands:
        print(" ")
        print("Available commands:")
        for cmd, info in commands.items():
            print(f"{cmd} - {info['desc']}")
        print(" ")
    else:
        print("No commands available. Please check your .inf configuration and try again.")
        print(" ")

def cli():
    """Basic CLI loop to accept commands."""
    display_credits()  # Display credits at the start

    load_commands()    # Load all commands at startup

    while True:
        command = input("WSCE> ").strip().lower()
        if command == "exit":
            break
        elif command == "help":
            display_help()
        elif command:
            run_command(command)

if __name__ == "__main__":
    cli()
