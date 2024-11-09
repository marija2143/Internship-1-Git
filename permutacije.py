ni=input()
niz=ni.split()
#print("Pocetni niz: ",niz)
def Perma(n,i):
        #print("i: ",i," j: ",j)
        if i==len(n)-1:
            print( ''.join(n))
            return
        for j in range(i,len(n)):
            n[i],n[j]=n[j],n[i]
            Perma(n,i+1)
            n[j],n[i]=n[i],n[j]
        

Perma(niz,0)
