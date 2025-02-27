#Practical_program_6_Menu_driven_Code_Tuples_Suriyan_L_MB12643
def vowel(t):
    for i in t:
        if 'a' in i and 'e' in i and 'i' in i and 'o' in i and 'u' in i:
            print(i)
def bmical(name,ht,wt):
    bmi=wt/(ht**2)
    if bmi<=18.5:
        print("Name:",name,"BMI:",bmi,"Under weight")
    elif bmi<=24.9:
        print("Name:",name,"BMI:",bmi,"Normal")
    elif bmi<=29.9:
        print("Name:",name,"BMI:",bmi,"Overweight")
    else:
        print("Name:",name,"BMI:",bmi,"Obese")
c='y'
while c=='y':
    print("MENU DRIVEN CODE-TUPLES")
    print("***********************")
    print("Choice1: Accept tuple of words and display words with all five vowels")
    print("Choice2: Accept name, height, weight of n people as nested tuple and print BMI along with obese/overweight/normal/underweight")
    choice=int(input("Enter your choice:"))
    t=()
    if choice==1:
        n=int(input("Enter number of words:"))
        for i in range(n):
            wd=input("Enter any word:")
            t+=(wd,)
        vowel(t)
    if choice==2:
        n=int(input("Enter number of people to check BMI:"))
        for i in range(n):
            name=input("Enter you name:")
            ht=float(input("Enter your height in metres:"))
            wt=float(input("Enter your weight in kgs:"))
            innert=(name,ht,wt)
            t+=(innert,)
        for i in t:
            bmical(i[0],i[1],i[2])
    c=input("Do you want to continue")
        
