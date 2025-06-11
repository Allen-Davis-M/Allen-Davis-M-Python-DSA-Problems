def minmax(data):
    lendata=len(data)
    mindata=maxdata=data[0]
    for i in range(0,lendata-1):
        if data[i]<mindata:
            mindata=data[i]
    for j in range(0,lendata-1):
        if data[j]>maxdata:
            maxdata=data[j]
    t=(mindata,maxdata)
    print(t)

s=[4,6,5,78,2,34,3]
minmax(s)

#We solve this problem by :-
#Inputting a list s
#We use a conditional operator in which we parse through through the list to evaluate whether a subsequent member of the list is greater or lower
#We will equate that to the minimum and maximum variable

        
    
