import os
import platform

current_os = platform.system()

if current_os == "Windows":
	os.system("cls")
elif current_os == "Linux" or current_os == "Darwin":
	os.system("clear")
