from jatekosok import jatekosok

class jatekter:
    def __init__(self):
        self.harcos = jatekosok("Tubamtolo", 0, "Harcos", "😎")
        self.varazslo = jatekosok("Waar'Ash Low", 3, "Varázsló", "🥳")
        self.lista = ["_","_","_","_"]
        self.lista[self.harcos.poz] = self.harcos.emo
        self.lista[self.varazslo.poz] = self.varazslo.emo
        self.kor = 1
        self.kiir()
    
    def kiir(self):
        print(f"{self.kor}. kör")
        print("*"*24," ","-"*28," ","-"*30)
        print(f"*{self.lista}*"," ",f"| A Tubamtolo életereje: {self.harcos.hp} |"," ",f"| A Waar'Ash Low életereje: {self.varazslo.hp} |")
        print("*"*24," ","-"*28," ","-"*30,"\n" )

    def kiir2(self):
        print(f"{self.kor}. kör")
        print("*"*22," ","-"*28," ","-"*30)
        print(f"*{self.lista}*"," ",f"| A Tubamtolo életereje: {self.harcos.hp} |"," ",f"| A Waar'Ash Low életereje: {self.varazslo.hp} |")
        print("*"*22," ","-"*28," ","-"*30,"\n" )

    def jatekmenet(self):
        while (self.harcos.hp > 0 and self.varazslo.hp > 0):
            self.harcos.set_poz()
            self.varazslo.set_poz()
            self.lista = ["_","_","_","_"]
            self.lista[self.harcos.poz] = self.harcos.emo
            self.lista[self.varazslo.poz] = self.varazslo.emo

            if (self.harcos.poz == self.varazslo.poz):
                self.lista[self.varazslo.poz] = "⚔"
                self.harcos.set_hp()
                self.varazslo.set_hp()
            self.kor += 1
            self.kiir2()
    
    def kinyert(self):
        if (self.varazslo.hp <= 0):
            print("A harcos nyert!\n")
        else:
            print("A varázsló nyert!\n")