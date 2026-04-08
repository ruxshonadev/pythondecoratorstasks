#Rekursiv funksiyalar
#Rekursiv funksiya bu sikl aylantirishning oziga xos usuli bolib, oz-ozini cqiruvchi  funksiyadir
# n! = 1*2*3*.....*n
#Rekursiv funkisya operativ xotirani oddiy funksiyaga  qaraganda koproq yeydi

#
# def factorial(n):
#     if n==1:
#         return 1        #Toxtatish sharti
#     else:
#         return n*factorial(n-1)   #oz-ozini chqirish
#
# print(factorial(5))




#


# def summa(n):
#     if n==1:
#         return 1
#     else:
#         return n+summa(n-1)
#
# print(summa(5))

#
#
# def countdown(n):
#     print(n)
#     if n==0:      # Base condition
#         return
#     else:
#         countdown(n-1)    #Rekursiv call
#
# countdown(5)

# def Quvvat(son,daraja):
#     if daraja==1:
#         return son
#     else:
#         return son*Quvvat(son,daraja-1)  # 2argument
#
#
# print(Quvvat(2,4))



def palindrom(soz):
    if len(soz)==1:
        return True

    if soz[0]==soz[-1]:
        return palindrom(soz[1:-1])
    else:
        return False


print(palindrom("aba"))
print(palindrom("abs"))

#
def summa_raqam(n):
    if n<10:
        return n

    return (n%10)+summa_raqam(n//10)

print(summa_raqam(1234))




def nima(n):
    if n == 0:
        return 0
    return n + nima(n - 1)

print(nima(3))



def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)