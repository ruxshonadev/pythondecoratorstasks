# #1
# class BankAccount:
#     def __init__(self, balance = 0):
#         self.balance = balance
#
#     def deposit(self,amount):
#         self.balance += amount
#
#
#     def withdraw(self,amount):
#         self.balance -= amount
#
#     def check_balance(self):
#         return self.balance
#
#
# account = BankAccount()
#
# account.deposit(100)
# account.withdraw(30)
# print(account.check_balance())
#
# #2
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         return self.length * self.width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#     def is_square(self):
#         return self.length ==self.width
#
#
# rect = Rectangle(30,15)
# print(rect.area())
# print(rect.perimeter())
# print(rect.is_square())
#
# square = Rectangle(10,20)
# print(square.area())
# print(square.perimeter())
# print(square.is_square())

#3
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.grades = []
#
#     def add_grade(self,grades):
#         self.grades.append(grades)
#
#     def calculate_average(self):
#         if len(self.grades)== 0 :
#             return 0
#         return sum(self.grades)/len(self.grades)
#
#     def print_summary(self):
#         print(f"Name: {self.name}\nAge: {self.age}\nGrades: {self.grades} Calculate average: {self.calculate_average()}")
#
#
# student = Student("Ruhshona",18)
# student.add_grade(5)
# student.add_grade(5)
# student.add_grade(5)
# student.print_summary()

#4
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#
#     def area(self):
#         return 3.14 * self.radius * self.radius
#
#     def circumference(self):
#         return 2 * 3.14 * self.radius
#
#     def diameter(self):
#         return 3.14 * self.radius * self.radius
#
# circle = Circle(7)
# print(circle.area())
# print(circle.circumference())
# print(circle.diameter())

#5
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.current_page = 0
#
#     def open(self,page):
#         self.current_page = page
#         print(f"Kitob {page} sahifasida ochildi")
#
#     def turn_page(self):
#         self.current_page += 1
#         print(f"Hozir {self.current_page} sahifadasiz")
#
#
#     def restart(self):
#         self.current_page = 1
#         print(f"Kitob {self.current_page} sahifadan qayta boshlandi")
#
# book = Book("Python", "Pavel")
# book.open(7)
# book.turn_page()
# book.turn_page()
# book.turn_page()
# book.restart()
#
# #6
# class Dog:
#     total_dogs = 0
#
#
#     def __init__(self, name):
#         self.name = name
#         Dog.total_dogs += 1
#
# @classmethod
# def get_total_dogs(cls):
#     return cls.total_dogs
#
# print(Dog.total_dogs)
#
# dog1 = Dog("Rex")
# print(Dog.total_dogs)
# dog2=Dog("Bobik")
# print(Dog.total_dogs)
# dog3 = Dog("Santa")
# print(Dog.total_dogs)
#
# #7
# class Computer:
#     total_computers = 0
#     computers_list = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_computer(self):
#         Computer.computers_list.append(self)
#         Computer.total_computers += 1
#
#     def __repr__(self):
#         return self.name
#
# c1 = Computer("Acer ")
# c1.add_computer()
# c2 = Computer("Macbook")
# c2.add_computer()
# print(Computer.total_computers)
# print(Computer.computers_list)
#
# #8
#
#
# class Employee:
#     total_employees = 0
#     employees_list = []
#
#     def __init__(self, name, position):
#         self.name = name
#         self.position = position
#
#     @classmethod
#     def hire_employee(cls, name, position):
#         new_employee = cls(name, position)
#         cls.employees_list.append(new_employee)
#         cls.total_employees += 1
#         return new_employee
#
#     def __str__(self):
#         return f"{self.name} - {self.position}"
#
#     def __repr__(self):
#         return f"Employee('{self.name}', '{self.position}')"
#
#
#
# Employee.hire_employee("Zahro", "Dizayner")
# Employee.hire_employee("Olim", "Kashfiyotchi")
# Employee.hire_employee("Olima", "Kotiba")
#
# print(f"Jami xodimlar: {Employee.total_employees}")
# print(f"Ro'yxati: {Employee.employees_list}")
#
# #9
# class Television:
#     avarage_screen_size = 0
#     total_tvs = 0
#     total_size = 0
#     def __init__(self, brand, screen_size):
#         self.brand = brand
#         self.screen_size = screen_size
#         Television.avarage_screen_size = self.screen_size
#
#
#     @classmethod
#     def update_screen_size(cls,new_size):
#         cls.total_tvs +=1
#         cls.total_size += new_size
#         cls.avarage_screen_size = cls.total_size / cls.total_tvs
#
# tv1 = Television("Samsung ", 55)
# print(Television.avarage_screen_size)
# tv2 = Television("LG",65)
# print(Television.avarage_screen_size)

#10
# class Course:
#     total_courses = 0
#     courses_list = []
#
#     def __init__(self, name, duration):
#         self.name = name
#         self.duration = duration
#
#     @classmethod
#     def add_course(cls, name, duration):
#         new_course = cls(name, duration)
#         cls.courses_list.append(new_course)
#         cls.total_courses += 1
#         return new_course
#
#     def __str__(self):
#         return f"{self.name} ({self.duration} soat)"
#
#     def __repr__(self):
#         return f"Course('{self.name}', {self.duration})"
#
#
# Course.add_course("Python", 40)
# Course.add_course("JavaScript", 35)
# Course.add_course("Kotlin", 33)
# Course.add_course("Java", 20)
#
# print(f"Jami kurslar: {Course.total_courses}")  # 3
# print(f"Ro'yxat: {Course.courses_list}")

#11
# class Math:
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
# result = Math.multiply(4, 7)
# print(result)
#
# result1 = Math.multiply(20, 4)
# print(result1)
#
# result2= Math.multiply(-3, 5)
# print(result2)
#
# #12
# class Temperature:
#
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         fahrenheit = (celsius * 9 / 5) + 32
#         return fahrenheit
#
#
#
#
# result1 = Temperature.celsius_to_fahrenheit(0)
# print(f"0°C = {result1}°F")
#
# result2 = Temperature.celsius_to_fahrenheit(100)
# print(f"100°C = {result2}°F")
#
# result3 = Temperature.celsius_to_fahrenheit(37)
# print(f"37°C = {result3}°F")
#
# #13
# class Distance:
#
#     @staticmethod
#     def miles_to_kilometers(miles):
#         kilometers = miles * 1.60934
#
#         return kilometers
#
#
# result1 = Distance.miles_to_kilometers(1)
# print(f"1 milya = {result1} km")
# result2 = Distance.miles_to_kilometers(10)
# print(f"10 milya = {result2} km")
# result3 = Distance.miles_to_kilometers(100)
# print(f"100 milya = {result3} km")
#
# #14
# class Utility:
#
#     @staticmethod
#
#     def is_even(number):
#         return number % 2 == 0
#
#
# print(Utility.is_even(4))
# print(Utility.is_even(10))
# print(Utility.is_even(7))
# print(Utility.is_even(1))
#
# #15
# class Time:
#
#     @staticmethod
#     def seconds_to_minutes(seconds):
#         minutes = seconds // 60
#         remaining_seconds = seconds % 60
#         return (minutes, remaining_seconds)
#
#
# result1 = Time.seconds_to_minutes(90)
# print(result1)
# result2 = Time.seconds_to_minutes(140)
# print(result2)
# result3 = Time.seconds_to_minutes(45)
# print(result3)










