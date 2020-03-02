def apakahKabisat(n):
    if(n%400==0):
        return "kabisat"
    if(n%100==0):
        return "bukan kabisat"
    if(n%4==0):
        return "kabisat"
    else:
        return "bukan kabisat"
