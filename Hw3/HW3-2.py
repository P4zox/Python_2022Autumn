class COD:
    def __init__(self,name,win,kd):
        self.name=name
        self.win=win
        self.kd=kd
    def stats(self):
        print(self.name+" has "+str(self.win)+" wins, and has "+str(self.kd))

player1=COD("SKTB_Halston",17,0.68)
player2=COD("Louie",0,0.0)
player1.stats()
player2.stats()