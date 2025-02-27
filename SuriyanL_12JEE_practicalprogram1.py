#_practical program 1_Sum of Series_Suriyan_L_MB12643
def factorial(p):
    r=1
    for i in range(1,p+1):
        r=r*i
    return r
def series1(x,n):
    s=0
    t=1
    for i in range(1,n+1):
        nr=x**(2*i-1)
        dr=factorial(2*i)
        s= s + t*(nr/dr)
        t=-t
    return s
def series2(x,y,n):
    s=0
    t=1
    for i in range(1,n+1):
        nr=x**(2*i-1)
        dr=factorial((2*i+1)*y)
        s= s + t*(nr/dr)
        t=-t
    return s
c="y"
while c=="y":
    print("SUM TO SERIES")
    print("*************")
    print("Choice 1= sum of series (x/2!) - (x^3/4!) + (x^5/6!) .....n terms")
    print("Choice 2= sum of series (x/3y!) - (x^3/5y!) + (x^5/7y!) .....n terms")
    choice= int (input("Enter your choice:"))
    if choice==1:
        x=int(input("Enter the x value:"))
        n=int(input("Enter the n value:"))
        print(series1(x,n))
    if choice==2:
        x=int(input("Enter the x value:"))
        n=int(input("Enter the n value:"))
        y=int(input("Enter the y value:"))
        print(series2(x,y,n))
    c=input("do you want to continue? (y/n):")
else:
    print("END OF PROGRAM")
        
        
