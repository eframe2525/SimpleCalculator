##Goal - simple calculator, PEMDAS, Accept complete string and solve
## no Eval function?

#Setup
import re
power_loop = "^"
root_loop = "r"
mult_loop = "*"
div_loop = "/"
add_loop = "+"
sub_loop = "-"
solution = []
decimal = 3

##Multiplication
def power():
    powerdet = next(i for i, v in reversed(list(enumerate(solve))) if '^' == v)
    power1st_value = powerdet - 1
    power2nd_value = powerdet + 1
    power_equal = float(solve[power1st_value]) ** float(solve[power2nd_value])
    power_equal = str(round(power_equal, decimal))
    del solve[power1st_value:power2nd_value + 1]
    solve.insert(power1st_value, power_equal)
    # print(solve, "Power")
    return solve

def root():
    rootdet = next(i for i, v in reversed(list(enumerate(solve))) if 'r' == v)
    root1st_value = rootdet - 1
    root2nd_value = rootdet + 1
    root_equal = float(solve[root1st_value]) ** (1 / float(solve[root2nd_value]))
    root_equal = str(round(root_equal, decimal))
    del solve[root1st_value:root2nd_value + 1]
    solve.insert(root1st_value, root_equal)
    # print(solve, "Root")
    return solve


def multiply():
    multdet = next(i for i, v in enumerate(solve) if '*' == v)
    mult1st_value = multdet - 1
    mult2nd_value = multdet + 1
    mult_equal = float(solve[mult1st_value]) * float(solve[mult2nd_value])
    mult_equal = str(round(mult_equal, decimal))
    del solve[mult1st_value:mult2nd_value + 1]
    solve.insert(mult1st_value, mult_equal)
    # print(solve, "Mult")
    return solve

##Division
def divide():
    divdet = next(i for i, v in enumerate(solve) if '/' == v)
    div1st_value = divdet - 1
    div2nd_value = divdet + 1
    div_equal = float(solve[div1st_value]) / float(solve[div2nd_value])
    div_equal = str(round(div_equal, decimal))
    del solve[div1st_value:div2nd_value + 1]
    solve.insert(div1st_value, div_equal)
    # print(solve, "Div")
    return solve

##Addition
def addition():
    Add = next(i for i, v in enumerate(solve) if '+' == v)
    Add1stValue = Add - 1
    Add2ndValue = Add + 1
    AddEqual = float(solve[Add1stValue]) + float(solve[Add2ndValue])
    AddEqual = str(round(AddEqual, decimal))
    del solve[Add1stValue:Add2ndValue + 1]
    solve.insert(Add1stValue, AddEqual)
    # print(solve, "Add")
    return solve

##Subtract
def subtract():
    Sub = next(i for i, v in enumerate(solve) if '-' == v)
    Sub1stValue = Sub - 1
    Sub2ndValue = Sub + 1
    SubEqual = float(solve[Sub1stValue]) - float(solve[Sub2ndValue])
    SubEqual = str(round(SubEqual, decimal))
    del solve[Sub1stValue:Sub2ndValue + 1]
    solve.insert(Sub1stValue, SubEqual)
    # print(solve, "Sub")
    return solve

##check new solve
def PEMDAS():
    global solution
    solution = solve

    while True:
        # print(solve, "MDAS")
        if power_loop in solution and root_loop in solution:
            try:
                Powercount = next(i for i, v in reversed(list(enumerate(solve))) if '^' == v)
                Rootcount = next(i for i, v in reversed(list(enumerate(solve))) if 'r' == v)
            except:
                pass
            if Powercount > Rootcount:
                solution = power()
                continue
            elif Powercount < Rootcount:
                solution = root()
                continue
            else:
                break
        elif power_loop in solution or "^" in solution:
            solution = power()
            continue
        elif root_loop in solution or "r" in solution:
            solution = root()
            continue
        elif mult_loop in solution and div_loop in solution:
            try:
                Multcounter = next(i for i, v in enumerate(solve) if '*' == v)
                Divcounter = next(i for i, v in enumerate(solve) if '/' == v)
            except:
                pass
            if Multcounter < Divcounter:
                solution = multiply()
                continue
            elif Multcounter > Divcounter:
                solution = divide()
                continue
            else:
                continue
        elif mult_loop in solution:
            solution = multiply()
            continue
        elif div_loop in solution:
            solution = divide()
            continue
        elif add_loop in solution and sub_loop in solution:
            try:
                Addcounter = next(i for i, v in enumerate(solve) if '+' == v)
                Subcounter = next(i for i, v in enumerate(solve) if '-' == v)
            except:
                pass
            if Addcounter < Subcounter:
                solution = addition()
                continue
            elif Addcounter > Subcounter:
                solution = subtract()
                continue
            else:
                continue
        elif add_loop in solution:
            solution = addition()
            continue
        elif sub_loop in solution:
            solution = subtract()
            continue
        else:
            return solution

#Parenthesis
def parenthesis():
    global solve
    while True:
        dup_parenthesis = []
        index_pair = []
        # print(solve, "Parenthesis")
        solve_storetemp = list(solve)
        solve = []
        prnthsfirst = next(i for i, v in enumerate(solve_storetemp) if '(' == v)
        prnths_scnd = next(i for i, v in enumerate(solve_storetemp) if ')' == v)
        prnthsfirst = prnthsfirst - 1 # Space from split remove
        del solve_storetemp[prnthsfirst]
        del solve_storetemp[prnths_scnd]
        listcounter = prnthsfirst + 1
        for i in range (prnthsfirst,prnths_scnd-2):
            solve.append(solve_storetemp[listcounter])
            listcounter = listcounter + 1
        solve = PEMDAS()
        for i in range(len(solve_storetemp) - 1):
            if solve_storetemp[i] == ')' and solve_storetemp[i + 1] == '(':
                dup_parenthesis.append((i, i + 1))
        if dup_parenthesis:
            for index_pair in dup_parenthesis:
                solve_storetemp.insert(index_pair[0] + 1, "*")
                solve_storetemp.insert(index_pair[0] + 2, " ")
                dup_parenthesis = []
        SolveAnswer = solve
        solve = []
        del solve_storetemp[prnthsfirst:prnths_scnd]
        solve_storetemp.insert(prnthsfirst, SolveAnswer[0])
        solve = solve_storetemp
        if "(" and ")" not in solve:
            return solve


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
#code check
print("Simple Calculator")
print("Note: Solves PEMDAS equations")
while True:

    solve = []
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
        # elif ")(" in Userinput: #Parenthesis Fix
        #     Userinput = Userinput.replace(')(', ')p(')
        else:
            break
    try:
        if "(" and ")" in Userinput: #Parenthesis Detector, solves them first.
            solve = re.split("([|p|r|(|)|*|/|+|^|-])", Userinput)
            solve = parenthesis()
        else: #If power and parenthesis does not exist
            solve = re.split("([|p|r|(|)|*|/|+|^|-])", Userinput)
        PEMDAS()
        if float(solution[0]).is_integer(): #Integer detector
            Intanswer = float(solution[0])
            print("The answer is:", int(Intanswer))
        else: #all other answers
            print("The answer is:", solution[0])
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