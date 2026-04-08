def hanoiminar(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"1-diskni {from_rod} ustundan {to_rod} ustunga ko‘chirildi")
        return

    hanoiminar(n-1, from_rod, aux_rod, to_rod)

    print(f"{n}-diskni {from_rod} ustundan {to_rod} ustunga ko‘chirildi")
    hanoiminar(n-1, aux_rod, to_rod, from_rod)
n =  int(input("disklar sonini yozing!"))
hanoiminar(n, n-1, n, n)