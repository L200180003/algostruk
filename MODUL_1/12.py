import random
def tebak():
    i=0
    a=random.randrange(0,100)
    while(i<=6):
        b=int(input("Masukkan angka : "))
        i+=1
        if(b>a):
            print("Angka terlalu besar")
        elif(b<a):
            print("Angka terlalu kecil")
        else:
            print("Tebakan anda benar!")
    print("\nMaaf batas mencoba hanya 7x")
    print('Jawabannya adalah',a)
