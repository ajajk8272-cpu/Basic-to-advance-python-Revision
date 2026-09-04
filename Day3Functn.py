#Functions in python
a = 5
b = 6#yeh h lazy jindagi 
sum = a+b
print(sum)

#More line of codes
a =2 
b = 10
sum = a+b
print(sum)

#More lines of code
a = 12
b = 17
sum = a+b        #jaise ki yeh bar bar sum kerne k liye code likh rha h isse bachne k liye hum function ka use karenge
print(sum)       #or ek he kam k liye baar bar code likhan bhout he galat mana jata h 



'''ayiye ab dekhte h mentos zindagi

def func_name(param1,param2):
    #some work
    return value

fun_name(arg1,arg2...) #function call



#code
def sum(a,b):
    s = a+b
    return s 

print(sum(2, 3))

'''

def calc_sum(a,b):  #yeh ho gya function ready ab jubhi plus kerna ho tub calc_sum(val1,val2) lik kr run kerna h 
    sum = a + b
    print(sum)
    return sum


calc_sum(8,9)
calc_sum(8,990)
calc_sum(18,79)

#ab ek function on multiplication
def multi_sum(a,b):
    sum = a * b
    print(sum)
    return sum


multi_sum(7,7)#multiply karega
calc_sum(7,7)#yeh plus karega 


# ab ek devision funstion bnaate h 
def div_sum(a,b):
    sum = a / b
    print(sum)
    return sum

div_sum(12,4)#divide
calc_sum(12,4)#plus
multi_sum(12,4)#multiply


def veggi():
    print("potato","garlic","brinjal","tomato")
    print(1,2,3,4)


veggi()

#Function for my self

def My_self():
    print("My name is ajaz.Good after every one hope you doing well " \
    "currently I am persuing dual degree 1st from ignou another from IITp " \
    "and also improving my skills with Ducat study center they looted me very breightly"
    )


My_self()


#functio for greeting
def greet(name):
    print("Hello every one. my name is",name)

greet("Taufik")
greet("ajaz")


#Function for Firstname and Last name
def greet(fname,lname):
    print("Hello every one. my name is",fname,lname)

greet("Taufik","Khan")
greet("ajaz","Idrishi")


def greet(name=""):
    print("hello",name)

greet()
greet("ajaz")

'''Key aarguments'''
#Key aarguments
#Key aarguments
def g(name="",city="Delhi"):
    print("Hello", name, city)

g()
g("Delhi","ajaz")
g(name="ajaz",city="Delhi")

'''Lambda functions'''
'''Lambda functions'''

add = lambda a,b: a +b  #Lambda function for plus
print(add(5,7))
print(add(11,9))

Multi = lambda a,b: a*b #Lambda function for Multipliction
print(Multi(7,7))

Div = lambda a,b: a/b #Lambda function for Division
print(Div(3,15))


#write a function the length of a list.(list is the parameter)
#write a function the length of a list.(list is the parameter)
cities = ["Delhi","Mumbai","Pune","Noida","Bangalore","Chennai","Patna"]
heroes = ["Batman","Spiderman","Actionkamin","Iron-Man","Thor","Shaktimaan"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)

#Question write a funct print the eliments of a list ina single line
#Question write a funct print the eliments of a list ina single line

heroes = ["Batman","Spiderman","Actionkamin","Iron-Man","Thor","Shaktimaan"]

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)

#Question write a function to find the factoreal of n 
#Question write a function to find the factoreal of n 

#factoreal(!) = 4! = 1x2x3x4 
#factoreal(!) = 6! = 1x2x3x4x5x6 

'''For loop mathod
n = 5
fact = 1
for i in range(1, n+1):
    fact *= 1
print(fact)
'''
#lets make a function for factoreal
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i
    print(fact)

cal_fact(8)


#Question Write a function to convert USD to INR
#Question Write a function to convert USD to INR
def m_converter(usd_val):
    inr_val = usd_val * 96
    print(usd_val,"USD =", inr_val,"INR")

m_converter(4)
m_converter(96)
m_converter(10000)




