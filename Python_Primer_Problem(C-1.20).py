from random import randint

def shufflerandom(n):
    Shuffled = []
    Record = []
    while len(Record) < len(n):
        p = randint(0, len(n) - 1)
        if p not in Record:
            Record.append(p)
            Shuffled.append(n[p])
    print(Shuffled)


data=[1,2,3,4,5,6,7,8,9]
shufflerandom(data)


        
    
