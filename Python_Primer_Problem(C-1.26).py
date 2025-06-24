a=int(input("Enter number here:"))
b=int(input("Enter number here:"))
c=int(input("Enter number here:"))

if a + b == c:
    print("a + b = c")
elif a == b + c:
    print("a = b + c")
elif a - b == c:
    print("a - b = c")
elif a == b - c:
    print("a = b - c")
elif a * b == c:
    print("a * b = c")
elif a == b * c:
    print("a = b * c")
elif b != 0 and a / b == c:
    print("a / b = c")
elif c != 0 and a == b / c:
    print("a = b / c")
else:
    print("No valid arithmetic relation found.")
