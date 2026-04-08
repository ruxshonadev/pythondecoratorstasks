# #1
#
#
# class Texnika:
#     def __init__(self, brand , model , type):
#       self.brand = brand
#       self.model = model
#       self.type = type
#
#
#
#     def info(self):
#         print(f" Bu texnika brendi {self.brand}  modeli {self.model} va tipi {self.type}")
#
# texnika1 = Texnika("Samsung", "Galaxy a17" ,"telefon" )
# texnika1.info()
#
# class Notebook(Texnika):
#     def __init__(self, brand , model , type, video_card, ram , display):
#       super().__init__(brand,model,type)
#       self.video_card = video_card
#       self.ram = ram
#       self.display = display
#
#     def more_info(self):
#         print(f"Buning  videocartasi {self.video_card} , rami {self.ram} va displayi {self.display}")
#
#
# notebook = Notebook("Acer","Aspire" , "notebook" , "gtx 1650" ," 16gb" ,"15,6 inch" )
#
#
# notebook.info()
# notebook.more_info()
#
# class Television(Texnika):
#     def __init__(self, brand, model, type, size ,display):
#         super().__init__(brand, model, type)
#         self.size =size
#         self.display = display
#
#
#     def more_info(self):
#         print(f"Buning size i {self.size} va displayi {self.display}")
#
# television = Television ("artel" , "yeeah" , "televizor", "16inch" , "14wuxga")
#
# television.info()
# television.more_info()
#
#
# class Smartphones(Texnika):
#     def __init__(self, brand , model , type , size , sim_count):
#         super().__init__(brand,model,type)
#         self.size = size
#         self.sim_count = sim_count
#
#
#     def more_info(self):
#         print(f"Buning size i {self.size} va simkartasi {self.sim_count} ta")
#
# smartphones = Smartphones("Samsung", "blue" , "telefon", "23cm", "2")
#
# smartphones.info()
# smartphones.more_info()

#2
# class Transport():
#     def __init__(self,brand,model,type):
#         self.brand = brand
#         self.model = model
#         self.type = type
#
#
#     def info(self):
#         print(f"Brand: {self.brand}, "
#               f"Model: {self.model}, "
#               f"Type: {self.type}")
#
# transport = Transport("BMW",
#                       "m5 f90",
#                       "car")
# transport.info()
#
#
#
# class Eloctrocars(Transport):
#     def __init__(self,brand,model,type,battery_life,chargin_time):
#        super(). __init__(brand,model,type)
#        self.battery_life = battery_life
#        self.chargin_time = chargin_time
#
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, "
#               f"Model: {self.model}, "
#               f"Type: {self.type}, "
#               f"Battery life: {self.battery_life}, "
#               f"Charging time: {self.chargin_time}")
#
# electrocars = Eloctrocars(f"Mercedes",
#                           f"CLS",
#                           f"car",
#                           f"24hour",
#                           f"2hour")
#
# electrocars.more_info()
#
#
# class SportCars(Transport):
#     def __init__(self,brand,model,type,motor,color):
#         super().__init__(brand,model,type)
#         self.motor = motor
#         self.color = color
#
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, "
#               f"Model: {self.model}, "
#               f"Type: {self.type}, "
#               f"Motor: {self.motor}, "
#               f"Color: {self.color}")
#
# sportcars = SportCars(f"PORSCHE",
#                       f"911",
#                       "sportcar",
#                       "macan",
#                       "red")
#
# sportcars.more_info()
#
# class Truck(Transport):
#     def __init__(self,brand,model,type,height,long,weight):
#         super().__init__(brand,model,type)
#         self.height = height
#         self.long = long
#         self.weight = weight
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, "
#               f"Model: {self.model}, "
#               f"Type: {self.type}, "
#               f"Height: {self.height}, "
#               f"Long: {self.long}, ")
#
# truck = Truck("Toyota",
#               "hilux sr",
#               "truck",
#               "1815",
#               "5.3",
#               "1855")
# truck.more_info()



#3.1
# class University:
#
#
#     def __init__(self, university):
#         self.university = university
#
#     def info(self):
#         print(
#             f"University: {self.university}")
#
# university= University(
#     f"AKHU")
#
# university.info()
#
#
# class Staff(University):
#         def __init__(self, university, first_name, last_name, age, group):
#             super().__init__(university)
#             self.first_name = first_name
#             self.last_name = last_name
#             self.age = age
#             self.group = group
#
#         def more_info(self):
#             print(
#                 f"University: {self.university}, "
#                 f"Name: {self.first_name} ,"
#                 f"Last name: {self.last_name},"
#                 f"Age: {self.age}, "
#                 f"Group: {self.group}"
#             )
#
# staff = Staff(
#         f"AKHU",
#         f"Ruhshona",
#         f"Rahimova",
#         f"18",
#         f"SE-107"
#     )
# staff.more_info()
#
# class Student(Staff):
#         def __init__(self, university, first_name, last_name, age,group, position, subject):
#             super().__init__(university, first_name, last_name, age , group )
#             self.group = group
#             self.position = position
#             self.subject = subject
#
#         def more_info(self):
#             print(
#                 f"University: {self.university},"
#                 f"Name: {self.first_name}, "
#                 f"Last name: {self.last_name},"
#                 f"Age: {self.age}. "
#                 f"Position: {self.position}. "
#                 f"Subject: {self.subject}"
#             )
#
# student = Student(
#         f"AKHU",
#         f"Ruhshona",
#         f"Rahimova",
#         18,
#         f"SE-107",
#         f"Senior teacher",
#     "Programming"
#     )
# student.more_info()
#
#
#
#
#
#
# class Teacher(Staff):
#     def __init__(self, university, first_name, last_name, age,group,position, subject):
#         super().__init__(university,first_name,last_name,age, group )
#         self.group = group
#         self.position = position
#         self.subject = subject
#
#     def more_info(self):
#         print(
#         f"University: {self.university},"
#         f"Name: {self.first_name},"
#         f"Last name: {self.last_name},"
#         f"Age: {self.age}. "
#         f"Position: {self.position}. "
#         f"Subject: {self.subject}"
#         )
#
#
#
# teacher = Teacher(
#     "AKHU",
#     "Ruhshona",
#     "Rahimova",
#     30,
#     "SE-117",
#     "Senior teacher",
#     "Programming")
# teacher.more_info()
#
#
# class OtherStaff(Staff):
#     def __init__(self, university, first_name, last_name,age,group, position):
#         super().__init__(university,first_name,last_name,age,group)
#         self.position = position
#
#     def more_info(self):
#         print(f"university : {self.university}, "
#               f"Name: {self.first_name} ,"
#               f"Last name: {self.last_name},"
#               f"Position: {self.position}")
#
#
# otherstaff = OtherStaff(
#     f"AKHU",
#     f"Ruhshona",
#     f"Rahimova",
#     f"18",
#     f"SE-117",
#     "senior teacher"
#
# )
# otherstaff.more_info()
#
#
# #3.2
# class Object(University):
#     def __init__(self, university, name):
#         super().__init__(university)
#         self.name = name
#
#     def object_info(self):
#         print(
#             f"University: {self.university},"
#             f"Name: {self.name}"
#         )
# object = Object("AKHU",
#                 "Ruhshona")
#
# object.object_info()
#
# class Computer(Object):
#     def __init__(self, university, name, tizimi, holati):
#         super().__init__(university, name)
#         self.tizimi = tizimi
#         self.holati = holati
#
#     def object_more_info(self):
#         print(
#             f"University: {self.university},"
#             f"Name: {self.name},"
#             f"Tizimi: {self.tizimi},"
#             f"Holati: {self.holati}"
#         )
# computer = Computer("AKHU",
#                     "ACER",
#                     "i5",
#                     "nice")
# computer.object_more_info()
#
# class Mebel(Object):
#     def __init__(self, university, name,soni,turi,holati):
#         super().__init__(university, name)
#         self.soni = soni
#         self.turi = turi
#         self.holati = holati
#
#     def object_more_info(self):
#         print(f"University: {self.university},"
#               f"Name: {self.name},"
#               f"Soni: {self.soni},"
#               f"Turi: {self.turi},"
#               f"Holati: {self.holati}")
#
# mebel = Mebel("AKHU",
#               "mebel",
#               "20ta",
#               "qora",
#               "nice"
#               )
#
# mebel.object_more_info()
