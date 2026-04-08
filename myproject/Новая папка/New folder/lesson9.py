# 1. ob-havo tavsifi

obhavo=int(input("Bugun ob-havo harorati qanday?"))

if 20>=obhavo :
    print("Bugun havo salqin")
elif 30>=obhavo:
    print("Bugun havo iliq")
else:
    print("Bugun havo issiq")

#2 Internet-do`kon chegirmasi
# pul=int(input("xarid summangizni kiriting"))
# if pul>=50000:
#     print("chegirma yo`q")
# elif pul>= 50:
#     print("5% chegirma")
# elif pul>=100:
#     print("10% chegirma")
# else:
#     print("100% chegirma")

#3 Tizimga kirish
# login="admin"
# password="12345"
#
# user_login=input("Enter your login: ")
# user_password=input("Enter your password: ")
#
# if user_login==login and user_password==password:
#     print("Login Successful!")
# else:
#         print("Login or password is wrong?!")

# 4 Film yosh cheklovi
# yosh=int(input("Enter your age: "))
#
# if yosh<13:
#     print('sizga ushbu film tavsiya etilmaydi')
# elif yosh>=13 and yosh<=17:
#     print('siz filmni ota -onangiz bilan korishingiz mumkin')
# elif yosh>=18 :
#     print("siz filmni tomosha qilishiz mumkin")

#5 Restoran menyusi
# Menu=int(input("menyudan taom tanlang: 1.Osh,2.Mastava,3.Shashlik"))
#
# if Menu==1:
#     print("50som,15min")
# elif Menu==2:
#         print("20som,10min")
# elif Menu==3:
#     print("10som,5min")

#6 Email tekshiruvi
# Email tekshiruvi
# email = input("Enter your email: ")
#
# if "@" in email and "." in email:
#     print("Email topildi")
# else:
#     print("Email noto'g'ri")

#7 Talaba baholash tizimi
# baho=int(input("enter your ball: "))
#
# if baho>=86 and baho<=100:
#     print("5 baho")
# elif baho>=70 and baho<=85:
#     print("4 baho")
# elif baho >=0 and baho<55:
#     print(" 2baho")

#8 Bankomatdan pul yechish
# cardsumma=int(input("Kartadagi summani kiriting"))
# yechmoqsum=int(input("Yechmoqchi bolgan summani kiriting"))
#
# if yechmoqsum <= 5000:
#      print("minimal yechish summasi 5000")
# elif yechmoqsum > cardsumma:
#     print("hisobda mablag yetarki emas")
# else:
#     qoldiq = cardsumma - yechmoqsum
#     print(f"Pul muvaffaqiyatli yechildi. Qoldiq: {qoldiq} som")

#9 ish jadvalini tekshirish
# haftakuni=input("hafta kunini ayting: ")
#
# if haftakuni== "Shanba" or haftakuni=="Yakshanba":
#     print("bugun dam olish kuni")
# else:
#     print("bugun ish kuni")

#10 Mobil tarif tanlash
# GB=int(input(" oyiga qancha gigabaytdan foydalanasiz?: "))
# if GB<=1:
#     print("sizga Mini tarif mos keladi")
# elif GB>=1 and GB<=5:
#     print("sizga standart tarifi mos keladi")
# elif GB>=5:
#     print("sizga unlimited tarifi mos keladi")
