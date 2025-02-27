#practical_program_4_Menu_Driven_Code_List/Strings_Suriyan_L_MB12643
def binsearch(k,x):
    p=0
    q=len(l)-1
    while p <= q:
        mid = (p +q)//2
        if k[mid] == x:
            return mid
        elif k[mid] < x:
            p = mid + 1
        else:
            q = mid - 1
    return -1
def reverse(s):
    print("Reversed string:",s[::-1])
c="y"
while c=="y":
    print("MENU DRIVEN CODE-LIST/STRINGS")
    print("*****************************")
    print("Choice1-Binary search for a number in list")
    print("Choice2-Reverse a string")
    choice=int(input("Enter your choice (1/2):"))
    if choice==1:
        l=[]
        n=int(input("Enter number of elements in list:"))
        for i in range(n):
            l.append(int(input("Enter any integer:")))
        x=int(input("Enter element to be searched:"))
        l.sort()
        r=binsearch(l,x)
        if r!= -1:
            print("Element is found")
        else:
            print("Not found")
    if choice==2:
        s=input("Enter a string to reverse:")
        reverse(s)
    c=input("Do you want to continue (y/n):")
            
        
    
