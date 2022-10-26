import math

def print_hello():
    '''print "Hello"'''
    print("Hello")

#print_hello()

def get_hello():
    '''return "Hello"'''
    return "Hello"

#print(get_hello())

def ask_name_and_greet_user():
    '''ask name and print sentence and different sentence when name is Thanos'''
    name = str(input("name: "))
    if name.capitalize() == "Thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {name.capitalize()} Would you like to have a Hamburger?")

#ask_name_and_greet_user()

def calculate_hypotenuse_length(x, y):
    '''calculate hypotenuse'''
    c = math.sqrt(int(x) ** 2 + int(y) ** 2)
    return c

#print(calculate_hypotenuse_length(2, 3))

def calculate_cathetus_length(c, x):
    '''calculate cathetus'''
    y = math.sqrt(int(c) ** 2 - int(x) ** 2)
    return y

#print(calculate_hypotenuse_length(3, 2))