#NUMBER_Practical_program_9_Suriyan_L_MB12643
def palindrome(a):
    k=a
    c=len(str(a))-1
    s=0
    while a>0:
        r=a%10
        s=s+(r*10**c)
        c=c-1
        a=a//10
    if s==k:
        return 1
    else:
        return -1
def special(a):
    k=a
    Sum=0
    while a>0:
        r=a%10
        s=1
        for i in range(1,r+1):
            s=s*i
        Sum=Sum + s
        a=a//10
    if Sum==k:
        return 1
    else:
        return -1




    
