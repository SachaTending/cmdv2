from re import S
from stringprep import c22_specials
def test(*cmd):
    print(cmd)

def init(shell, cmd, colors):
    global s, c, c2
    s = shell
    c = cmd
    c2 = colors
    s.addcmd("test", test)
    print("example plugin loaded xd")