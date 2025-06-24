def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,"is a factor")

p=int(input("Enter number:"))
factors(p)
