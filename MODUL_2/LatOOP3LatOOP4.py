class Manusia(object):
      keadaan='Lapar'
      def __init__(self,nama):
            self.nama=nama
      def ucapkansalam(self):
            print("salam, namaku",self.nama)
      def makan(self,s):
            self.keadaan='kenyang'
      def olahraga(self, k):
            print("Saya baru saja latihan",k)
            self.keadaan='lapar'
      def mengalikandengandua(self,n):
            return n*2
class mahasiswa(Manusia):
      def __init__(self,nama,NIM,kota,us):
            self.nama=nama
            self.NIM=NIM
            self.kotatinggal=kota
            self.uangsaku=us
      def __str__(self):
            s=self.nama + ', NIM '+str(self.NIM)\
               + ',  Tinggal di  '+self.kotatinggal\
               + ', Uang saku Rp '+str(self.uangsaku)\
               + ', tiap bulannya '
            return s
      def ambilNama(self):
            return self.nama
      def ambilNIM(self):
            return self.NIM
      def ambilUangSaku(self):
            return self.uangsaku
      def makan(self,s):
            print("Saya nbaru saja makan",s,"sambil tidur.")
            self.keadaan='kenyang'

            
