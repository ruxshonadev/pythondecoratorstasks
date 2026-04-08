# class Talaba:
#     # Konstruktor
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#         print(f"{ism} nomli talaba yaratildi!")
#
#     def malumot(self):
#         print(f"Ism: {self.ism}, Yosh: {self.yosh}")
#
#
# # Ishlatish
# t1 = Talaba("Ali", 20)  # "Ali nomli talaba yaratildi!"
# t1.malumot()  # "Ism: Ali, Yosh: 20"
#
# INHERTANCE -vorisdorlik
# class Talaba:
#     def __init__(self, ism):
#         self.ism = ism
#         print(f"{ism} yaratildi")
#
#     # Destruktor
#     def __del__(self):
#         print(f"{self.ism} o'chirildi")
#
#
# # Ishlatish
# t1 = Talaba("Ali")  # "Ali yaratildi"
# del t1  # "Ali o'chirildi"
#
#
# # OTA KLASS
# class Odam:
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#
#     def yurish(self):
#         print(f"{self.ism} yuryapti")
#
#
# # BOLA KLASS - Odam'dan meros oladi
# class Talaba(Odam):  # Qavsda ota klassni yozdik
#     def __init__(self, ism, yosh, kurs):
#         super().__init__(ism, yosh)  # Ota konstruktorini chaqiramiz
#         self.kurs = kurs
#
#     def oqish(self):
#         print(f"{self.ism} {self.kurs}-kursda o'qiyapti")
#
#
# # Ishlatish
# t1 = Talaba("Ali", 20, 3)
# t1.yurish()  # Ota klassdan kelgan: "Ali yuryapti"
# t1.oqish()  # O'zining metodi: "Ali 3-kursda o'qiyapti"
#
#
#
# class Hayvon:
#     def tovush(self):
#         print("Hayvon tovush chiqaradi")
#
# class Mushuk(Hayvon):
#     def tovush(self):  # Qayta yozdik
#         print("Miyov! 🐱")
#
# class It(Hayvon):
#     def tovush(self):  # Qayta yozdik
#         print("Vov-vov! 🐕")
#
# # Ishlatish - BU POLIMORFIZM!
# hayvonlar = [Mushuk(), It(), Hayvon()]
#
# for h in hayvonlar:
#     h.tovush()  # Har biri o'ziga xos tovush chiqaradi

# Natija:
# Miyov! 🐱
# Vov-vov! 🐕
# Hayvon tovush chiqaradi




#polimorfizm
# class Hisoblash():
#     def natija(self,a,b):
#         pass
#
# class   Qoshish(Hisoblash):
#     def natija(self,a,b):
#         return a+b
#
# class Ayirish(Hisoblash):
#     def natija(self,a,b):
#         return a-b
#
#
# class Kopaytirish(Hisoblash):
#     def natija(self,a,b):
#         return a*b
#
# class Bolish(Hisoblash):
#     def natija(self,a,b):
#         return a/b
#
#   #POLIMORFIZM BU - BIR HIL METOD TURLI NATIJA
# amallar = [Qoshish(),Ayirish(),Kopaytirish()]
#
# for amal in amallar:
#     print(amal.natija(3,7))



    #2

# class Ovqat():
#     def __init__(self, nom):
#         self.nom = nom
#
#     def Tayyorlash(self):
#         print(f" {self.nom} tayyorlanmoqda")
#
# class Pitsa(Ovqat):
#     def Tayyorlash(self):
#         print(f" {self.nom} xamir yoyildi, pech qyoqildi ,pechga qo`yildi 15-daqiqa")
#
#
# class Osh(Ovqat):
#     def Tayyorlash(self):
#         print(f"{self.nom} go`sht qovurildi, guruch qo`shildi, damga qo`yildi")
#
# class Lagmon(Ovqat):
#     def Tayyorlash(self):
#         print(f"{self.nom} xamir qo`shildi,sho`rva tayyorlandi- 30daqiqa")
#
#
# class Burger(Ovqat):
#     def Tayyorlash(self):
#         print(f"{self.nom} kotlet qovurildi,non qizdirildi, yigildi 10daqiqa")
#
#
# menu = [
#     Pitsa("pereperoni pitsa"),
#     Osh("xorazm oshi"),
#     Lagmon("uygur lagmon"),
#     Burger("cheeseberger")
# ]
#
# print("====== BUGUNGI MENU ======")
# for ovqat in menu:
#     ovqat.Tayyorlash()
#     print()



#20
class Bank:
    def __init__(self, nom, balans):
        self.nom = nom
        self.balans = balans

    def malumot(self):
        print(f"🏦 Bank: {self.nom}")
        print(f"💰 Balans: {self.balans} so'm")


class Omonat(Bank):
    def __init__(self, nom, balans, foiz):
        super().__init__(nom, balans)  # ✅ Ikkalasini ham yuborish
        self.foiz = foiz

    def hisoblash(self):
        daromad = self.balans * self.foiz / 100
        print(f"📈 Omonat foizi: {self.foiz}%")
        print(f"💵 Yillik daromad: {daromad} so'm")
        return daromad


class Kredit(Bank):
    def __init__(self, nom, balans, qarz):
        super().__init__(nom, balans)
        self.qarz = qarz

    def hisoblash(self):
        qolgan = self.qarz - self.balans
        print(f"💳 Qarz miqdori: {self.qarz} so'm")
        print(f"❗ Qolgan qarz: {qolgan} so'm")
        return qolgan


# ===== OB'EKTLAR YARATISH =====

print("=" * 40)
omonat1 = Omonat("Asakabank Omonat", 10000000, 15)
omonat1.malumot()
omonat1.hisoblash()

print("\n" + "=" * 40)
kredit1 = Kredit("Ipoteka krediti", 50000000, 200000000)
kredit1.malumot()
kredit1.hisoblash()

print("\n" + "=" * 40)

# ===== POLIMORFIZM =====
print("📊 POLIMORFIZM NAMOYISHI:\n")

hisoblar = [
    Omonat("Tejamkor", 5000000, 12),
    Kredit("Avto kredit", 20000000, 80000000)
]

for hisob in hisoblar:
    print(f"\n🔹 {hisob.nom}")
    hisob.hisoblash()  # ✅ Har biri o'z usulida hisoblaydi!
    print("-" * 30)

