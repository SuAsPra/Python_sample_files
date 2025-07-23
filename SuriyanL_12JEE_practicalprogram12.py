#Practical_program_12_Text file 2_Suriyan L_MB12643
f=open("txts2.txt",'w')
N=int(input("Enter number of lines to add:"))
for i in range(N):
    p=input("Enter the line:")
    f.write(p+'\n')
f.close()
c='y'
while c=='y':
    print("MENU DRIVEN TEXT FILE 2")
    print("***********************")
    print('Choice-1:Count the number of words')
    print('Choice-2:Display palindrome words')
    print('Choice-3:Display words starting and ending with a vowel')
    print('Choice-4:Exit')
    ch=int(input('Enter your choice [1/2/3/4]:'))
    f=open("txts2.txt",'r')
    r=f.read()
    d=r.split()
    f.close()
    if ch==1:
        print('Number of words:',len(d))
    elif ch==2:
        for i in d:
            if i==i[ : :-1]:
                print(i) 
    elif ch==3:
        for i in d:
            if i[0] in 'AEIOUaeiou' and i[-1] in 'AEIOUaeiou':
                print(i)

    elif ch==4:
        break
    c=input('Do you want to continue [y/n]:')
