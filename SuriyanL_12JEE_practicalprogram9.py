#Practical_program_9_USER_DEFINED_MODULE_1_Suriyan_L_MB12643
import NUMBER as N
while True:
    tup=tuple()
    n=int(input("Enter the number of integers to be added:"))
    paltuple=tuple()
    spltuple=tuple()
    for i in range(n):
        p=int(input("Enter the integer:"))
        tup=tup+(p,)
    for i in tup:
        if N.palindrome(i)==1:
            paltuple=paltuple+(i,)
        if N.special(i)==1:
            spltuple=spltuple+(i,)
    print("The palindromes in tuple are",paltuple)
    print("The special numbers in tuple are",spltuple)
    y=input("Do you want to exit?-(y/n):")
    if y=='y':
        break
