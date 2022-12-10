# Imports
import cmd
import os, sys
import socket
import glob

# Initialize colors first
colors = cmd.color.Colors()

# Print motd
print("Welcome to",colors.get_color("Fore", "green"),end="")


def genps1():
    return f"[{os.getlogin()}@{socket.gethostname()} {os.getcwd()}]: "

def run(cmd): os.system(" ".join(cmd))

def exit(*cmd): 
    if cmd == []: code = 0
    else: code = cmd[0]
    print("Bye!")
    sys.exit(code)

def cd(*cmd): os.chdir(cmd[1])

def ls(*cmd):
    if cmd == ("ls",):
        print("\n".join(glob.glob("*")))
    else:
        print("\n".join(glob.glob(cmd[1])))

# Initialize base shell

shell = cmd.shell.Shell(ps1=genps1, name="CMDv2", nocmd=run)

shell.addcmd("exit", exit)
shell.addcmd("cd", cd)
shell.addcmd("ls", ls)

# Print name
print("CMDv2!")

# Load plugins

colors.print_color(colors.get_color("Fore", "white"))

cmd.plugins.load(shell=shell, cmd=cmd, colors=colors)

try: shell.run()
except KeyboardInterrupt: print("Bye!");input()