#Practical_program_14_Binary files2_Suriyan_L_MB12643
import pickle
f=open('EMPLOYEE.dat','wb')
while True:
    age=int(input('Enter age : '))
    name=input('Enter name of the employee : ')
    dept=input('Enter department (Admin/Finance/Hr): ')
    des=input('Enter designation (Manager/Clark/Dymanager :) ')
    sal=int(input('Enter salary : '))
    data=[name,age,dept,des,sal]
    pickle.dump(data,f)
    ch=input('Do you want to continue : ')
    if ch.lower()=='n':
        break
f.close()
print('\tMENU')
print('1.Display details of Managers earning more than 50000 in Finance and inAdmin Dept.\n2.Delete the employee details who have reached retirement age(58years)\n3.Exit')
while True:
    ch=int(input('Enter your choice : '))
    if ch==1:
        f=open('EMPLOYEE.dat','rb')
        flag=0
        print('Managers earning more than 50000 in Finance and in Admin Dept are : ')
        while True:
            try:
                s=pickle.load(f)
                if s[2]=='Finance' or s[2]=='Admin':
                    if s[3]=='Manager' and s[4]>50000:
                        flag=1
                        print(s)
            except EOFError:
                break
        if flag==0:
            print('There is no such employee')
            f.close()
    elif ch==2:
        f=open('EMPLOYEE.dat','rb')
        lst=[]
        flag=0
        while True:
            try:
                s=pickle.load(f)
                if s[1]<58:
                    flag=1
                    lst.append(s)
            except EOFError:
                break
        if flag==0:
            print('There are no such people in the file')
        f.close()
        f=open('EMPLOYEE.dat','wb')
        pickle.dump(lst,f)
        f.close()
        f=open('EMPLOYEE.dat','rb')
        print('The file after deletion is : ')
        while True:
            try:
                s=pickle.load(f)
                for i in s:
                    print(i)
            except EOFError:
                break
        f.close()
    elif ch==3:
        break
    else:
        print('Invalid choice')


