#Practical_program_15_CSV file with lists_Suriyan_L_MB12643
import csv
f=open("GST.csv",'w',newline="")
wr=csv.writer(f)
data=[["Automobiles",25],["Stationary",12],["Chocolate",10],["Dairy",3]]
wr.writerows(data)
f.close()
N=int(input("Enter number of items to add:"))
f2=open("ITEMS.csv",'w',newline="")
for i in range(N):
    itmid=int(input("Enter item id:"))
    n=input("Enter item name:")
    cat=input("Enter item category:")
    up=int(input("Enter the unit price:"))
    if cat==data[0][0]:
        fp=up+(up*data[0][1]/100)
    elif cat==data[1][0]:
        fp=up+(up*data[1][1]/100)
    elif cat==data[2][0]:
        fp=up+(up*data[2][1]/100)
    elif cat==data[3][0]:
        fp=up+(up*data[2][1]/100)
    else:
        print("Invalid entry")
        fp="invalid"
    f2wr=csv.writer(f2)
    f2wr.writerow([itmid,n,cat,up,fp])
f2.close()
with open("ITEMS.csv",'r',newline="") as f2:
    rdr=csv.reader(f2)
    for i in rdr:
        print(i)
f2.close()






    
    
    
        
        
        
        
