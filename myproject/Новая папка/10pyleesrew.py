#FOR sikli
# royxat ustida

# mevalar = ['olma' , 'banan','gilos']   #3ta elementli royxat yaratildi
# for meva in mevalar:                   #har bir elementni navbatma_navbat oladi
#     print(meva)                        #ekranga chiqaradi






# ismlar = ["Ali", "Vali", "Soli"]
#
# for ism in ismlar:
#     print(ism)

#
# nums = [2, 4, 6, 8, 10]
#
# for num in nums:
#     print(num+3)


# sonlar = [1, 2, 3, 4, 5, 6]
#
# for son in sonlar:
#     if son%2 ==0:
#         print(son)

#
# sonlar = [10, 20, 30, 40, 50]
#
# for son in sonlar:
#     print(son -5 )

# ismlar = ["ali", "vali", "soli"]
#
# for ism in ismlar:
#     print(ism.capitalize())


#
#
# sonlar = [1,2,3,4,5]
# yigindi = 0
#
# for son in sonlar:
#     yigindi = yigindi+son
# print(yigindi)









##############

# sonlar = [2, 4, 6, 8, 10]
# yigindi = 0
# for son in sonlar:
#    yigindi=yigindi+son        #yigindisni chiqardi
# print(yigindi)


# ismlar = ["hasan", "husan", "alibek"]
#
# for ism in ismlar:
#     print(ism.capitalize())  #ismni bosh harflarini hammasini katta bilan yozib beradi


# sonlar = [1, 2, 3, 4, 5, 6, 7, 8]
#
# for son in sonlar:
#     if son %2 !=0:    #  faqat toq sonlarni chiqaradi
#         print(son)


# sonlar = [5, 12, 3, 18, 7, 20]
#
# for son in sonlar:
#     if son>10:          #faqat 10dan katta sonlarni print qiladi
#         print(son)

#
# sonlar = [1, 2, 3, 4, 5]
#
# for son in sonlar:
#     print(son**2)     #sonni kvadratini chiqarb beradi



# #
# sonlar = [3, 7, 1, 9, 4, 2]
#
# eng_kichik = sonlar[0]
# for son in sonlar:
#     if son < eng_kichik:
#         eng_kichik = son
# print(eng_kichik)





















# ``` 1. Elektron Pochta Manzillarini Tekshirish:
# Email manzillar ro'yxati berilgan:
# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for sikli va string metodlari yordamida har bir email manzilida "@" belgisi
# bor-yo'qligini tekshiring: Agar bo'lmasa, "Noto'g'ri email: email_manzi" deb
# chiqaring. ```

# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
#
#
# for email in pochtalar:
#     if "@" in email:
#         print(f'Togri email {email}')
#     else:
#         print(f'notogri email {email}')

#2
# passwords =(["password123", "Qwerty!", "admin", "StrongPass1!"])
#
# for password in passwords:
#     if len(password) < 8:
#         print(f"Juda qisqa parol: {password}")
#     elif any(not c.isalpha() for c in password):
#         print(f"Kuchsiz parol:{password}")
#     else:
#         print(f'Kuchli parol :{password}')


#3
#
# tempratures = ([20,22, 19, 24, 25, 23, 21])
#
# ortaca = sum(tempratures)/len(tempratures)
# print("ortaca harorat", ortaca)
#
# for temprature in tempratures:
#     if temprature > 22:
#         print("Iliq kun")
#     else:
#         print("Salqin kun")

#4

#
# taomlar =["osh","shashlik","manti","lagmon"]
#
# buyurtma = input("Iltmos, buyurtmangzini kiriting!")
#
# for taom in taomlar:
#     if buyurtma ==taom:
#         print("Buyurtmangzi qabul qilindi!")
#         break
# else:
#         print("Kecirasiz ,bizda bunday taom  yoq")


# anketa tahlili

# user_ages = [16,21,17,30,25]
#
# for age in user_ages:
#     if age<18:
#         print("Yosh chegarasiga yetmagan!")
#     else:
#      print("Xush kelibsiz!")

# mobil ilova bildirishnomalri
#
# xabarlar = ["Yangi xabar","Btareya past","Yangilanish mavjud"]
#
# for xabar in xabarlar:
#     if xabar=="Batareya past":
#         print("Telefoningizni quvvatlang!")


#Fayllarni guruhlash
# fayllar = [ "kitob.jpg", "ko_ jiguli.mp3", "tabiat.jpg"," malohat.mp3", "iphone16.jpg"]
#
# musiqalar = []
# rasmlar = []
#
# for i in fayllar:
#     if i.endswith(".mp3"):
#         musiqalar.append(i)
#     elif i.endswith(".jpg"):
#         rasmlar.append(i)
#
# print("Musiqalar: ", musiqalar)
# print("Rasmlar: ", rasmlar)









