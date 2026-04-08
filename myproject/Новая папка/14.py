# # #14-dars . Copy, deepcopy
# # #
# # # import copy
# # #
# # # a = [[1, 2]]
# # # b = copy.copy(a)
# # #
# # # b[0][0] = 100
# # # # bitta narsani bolishib ishlatish
# # # print(a)
# # #
# # #
# # #
# # #
# # # import copy
# # #
# # # a = [[1, 2]]
# # # b = copy.deepcopy(a)
# # #
# # # b[0][0] = 100
# # # #harkimning alohida nusxasi bor
# # # print(a)
# #
# #
# #
# #
# #
# # # CRUD = Create.Read.UPdate.Delete
# # #Create - yasash
# # #
# # # d = {"ism:Nodir","yoshi:23"}   #pyhton oddiy sintaksisidan yaratish
# # # d2 = dict(ism="Nodir", yoshi = 24)     # funksiya orqali yaratish
# # # d3 = dict(ism="Nodir", yoshi = 2)
# # # print(d)
# # # print(d2)
# # # print(d3)
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
#
#
#
#
#
#
# #Dictlarni keylari takrorlanmas, agar bir xil key takrorlansa, oxirgi kelgan keyni valuesini qaytaradi.
#
#
#
#
# harry_potter_dict={
#     "Harry Potter":"Gryffindor",
#     "Ron Weasley":"Gryffindor",
#     "Germione Granger":"Gryffindor"
# }
#
# add_characters_1={
#     "Albus Dumbldore":"Gryffindor",
#     "Luna Lovegood":"Ravenclaw"
# }
#
# add_characters_2={
#     "Draco Malfoy":"Slytherin",
#     "Sedric Diggory":"Hufflepuff"
# }
#
# add_characters_3={
#     "Rubeus Hagrid":"Gryffindor",
#     "Minerva Mcgonagal":"Gryffindor"
# }
#
# harry_potter_dict.update(add_characters_1)   #yangilaydi,
# print(harry_potter_dict)
# #
# # harry_potter_dict.update(add_characters_2)
# # print(harry_potter_dict)
# #
# # harry_potter_dict.update(add_characters_3)
# # print(harry_potter_dict)
# #
# # print(harry_potter_dict.keys())   # kalitlarini print qilib beradi
# # print(harry_potter_dict.values())   # qiymatlarini print qiladi
# # #2
# # #
# # # del harry_potter_dict["Voldemort"]   # agar yoq bolgan narsani ocrib tashla desak, KeyError chiqadi
# # # print(harry_potter_dict)
# #
# # harry_potter_dict["Voldemort"]="Slytherin" # agar topilmasa, uni valuesi bn qoshib qoyish
# # print(harry_potter_dict)
# # #
# # # harry_potter_dict.popitem()   # agar pop item methodini ishlatsak, dictni oxiridagi itemni olib tashlaydi, yani bu yerda, voldemort va uning valuesini ham olib tashlaydi
# # # print(harry_potter_dict)
# #
# #
# # harry_potter_dict.pop("Voldemort")    # dictdan voldemortni ozini topib, ochirib beradi
# # print(harry_potter_dict)
# #
# # new =harry_potter_dict["Ron Weasley"]   # Ron Weasleyni qiymatini olib beradi
# # print(new)
# #
# # new= harry_potter_dict.get("Voldemort",None)   # Voldemortni print chiqarsin dedik, agar bu qiymat bizda yoq bolsa, None qaytar dedik, getni vazifasi, error chiqarmasdan none
# # print(new)
# #
# #
# # print(harry_potter_dict.setdefault("Voldemort","Slytherin") )   #setdefault -agar topolmasa shuni qiymati bn qoshib qoyadi
# # #get bn setdeafultni farqi, getda none chiqaradi a setdefaultda esa , uni qiymati bn qoshib qoyadi
# #
# #
# #
# #
# #
# # student = [{
# #     "name": "Ali",
# #     "age": 20},
# #     {"name":"aliy",
# #     "age":"12"
# # }]
# #
# # print(student)
# #
# #
# #
# #
# #
# #
# # person = [
# #     {"name": "Vali"},
# #     {"age":25}
# # ]
# # print(person)
# #
# #
# # user = {"name": "Ali", "age": 22, "city": "Tashkent"}
# #
# # del user["age"]
# # print(user)
# #
# #
# #
# #
# #
# # car = {"brand": "BMW", "year": 2020}
# #
# # for _ in car:
# #     print(_)
# #
# #
# # numbers = {"a": 2, "b": 3, "c": 4}
# # for k in numbers:
# #     numbers[k] *=2    # 2ga kopaytirib beradi
# # print(numbers)
# #
# # d1 = {"a": 1}
# # d2 = {"b": 2}
# #
# # d1.update(d2)
# # print(d1)
# #
# #
# #
# # scores = {"Ali": 85, "Vali": 90, "Sami": 78}
# #
# # new = max(scores, key=scores.get)
# # print(new)
# #
# #
# #
# # students = {
# #     "Ali": {"age": 20, "city": "Tashkent"},
# #     "Vali": {"age": 22, "city": "Samarkand"}
# # }
# #
# # # students["Ali"(age)]
# # # print(students)
# #
# #
# # students.update({"Vali": { "city": "Bukhara"}})
# # print(students)
# #
# # add_student={
# #     "Sami": {"age": 19, "city": "Khiva"}
# #
# # }
# # students.update(add_student)
# # print(students)
# #
# #
#
# #sanab beradi
#
#
# #
#
# #dic,mini proyekt
# #
# # students = {
# #     "Ali": {"age": 20, "city": "Tashkent"},
# #     "Vali": {"age": 22, "city": "Samarkand"},
# #     "Hasan":{"age": 23, "city":"Bukhara"},
# #     "Husan":{"age":24,"city":"Bukhara"}
# # }
# #
# # user = input("studentni ismini kiriting..")
# # user1 =input("studentni ismini kiriting..")
#
#
# from collections import Counter   #bu kutubhona, sanab beradi
# #
# counter = Counter(harry_potter_dict.values())
# print(counter)
#
# #
# arr = [1,1,1,1,2,2]
# counter = Counter(arr)
#
# print(counter)
#
#
# from collections import defaultdict
#
# default_d = defaultdict(list)
#
# print(default_d)






#SET = TOPLAM

#setda elementlar har print qilganida tartibsz boladi, yanai element joylari almashinib turadi
#setda True va 1 ni ham True deb oladi demak True = 1
# thisset = { "apple","banana","cherry",True,1,1,2}
# print(thisset)
#
#
# thisset ={"apple","banana","cherry"}
# thisset.add("orange")   # agar setga element qoshmoqchi bolsak . add metodini ishlatamz
# print(thisset)
#
#
# thisset= {"apple","banana","cherry"}
# tropical = {"pineapple","mango","papaya"}
#
# thisset.update(tropical)   # setni bir-biriga qoshsa boladi, qoshib yangilaydi yani
# print(thisset)


set1 = {"a","b","c"}
set2 ={1,2,3}

set3 = set1.union(set2)   # bu method ikkala dictda ham bor hamma elementlarni print qiladi
print(set3)


x ={"apple","banana","cherry"}
y={"google","microsoft","apple"}
x.intersection_update(y)   # ikkala listda bir xil bolgan elementlarni print qiladi
print(x)


x ={"apple","banana","cherry"}
y={"google","microsoft","apple"}
x.symmetric_difference_update(y)    # ikkalasidan bir_biridan faqrqini qaytaradi
print(x)
# set shunday data typeki unga element qoshib, ochirib boladi lekin uni ozgartirib bolmaydi