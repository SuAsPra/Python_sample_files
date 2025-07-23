import pickle
f=open('STUDENT.dat','wb')
st=[]
print("Enter atleast one record for each stream")
while True:
    roll=int(input('Enter roll no : '))
    name=input('Enter name : ')
    stream=input('Enter stream(cs/bio/eg/market) : ')
    marks=int(input('Enter total marks : '))
    st.append([roll,name,stream,marks])
    ch=input('Do u wanto to continue (y/n): ')
    if ch.lower()=='n':
        break
pickle.dump(st,f)
print('MENU\n1.display topper detail wrt each stream\n2.increment 3 marks for studentin bio and decrement 2 marks for student in eg stream\n3.exit')
while True:
    ch=int(input('Enter choice : '))
    if ch==1:
        p,bi,e,m=[],[],[],[]
        for i in range(len(st)):
            if st[i][2]=='cs':
                p.append(st[i][3])
            elif st[i][2]=='market':
                m.append(st[i][3])
            elif st[i][2]=='bio':
                bi.append(st[i][3])
            elif st[i][2]=='eg':
                e.append(st[i][3])
        a,b,c,d=max(p),max(m),max(bi),max(e)
        for i in range(len(st)):
            if a==st[i][3] and st[i][2]=='cs':
                print('Details of topper in cs : ',st[i])
            elif b==st[i][3] and st[i][2]=='market':
                print('Details of topper in market : ',st[i])
            elif c==st[i][3] and st[i][2]=='bio':
                print('Details of topper in bio : ',st[i])
            elif d==st[i][3] and st[i][2]=='eg':
                print('Details of topper in eg : ',st[i])
    elif ch==2:
        for i in range(len(st)):
            if st[i][2]=='bio':
                st[i][3]+=3
            elif st[i][2]=='eg':
                st[i][3]-=2
        print(st)
        pickle.dump(st,f)
    elif ch==3:
        print('Program ended')
        f.close()
        break
    else:
        print('Wrong choice')

