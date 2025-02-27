#Practical_program_7_Dictionary_Operations_Telephone_Directory_Suriyan_L_MB12643
d={}
def add():
    name=input("Enter the subscriber name:")
    phn=int(input("Enter the subscriber phone number:"))
    address=input("Enter your address:")
    d[phn]=[name,address]
def view():
    for i in d:
            print("Name:", d[i][0])
            print("Address:",d[i][1])
            print("Number:",i)
            break
    else:
        print("Error.No data found")
def modify():
    num=int(input("Enter the phone number to modify:"))
    for i in d:
        if i==num:
            k=input("Enter the detail you want to change (name/address):")
            if k.lower()=="name":
                newname=input("Enter the new name to modify:")
                d[i][0]=newname
            elif k.lower()=="address":
                newad=input("Enter the new address to modify:")
                d[i][0]=newad
            break
    else:
        print("Error.Number not found")
def delete():
    num=int(input("Enter the phone number to delete:"))
    for i in d:
        if i==num:
            d.pop(i)
            print("Number successfully deleted")
            break
    else:
        print("Error.Number not found")
c='y'
while c=='y':
    print("MENU DRIVEN CODE-DICTIONARY")
    print("***************************")
    print("Choice1: Add a subscriber")
    print("Choice2: View a subscriber detail")
    print("Choice3: Modify a subscriber detail")
    print("Choice4: Delete a subscriber")
    print("Choice5: Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
          add()
    elif ch==2:
        view()
    elif ch==3:
        modify()
    elif ch==4:
        delete()
    elif ch==5:
        break
    c=input("Do you want to continue(y/n):")
    
        
        
