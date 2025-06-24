def CountVowels(data):
    p=list(data)
    Vowels=("aeiouAEIOU")
    q=list(Vowels)
    count=0
    for i in range(0,len(q)):
        for j in range(0,len(p)):
            if q[i]==p[j]:
                count=count+1
    print("The number of vowels are",count)

data="hello my name is Dawson"
CountVowels(data)
