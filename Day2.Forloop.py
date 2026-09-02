#Loops are used fro sequential traversal.For traversing list,string,tuples etc.
'''
el = elements

for loops                   list=[1,2,3]
for el in list:     for el in list:
                        print(el)

for loop with else

for el in list:            for el in list:
#somework                      print(el)
                           else:
else:                          print("END")
    #work when loops ends

            
                        '''


nums = [1,2,3,4,5]
for val in nums:
    print(val)



veggies = ["potato","Brinjal","tomato","carrot","lady finger","cacumber"]
for val in veggies:
    print(val)


tup = (1,2,3,4,5,2,8,9,0)
for num in tup:
    print(num)



str = "MeracollegeIITp"
for char in str:
    print(char)

else:# it is optional
    print("END")




str = "ApnacollegeIITp"

for char in str:
    if(char == '0'):
         print("o found")
         break
    print(char)
else:# it is optional
    print("END")







'''Questions practice'''

#Question1
nums = [1,4,9,16,25,64,81,100]
for el in nums:
    print(el)

# Question2
nums = [1,4,9,16,25,64,81,100]
x = 25
idx = 0
for el in nums:
    if(el == x):
        print("Number found at idx",idx)
        break
    idx += 1

'''Range funstions

Range function returns a sequence of numbers from 0 by default,and
increment by 1(by default),and stops before a specified number.

range(start?,stop,step?)

for el in range(5):
    print(el)

for el in range(1,5):
    print(el)
     
for el in range(1,5,2):
    print(el)


'''

seq = range(10)#stop condtion
for i in seq:
    print(i)

for i in range(2,10):#range(start,stop)
    print(i)

for i in range (2,10,2):#range(start,stop,step)
    print(i)


for i in range(2,100,2):# isme 2 se strt hua and 100 stop hua and 2 chor kr chla
    print(i)

for i in range(1,30,2):#isem 1 se strt hua and 30 pr ruka and 2 digit chor kr chala
    print(i)

# some question on range function
# print number 1 to 100

for i in range(1,100):
    print(i)

#print numbers 100 to 1
for i in range(100,0,-1):
    print(i) 

# print the multipliaction of n
n = int(input("enter number : "))
for i in range(1,11):
    print(n*i)
