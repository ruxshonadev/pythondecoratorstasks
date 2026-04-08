# i = 1
#
# while i <= 5:
#     print(str(i) * i)
#     i += 1

#2
# son = input("Son kiriting..")
# yigindi = 0
# i = 0
#
# while i <len(son):
#     yigindi+= int(son[i])
#     i+=1
#
# print("Yigindi" ,yigindi)


#3
#
# i = 1
# a= 0
# while i<=100:
#     if i%2==1:
#         a+=1
#     i+=1
# print(a)


#4
# sonlar = [3,5 ,6,7,8,5,4,3,22,2,4,55,6]
#
#
# first = -1
# second = -1
# i = 0
#
# # while i < len(sonlar):
#     if sonlar[i] > first:
#         second = first
#         first = sonlar[i]
#     elif sonlar[i] > second:
#         second = sonlar[i]
#         i+=1
#     print("2-eng katta son")


import random

def taxmin_oyini():

    secret = random.randint(1, 100)

    print("1 dan 100 gacha son taxmin yozing!")

    while True:

        guess_input = input("Taxminingiz: ")


        try:
            guess = int(guess_input)
        except ValueError:
            print("Iltimos, butun son kiriting!")
            continue


        if guess > secret:
            print("JUDA BALAND!")
        elif guess < secret:
            print("JUDA PAST!")
        else:
            print("Tabriklayman! SZ Yuttingiz:", secret)
            break

if __name__ == "__main__":
    taxmin_oyini()



