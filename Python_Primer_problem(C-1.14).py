def ProductOdd(data):
    for i in range(0,len(data)):
        for j in range(0,len(data)):
            if (i*j)%2!=0 and i!=j:
                print("The product of",i,"and",j,"is odd")
                
p=[2,3,5,6,5,4]
ProductOdd(p)
