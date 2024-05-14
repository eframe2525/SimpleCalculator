##Goal - simple calculator, PEMDAS, Accept complete string and solve
## no Eval function?

#Setup
import re
PowerLoop = "^"
RootLoop = "r"
MultLoop = "*"
DivLoop = "/"
AddLoop = "+"
SubLoop = "-"
Solution = []

##Multiplication
def power():
    Power = next(i for i, v in reversed(list(enumerate(Solve))) if '^' == v)
    Power1stValue = Power - 1
    Power2ndValue = Power + 1
    PowerEqual = float(Solve[Power1stValue]) ** float(Solve[Power2ndValue])
    PowerEqual = str(PowerEqual)
    del Solve[Power1stValue:Power2ndValue + 1]
    Solve.insert(Power1stValue,PowerEqual)
    return Solve

def root():
    Root = next(i for i, v in reversed(list(enumerate(Solve))) if 'r' == v)
    Root1stValue = Root - 1
    Root2ndValue = Root + 1
    RootEqual = float(Solve[Root1stValue]) ** (1/float(Solve[Root2ndValue]))
    RootEqual = str(RootEqual)
    del Solve[Root1stValue:Root2ndValue + 1]
    Solve.insert(Root1stValue,RootEqual)
    return Solve


def multiply():
    Mult = next(i for i, v in enumerate(Solve) if '*' == v)
    Mult1stValue = Mult - 1
    Mult2ndValue = Mult + 1
    MultEqual = float(Solve[Mult1stValue]) * float(Solve[Mult2ndValue])
    MultEqual = str(MultEqual)
    del Solve[Mult1stValue:Mult2ndValue + 1]
    Solve.insert(Mult1stValue,MultEqual)
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
    return Solve

##Test new solve
def PEMDAS():
    global Solution
    Solution = Solve
    while True:
        if PowerLoop in Solution and RootLoop in Solution:
            try:
                Powercount = next(i for i, v in reversed(list(enumerate(Solve))) if '^' == v)
                Rootcount = next(i for i, v in reversed(list(enumerate(Solve))) if 'r' == v)
            except:
                pass
            if Powercount > Rootcount:
                Solution = power()
                continue
            elif Powercount < Rootcount:
                Solution = root()
                continue
            else:
                break
        elif PowerLoop in Solution or "^" in Solution:
            Solution = power()
            continue
        elif RootLoop in Solution or "r" in Solution:
            Solution = root()
            continue
        elif MultLoop in Solution and DivLoop in Solution:
            try:
                Multcounter = next(i for i, v in enumerate(Solve) if '*' == v)
                Divcounter = next(i for i, v in enumerate(Solve) if '/' == v)
            except:
                pass
            if Multcounter < Divcounter:
                Solution = multiply()
                continue
            elif Multcounter > Divcounter:
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
                Addcounter = next(i for i, v in enumerate(Solve) if '+' == v)
                Subcounter = next(i for i, v in enumerate(Solve) if '-' == v)
            except:
                pass
            if Addcounter < Subcounter:
                Solution = addition()
                continue
            elif Addcounter > Subcounter:
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

#Parenthesis
def parenthesis():
    global Solve
    while True:
        SolveStoretemp = list(Solve)
        Solve = []
        Prnthsfirst = next(i for i, v in enumerate(SolveStoretemp) if '(' == v)
        PrnthsScnd = next(i for i, v in enumerate(SolveStoretemp) if ')' == v)
        Prnthsfirst = Prnthsfirst - 1 # Space from split remove
        del SolveStoretemp[Prnthsfirst]
        del SolveStoretemp[PrnthsScnd]
        listcounter = Prnthsfirst + 1
        for i in range (Prnthsfirst,PrnthsScnd-2):
            Solve.append(SolveStoretemp[listcounter])
            listcounter = listcounter + 1
        Solve = PEMDAS()
        SolveAnswer = Solve
        Solve = []
        del SolveStoretemp[Prnthsfirst:PrnthsScnd]
        SolveStoretemp.insert(Prnthsfirst, SolveAnswer[0])
        Solve = SolveStoretemp
        if "(" and ")" not in Solve:
            break
    return Solve

#Continue
def ASKTOCONTINUE(message):
    while True:
        Userinput = input("Retry? (Y/N): ")
        if Userinput.lower() in ["yes", "y"]:
            Userinput = "Yes"
            break
        elif Userinput.lower() in ["no", "n"]:
            Userinput = "No"
            break
        else:
            print("Invalid input. Please enter yes/no.")
    return Userinput

#Calc
print("Simple Calculator")
print("Note: Solves PEMDAS equations")
while True:

    Solve = []
    Userinput = input("Put your math equation: ") #Userentry
    while True:
        if "{" in Userinput: #Convert brackets
            Userinput = Userinput.replace('{', '(')
            Userinput = Userinput.replace('}', ')')
        elif "[" in Userinput: #Convert brackets
            Userinput = Userinput.replace('[', '(')
            Userinput = Userinput.replace(']', ')')
        elif '**' in Userinput: #Power Converter
            Userinput = Userinput.replace('**','^')
        elif "R" in Userinput: #Root Converter
            Userinput = Userinput.replace('R', 'r')
        else:
            break
    try:
        if "(" and ")" in Userinput: #Parenthesis Detector, solves them first.
            Solve = re.split("([|r|(|)|*|/|+|^|-])", Userinput)
            Solve = parenthesis()
        else: #If power and parenthesis does not exist
            Solve = re.split("([|r|(|)|*|/|+|^|-])", Userinput)
        PEMDAS()
        if float(Solution[0]).is_integer(): #Integer detector
            Intanswer = ''
            Intanswer = float(Solution[0])
            print("The answer is:", int(Intanswer))
        else: #all other answers
            print("The answer is:", Solution[0])
        Continue = ASKTOCONTINUE("Continue? Yes or No: ")
        if Continue == "Yes":
            Continue = ""
            continue
        if Continue == "No":
            Continue = ""
            print("Thank you for using this Simple Calculator")
            break
    except:
        print("Invalid Input. Please try again")
        print()
        continue