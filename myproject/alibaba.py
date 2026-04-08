import random



class Qahramon:
    def __init__(self, ism , sogliq, x, y):
        self.ism = ism
        self.sogliq = sogliq
        self.pos_x = x
        self.pos_y = y
        self.sumka = []

class Dushman:
    def __init__(self, nomi,ziyon, x,y):
        self.nomi = nomi
        self.ziyon = ziyon
        self.pos_x = x
        self.pos_y = y

    def random_move(self, rows, cols):
        yurish = random.choice(['w', 's', 'a', 'd'])

        if yurish == 'w' and self.pos_x > 0:
            self.pos_x -= 1
        elif yurish == 's' and self.pos_x < rows - 1:
            self.pos_x += 1
        elif yurish == 'a' and self.pos_y > 0:
            self.pos_y -= 1
        elif yurish == 'd' and self.pos_y < cols - 1:
            self.pos_y += 1


class  Buyum:
    def __init__(self,nomi,effekt,x,y):
        self.nomi = nomi
        self.effekt = effekt
        self.pos_x = x
        self.pos_y = y

qahramon  = Qahramon("Yusuf",100,0,0)

dushman = Dushman("Yovuz",30,3,3)

buyum = Buyum("sehrli dori", 20,2 ,4)

x_x, x_y =4 ,4


while qahramon.sogliq > 0:
    print(f"\nSogliq: {qahramon.sogliq} I  Sumka:{len(qahramon.sumka)} ta buyum")
    print("=" * 30)

    for r in range(5):
        qator = ""
        for c in range(5):

            if r == qahramon.pos_x and c == qahramon.pos_y:
                qator += "[Q]"
            elif r == dushman.pos_x and c == dushman.pos_y:
                qator += "[D]"
            elif r == x_x and c == x_y:
                qator += "[X]"
            elif buyum and r == buyum.pos_x and c == buyum.pos_y:
                qator += "[B]"
            else:
                qator += "[]"
        print(qator)

    if qahramon.pos_x == x_x and qahramon.pos_y == x_y:
        print("GALABA MUBORAK XAZINA SIZNIKI!!!")
        break

    if buyum and qahramon.pos_x == buyum.pos_x and qahramon.pos_y == buyum.pos_y:
        qahramon.sogliq += buyum.effekt
        qahramon.sumka.append(buyum.nomi)
        print(f"\n{buyum.nomi}ni  yedingiz! Sog'liq +{buyum.effekt}")
        buyum = None

    if qahramon.pos_x == dushman.pos_x and qahramon.pos_y == dushman.pos_y:
        qahramon.sogliq -= dushman.ziyon
        print(f"\nDushman jarohatladi! Sog'liq: {qahramon.sogliq}")
        if qahramon.sogliq <= 0:
            print("O'yin tugadi!")
            break

    yurish = input("W/A/S/D: ").lower()
    if yurish == 'w' and qahramon.pos_x > 0:
        qahramon.pos_x -= 1
    elif yurish == 's' and qahramon.pos_x < 4:
        qahramon.pos_x += 1
    elif yurish == 'a' and qahramon.pos_y > 0:
        qahramon.pos_y -= 1
    elif yurish == 'd' and qahramon.pos_y < 4:
        qahramon.pos_y += 1

    dushman.random_move(5, 5)
