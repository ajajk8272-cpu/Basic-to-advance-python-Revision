#Loops For loops and While Loops


#while = Jub tak
#loops are used to repeat instructions.
#while loops

# while condition:
#     #some work
#   print("Hello world")
#   print("Hello world")
#   print("Hello world")
#   print("Hello world")
#   print("Hello world")

# count = 1
# while count<=5:
#     print("Hello world",count)
#     count+=1

# i = 1
# while i <=5:
#     print("apnacollegeIITP",i)
#     i+=1


# b = 1
# while i <=5:
#     print("My name is khan")
#     i+=1


# i = 1
# while i<=5:
#     print("ajaz",i)
#     i+=1
# print("Loop is ended")




# i = 8
# while i>=1:
#     print("ajaz",i)
#     i-=1
# print("Loop is ended")



#Question 1
# i = 1
# while i<=100:
#     print("a",i)
#     i+=1




#question no 2

# i = 100
# while i>=1:
#     print("ak",i)
#     i-=1

# print("Loop is ended")


# i = 1
# while i<= 10:
#     print(4*i)
#     i+=1

# i = 1
# while i<= 10:
#     print(8*i)
#     i+=1


# i = 1
# while i<= 10:
#     print(15*i)
#     i+=1


#Question 4 

# nums = [1,4,9,16,25,36,49,64,81,100]

# # print(nums[0])
# print(nums[1])
# print(nums[2])
# print(nums[3])
# print(nums[4])
# print(nums[5])

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx +=1


# heroes = ["ironman","thor","superman","batman","spiderman"]
# i = 0
# while i<len(heroes):
#     print(heroes[i])
#     i +=1

# #Ques 5
# list = (1,4,9,16,25,49,64,81,100)
# i = 0# intitalisation
# while i < len(list):
#     print(list[i])
#     i +=1

# #suppose muje koi index seaarch kerna h 
# list = (1,4,9,16,25,49,64,81,100)

# x = 36

# i = 0# intitalisation
# while i < len(list):
#     if(list[i] ==  x):
#         print("FOUND at idx",i)
#         break #Loop mbreak lagata h yeh jo kis iska naam h vohi iska kaam h 
#     else:
#         print("Finding.....")
#     i +=1

# print("End of loop")




#continue

i = 0
while i <=5:
    if(i ==3):
        i+=1
        continue
       
    print(i)
    i +=1