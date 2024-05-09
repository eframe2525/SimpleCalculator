##Goal - simple calculator, PEMDAS, Accept complete string and solve
## no Eval function?

#Setup
import re
PowerLoop = "^"
MultLoop = "*"
DivLoop = "/"
AddLoop = "+"
SubLoop = "-"
Solution = []

##Multiplication
def power():
    Power = next(i for i, v in enumerate(Solve) if '^' == v)
    Power1stValue = Power - 1
    Power2ndValue = Power + 1
    PowerEqual = float(Solve[Power1stValue]) ** float(Solve[Power2ndValue])
    PowerEqual = str(PowerEqual)
    del Solve[Power1stValue:Power2ndValue + 1]
    Solve.insert(Power1stValue,PowerEqual)
    return Solve

def multiply():
    Mult = next(i for i, v in enumerate(Solve) if '*' == v)
    Mult1stValue = Mult - 1
    Mult2ndValue = Mult + 1
    MultEqual = float(Solve[Mult1stValue]) * float(Solve[Mult2ndValue])
    MultEqual = str(MultEqual)
    del Solve[Mult1stValue:Mult2ndValue + 1]
    Solve.insert(Mult1stValue,MultEqual)
    # print(Mult)
    # print(Mult1stValue)
    # print(Mult2ndValue)
    # print(MultEqual)
    # print(Solve)
    return Solve

##Division
def divide():
    Div = next(i for i, v in enumerate(Solve) if '/' == v)
    Div1stValue = Div - 1
    Div2ndValue = Div + 1
    DivEqual = float(Solve[Div1stValue]) / float(Solve[Div2ndValue])
    DivEqual = str(DivEqual)
    del Solve[Div1stValue:Div2ndValue + 1]
    Solve.insert(Div1stValue,DivEqual)
    # print(Div)
    # print(Div1stValue)
    # print(Div2ndValue)
    # print(DivEqual)
    # print(Solve)
    return Solve

##Addition
def addition():
    Add = next(i for i, v in enumerate(Solve) if '+' == v)
    Add1stValue = Add - 1
    Add2ndValue = Add + 1
    AddEqual = float(Solve[Add1stValue]) + float(Solve[Add2ndValue])
    AddEqual = str(AddEqual)
    del Solve[Add1stValue:Add2ndValue + 1]
    Solve.insert(Add1stValue,AddEqual)
    # print(Add)
    # print(Add1stValue)
    # print(Add2ndValue)
    # print(AddEqual)
    # print(Solve)
    return Solve

##Subtract
def subtract():
    Sub = next(i for i, v in enumerate(Solve) if '-' == v)
    Sub1stValue = Sub - 1
    Sub2ndValue = Sub + 1
    SubEqual = float(Solve[Sub1stValue]) - float(Solve[Sub2ndValue])
    SubEqual = str(SubEqual)
    del Solve[Sub1stValue:Sub2ndValue + 1]
    Solve.insert(Sub1stValue,SubEqual)
    # print(Sub)
    # print(Sub1stValue)
    # print(Sub2ndValue)
    # print(SubEqual)
    # print(Solve)
    return Solve

##Test new solve
def MDAS():
    global Solution
    Solution = Solve
    while True:
        if PowerLoop in Solution or "^" in Solution:
            Solution = power()
            continue
        elif MultLoop in Solution and DivLoop in Solution:
            try:
                Mult2 = next(i for i, v in enumerate(Solve) if '*' == v)
                Div2 = next(i for i, v in enumerate(Solve) if '/' == v)
            except:
                pass
            if Mult2 < Div2:
                Solution = multiply()
                continue
            elif Mult2 > Div2:
                Solution = divide()
                continue
            else:
                continue
        elif MultLoop in Solution:
            Solution = multiply()
            continue
        elif DivLoop in Solution:
            Solution = divide()
            continue
        elif AddLoop in Solution and SubLoop in Solution:
            try:
                Add2 = next(i for i, v in enumerate(Solve) if '+' == v)
                Sub2 = next(i for i, v in enumerate(Solve) if '-' == v)
            except:
                pass
            if Add2 < Sub2:
                Solution = addition()
                continue
            elif Add2 > Sub2:
                Solution = subtract()
                continue
            else:
                continue
        elif AddLoop in Solution:
            Solution = addition()
            continue
        elif SubLoop in Solution:
            Solution = subtract()
            continue
        else:
            break
    return Solution

def entmath(message):
    while True:
        try:
            Userinput = input(message)
        except ValueError:
            print ("Try again")
            continue
        else:
            return Userinput

#Continue
def ASKTOCONTINUE(message):
    while True:
        Userinput = input("Retry? (Y/N): ")
        if Userinput.lower() in ["yes", "y"]:
            Userinput = "y"
            break
        elif Userinput.lower() in ["no", "n"]:
            Userinput = "n"
            break
        else:
            print("Invalid input. Please enter yes/no.")
    return Userinput

#Calc
while True:
    print("Simple Calculator")
    Solve = []
    Userinput = input("Enter your arithmetic: ")
    try:
        if '**' in Userinput:
            Userinput = Userinput.replace('**','^')
        Solve = re.split("([*|/|+|-|^|])", Userinput)
        # print(Solve)
        MDAS()
        print("The answer is:", Solution[0])
        Continue = ASKTOCONTINUE("Continue? Yes or No: ")
        if Continue == "Yes":
            Continue = ""
            continue
        if Continue == "No":
            Continue = ""
            break
    except:
        print("Invalid Input. Please try again")
        continue