import sys, glob, os

plugs = []

def load(shell, colors, cmd):
    global plugs
    oldpwd = os.getcwd()
    sys.path.append(f"{oldpwd}/plugins")
    os.chdir("plugins")
    for i in glob.glob("*"):
        try: plugs.append(__import__(i[:-3]))
        except: 
            try: 
                if i != "__pycache__": plugs.append(__import__(i))
            except: pass
    sys.path.remove(f"{oldpwd}/plugins")
    os.chdir(oldpwd)
    for i in plugs:
        try: i.init(shell, cmd, colors)
        except Exception as e: 
            print(e)
            plugs.remove(i)