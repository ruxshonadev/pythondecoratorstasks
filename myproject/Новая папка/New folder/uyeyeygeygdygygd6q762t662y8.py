# import json
# json_string = '{"ism": "Ruhshona", "yosh" : 18}'
# data = json.loads(json_string)  # JSON stringdan Python obyektiga o`tkazadi, OQIYDI
# print(data)
# print(data["yosh"])
# print(data["ism"])
#
# #json.load
#
# import json
# with open('malumot.json','r') as file:
#     data = json.load(file)
#     print(data)
#     print(data["univercity"])
#     print(data["name"])
#
# import json
#
# data = {"ism":"Vali", "yosh":30}
# json_string = json.dumps(data)
# print(json_string)
#
#
# import json
#
# data = {"ism":"hasan", 'yosh':28}
# with open('malumot.json', "w") as f:
#     json.dump(data, f)
#
# fiksik = {"ism": "anamoy", "yosh":20}
# with open("malumot.json", "w") as f:
#     json.dump(fiksik,f)

#
# import json
#
# men = {
#     "name": "Ruhshona",
#     "age":18,
#     "country":"Xorazm",
#     "fav_color": "green,dark,white"
# }
#
# json_string = json.dumps(men)
# print(json_string)

#
# import json
#
# json_malumot = '{"talaba": "Aziza", "fan": "Matematika", "baho": 5}'
# data = json.loads(json_malumot)  # loads ishlatish kerak (string dan o'qish)
# print(data["talaba"])  # Aziza

# import json
#
# with open ('talabalar.json', "r") as f:
#     talabalar = json.load(f)
#     print(talabalar)














import json

# Kitoblarni yaratish
kitoblar = {
    "kitob1": "Otamdan qolgan dalalar",
    "kitob2": "Mehrobdan chayon",
    "kitob3": "O'tkan kunlar"
}

# Faylga saqlash
with open('kitoblar.json', 'w', encoding='utf-8') as f:
    json.dump(kitoblar, f, indent=4, ensure_ascii=False)

print("✅ Fayl yaratildi!")




import json

# Fayldan o'qish
with open('kitoblar.json', 'r', encoding='utf-8') as file:
    kitoblar = json.load(file)

print("📚 Mening kitoblarim:")
print(kitoblar)

for nomi, kitob in kitoblar.items():
    print(f"  - {kitob}")


















