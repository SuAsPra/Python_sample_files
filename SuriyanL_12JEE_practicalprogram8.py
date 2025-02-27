#Practical_program_8_Dictionary_Operations_Exam_Scores_Suriyan_L_MB12643
#house names taken as Bharathi, Tagore, Shivaji, Pratap
def MAX_SCORE(d):
    for i in d:
        c=0
        for j in d[i]:
            if d[i][j]>=c:
                c=d[i][j]
        print("Maximum score in", i,"is:")
        for j in d[i]:
            if d[i][j]==c:
                print(j,"Score:",c)
l=[" BHARATHI "," TAGORE "," SHIVAJI "," PRATAP "]
d={"SENIORS":{},"JUNIORS":{},"SUBJUNIORS":{}}
#Creation of dictionary
print("NESTED DICTIONARY-fINDING MAXIMUM SCORE")
print("***************************************")
for i in l:
    a=int(input("Enter the score for team" + i +"in seniors:"))
    b=int(input("Enter the score for team" + i +"in juniors:"))
    c=int(input("Enter the score for team" + i +"in subjuniors:"))
    d["SENIORS"][i]=a
    d["JUNIORS"][i]=b
    d["SUBJUNIORS"][i]=c
MAX_SCORE(d)
    
