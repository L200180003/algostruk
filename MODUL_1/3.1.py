vokal="aiueoAIUEO"
def jumlahHurufKonsonan(x):
    hrfkonsonanl=0
    jmlHuruf=len(x)
    for i in x:
        if i not in vokal:
                hrfkonsonanl+=1
    print(hrfkonsonanl, ",",jmlHuruf)
