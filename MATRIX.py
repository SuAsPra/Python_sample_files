def swap(matrix):
    for i in range(len(matrix)):
        matrix[i][i],matrix[i][-(i+1)]=matrix[i][-(i+1)],matrix[i][i]
def sortrowcol(matrix):
    print("1.Sort rowwise\n2.sort cloumnwise")
    ch1=int(input("enter your choice"))
    if ch1==1:
        bub(matrix)
    else:
        insertion(matrix)
def bub(matrix):
    for i in range(len(matrix)):
        m=matrix[i]
        for p in range(len(m)):
            for j in range(len(m)-1-p):
                if m[j]>m[j+1]: m[j],m[j+1]=m[j+1],m[j]
def insertion(matrix):
    mat=[]
    for i in range(len(matrix)):
        col=[]
        for p in range(len(matrix)):
            col+=[matrix[p][i]]
        for p in range(1,len(col)):
            temp=col[p]
            j=p-1
            while temp<=col[j] and j>=0:
                col[j+1]=col[j]
                j-=1
            col[j+1]=temp
        mat+=[col]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            matrix[j][i]=mat[i][j]
