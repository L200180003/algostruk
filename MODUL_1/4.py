def rerata(b):
        hasil=str(round(sum(b) / len(b), 2))
        print(hasil)
        return

def variance(x):
    m=str(round(sum(x) / len(x), 2))
    for a in x:
        z=(int(a)-int(m))**2
        print z
        return
