def SquareSums(n):
    Sum=0
    for i in range(1,n):
        Sum=Sum+(i**2)
    print("The sum of squares of all positive integers up till",n,"is:-",Sum)

SquareSums(8)
