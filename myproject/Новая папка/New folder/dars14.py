#1.
# def str_counter(str):
#     result = {}
#     for s in str:
#         length = len(s)
#         result[length] = s
#     return result
# print(str_counter(["shaftoli", "olma","nok"]))

#2.
# def merge_list(l1, l2):
#     result = {}
#     for i in range(len(l1)):
#         key = l1[i]
#         value = l2[i]
#         result[key] = value
#     return result
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# print(merge_list(list1, list2))

#3.
# Kontaktlar = {
#     "Nodir": "+998918602711",
#     "Laziz": "+998908002534"
# }
#
# def add_contact():
#     ism = input("Ismini kiriting: ")
#     telefonraqam = input("Telefon raqamni kiriting: ")
#     contacts[name] = phone
#     print("Kontaktlarga qo‘shildi.")
#
# def update_contact():
#     ism = input("Yangilamoqchi bo‘lgan ismini kiriting: ")
#     if ism in contacts:
#         telefonraqam = input("Yangi telefoni raqamni kiriting: ")
#         Kontaktlar[name] = phone
#         print("Kontaktingiz yangilandi.")
#     else:
#         print("Bunday kontakt yo`q.")
#
# def delete_contact():
#     ism = input("O‘chirmoqchi bo‘lgan ismni kiriting: ")
#     if ism in Kontaktlar:
#         del Kontaktlar[ism]
#         print(" Bu kontakt o‘chirildi.")
#     else:
#         print("Bunday kontakt yo`q.")
#
# def search_contact():
#     ism= input("Qidirayotgan ismni kiriting: ")
#     if ism in Kontaktlar:
#         print(f"{ism}: {Kontaktlar[ism]}")
#     else:
#         print("Bunday kontakt yo‘q.")
#
# def show_contacts():
#     if not Kontaktlar:
#         print("Kontaktlar ro‘yxati bo‘sh.")
#     else:
#         for ism, telefonraqam in conatact.items():
#             print(f"{ism}: {telefonraqam}")
#
# def main_menu():
#     while True:
#         print("1. Kontakt qo‘shish")
#         print("2. Kontaktni yangilash")
#         print("3. Kontaktni o‘chirish")
#         print("4. Kontaktni qidirish")
#         print("5. Barcha kontaktlarni ko‘rish")
#         print("6. Chiqish")
#
#         choice = input("Tanlang (1-6): ")
#
#         if choice == "1":
#             add_contact()
#         elif choice == "2":
#             update_contact()
#         elif choice == "3":
#             delete_contact()
#         elif choice == "4":
#             search_contact()
#         elif choice == "5":
#             show_contacts()
#         elif choice == "6":
#             print("Dastur tamom boldi.")
#             break
#         else:
#             print("Noto‘g‘ri tanlov!")
#
# if __name__ == "__main__":
#     main_menu()

#4
# def counter_dict(sonlar):
#     natija = {}
#     for son in sonlar:
#         if son in natija:
#             natija[son] += 1
#         else:
#             natija[son] = 1
#     return natija
# print(counter_dict([2, 1, 1, 1]))

#5
# def max_ball_students(talabalar):
#     ranked_students = sorted(talabalar.items(), key=lambda x: x[1], reverse=True)
#     best_two = dict(ranked_students[:2])
#     return best_two
#
# print(max_ball_students({
#     "Akmal": 64,
#     "Tohir": 55,
#     "Nodir": 76,
#     "Zafar": 80
# }))


