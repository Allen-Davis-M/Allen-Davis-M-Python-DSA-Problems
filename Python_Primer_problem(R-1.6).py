def SumSquareOdd(n):
    Sum=0
    for i in range(1,n):
        if i%2!=0:
            Sum=Sum+(i**2)
    print(Sum)

SumSquareOdd(8)
