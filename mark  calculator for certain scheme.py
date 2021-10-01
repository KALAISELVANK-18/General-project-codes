import sqlite3
def ef():
    t=['T','E','M','S','SS']
    m = []
    for i in range(0,5):

        s= int(input('Enter '+t[i]+":"))
        m.append(s)



    for b in range(0,2):

        g=m.index(min(m))
        del(m[g])

    print(m)
    b=0
    for h in range(0,3):
       b+=int(m[h])
    tmark=round((b/6),2)
    print(tmark)

    w=['T','E','M','P','C','CS']
    E=[]
    for h in range(0,6):
        s= int(input('Enter '+w[h]+':'))
        E.append(s)
    print(E)
    n=0
    cut=0
    for c in range(0,6):
        if c<=2:
            m=((((int(E[c]))-10)/90)*20)+tmark+30
            ii=round(m,2)
            print('twelvth '+w[c]+' mark:',ii)
            n+=ii
            if c==2:
                cut+=ii
        if c>2:
            mm=((((int(E[c])) - 30)/70) * 20) + tmark + 30
            iii=round(mm,2)
            print('twelvth ' + w[c] + ' mark:',iii )
            n+=iii
            if c==3 or c==4:
                nn=iii/2
                cut+=round(nn,2)



    print('total:',round(n,2))
    print(round(cut,2))

ef()





