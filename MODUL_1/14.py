def formatRupiah(x):
    y=str(x)
    if len(y)<=3:
        return 'Rp '+y
    else:
        p=y[-3:]
        q=y[:-3]
        return formatRupiah(q) + '.' + p
