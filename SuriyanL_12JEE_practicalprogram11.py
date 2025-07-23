#Practical_program_11_Text file 1_Suriyan_L_MB12643
c='y'
while c=='y':
    while True:
        p=input("Do you want to input a line(y/n):")
        if p=='y':
            q=input("Enter a line to be added:")
            f=open("txts1.txt",'a')
            f.write(q+'\n')
            f.close()
        else:
            break
    print("MENU DRIVEN TEXT FILE")
    print("*********************")
    print("1-Display number of lines")
    print("2-Copy words with U into another file and display it")
    print("3-Convert the case of letters (upper to lower and vice versa in original file)")
    print("4-Exit")
    ch=int(input("Enter your choice(1/2/3/4):"))
    if ch==1:
        f=open("txts1.txt",'r')
        s=f.readlines()
        print("The number of lines are:",len(s))
        f.close()
    elif ch==2:
        f=open("txts1.txt",'r')
        f2=open("copy1.txt",'w')
        s=f.read()
        k=s.split()
        for i in k:
            if "U" in i:
                f2.write(i+'\n')
        f2.close()
        f2=open("copy1.txt",'r')
        s2=f2.read()
        print(s2)
        f2.close()
        f.close()
    elif ch==3:
        str1=""
        f=open("txts1.txt",'r')
        k=f.read()
        for i in k:
            if i.isupper():
                str1+=i.lower()
            elif i.islower():
                str1+=i.upper()
            else:
                str1+=i
        f.close()
        f=open("txts1.txt",'w')
        f.write(str1)
        print(str1)
        f.close()
    elif ch==4:
        break
    c=input("Do you want to continue(y/n):")
    
    
    
