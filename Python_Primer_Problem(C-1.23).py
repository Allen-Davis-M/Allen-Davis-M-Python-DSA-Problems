my_list = [1, 2, 3]

index = int(input("Enter an index to modify: "))
value = int(input("Enter a value to assign: "))

try:
    my_list[index] = value
except IndexError:
    print("Don’t try buffer overflow attacks in Python!")
