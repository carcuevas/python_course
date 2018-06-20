#Scope of variables

a = 100

# We define a function which add two numbers

def f1():
    a = 200
    print(a)

def f2():
    print(a)

f1()
f2()

## So heere we can see how is it with the local scope and the global, it will be created a new local variable with the same name inside the function.


### but if we have for example

b = 100

def f3():
    global b
    b = 125 # global
    # This will modify the global variable.

f3()

print(b)


### but we will happen if we have a list, that would be different we will able to modify elements inside a global list inside a function without using the global keyword


c = [1,2,3]

def f4():
    # we can do the follwing and it will modify the global variable
    c[0]= 99

print("Before running the function we had c = ",c)
f4()
print("After the function we have modify one element of c, c = ",c)
