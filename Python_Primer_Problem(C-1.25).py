def RemovePunctuation(data):
    p=list(data)
    q=[]
    Punc=['.',',','?',';',':','!','-','/','"']
    for i in range(0,len(p)):
        if p[i] not in Punc:
            q.append(p[i])
    print("The string without punctuation is:-","".join(q))

string="Hello, my name is ! ! . Not - - Allen"
RemovePunctuation(string)
