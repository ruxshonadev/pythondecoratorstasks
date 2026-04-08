#list methods
#1
# mevalar = ['olma','anor','nok']
# mevalar.append("behi") # oxiriga qoshib beradi
# print(mevalar)

# 2
# mevalar = ['olma', 'anor', 'nok']
# mevalar.extend(['shaftoli','behi','uzum'])
# print(mevalar)

#
# mevalar = ["olma","anor","nok"]
# mevalar2 = ['shaftoli',"behi","uzum"]
# mevalar.extend(mevalar2)     # 2-arrayni 1-arrayga qoshinb birlashtirdi
# print(mevalar)

#3
# mevalar = ["olma","anor","nok"]
# mevalar.insert(1,"orik")  # hohlagan bir joyga elemnt qoshadi
# print(mevalar)

#4
# mevalar = ["olma","anor","nok"]
# mevalar.pop(0) #yulib tashlaydi
# print(mevalar)
#
# mevalar = ["olma","anor","nok"]
# mevalar.pop(1)  #1-indexda turgan elementni yulib tashlaydi\
# print(mevalar)
#5
# mevalar = ["olma","anor","nok","behi"]
# mevalar.remove("olma")   #kiritgan elementni ochirib tashalydi
# print(mevalar)

#6
# mevalar = ["olma", "anor", "nok", "behi"]
# mevalar.clear()  #listni tozalaydi
# print(mevalar)


#7
# mevalar = ["olma", "anor", "nok", "behi"]
# x = mevalar.copy()  # listni nsuxalaydi
# print(x)

#8
# mevalar = ["olma", "anor", "nok", "behi","olma","olma","olma"]
# x = mevalar.count("olma")   # sanab beradi
# print(x)

# num = [1,4,3,5,7,2,8,2,7,7,7,7,9,4,5]
# x = num.count(7)
# print(x)

#9
# mevalar = ["olma", "anor", "nok", "behi"]
# x= mevalar.index("olma")  #nechanchi indexdaligini chiqarib beradi
# print(x)
#
# num = [1,4,3,5,7,2,8,2,7,7,7,7,9,4,5]
# x = num.index(7)
# print(x)

#10
# num = [3,1,4,2,5]
# num.sort()  # sortlab beradi yani taxlab
# print(num)



# words = ["akmal", "botir","nodir"]
# words.sort(reverse=True)
# print(words)
#
# words = ["akmal", "botir","nodir"]
# words.sort()
# print(words)




#11
# fruits = ["apple",'banana','mango']
# fruits.reverse()  # teskarisiga ogirib beradi
# print(fruits)


#chatgpt tasks
# #1
# nums = [1,2,3,4,5]
# print(nums)
# #2
# nums = [1,2,3,4,5]
# nums.append(6)
# print(nums)
# #3
# nums = [1,2,3,4,5]
# print(nums[0])
# # #4
# nums = [1,2,3,4,5]
# print(nums[-1])   #-1 oxirgi elementni chiqaradi
# #
# # #5
# nums = [1,2,3,4,5]
# print(len(nums))  #len, nechta element borligini sanab beradi
#
#
# #5
# nums = [4, 9, 2, 7, 1]
# print(max(nums))  #ichidagi maximum sonni topib chiqaradi
# #6
# nums = [4, 9, 2, 7, 1]
# print(min(nums))  #ichidagi eng kichik sonni topadi

#chgpt+
#1
# nums = [1,2,3,4,5]
# x = nums.append(10)  #!0ni qoshibb eberdi
# print(nums)
# #2
# nums = [7,3,9,2]
# print(len(nums))   #len - listda nechta element borligini sanab berdi
# #3
# nums = [4,8,1,6]
# print(max(nums))   #maximum sonni topib beradi
# #4
# nums = [9,2,5,1]
# print(min(nums))  #minimum sonnni topibberadi
# #5
# nums = [3,7,5,9]
# x =  5 in nums
# print(x)

# #+
# nums = [10, 20, 30, 40, 50]
# x = nums.pop(-1)  #yulib tashlaydi, va biz ekranga chiqadik uni
# print(x)
# #2
# nums = [10, 20, 30, 40, 50]
# nums.remove(20)  #remove = ochirib tashlaydi
# print(nums)
#
# #3
# nums = [10, 20, 30, 40, 50]
# x= nums.index(30)   #shu son nechnchi indxdaligni chiqarib beradi
# print(x)
#
# #4
# nums = [1, 2, 3, 2, 4, 2, 5]
# x = nums.count(2)   # count - necha marta takrorlanishni topadi
# print(x)
# #5
# nums = [5, 10, 15, 20, 25]
# x = nums.pop(2)  # 3-chi element indeksi 2
# print(x)


#homework
# nums = [5, 10, 15, 20, 25]
# nums.append(46)
# print(nums)

# nums = [5, 10, 15, 20, 25]
# alphas = ["a","s","f","e","r","e"]
# nums.extend(alphas)
# print(nums)

# cars =['Bmw',"MERS","kia"]
# cars.insert(2,"byd")
# print(cars)

# cars =['Bmw',"MERS","kia","Bmw","Bmw"]
# x= cars.count("Bmw")
# print(x)

# cars =['Bmw',"MERS","kia","Bmw","Bmw"]
# x = cars.index("MERS")
# print(x)

# cars =['Bmw',"MERS","kia","Bmw","Bmw"]
# x = cars.pop(3)
# print(x)

# cars =['Bmw',"MERS","kia","Bmw","Bmw"]
# cars.remove("kia")
# print(cars)

# cars =['Bmw',"MERS","kia","Bmw","Bmw"]
# x = cars.clear()
# print(cars)

# cars =['Bmw',"MERS","kia","Bmw","Bmw"]
# x = cars.copy()
# print(x)

# cars =['Bmw',"MERS","kia","Bmw","Bmw"]
# cars.sort()
# print(cars)

# cars =['Bmw',"MERS","kia","Bmw","Bmw"]
# cars.reverse()
# print(cars)