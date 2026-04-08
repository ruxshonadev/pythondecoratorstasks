#1
# def upper_case(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result.upper()
#         return result
#     return wrapper
#
# @upper_case
# def salom_ber():
#     return "assalomu alaykum"
#
# print(salom_ber())

#2
# def reverse_string(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, str):
#             return result[::-1]
#         return result
#     return wrapper
#
# @reverse_string
# def text_reverse():
#     return "Kod ishlayapdimi tegma!"
#
# print(text_reverse())

#3
# import time
#
# def time_keeper(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"{func.__name__} ishlashi uchun {end - start:.6f} soniya ketdi")
#         return result
#     return wrapper
#
# @time_keeper
# def slow_function():
#     time.sleep(2)
#     return "Tugadi"
#
# print (slow_function())

#4
# def called_count(func):
#     count = 0
#
#     def wrapper(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"{func.__name__} {count}-marta chaqirildi")
#         return func(*args, **kwargs)
#
#     return wrapper
#
# @called_count
# def men():
#     print("MEN")
#
# men()
# men()
# men()
# men()
# men()




