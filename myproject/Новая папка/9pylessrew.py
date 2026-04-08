#string and list slicing

# matn = "salom dunyo"
# matnn1 = matn[0:2]   #0 dan 2-indexgacha  kseib oladi
# print(matnn1)

# matnn2 = matn[:5]   #5-indexggacah kesib olib beradi
# print(matnn2)

# matn = "salom dunyo"
# matnn1 = matn[0:] #   0dan boshlab listni oxirigacha kesvoladi
# print(matnn1)

# num = [1,2,4,3,6,2,6,6,9]
# numm = num[4:]   #indexi 4 -dan boshlab oxirigacha keib oladi
# print(numm)

# num = [0,1,2,3,4,5,6,7,8,9,10]
# num1 = num[1:11:2]   #0 (begin)dan 11(end)gacha 2(step)talab sana
# print(num1)

# matn = "72576427648790"
# matnn = matn[::-1]   #-1 hisobiga string teskari qilib kesib beradi
# print(matnn)
#
# matn = "72576427648790"
# matnn = matn[::-2]   #-2 hisobiga string teskari qilib 2tadan sanab kesib beradi
# print(matnn)

































#Conditions - if elif else
# print("Saylovga xuhs kelibsiz")
# user = input("Enter your name: ")
# age = int(input("Enter your age: "))
# if age < 18:
#     print("Yoshingiz yetmaydi ruxsat yoq")
# else:
#     print("Xush kelibsiz!")

# print(15!=15)     #false qaytaradi
# print(15==15)    #true qaytradi



# arr = [1,2,3,4,5,6]
# print(15 in arr)  #arrayni ichidami 15?  false qaytaradi
# print(2 in arr) # arrayni ichidami 2? True qaytaradi
# print(15  not in arr)   #ichida emasmi? True qaytaradi, yoq


#
# yosh = int(input("Yoshingiz:  "))
# if yosh < 18:
#     print("Voyaga yetmagan")
# elif yosh >= 18 and  yosh < 30:
#     print("Yoshlar toifasi")
# elif yosh>=30 and  yosh<60:
#     print("orta yosh")
# else:
#     print("qariya")


# login = "admin"
# password = "qwerty"
#
# user_login = input("Enter your username: ")
# user_password =input("Enter your password: ")
# if user_password == password and user_login == login:      # AND 2ala variant ham togri bolsagina true chiqaradi
#     print("Login Successful")
# else:
#     print("Login Failed")





# parol = "qwerty"
# parol2= "1234"
# parol3 = "asdf"
#
# user_parol =input("Please enter your password: ")
# if user_parol == parol or user_parol ==parol2 or user_parol ==parol3:    #OR  2ala variantdan 1tasi togri bolsa ham true chiqaradi
#     print("Ruxsat")
# else:
#      print("parol yoki login xato")



#1
# a = int(input("Enter a number: "))
# if a<0:
#     print("manfiy")
# else:
#     print("musbat")

#2
# a = int(input("A: "))
# b = int(input("B: "))
# if a>3 and b<=6:
#     print(True)
# else:
#     print(False)


#3
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# c = int(input('Enter another number: '))
#
# if a<b<c:
#     print("ROST")
# else:
#     print("Yolgon")

#
# a = int(input("A: "))
#
# if a%2==0:
#     print("Juft")
# else:
#     print("Toq")



#
# a = int(input('A: '))
# if a % 2 == 0 and len(str(a)) == 2:       # sonni juft va 2xonaliligini isbotlash uchun
#     print("Rost")
# else:
#     print("yolgon")

# sonlar teng emasligini isbotlash
# nums = input("NUMBERS ENTERED: ")
# if nums[0]==nums ==[1] and nums[1]==nums[-1]:
#     print("sonlar teng emas")
# else:
#     print("sonlar teng")

# son = int(input("hafta kunini kiriting"))
# if son ==1:
#     print("Dushanba")
# elif son ==2:
#     print("Seshanba")
# elif son ==3:
#     print("Chorshanba")
# elif son==4:
#         print("Payshanba")
# elif son ==5:
#     print("Juma")
# elif son ==6:
#     print("Shanba")
# else:
#     print("Yakshanba")



#shaxmat doskasi yurishi
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
#
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))
#                        #abs = moduli
# if abs(x1 - x2) > abs(y1 - y2):
#     print('bora oladi')
# else:
#     print("bora olmaydi")

















##################################













#str lst slicing task
#1
# s = "Python"
# x = s[0:3]
# print(x)
#
# #2
# nums = [10, 20, 30, 40, 50]
# x = nums[::2]
# print(x)
#3
# s = "abcdefgh"
# s1 = s[0:7:2]
# print(s1)
#4
# s = "salom"
# s1 = s[::-1]
# print(s1)
# #5
# nums = [1, 2, 3, 4, 5, 6, 7]
# x = nums[2:5]
# print(x)


##cgp
#1
# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = nums[::2]   #faqat juft indexdagi larni print qil
# print(x)
#2
# s = "abcdefghi"
# x = s[3:6]  # ortadagi 3 ta harfni kesib oldik "def'
# print(x)
#3
# nums = [1, 2, 3, 4, 5]
# x = nums[::-1]   # slicing yordamida teskari qilib chiqardk
# print(x)
# #4
# s = "abcdefghij"
# x = s[0:10:3]   # har uchinchi harfni ol
# print(x)
# #5
# nums = [10, 20, 30, 40, 50, 60, 70]
# x = nums[-4::][::-1]  # oxirgi 4ta elementini keisb teskari tartibda chiqar
# print(x)
#
#
#
#
#
# #1
# a = [1, 2, 3, 4, 5]
# b = [6, 7, 8, 9, 10]
# x = a[3:]
# x.extend(b[0:2])
# print(x)
#
# #2
# s = "madam"
# print(s==s[::-1])    # soz polindromligini isbotlayapmz
#
# s1 = "level"
# print(s1==s1[::-1])
# #3




















#1
# nums = int(input("Son kiriting: "))
# if nums>0:
#     print("Mmusbat")
# elif nums<0:
#     print("Manfiy")
# elif nums==0:
#     print("Nol")
# else:
#     print("404 error")

#2
# a=2
# b=4
# c=6
# if a>b and a>c:
#     print("A", "big number")
# elif b>c and b>a:
#     print("B","big number")
# elif c>a and c>b:
#     print("C","big number")
# else:
#     print("watchamacallat")

#3
# ball = int(input("Balingizni kiriting darajangizni aytamiz!"))
#
# if 90 <= ball<=100:
#     print("A")
# elif 79<=ball<=89:
#     print("B")
# elif 50<=ball<=69:
#     print("C")
# else:
#     print("D")

#4
# son = int(input("son kiriting iltimos!"))
#
# if son%2==0:
#     print("juft")
# else:
#     print("toq")

#5   OR agar shu berilganlardan 1ttasiyam togri bolsa print ishlaydi
# moon_n = int(input("oy raqamini kiriting:  "))
# if moon_n==12 or moon_n==1 or 2==moon_n:
#     print("Qish")
# elif moon_n==3 or moon_n==4 or 5==moon_n:
#     print("Bahor")
# elif moon_n==6 or moon_n==7 or 8==moon_n:
#     print("YoZ")
# elif moon_n==9 or moon_n==10 or 11==moon_n:
#     print("KUZ")

#




















#

# username= input("Usernamengizni kiriting:  ")
# password = input("Passwordingzini kiriting: ")
#
# if username =="admin" and password =="1234":
#     print("Xush kelibsiz admin!")
# elif username =="admin":
#     print("Parol notogri")
# else:
#     print("Foydalanuchi topilmadi!")



#3
# age = int(input("Iltimos yoshizini kiriting..."))
#
# if 0<=age<=5:
#     print("Bepul")
# elif 6<=age<=12:
#     print("10.000sum")
# elif 13<=age<=17:
#     print("20.000sum")
# elif 18<= age <=64:
#     print("35.000sum")
# elif 65>=age :
#     print("15.000 sum , pensioner chegirma!")
# elif age<0:
#     print("Notogri yosh")
# else:
#     print("xexxexex")




#5
# harorat = int(input("havo haroratini kiriting!.."))
#
# if harorat<0:
#     print("Sovuq, Qolingizga qolqop kiying!")
# elif 0<harorat<=15:
#     print("Salqingina, qalin kiyim kiying!")
# elif 16<=harorat<=25:
#     print("Ajoyib ob havo")
# elif 26<=harorat<=35:
#     print("Issiq, suv iching!")
# elif harorat>35:
#     print("Tashqariga chiqmang, xavo judayam issiq!")
# else:
#     print("Havo haroratini notogri kiritgansiz!")



    #2
# a = int(input("1-tomon: "))
# b = int(input("2-tomon: "))
# c = int(input("3-tomon: "))
#
# if a==b and b==c:
#     print("Teng tomonli")
# elif a==b or b==c:
#     print("teng yonli")
# else:
#     print("Harx xil tomonli")

#1
# year = int(input("Iltimos yilni kiriting!.."))
#
# if year % 4 ==0 and year%100!=0:
#     print("Kabisa yili")
# elif year%400==0 :
#     print("Kabisa yili")
# else:
#     print("Kabisa yili emas!")

#2
#
# print("tosh = 1")
# print("qogoz = 2")
# print("qaychi = 3")
#
# oyinchi1 = input("Iltimos, oyinni boshlash uchun tosh, qogoz yoli qaaychini tanlab yozing! ")
# oyinchi2 = input("Iltimos, oyinni boshlash uchun tosh, qogoz yoki qaychini tanlab yozing! n")
#
# if oyinchi1==oyinchi2:
#     print("Durrang")
# elif oyinchi1==1 and oyinchi2==3:
#     print("Tosh qaychini yengdi")
# elif oyinchi1==3 and oyinchi2==1:
#     print("Tosh qaychini yengdi")
# else:
#     print("Harx xil amal")