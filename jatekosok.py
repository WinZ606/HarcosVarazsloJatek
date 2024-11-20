import random

class jatekosok:
    def __init__ (self,nev="Játékos",poz:int=0,kaszt:str="",emo:str=""):
        self.nev = nev
        self.poz = poz
        self.kaszt = kaszt
        self.emo = emo
        self.hp = 3 + random.randint(1,6)

    def set_poz(self):
        self.poz = random.randint(0,2)

    def set_hp(self):
        self.hp = self.hp - random.randint(0,1)

    def __str__(self):
        return f"Név: {self.nev}, Pozició: {self.poz}, Kaszt: {self.kaszt}, HP: {self.hp}, Fej: {self.emo}"