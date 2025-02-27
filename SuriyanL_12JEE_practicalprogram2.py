#practical_program_2_Statistical function/palindrome_Suriyan_L_MB12643
import statistics
def MEAn(l):
    a=statistics.mean(l)
    return a
def MEDIAn(l):
    b=statistics.median(l)
    return b
def MODe(l):
    try:
        c=statistics.mode(l)
    except:
        c="No mode found"
    return c
def PALINDROMe(l):
    k=[]
    for i in range(len(l)):
        e=str(l[i])
        if e==e[::-1]:
            k.append(l[i])
    return k
d='y'
while d=='y':
    print("STATISTICAL FUNCTIONS")
    print("*********************")
    l=[]
    n=int(input("Enter the number of elements in list:"))
    for i in range(n):
        l.append(int(input("Enter any element:")))
    p,q,r,s= MEAn(l),MEDIAn(l),MODe(l),PALINDROMe(l)
    print("Mean:", p)
    print("Median:", q)
    print("Mode:", r)
    if s==[]:
        print("Palindromes: None")
    else:
        print("Palindromes:" , s)
    d=input("Do you want to contine? (y/n):")
        
            
