#1
# def user_data(first_name, last_name, age):
#     print("Ism",":", first_name)
#     print("Familiya", ":", last_name)
#     print("Yosh", ":", age)
# first_name = input("Ismingizni kiriting: ")
# last_name = input("Familyangizni kiriting: ")
# age = int(input("yoshingizni kiriting: "))
# user_data(first_name, last_name, age)

#2
# def find_max(a, b, c):
#     if a > b and a > c:
#         print(f"Eng katta son - A = {a}")
#     elif b > a and b > c:
#         print(f"Eng katta son - B = {b}")
#     elif c > a and c > b:
#         print(f"Eng katta son - C = {c}")
#     elif a == b and a > c:
#         print(f"Eng katta son - A va B = {a}")
#     elif a == c and a > b:
#         print(f"Eng katta son - A va C = {a}")
#     elif b == c and b > a:
#         print(f"Eng katta son - B va C = {b}")
#     else:
#         print(f"Barcha sonlar teng = {a}")
#
# print("3 ta son kiriting:")
# a = float(input("Birinchi sonni kiriting (A): "))
# b = float(input("Ikkinchi sonni kiriting (B): "))
# c = float(input("Uchinchi sonni kiriting (C): "))
# find_max(a, b, c)

#3
# def find_letter_count(word, letter):
#     count = 0
#     for belgi in word:
#         if belgi == letter:
#             count += 1
#     print(f"'{letter}' harfi so‘zda {count} marta qatnashdi.")
# word = input("So‘z kiriting: ")
# letter = input("Qidirayotgan belgini kiriting: ")
# find_letter_count(word, letter)

#4
# def list_sum(myList):
#     jami = 0
#     for son in myList:
#         jami += son
#     print(f"Listning elementlar yig'indisi = {jami}")
# sonlar = [8, 22, 5, 99]
# list_sum(sonlar)

#5
# def daraja(a, b):
#     natija = a ** b
#     print(f"{a} ning {b} darajasi = {natija}")
# a = float(input("Sonni kiriting (a): "))
# b = float(input("Darajani kiriting (b): "))
# daraja(a, b)

#6
# def daraja4(a, b, c, d):
#
#     natija_b = a ** b
#     print(f"{a} ning {b} darajasi = {natija_b}")
#
#     natija_c = a ** c
#     print(f"{a} ning {c} darajasi = {natija_c}")
#
#     natija_d = a ** d
#     print(f"{a} ning {d} darajasi = {natija_d}")
#
# print("Sonlarni kiriting:")
# a = float(input("Son (a): "))
# b = float(input("Birinchi daraja : "))
# c = float(input("Ikkinchi daraja: "))
# d = float(input("Uchinchi daraja: "))
#
# print("\nNatijalar:")
# daraja4(a, b, c, d)

#7
# def digit_count_and_sum(word):
#     count=0
#     total = 0
#     for belgi in word:
#         if belgi.isdigit():
#             count += 1
#             total += int(belgi)
#
#     print(f"Raqamlar soni: {count}")
#     print(f"Raqamlar yig'indisi: {total}")
#
# user_input = input("Matn kiriting: ")
# digit_count_and_sum(user_input)

#8
# def add_right(a, b):
#     str_a = str(a)
#     str_b = str(b)
#     birlashgan = str_a + str_b
#     natija = int(birlashgan)
#     print("Natija:", natija)
#
# x = int(input("Birinchi sonni yozing: "))
# y = int(input("Ikkinchi sonni yozing: "))
# add_right(x, y)


#9
# def add_left(b, a):
#     str_a = str(a)
#     str_b = str(b)
#     birlashgan = str_b + str_a
#     natija = int(birlashgan)
#     print("Natija:", natija)
#
# y = int(input("ikkinchi sonni kirting: "))
# x = int(input("birinchi sonni kirting: "))
# add_left(x, y)

#10
# def work_with_list(a):
#     engkichik = min(a)
#     newlist = []
#     for son in a:
#         kopaytma = son * engkichik
#         new_list.append(kopaytma)
#     print (new_list)
# print("\nFoydalanuvchi kiritishi:")
# kiritish = input("List elementlarini vergul bilan kiriting: ")
# n_list = [int(x.strip()) for x in kiritish.split(",")]
# work_with_list(n_list)

#11
# sales = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }
#
# def big_sales(sales):
#     katta_sum = 0
#     b_month = ""
#
#     for month, money in sales.items():
#         print(month, "oyidagi sotuv:", money)
#
#         if money > katta_sum:
#             katta_sum = money
#             b_month = month
#             print("→ Yangi eng katta sotuv topildi:", katta_sum, "oy:", b_month)
#
#     return b_month
#
# print("Eng ko‘p sotuv bo‘lgan oy bu:", big_sales(sales))


#12
# sonlar = [3, 7, 1, 9, 5]
#
# def kattakichik(numbers, max_num, min_num):
#
#     eng_katta = numbers[0]
#     eng_kichik = numbers[0]
#
#     for son in numbers:
#         print("Tekshirilayotgan son:", son)
#
#         if son > eng_katta:
#             eng_katta = son
#             print("→ Yangi eng katta son topildi:", eng_katta)
#
#         if son < eng_kichik:
#             eng_kichik = son
#             print("→ Yangi eng kichik  son topildi:", eng_kichik)
#
#     print("Topilgan eng katta son bu:", eng_katta)
#     print("Topilgan eng kichik son bu:", eng_kichik)
#
#     katta = (max_num == eng_katta)
#     kichik = (min_num == eng_kichik)
#
#     return katta, kichik
#
#
# natija = kattakichik(sonlar, 9, 1)
# print("Natija (max, min):", natija)
#13
# phones = [
#     {"name": "Iphone X", "price": 600},
#     {"name": "Iphone 12", "price": 1500},
#     {"name": "Samsung Note 9", "price": 800},
#     {"name": "Samsung S10", "price": 1100},
# ]
# def expensiveProduct(phones):
#     maxprice = 0
#     expensive_name = ""
#     for product in phones:
#         if product["price"] > maxprice:
#             maxprice = product["price"]
#             expensive_name = product["name"]
#     print("Eng qimmat telefon:", expensive_name)
# expensiveProduct(phones)

13















