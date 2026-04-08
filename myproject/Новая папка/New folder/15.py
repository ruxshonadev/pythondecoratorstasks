# #LIST COMPREHENSION - QISQA ROYXAT YARATISH
# #VAZIFASI: map() va filter() ni yanada o'qilishi oson korinishi
# #
# # l =[1,2,3,4,5,6,7,8,9,0]
# #
# # # toqlar=[]
# # #
# # # for i in l:
# # #     if i%2==1:
# # #         toqlar.append(i)
# # #
# # # print(toqlar)   # bu juda uzun code
# #
# #
# # toqlar=[i for i in l if i%2==1]     # bu list compheresion
# # print(toqlar)
#
#
# #1-misol
#
# regions = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"],
#             ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]
#
#
# from_city = [l[1]for l in regions]   # qaysi shaharlardan chiqadi
# print(from_city)
#
#
# #2-misol
# # ushbu listdagi sonlarni 2ga kopaytiring va yangi listga otkazing
# sonlar = [1,2,3,4,5]
#
#
#
# toqlar=[i for i in sonlar if i%2==1]
#
#
# #3-misol
#
# lst = [1,2,3,'Alice','Alice']
# #listdagi ma'lum elementnng ilk uchragan ideksini topadi.
#
# indice = lst.index('Alice')
# print(indice)
#
# #listlarning malum elementning barcha indexlarini topadi.
#
# indices = [i for i in range(len(lst)) if lst [i] == 'Alice']    # Barcha Alice larni indexini olib beradi
# print(indices)
#
# #4-misol - Millionerni toping
#
# people = [("John", 240_000), ("Alice", 120_000), ("Ann", 1_100_000), ("Zach", 44_000), ("Doe", 2_300_000)]
#
# millioners = [name for name,money in people if money >=1_000_000]
# print(millioners)
#
#
# #Millionerni topib beruvhci funksiya
# def find_millioners(people):
#     return [name for name,money in people.items if money>=1_000_000]
#
#
# #find_millioner funksiyasini yozib, uni quyidagi qiymatlar bialn testlang
#
# people_data1 = {'Alice': 1_000_000, 'Bob': 998_170, 'Carol': 1_229_080, 'Frank': 881_230, 'Eve': 93_121}
# people_data2 = {'Alice': 1_000_000, 'Bob': 998_170, 'Frank': 1_881_230, 'Eve': 93_121}
#
# def test():
#     assert find_millioners(people_data1)==[]
#     ["Alice","Carol"]
#     assert find_millioners(people_data2)==[]
#     ["Alice","Carol"]
#
# test()

#5-misol
#Quyidagi listni ichma-ich siklorqali yarating
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# l=[]
#
# for x in range(3):
#     for y in range(3):
#         l.append((x,y))        #uzuuun code
# print(l)
#
#
# print([(x,y)for x in range(3) for y in range(3)])   #list compherehension
#
#
# #6-misol
# #matndagi uzunuligi 5ta harfdan ortiq bolgan sozlarni toping
#
# text = '''Call me Ishmael. Some years ago - never mind how long precisely - having little
# or no money in my purse, and nothing particular to interest me on shore, I thought I would
# sail about a little and see the watery part of the world. It is a way I have of driving off
# the spleen, and regulating the circulation. - Moby Dick '''
#
# print(([i for i in text.split() if len(i)>5]))   #List comprehension
#
#
# #Har bitta qator uchun print qilib ber?)
#
# print([[i for i in line.split() if len(i) >7] for line in text.split("\n")])
#
#



#list comp, tasks

print([for i in range ])
