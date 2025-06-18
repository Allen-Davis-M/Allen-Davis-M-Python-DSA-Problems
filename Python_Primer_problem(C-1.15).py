def distinct(n):
    NotDistinct=[]
    for i in range(0,len(n)):
        for j in range(i+1,len(n)):
            if n[i]==n[j] and n[i] not in NotDistinct:
                NotDistinct.append(n[i])
    print(NotDistinct,"Is the list of numbers that are not distinct from the list",n)

p=[4,3,24,4,3,5,5,2,9,0,1,3,9]
distinct(p)
