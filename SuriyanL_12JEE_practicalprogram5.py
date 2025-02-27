#practical_program_5_Largest,second largest, prime from random generation_Suriyan_L_MB12643
def largest(l):
    print("Largest number in list is:", max(l))
def seclargest(l):
    temp=l.copy()
    p=max(temp)
    temp.remove(p)
    print("Second largest number in list:", max(temp))
def prime(l):
    q=[]
    for i in l:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c=c+1
        if c==2:
            q.append(i)
    if q==[]:
        print("No prime numbers in list")
    else:
        print("Prime numbers:",q)
import random
r='y'
while r=='y':
    l=[]
    print("LARGEST/SECOND LARGEST/PRIME FROM RANDOM GENERATION")
    print("***************************************************")
    x=int(input("Enter the lower limit of list:"))
    y=int(input("Enter the upper limit of list:"))
    n=int(input("Enter the number of intergers in list:"))
    if y-x<n:
        print("Error.Numbers will have to be repeated,since number of integer greater than upper limit-lower limit")
        continue
    else:
        s=0
        while n!=s:
            num=random.randint(x,y)
            if num not in l:
                l.append(num)
                s+=1
            else:
                continue
        print("Randomly made list:", l)
    print("Choice1:largest number in list")
    print("Choice2:second largest number in list")
    print("Choice3:prime numbers in list")
    choice=int(input("Enter your choice:"))
    if choice==1:
        largest(l)
    if choice==2:
        seclargest(l)
    if choice==3:
        prime(l)
    r=input("Do you want to continue(y/n):")

            
              
