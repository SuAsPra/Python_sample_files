#Practical_program_10_USER DEFINED MODULE 2_Suriyan_L_MB12643
import MATRIX
matrix=[]
r=int(input("enter the length of nested list:"))
#in matrix, number of rows=columns
for i in range(r):
    a=[]
    for j in range(r):
        x=int(input("enter the number"))
        a+=[x]
    matrix+=[a]
print("MENU\n 1.swap the left and right diagonal")
print("2.sort the elements rowwise/columnwise")
print("3.Exit")
print(matrix)
while True:
    ch=int(input("enter choice:"))
    if ch==1:
        MATRIX.swap(matrix)
        print(matrix)
    elif ch==2:
        MATRIX.sortrowcol(matrix)
        print(matrix)
    elif ch==3:
        break
    else:
        print("wrong choice")

        
        
                    
            
        
        
