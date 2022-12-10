import traceback

class Shell:
    def __init__(self, ps1, name: str="null", nocmd=None):
        self.name = name
        self.ps1 = ps1
        self.cmdlist = {}
        if nocmd != None: self.nocmd = nocmd
    def getinput(self):
        return input
    def addcmd(self, cmdn: str, cmd):
        self.cmdlist[cmdn] = cmd
    def run(self):
        while True:
            try:
                cmd = self.getinput()(self.ps1()).split()
                if len(cmd) != 0:
                    if cmd[0] in self.cmdlist:
                        try: self.cmdlist[cmd[0]](*cmd)
                        except Exception as e:
                            print(f"Error while executing {cmd[0]}:")
                            print(e)
                    else: self.nocmd(cmd)
            except SystemExit: break
            except: pass

    def nocmd(self, cmd):
        print(f"{cmd[0]}: command not found")
