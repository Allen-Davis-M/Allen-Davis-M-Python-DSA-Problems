def DotProduct(a,b):
    c=[]
    n=len(a)
    for i in range(0,n):
        c.append(a[i]*b[i])
    print(c)

a=[2,4,5,3,2,6,7]
b=[4,6,3,2,6,7,4]

DotProduct(a,b)
