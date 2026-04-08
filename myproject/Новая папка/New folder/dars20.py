#Astrum mehmonxonasi

def main():
    print("ASTRUM Mehmonxonasiga xush kelibsiz!")

    while True:
        print("\n" + "="*30)
        print("1-Mehmon qo`shish")
        print("2-Mehmonni ro`yxatdan chiqarish")
        print("3- Mehmonlar ro`yxatini ko`rish")
        print("4-Chiqish")
        print("\n" + "="*35)

        tanlov = input("Tanlang:  ")
        if tanlov =="1":
            mehmon_qoshish()
        elif tanlov =="2":
                mehmon_chiqarish()
        elif tanlov =="3":
            royxatni_korish()
        elif tanlov =="4":
            chiqish()
        break

def mehmon_qoshish():
    print("\n=====Yangi Mehmon qo`shish======")
    ism= input("ism:  ")
    tel=input("tel: ")

    with open("mehmonlar.txt", "a") as f:
        f.write(f"{ism},{tel}\n")

    print(f"{ism} qo`shildi" )


def mehmon_chiqarish():
    print("Mehmon chiqarish")
    try:
        with open("mehmonlar.txt", "r") as f:
            hammasi = f.readlines()
    except:
        print("Fayl yo'q")
        return

    ism = input("Kim chiqyapti? ")
    with open("mehmonlar.txt", "w") as f:
        for qator in hammasi:
            if ism in qator:
                yangi = qator.replace("mehmonda", "chiqdi")
                f.write(yangi)
                print(f"{ism} chiqdi!")
            else:
                f.write(qator)


def royxatni_korish():
    print("\n=====MEHMONLAR======")

    try:
        with open("mehmonlar.txt", "r") as f:
            mehmonlar = f.readlines()

        for mehmon in mehmonlar:
            print(f"  - {mehmon.strip()}")
    except:
        print("Hozircha mehmon yo'q")

def chiqish():
    print("\n Xayr Dastur tugadi!")
    exit()

if __name__ == "__main__":
    main()









