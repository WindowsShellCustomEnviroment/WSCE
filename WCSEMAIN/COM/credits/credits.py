import sys
import colorama
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    """Clears the terminal screen."""
    # ANSI escape sequence to clear the screen and move the cursor to the top-left corner
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()



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


display_credits()
print(f"{Style.BRIGHT}{Fore.CYAN}WSCE{Style.RESET_ALL} - {Style.BRIGHT}Windows Shell Custom Enviroment")
print(" ")
print(f"{Style.BRIGHT}Credits for built-in commands go to Orion")
print(" ")
print(f"{Style.BRIGHT}{Fore.CYAN}WSCE{Style.RESET_ALL} - {Style.BRIGHT}Developed By Orion 27/8/24")
print(" ")
# Orion was here 25/08/24 12:28 BST
