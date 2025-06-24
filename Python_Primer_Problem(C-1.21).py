lines = []

try:
    while True:
        lines.append(input())
except EOFError:
    for line in reversed(lines):
        print(line)
