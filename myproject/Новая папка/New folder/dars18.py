#1global
# a = 7
#
# def f1():
# 	print(a)
#
# def f2():
# 	global a
# 	a+=1
#
# f1()
# f2()
# print(a)

#2localscope
# def f1():
# 	a = 6
# 	print(a)
# f1()

#3nonlocal
# def f1():
#     b = 8
#     def f2():
#         print(b)
#     f2()
#
# f1()

#4
# def f1():
# 	a = 4
# 	def f2():
# 		nonlocal a
# 		a += 2
# 	print(a)
#
# f1()
# f2() #ishlamaydi

#5

# def f(x):
#     def g(y):
#         return y
#     return g
# x = 5
# y = 1
#
# result = f(x)(y)
# print(result )

#6
# def f(x):
#     def g(y):
#         def h(z):
#             return z
#         return h
#     return g
# a = 7
# b = 5
# c = 1
# f(a)(b)(c)
# print(f(a)(b)(c))

#7
# def f(x):
#     z = 2
#     def g(y):
#         return z*x* y
#     return g
# a = 4
# b = 8
# h = f(a)
# print(h(b))

#8
# def f(x):
#     z = 2
#     def g(y):
#         return z*x + y
#     return g
# a = 5
# b = 1
# h = f(a)
# print(h(b))

#8bu closer emas
# def f(x):
#     z = 2
#     def g(y):
#         return y
#     return g
# a = 11
# b = 6
# h = f(a)
# print(h(b))
# print(h.__code__.co_freevars)

#9closer sifatida lambda funksiyani ishlata olamiz
# def f(x):
#     z = 2
#     return lambda y: z*x+y
# a = 5
# b = 1
# print(f(a)(b))

#10composer
# def compose(g, f):
#     def h(*args, **kwargs): #closure funksiya
#         return g(f(*args, **kwargs))
#     return h
# km_dan_m= lambda x: x*1000
# m_dan_sm= lambda x: x * 100
#
# km_dan_sm = compose(m_dan_sm, km_dan_m)
# print(km_dan_sm(17))




