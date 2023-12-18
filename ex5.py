def matmul(a,b,m,n,p):
    c=[[0 for i in range (p)]for j in range(m)]
    for i in range(m):
        for j in range(p):
            c[i][j]=0
            for k in range(n):
                c[i][j]=c[i][j]+a[i][k]*b[k][j]
    return c

m=int(input("Enter no of rows in first matrix"))
n=int(input("Enter no of columns in first matrix"))
p=int(input("Enter no of columns in first matrix"))
a=[]
print("Enter elements of matrix 1(row order):")
for i in range(m):
    r=[]
    for j in range(n):
        a=int(input())
        r.append(a)
    a.append(r)
print("Enter elements of matrix 2(row order):")
b=[[0 for i in range(p)]for i in range(n) ]
for i in range(n):
    for j in range(p):
        b[i][j]=int(input())

print("Matrix 1")
print(a)
print("Matrix 2")
print(b)
print("Resulant matrix")
print(matmul(a,b,m,n,p))
