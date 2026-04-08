#1
# class Oson1:
#    a=2
#
#
#    def print_a(cls):
#        print(cls.a)
#
#
# Oson1.print_a(Oson1)

#2
# class Oson2:
#     a=3
#     b=7
#
#     def sum(cls):
#         print(cls.a+cls.b)
#
# Oson2.sum(Oson2)

#3
# class Oson3:
#     a=9
#
#     def plus_minus(cls):
#           if cls.a>0:
#               print(f"{cls.a} musbat son")
#           elif cls.a<0:
#               print(f"{cls.a} manfiy son")
#           else:
#               print(f"Son nolga teng")
#
# Oson3.plus_minus(Oson3)

#4
# class Oson4:
#     a=67
#
#     def odd_even(cls):
#         if cls.a%2==0:
#             print("Bu son juft")
#         elif cls.a%2!=0:
#             print("Bu son toq")
#         else:
#             print("notogri son")
#
# Oson4.odd_even(Oson4)

#5
# class Oson5:
#     a=68
#     b=71
#
#     def daraja(cls):
#         print(cls.a**2)
#         print(cls.b**2)
#
# Oson5.daraja(Oson5)

#6
# class MyClass6:
#     def __init__(self):
#         self.words = []
#
#     def add_word(self, word):
#         self.words.append(word)
#
#     def remove_word(self, word):
#         if word in self.words:
#             self.words.remove(word)
#
#
#
# obj = MyClass6()
# obj.add_word("Assalomu alaykum")
# obj.add_word('Vaaleykum assalom')
# obj.remove_word('Assalomu alaykum')
# print(obj.words)

#7
# class MyClass7:
#     def __init__(self):
#         self.myDict = {}
#
#     def add_elem(self, key, val):
#             if key not in self.myDict:
#              self.myDict[key] = val
#              print(f"'{key}': '{val}' qo'shildi")
#             else:
#                print(f"'{key}' allaqachon bor. Qo'shilmaydi")
#
#     def update_elem(self, key, val):
#         if key in self.myDict:
#             self.myDict[key] = val
#             print(f"'{key}' yangilandi: '{val}'")
#         else:
#             print(f"'{key}' topilmadi. Yangilanmadi")
#
# if __name__ == "__main__":
#     obj = MyClass7()
#     obj.add_elem("ism", "Ali")
#     obj.add_elem("yosh", 25)
#     obj.add_elem("ism", "Vali")
#     obj.update_elem("yosh", 26)
#     obj.update_elem("tel", "12345")
#
#     print(f"\nNatija: {obj.myDict}")

#8
# class MyClass8:
#     def __init__(self, numbers=None):
#         self.numbers = numbers if numbers else []
#
#     def compare_lists(self, new_list):
#         sum1 = sum(self.numbers)
#         sum2 = sum(new_list)
#
#         if sum1 > sum2:
#             print(f"Birinchi list katta: {self.numbers}")
#             return self.numbers
#         else:
#             print(f"Ikkinchi list katta: {new_list}")
#             return new_list
#
# obj = MyClass8([1, 2, 3])
# katta_list = obj.compare_lists([4, 5,6])

#9
# class MyClass9:
#     def __init__(self):
#         self.list1 = []
#         self.list2 = []
#
#     def list1_maximal(self):
#         if self.list1:
#             return max(self.list1)
#         else:
#             return 0
#
#     def list2_maximal(self):
#
#         if self.list2:
#             return max(self.list2)
#         else:
#             return 0
#
#     def sum_of_two_maximal(self):
#         max1 = self.list1_maximal()
#         max2 = self.list2_maximal()
#
#         yigindi = max1 + max2
#
#         print(f"list1 max: {max1}")
#         print(f"list2 max: {max2}")
#         print(f"Yig'indi: {yigindi}")
#
# obj = MyClass9()
# obj.list1 = [10, 30, 60]
# obj.list2 = [15, 30, 90]
#
# print("list1 maximal:", obj.list1_maximal())
# print("list2 maximal:", obj.list2_maximal())

#10
# class MyClass10:
#     def __init__(self):
#         self.numbers = []
#
#     def divide(self, d):
#         return [x for x in self.numbers if x % d == 0]
#
# m = MyClass10()
# m.numbers = [2, 3, 4, 6, 8, 10, 11 , 12 , 13 ]
# print(m.divide(2))


