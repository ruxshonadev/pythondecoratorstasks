# WHILE TASKS
#1
# i = 1
# while i <= 5:
#     print(str(i) * i)
#     i += 1

#2
# son= 555
# yigindi= 0
#
# while son > 0:
#     nomer= son % 10
#     yigindi= yigindi +nomer
#     son=son//10
# print(yigindi)
#
# son= 8125
# yigindi= 0
#
# while son > 0:
#     nomer= son % 10
#     yigindi= yigindi +nomer
#     son=son//10
# print(yigindi)

#3

# i=1
# a=0
# while i<=100:
#     if  i % 2==1:
#         a+=i
#     i+=1
# print(a)

#3
# sonlar=[66,21,33,77,99]
# i=0
# katta1=0
# katta2=0
#
# while i<len(sonlar):
#        if sonlar[i]==katta1:
#            katta2=katta1
#            katta1=sonlar[i]
#        elif sonlar[i]==katta2 and sonlar[i]!=katta1:
#            katta2=sonlar[i]
#            i=i+1
#            print("2-eng katta son: " ,katta2)

#4
#
# import random
#
# def taxmin_oyini():
#
#     secret = random.randint(1, 100)
#
#     print("1 dan 100 gacha son taxmin yozing!")
#
#     while True:
#
#         guess_input = input("Taxminingiz: ")
#
#
#         try:
#             guess = int(guess_input)
#         except ValueError:
#             print("Iltimos, butun son kiriting!")
#             continue
#
#
#         if guess > secret:
#             print("JUDA BALAND!")
#         elif guess < secret:
#             print("JUDA PAST!")
#         else:
#             print("Tabriklayman! SZ Yuttingiz:", secret)
#             break
#
# if __name__ == "__main__":
#     taxmin_oyini()




#WHILE SIKLI
#1
# trafficlightclr=input("svetafor qaysi rangda?: ")
#
# while  trafficlightclr!="qizil" and trafficlightclr!="sariq" and trafficlightclr!="yashil":
#     print("Xato rang")
#     trafficlightclr=input("svetafor qaysi rangda?: ")
#
# print("Rahmat, togri keladi!")

#2
# import random
# random_number = random.randint(1,10)
# SON= int(input("sonni kiriting!: "))
# while SON!=random_number:
#     print("xato, qayta urinib koring! ")
#     SON= int(input("sonni kiriting!: "))
# print("siz togri topdinigz, TABRIKLAYMIZ!!!")

#3
# friends = []
# ism = input("Dostingizni ismini kiriting!: ")
# while ism != "stop":
#     friends.append(ism)
#     ism =input("Dostingizni ismini kiriting!: ")
# print(friends)

#4
# valuta_usd = 12000
# while True:
#     summa = input("So'm miqdorini kiriting (yoki 'exit' deb yozing=dasturdan ciqasiz!!!)): ")
#     if summa.lower() == "exit":
#         print("Dastur tugadi. Rahmat szga!")
#         break
#     try:
#         su_miqdori = float(summa)
#         dollar = su_miqdori / valuta_usd
#         print(f"{su_miqdori} so'm = {dollar:.2f} USD")
#     except ValueError:
#         print("Iltimos, raqam kiriting yoki 'exit' deb chiqish yozing.")









