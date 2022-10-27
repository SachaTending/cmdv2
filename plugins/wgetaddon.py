import wget as w

def wget2(c, file, savepath=None):
    w.download(file, savepath)
    print()
    print("Done!")

def init(s, c, colors2):
    global shell, cmd, colors
    shell = s
    cmd = c
    colors = colors2
    shell.addcmd("wget", wget2)
    print("Wget loaded!")