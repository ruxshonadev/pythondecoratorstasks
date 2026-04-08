#decorator
#1
def rufuz(f):
    def g(*args, **kwargs):
        print("by rufuz",f.__name__)
        return f(*args, **kwargs)
    return g

@rufuz
def kv(x):
    print(f"x ning kvadrati {x*x}")

kv(2)
#

#2
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


@uppercase
def greet():
    return 'Hello'

print(greet())


#3
def  add_one(number):
    return number + 1


print(add_one(2))

#4
def salom_de(ism):
    return f'Assalomu alaykum {ism}'


def xursand(ism):
    return f"{ism} men sen bilan birgaligimdan hursandman!"

def greet_rufuz(greeter_func):
    return greeter_func("rufuz")



print(greet_rufuz(salom_de))

print(greet_rufuz(xursand))




#5
def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

        print(second_child())
        print(first_child())

print(parent())

#6
def parent(num):
    def first_child():
        return "Hi, I'm Elias"

    def second_child():
        return "Call me Ester"


    if num ==1:
        return first_child()
    elif num ==2:
        return second_child()

first = parent(1)
second =parent(2)

print(first)
print(second)


#7
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_whee():
 print("Whee!")

say_whee()


#8
from decorators import do_twice

@do_twice          #asl nusxa 2marta bajariladi
def say_whee():
    print("Whee!")


say_whee()


#9
from decorators import do_twice

@do_twice
def greet(name):
    print("Hello {name}")

# greet(name="bob")   # error



#10
# bu decorator boshqa  funksiyani "orab oluvchi" funksiya
def uppercase_decorator(func):
   # func - bu bizning asosiy funksiyamz(say_hello)
    def wrapper():
        #Avval asosiy funksiyani ishlatib, natijasini saqlaymiz
        result = func()

        #Natijani KATTA harfga otkazamiz
        return result.upper()
   #wrapper funksiyasini qaytaramz(caqirmaymiz)
    return wrapper


@uppercase_decorator
def say_hello():
    return "Hello World" # kichik harf qaytaradi

print(say_hello())  # HELLO WORLD



#11

def reverse_decorator(func):
    def wrapper():
        result = func()
        return result[::-1]
    return wrapper

@reverse_decorator
def say_hello():
    return "Hello world"

print(say_hello()


print('Xush kelibsiz')







git add 19.py