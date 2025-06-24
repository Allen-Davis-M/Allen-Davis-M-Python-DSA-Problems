def norm(v,p):
    q=0
    for i in v:
        q=q+(i**p)
    t=q**(1/p)
    print("The ",p,"-norm of",v,"is",t)

a=[3,4]
b=2
norm(a,b)
        
