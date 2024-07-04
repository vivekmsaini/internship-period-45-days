# <<<<<<<<<<     operaters       >>>>>>>>>>>>>

num1 = 10
num2 = 20
print(num1+num2)        
print(num2 / num1)

num1 = input("please enter first number : ")
num2 = input("please enter second number : ")
print(num1 /num2)


# type casting

int,float,str,dict,list,tuple,set

var = 10.2
var = int(var)
print(var)
print(type(var))


num1 = int(input("please enter first number : "))
num2 = int(input("please enter second number : "))

num1 = int(num1)
num2 = int(num2)

print(num1)
print(num2)
print(type(num1))
print(type(num2))

print(num1 // num2)
print(num1 ** num2)     
print(num1 % num2)  #this is show reminder(modules)

num = 10
num+=5   # or num = num+5
print(num)

x = 15
x%=3
print(x)


num1 = int(input("please enter first number : "))
num2 = int(input("please enter second number : "))

print(num1==num2)
print(num1!=num2)
print(num1<num2)
print(num1>num2)
print(num1>=num2)

relative = input("are you relative person of my family press y :")

if relative == 'y':
    print("welcome")

elif relative == "padosi":
    print("no need to welcome")    
else:
    print("bheed kam")    

