r1=[" "," "," "]
r2=[" "," "," "]
r3=[" "," "," "]
polje=[r1,r2,r3]
krizic=True

def Provjera(b):
    if ((r1[0]!=" ") & (r1[0]==r1[1]==r1[2])):
        print("Gotova igra")
        igra=False
    elif((r2[0]!=" ") & (r2[0]==r2[1]==r2[2])):
        print("Gotova igra")
        igra=False
    elif((r3[0]!=" ") & (r3[0]==r3[1]==r3[2])):
        print("Gotova igra")
        igra=False
    elif((r1[0]!=" ") & (r3[0]==r2[0]==r1[0])):
        print("Gotova igra")
        igra=False
    elif((r1[1]!=" ") & (r3[1]==r2[1]==r1[1])):
        print("Gotova igra")
        igra=False
    elif((r1[2]!=" ") & (r3[2]==r2[2]==r1[2])):
        print("Gotova igra")
        igra=False
    elif((r1[0]!=" ") & (r1[0]==r2[1]==r3[2])):
        print("Gotova igra")
        igra=False
    elif((r3[0]!=" ") & (r3[0]==r2[1]==r1[2])):
        print("Gotova igra")
        igra=False
    elif(b==9):
        print("Gotova igra")
    else: igra=True
    return igra


def Ispis():
    print("____________________")
    for item in polje:
        print("| ",item[0]," | ",item[1]," | ",item[2]," |")
        print("____________________")


def Postavi(broj,znak):
    if broj==1:
        if(r1[0]==" "):
            r1[0]=znak
            Ispis()
        else: print("Polje zauzeto")
    elif broj==2:
        if(r1[1]==" "):
            r1[1]=znak
            Ispis()
        else: print("Polje zauzeto")
    elif broj==3:
        if(r1[2]==" "):
            r1[2]=znak
            Ispis()
        else: print("Polje zauzeto")
    elif broj==4:
        if(r2[0]==" "):
            r2[0]=znak
            Ispis()
        else: print("Polje zauzeto")
    elif broj==5:
        if(r2[1]==" "):
            r2[1]=znak
            Ispis()
        else: print("Polje zauzeto")
    elif broj==6:
        if(r2[2]==" "):
            r2[2]=znak
            Ispis()
        else: print("Polje zauzeto")
    elif broj==7:
        if(r3[0]==" "):
            r3[0]=znak
            Ispis()
        else: print("Polje zauzeto")
    elif broj==8:
        if(r3[1]==" "):
            r3[1]=znak
            Ispis()
        else: print("Polje zauzeto")
    elif broj==9:
        if(r3[2]==" "):
            r3[2]=znak
            Ispis()
        else: print("Polje zauzeto")
    else: print("Nije dobar unos, broj mora biti izmedu 1 i 9")

def Ispis():
    print("____________________")
    for item in polje:
        print("| ",item[0]," | ",item[1]," | ",item[2]," |")
        print("____________________")
    

print("Igra krece")
Ispis()
brojac=0
while(Provjera(brojac)):
    if krizic:
        print("Unesite vrijedost za X: ")
        br=int(input())
        Postavi(br,"X")
        krizic=False
    else:
        print("Unesite vrijedost za O: ")
        br=int(input())
        Postavi(br,"O")
        krizic=True
    brojac+=1
