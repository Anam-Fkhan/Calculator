# Magical Calculator
import re
print("OUR MAGICL CALCULATOR ")
print("Type 'Quit' to exit \n")
 
previous=0
run = True

def performMath():
    global run 
    global previous
    equation = 0
    if previous == 0:
      equation = input("Enter Eqution:")
    else:
        equation = input(str(previous))

    if equation =="Quit":
        print("GoodBYe, Human")
        run = False
    else:
        equation= re.sub('[a-z-A-Z , . : () +" "]','', equation)
        if previous == 0:
         previous=eval(equation)
        else:
           previous = eval(str(previous) + equation)

print("Your Answer", previous)

while run:
    performMath()
