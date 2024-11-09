#import math
tekst=input()
provj=True

def Provjera(m,n):
    if m<=0 or n<=0:
        print("Oba broja moraju biti pozitivna!")
        provj=True
    elif m>n:
        print("Duljina linije mora biti minimalno koliko i broj znakova!")
        provj=True
    else: provj=False
    return provj

def Ispis(tekst,m,n):
    mandat=n-m
    rici=tekst.split()
    info=list()
    for ric in rici:
        dodaj=[ric,len(ric)]
        info.append(dodaj)
    ost_dulj=maks
    redovi=list()
    red=""
    for i in range(len(info)):
        fr=info[i]
        if i==(len(info)-1):
            if (len(red)+fr[1])<ost_dulj:
                red+=fr[0]
            else:
                redovi.append(red)
                red=fr[0]
            redovi.append(red)
        elif (fr[1]+1)>ost_dulj:
            redovi.append(red)
            red=fr[0]+" "
            ost_dulj=maks-(fr[1]+1)
        else:
            red=red+fr[0]+" "
            ost_dulj=ost_dulj-(fr[1]+1)
            
    for red in redovi:
        margina=""
        for ma in range(mandat):
            margina+=" "
        if len(red)<m:
            pol_raz=round((m-len(red)/2))
            for md in range(round(pol_raz)):
                margina+=" "
        print(margina,red,margina)
        

while(provj):
    print("Unesite maksimalan broj znakova: ")
    maks=int(input())
    print("Unesite duljinu linije: ")
    duzlin=int(input())
    provj=Provjera(maks,duzlin)

Ispis(tekst,maks,duzlin)
