# List compherension
# numbers = [66,33,77,99,22]
# result = []
#
# result = [i*2 for i in numbers if i % 3 == 0]
# print(result)

#map
# numbers = [ 233,54,76]
# result = []
#
# print(list(map(lambda x: x**2, numbers)))
#
# words = ["js", "kotlin" , "ruby"]
# print(list(map(str.upper, words)))

#filter
# words = ["orange", "granate", "kiwi",  "strawberry"]
# for word in words:
#     print(word)
# print(list(filter(lambda w: len(w) > 3, words)))

#reduce
# from functools import reduce
#
# n = 7
# print(reduce(lambda x, y: x * y, range(2, n + 2)))

#zip
# keys = ['name', 'age']
# values = ['ruhshona', 18]
#
# print(list(zip(keys, values)))
# print(dict(zip(keys, values)))

#lambda
# print((lambda x: x * 3)(8))
#
# def f(x):
#         return x * 2
#
# print(f(7))






