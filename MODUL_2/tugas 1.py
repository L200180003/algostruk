class Pesan(object):
    def __init__(self, sebuahString):
        self.teks = sebuahString
    def cetakIni(self):
        print(self.teks)
    def cetakPakaiHurufKapital(self):
        print(str.upper(self.teks))
    def cetakPakaiHurufKecil(self):
        print(str.lower(self.teks))
    def jumKar(self):
        return len(self.teks)
    def cetakJumlahKarakterku(self):
        print('Kalimatku mempunyai', len(self.teks),'karakter.')
    def perbarui(self, stringBaru):
        self.teks=stringBaru
    def apakahTerkandung(self,a): 
        self.a=a
        if self.a in self.teks:
            return True
        else:
            return False
    def jumlahHurufKonsonan(self):
        vokal="aiueoAIUEO"
        x=self.teks
        hrfkonsonanl=0
        jmlHuruf=len(x)
        for i in x:
            if i not in vokal:
                hrfkonsonanl+=1
        print(hrfkonsonanl)
    def jumlahHurufVokal(self):
        vokal="aiueoAIUEO"
        y=self.teks
        hrfvokal=0
        jmlHuruf=len(y)
        for i in y:
            if i in vokal:
                hrfvokal+=1
        print(hrfvokal)


