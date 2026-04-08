# Functions
# def print_5_greetings():
#     for _ in range(5):  # 5marta sikl aylantiradi
#         print("HELLO WORLD")



# def sanoq():
#     for _ in range(0,40):
#         if _ % 2 == 0 and _ % 3 == 0:   # 2ga va 3 ga qoldiqsiz bolinadiganlarni print qiladi
#             print(_)





  # BULAR QIYMAT QAYTARADIGAN FUNKSIYA:::

# def bir():
#     return 1
#
# def ikki():
#     return 2
#
# def uch():
#     return 3
#
# def tort():
#     return 4
#
# print(bir())



# def add(a,b):    # A B parameter
#     return a+b
#
# yigindi = add(1,2)      #   2 3 ARGUMENT
# print(yigindi)


######

# login = "admin"
# parol = 123456789
#
# def login_print(l,p):
#     print(f"""
#
#     *****************
#     *    login: {l} *
#     *    parol: {p} *
#     *               *
#     *****************
#     """)
#
# login_print(login,parol)



# def find_letter_count(word,letter):
#     return word.count(letter)   # neca marta sozda harf kelishini topuvchi funksiya
#
# natija = find_letter_count('wordwordword','w')
# print(natija)




#isolution
########

# sales = {
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }
#
# def big_sales(sales):
#     max_value = max(sales.values())
#     max_month = max(sales, key=sales.get)
#     print(f" Eng kop sotuv : {max_month} ")
#
# big_sales(sales)

#teachsolution
#
# def find_max(d):
#     return max(d, key=d.get)
#
# print(find_max({
#   "yanvar": 12000,
#   "mart": 6000,
#   "aprel": 15000,
#   "sentabr": 9000,
#   "dekabr": 10000,
# }))






##########################
#hometasks
#1
# ism = input("Enter your first name: ")
# familiya = input("Enter your last name: ")
# yosh = input("Enter your age: ")
#
# def user_data(first_name,last_name,age):
#     print(f"Ism:{first_name}")
#     print(f"familiya:{last_name}")
#     print(f"yosh:{age}")
#
#
# user_data(first_name=ism,last_name=familiya, age=yosh)

#2
#
# num1 = int(input("Iltimos 1-sonni kiriting!"))
# num2 = int(input("Iltimos 2-sonni kiriting!"))
# num3 = int(input("Iltimos 3-sonni kiriting!"))
#
# def find_max(a,b,c):
#     if a>b and a>c:
#         print("a katta")
#     elif b>a and b>c:
#         print("b katta")
#     else:
#         print("c katta")
#
#
# find_max(num1,num2,num3)


#3
#
#
# myList = [8,9,15]
#
# def list_sum(myList):
#     print(myList)
#
# print(sum(myList))


#5

# def daraja(a,b):
#     print(a**b)
#
# daraja(7,8)
#6
# def daraja4(a,b,c,d):
#     print(a**b)
#     print(d**c)
#
# daraja4(4,5,8,7)


#7
#
#
# words = "yuehfb8734gdsjgg"
#
# def digit_count_and_sum(words):
#     total = 0
#     count = 0
#
#     for w in words:
#         if w.isdigit():
#             total += int(w)
#             count += 1
#
#     print(f"Yig'indi: {total}, Soni: {count}")
#
# digit_count_and_sum(words)

#8


# def add_right(a,b):
#     print(str(a)+str(b))
#
# add_right(7,7)

#9
# def add_left(a,b):
#     print(str(b)+str(a))
#
# add_left(7,7)

#10
# def work_with_list(a):
#     kichik = min(a)
#     natija = []
#     for x in a:
#         natija.append(x * kichik)
#     print(natija)
#
# work_with_list([3, 2, 4])

#11
# def min_max(numbers, max_num, min_num):
#     is_max = max(numbers) == max_num
#     is_min = min(numbers) == min_num
#     print(is_max, is_min)
#
# min_max([3,1,7,2], 7, 1)


#13
# def expensiveProduct(products):
#     expensive = max(products, key=lambda x: x["price"])
#     print(expensive["name"])
#
# expensiveProduct([
#   {"name": "Iphone X", "price": 600},
#   {"name": "Iphone 12", "price": 1500},
#   {"name": "Samsung Note 9", "price": 800},
#   {"name": "Samsung S10", "price": 1100},
# ])





































