uvjet=True
def Zvjezdice(b):
    if b%2==0:
        print("Unesite neparan broj")
        return True
    else:
        for i in range(0,b,2):
            x=""
            for j in range(int(b-i/2)):
                x+=" "
            for f in range(i+1):
                x+="*"
            for j in range(int(b-i/2)):
                x+=" " 
            print(x)
        for i in range(b-2,0,-2):
            x=""
            for j in range(int(b+1-i/2)):
                x+=" "
            for f in range(i):
                x+="*"
            for j in range(int(b+1-i/2)):
                x+=" " 
            print(x)
        return False

while(uvjet):
    print("Unesite broj redova: ")
    br=int(input())
    uvjet=Zvjezdice(br)
