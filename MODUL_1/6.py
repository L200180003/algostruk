def cetakPrima():
    for a in range(2,1001):
        prima=1;
        for b in range(2,a):
            if(a%b==0):
                prima=0;
            if (prima == 1):
                print(a)
                break
                
                
