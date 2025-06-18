def ReverseList(data):
    ListReverse=[]
    for i in range(len(data)-1,-1,-1):
        ListReverse.append(data[i])
    print(ListReverse)
p=[1,2,3,4,5,6,7,8,9]
ReverseList(p)
