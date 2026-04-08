# 1.
# def tub_son_mi(son):
#     if son < 2:
#         return False
#     for i in range(2, son):
#         if son % i == 0:
#             return False
#     return True
#
# def tub_son_mi_generator():
#     son = 2
#     while True:
#         if tub_son_mi(son):
#             yield son
#         son += 1
# gen = tub_son_mi_generator()
#
# for _ in range(6):
#     print(next(gen))

#2
# import itertools
#
# def parol_oluvchi(kubiklar):
#     for tartib in itertools.permutations(kubiklar):
#         yield ''.join(tartib)
#
# kubiklar = "abs"
# parollar = parol_oluvchi(kubiklar)
#
# for i in range(6):
#     print(next(parollar))

#3
# def fibbonachchi_generator():
#     a=0
#     b=1
#
#     while True:
#         yield a
#         a,b=b,a+b
#
# gen=fibbonachchi_generator()
#
# for i in range (10):
#     print(next(gen))

#4
# import itertools
#
# def guruh_generator(ro_yxat, n):
#
#     for combo in itertools.combinations(ro_yxat, n):
#         yield combo
#
# my_list = [1, 2, 3, 4]
# n = 2
#
# gen = guruh_generator(my_list, n)
#
# for _ in range(6):
#     print(next(gen))



