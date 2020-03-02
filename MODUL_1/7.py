def faktorPrima(x):
    list=[]
    n=2
    while n<=x:
        if x%n==0:
            x/=n
            list.append(n)
        else:
            n+=1
    return list

