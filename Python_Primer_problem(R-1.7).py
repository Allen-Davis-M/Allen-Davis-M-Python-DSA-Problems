def sumsquare(n):
    Sum=0
    Square=[k*k for k in range(1,n) if k%2!=0]
    Sum=sum(Square)
    print(Sum)

sumsquare(8) 
