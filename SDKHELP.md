# How to make your own WSCE commands

Welcome to the WSCE SDK Documentation, this guide will help you to make your own command for WSCE

# Step 1: Understanding how the commands work

Commands in WSCE are incredibly simple, First of all go to WSCEMAIN, You should see a COM Folder like this

![image](https://github.com/user-attachments/assets/c40516ab-8312-49b7-81d3-f560b5cda891)

That folder is where all the Non-Built-in WSCE Commands are stored, and is also where you will be storing your own custom WSCE Command

But thats not all!

You might notice that in COM all the commands have their own seperate folder, this is because commandsearch (The script that automatically searches for custom commands) needs 2 files, these files are

- (conmandname).inf (Contains all the information needed for commandsearch)
- (commandname).py (Contains the actual code for your command)

And thats all you need to understand, now, lets get to making a command shall we?

# Step 2: Creating your project folder

First of all, you need to make a folder to store your files inside, this is called the Project Folder and can really be called whatever you want, but it's recommended to relate the name to your command

# Step 3: Creating <commandname>.inf

Now we need to make a .inf file, this is so commandsearch can get the information needed by WSCE to make your command work, yet again the inf file can be called whatever you want, but the name is important for later so dont make it complex

Now you have made the .inf file, We need to add it with the information WSCE needs for your command to work, so complete your .inf file with the following lines

```
[WSCE] # This tells commandsearch that this is a .inf file compatible with the WSCE command configuration
commandname=COMMAND-NAME-GOES-HERE # This is what the user will type to run your command
commanddesc=Command Description Goes Here # This is the description the user will see when running the "help" command in WSCE, so make it short, but straightforward, and explains what your command does
```

And that's all the information WSCE needs, now let's make the actual python code for your command

# Step 4: Coding the command

WSCE uses regular python, there is nothing special to it, meaning anything that can be coded in python can be coded in WSCE

First of all, an important note before you get started, the .py file **NEEDS TO HAVE THE SAME NAME AS THE .inf FILE**

Now for the code? Nothing is required, just ensure it's linux and windows compatible so that all users can run the command, if there is no way to make it cross-compatible, that's fine, just list in your command description what OS'es your command is compatible with

# Step 5: Good luck with making your command, And thank you for contributing to the WSCE Community

# Want to contribute even more?

Want to contribute to the WSCE Project even more? Point out issues or fix bugs in the code to make WSCE a bug-free project Or even better, DM Suggestions to me at orion_0r10n to make WSCE An even better project


Orion 04/09/2024
