def gambarlahPersegiEmpat(l,p):
    for i in range(l):
        if(i==0 or i==(l-1)):
            print("@"*p)
        else:
            print("@" + (" "*(p-2)+"@"))
