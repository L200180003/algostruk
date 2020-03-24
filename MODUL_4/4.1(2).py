##################### LATIHAN #####################
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

class mhsTIF(mahasiswa):
    def katakanPy(self):
        print('Python is cool')
##################### TUGAS #####################

#Nomor 1
def cari(n,target):
    x=[]
    y=1
    for i in n:
        if i.kotatinggal==target:
            x.append(y)
        y+=1
    print(x)

#Nomor 2
def sakuKecil(x):
    n=len(x)
    terkecil=x[0].uangsaku
    for i in range(1,n):
        if x[i].uangsaku < terkecil:
            terkecil=x[i].uangsaku
    return terkecil

#Nomor 3
def sakuKecil2(x):
    n=len(x)
    a=[]
    terkecil=x[0].uangsaku
    for i in range(1,n):
        if x[i].uangsaku < terkecil:
            terkecil=x[i].uangsaku
            a.append(x[i])
    return a

#Nomor 4
def bawah250(x):
    n=len(x)
    for i in range(1,n):
        if x[i].uangsaku < 250000:
            print(x[i])

#Nomor 5
class node (object):
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next
    def cari (self, cari):
        curNode = self
        while curNode is not None :
            if curNode.next != None :
                if curNode.data != cari :
                    curNode = curNode.next
                else :
                    print ("Item", cari, "ada dalam Linked List")
                    break
            elif curNode.next == None :
                print ("Item", cari, "tidak ada linked list")
                break    

#Nomor 6
def binSe(x, target):
    low = 0
    high = len(x) -1
    data = []

    while low <= high:
        mid = (high + low) //2
        if x[mid] == target:
            data.append(x.index(target))
            return True
        elif target < x[mid]:
            high = mid -1
        else :
            low = mid +1
    return False

#Nomor 7
def binSearch(x, target):
    low = 0
    high = len(x) -1
    data = []
    while low != high:
        mid = (high + low) //2
        if x[mid] == target:
            break
        elif target < x[mid]:
            high = mid -1
        else :
            low = mid +1
    for i in range (low, high):
        if target == x[i]:
            data.append(i)
    return data

#Nomor 8

#Untuk membuat permainan tebak angka, kalau angka yang ditebak di antara 1 dan 100 maksimal jumlah tebakan adalah 7.
#Kalau angka yang harus ditebak berada diantara 1 dan 1000 maksimal jumlah tebakan adalah 10.
#Dikarenakan jumlah tebakannya bila dipangkatkan 2 haslnya tidak boleh lebih dari 100 atau 1000.
#Jadi, pola yang digunakan pada tebakan adalah 2^n.












    
c0=mhsTIF('Ika',10,'Sukoharjo',240000)
c1=mhsTIF('Budi',51,'Sragen',230000)
c2=mhsTIF('Ahmad',2,'Surakarta',250000)
c3=mhsTIF('Chandra',18,'Surakarta',235000)
c4=mhsTIF('Eka',4,'Boyolali',240000)
c5=mhsTIF('fANDI',31,'Salatiga',250000)
c6=mhsTIF('Deni',13,'Klaten',245000)
c7=mhsTIF('Galuh',5,'Wonogiri',245000)
c8=mhsTIF('Janto',23,'Klaten',230000)
c9=mhsTIF('Hasan',64,'Karanganyar',270000)
c10=mhsTIF('Khalid',29,'Purwodadi',265000)
daftar=[c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]






