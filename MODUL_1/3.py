vokal="aiueoAIUEO"
def jumlahHurufVokal(x):
    hrfvokal=0
    jmlHuruf=len(x)
    for i in x:
        if i in vokal:
                hrfvokal+=1
    print(hrfvokal, ",",jmlHuruf)
