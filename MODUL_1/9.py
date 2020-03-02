def cetak():
    for i in range (1,100):
        if (i%3==0):
            print("Phyton")
        elif(i%5==0):
            print("UMS")
        elif(i%3==0 and i%5==0):
            print("Python UMS")
        else:
            print(i)
