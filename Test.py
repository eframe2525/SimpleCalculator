import re


# def parenthesis():
#     global Solve
#     Prnthsfirst = next(i for i, v in enumerate(Solve) if '(' == v)
#     PrnthsScnd = next(i for i, v in enumerate(Solve) if ')' == v)
#     Prnthsfirst = Prnthsfirst - 1
#     del Solve[Prnthsfirst]
#     print(Solve)
#     del Solve[PrnthsScnd]
#     print(Solve)
#     PrnthsScnd = PrnthsScnd + 1
#     Tempsolve = []
#     listcounter = Prnthsfirst + 1
#     for i in range (Prnthsfirst,PrnthsScnd-3):
#         print(Solve)
#         print(Solve[listcounter])
#         Tempsolve.append(Solve[listcounter])
#         print(Tempsolve)
#         listcounter = listcounter + 1
#     Tempsolve = MDAS()
#     print(Tempsolve)



Solve = []
Userinput = input("Enter your arithmetic: ")
Solve = re.split("([(|)|*|/|+|^|-])", Userinput)
if "{" in Userinput:
    Userinput = Userinput.replace('{', '(')
    Userinput = Userinput.replace('}', ')')
if "{" in Userinput:
    Userinput = Userinput.replace('[', '(')
    Userinput = Userinput.replace(']', ')')
print(Userinput)
# Solve = parenthesis()