'''Recursion'''
#When a function calls iself repeatedly
#print n to backwords
'''
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

'''
def show(n):
    print(n)

show(5) 

#Recursive function
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("End") 

show(5)

#Recursion in Factoreal
'''
def fact():
    if(n == 0 or n == 1):
        return 1
    else:
        return n * fact(n-1)
'''