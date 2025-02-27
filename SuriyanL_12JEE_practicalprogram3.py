#practical_program_3_Menu_driven_code_Numeric_Suriyan_L_MB12643
def factorial(x):
    r=1
    for i in range(1,x+1):
        r=r*i
    return r
def fibonacci():
    a=-1
    b=1
    endval=0
    k=[]
    while endval<n:
        endval= a+b
        a=b
        b=endval
        if endval<=n:
            k.append(endval)
    return k
c='y'
while c=='y':
    print("MENU DRIVEN CODE-NUMERIC")
    print("************************")
    print("Choice-1: factorial for an integer")
    print("Choice-2: fibonacci series upto value n")
    choice=int(input("Enter your choice:"))
    if choice==1:
        x=int(input("Enter the integer:"))
        print("Factorial is:", factorial(x))
    if choice==2:
        n=int(input("Enter the value upto the which the series will be formed:"))
        print(fibonacci())
    c=input("Do you want to continue (y/n):")
