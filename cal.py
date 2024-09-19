# Python cal

def add(a,b):
    return (a+b)
def subtract(a,b):
    return (a-b)
def multiply (a,b):
    return (a*b)
def divide (a,b):
    return (a/b)
def mod (a,b):
    return (a%b)

print("Select an operator")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")

choice = input("Enter a number (1/2/3/4) :")

a= int(input("Enter a :"))
b= int(input("Enter b:"))

if choice == "1":
    print (a, "+", b ,"=" ,add(a,b))
elif choice == "2":
    print (a,"-",b,"=" ,subtract(a,b))
elif choice == "3":
    print (a,"*",b ,"=", multiply(a,b))
elif choice =="4":
    print(a,"/",b, "=",divide(a,b))
elif  choice =="5":
    print(a,"%",b ,"=", mod(a,b))
else:
    print("invalid choice")
