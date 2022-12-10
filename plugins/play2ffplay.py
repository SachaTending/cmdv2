import os

def ffplay(cmd, *argv):
    os.system(f"ffplay \"{' '.join(argv)}\"")

def init(shell,*other):
    shell.addcmd("play", ffplay)