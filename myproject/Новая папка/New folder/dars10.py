# savol = input("Savol: nimalarga qiziqasiz? ")
#
# if savol.find("sport") >= 0:
#     if savol.find("futbol") >= 0:
#         print("Sizga qaysi komanda yoqadi")
#     elif savol.find("valleybol") >= 0:
#         print("Siz qaysi valleybolistlarimizni bilasiz?")
#
# if savol.find("kitob") >= 0:
#     if savol.find("detektiv") >= 0:
#         print("Shaytanat kitobi haqida fikringiz?")
#     elif savol.find("islom") >= 0:
#         print("Sizga Hadis va hayot kitoblarini sovga qilamiz!")

#1 Elektron pochta maznillarini tekshirish

# pochtalar= ["user1@gmail.com", "user2yahoo.com", "user3outlook.com"]
#
#
# for email  in pochtalar:
#     if "@" not in email:
#         print( "notogri email" ,email)

#2 Parol kuchini tekshirish
#
# parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# maxsus_belgilar = "!@#$%^&*()"
#
# for parol in parollar:
#     if len(parol) < 8:
#         print("Juda qisqa")
#     else:
#         raqam_bor = False
#         maxsus_belgi_bor = False
#
#         for belgi in parol:
#             if belgi.isdigit():
#                 raqam_bor = True
#             if belgi in maxsus_belgilar:
#                 maxsus_belgi_bor = True
#
#         if not raqam_bor or not maxsus_belgi_bor:
#             print("Kuchsiz parol")
#         else:
#             print("Kuchli parol")

#3  Ob havo malumotlarini tahlil qilish

# degrees = [20, 22, 19, 24, 25, 23, 21]
#
# ortacha = sum(degrees) / len(degrees)
#
# print("O'rtacha harorat:", ortacha)
#
# for degree in degrees:
#     if degree > 22:
#         print("Iliq kun")
#     else:
#         print("Salqin kun")

#4 Restoran buyurtmalari
# taomlar = ["Osh", "Shashlik", "Manti", "Lag'mon"]
#

# buyurtma = input("Taom nomini kiriting: ")
#

# topildi = False

# for taom in taomlar:
#     if buyurtma == taom:
#         topildi = True

# if topildi == True:
#     print("Buyurtmangiz qabul qilindi")
# else:
#     print("Kechirasiz, bunday taom yo'q")

#5  Anketa tahlili
# yoshlar = [16, 21, 17, 30, 25]

# for yosh in yoshlar:
#     if yosh < 18:
#         print("Yosh chegarasiga yetmagan")
#     else:
#         print("Xush kelibsiz")

#6 Mobil ilova bildirishnomalari
# xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
#
# for xabar in xabarlar:
#     if xabar == "Batareya past":
#         print("Telefoningizni quvvatlang")

#7# Fayllarni guruhlash
# fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone16.jpg"]
#
#
# musiqalar = []
# rasmlar = []
#
# for fayl in fayllar:
#     if fayl.find(".jpg") != -1:
#         rasmlar.append(fayl)
#     elif fayl.find(".mp3") != -1:
#         musiqalar.append(fayl)
#
# print("Rasmlar:", rasmlar)
# print("Musiqalar:", musiqalar)














