#

#list methods
# .append = biriktirish
#mevalar = ["olma", "anor","nok"]
#mevalar.append("shaftoli")
#print(mevalar)

#.extend = 2ta arrayni birlashtirish
#mevalar = ["olma", "anor","nok"]
#mevalar2=["shaftoli","uzum","anor"]
#mevalar.extend(mevalar2)
#print(mevalar)

# .insert = ortasiga yoki aniq biton joyga element kiritish
#mevalar = ["olma", "anor","nok"]
#mevalar.insert(2,"anjir")
#print(mevalar)

# .pop= (yulib olish)
# mevalar = ["olma", "anor","nok"]
# mevalar.pop() #oxiridagi 1 elementi ociradi
# mevalar.pop(1) #1-elementni ociradi
# print(mevalar)


# .remove = ocirish
#mevalar= ["anor", "olcha", "uzum","shaftoli"]
#mevalar.remove("uzum")
#print(mevalar)

# .clear = tozalash
# cars = ["bmw","mers","limuzin","kia"]
# cars.clear()
# print(cars)

# .copy = nusxalash
# fruits = ["apple","banana","mango", "kiwi","pineapple"]
# x = fruits.copy()
# x.append("orange")
# print(x)
# print(fruits)

# .count = sanash ( icida necta dona element borligini aniqlaydigan)
# fruits = ["apple","banana","cherry","ornage",'cherry', "pinaapple", "cherry", "pomegranate", "cherry"]
# x = fruits.count("cherry")
# print(x)

# .index = berilgan elementn nechanchi indexdaligini chiqradi

# fruits = ["apple","banana","cherry"]
# x = fruits.index('cherry')
# print(x)

# .sort = tartib boyicha saralash
# sonlar = [3,4,7,3,9,7,5]
# sonlar.sort()
# print(sonlar)

# .reverse = teskarisiga
# sonlar = [3,4,7,3,9,7,5]
# sonlar.reverse
# print(sonlar)




#################################################################################################
########################
#######################################################
############################
########################################
##################################
#####################################################
###############################################################





#list.append= birlashtirish
kasblar = ['oqituvchi','tikuvchi','shifokor','olim','kimyogar']
kasblar.append('dasturchi')
print(kasblar)

#list.extend = 2 ta arrayni birlashtirish
mexanika = ['samsung','iphone','redmi','nokia']
notbuklar = ['hp','ACER','macbook','linux']
mexanika.extend(notbuklar)
print(mexanika)

#list.insert = biron bir aniq joyiga elemen kiritish
ruchka = ['qora','qizil','kok','sariq']
ruchka.insert(0,'yashil')
print(ruchka)

#list.pop = yulib olsih
ajoyibotlar = ['telefon','notbuk','soat']
ajoyibotlar.pop(2)
print(ajoyibotlar)

#list.remove = ocirish
ajoyibotlar = ['telefon','notbuk','soat']
ajoyibotlar.remove('telefon')
print(ajoyibotlar)

#list.clear = listni tozalash
cars = ['bmw','mers','kia','byd']
cars.clear()
print(cars)

#list.copy = listni nushalash
fruits = ['apple','banana','orange']
x= fruits.copy()
x.append('orange')
print(x)
print(fruits)


#list.count = sanash (ichida sz qidirgan elementdan nechta donasi borligini aniqlash)
fruits = ['apple','banana','orange','apple','apple','apple','apple','apple']
x = fruits.count('apple')
print(x)

#list.index = berilgan index nechanchi indexdaligini chiqaradi
fruits = ['apple','banana','orange','apple','apple','apple','apple']
x= fruits.index('banana')
print(x)

#list.sort = tartib boyicha saralash
sonlar = [3,7,9,7,6,4,3,2]
sonlar.sort()
print(sonlar)

#list.reverse= teskarisi
sonlar = [3,7,9,7,6,4,3,2]
sonlar.sort(reverse = True)
print(sonlar)


