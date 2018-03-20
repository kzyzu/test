import  random
import  webbrowser
import time
#mandaty do rozdania

mandaty =460

print("ilosc mandatów " + str(mandaty))

#ilosc osób uproawnionch do głosowania
ilosc_uprawnionych = 30000000

print("ilosc uprawnionych osob " + str(ilosc_uprawnionych))

#losowanie frekfencji


frekfencja = random.randrange(1,99)
print("frekfencja " + str(frekfencja) +"%")

#ile osob wzielo udzial w glosowaniu

print("ile osob wzielo udzial w glosowaniu " + str(ilosc_uprawnionych * frekfencja))

#losowanie rozkladu glosów

partiaA = random.randrange(1,99)
partiaB = random.randrange(1,99)
partiaC = random.randrange(1,99)

suma = partiaA +partiaB + partiaC

#Liczba Glosow

glosyA = partiaA/suma * ilosc_uprawnionych * frekfencja
glosyB = partiaB/suma * ilosc_uprawnionych * frekfencja
glosyC = partiaC/suma * ilosc_uprawnionych * frekfencja

print("glosy na partie A " + str(int(glosyA)))
print("glosy na partie B " + str(int(glosyB)))
print("glosy na partie C " + str(int(glosyC)))

iloscGlosowNa1Partie = 2

#Rozklad mandatów

#ilosc glosow metoda d honta
#partia
listyA =[]
listyB = []
listyC = []

sort =[]
wszystkieGlosy =[]
listaGlosyPartia = {'a' : 2}
for i in range(mandaty+1):
    listyA.append(glosyA/(i+1))
    listyB.append(glosyB/(i+1))
    listyC.append(glosyC/(i+1))
    wszystkieGlosy.append(glosyA/(i+1))
    wszystkieGlosy.append(glosyB/(i+1))
    wszystkieGlosy.append(glosyC/(i+1))
sort = sorted(wszystkieGlosy,reverse=True)


#rozklad mandatow

print("Partia A otrzymala mandatów:")
for i in range(460):
    if listyA[i]<=sort[460]:
        print(i)
        break

print("Partia B otrzymala mandatów:")
for i in range(460):
    if listyB[i]<=sort[460]:
        print(i)
        break

print("Partia C otrzymala mandatów:")
for i in range(460):
    if listyC[i]<=sort[460]:
        print(i)
        break


if(glosyA<ilosc_uprawnionych*frekfencja*0.05 or glosyB<ilosc_uprawnionych*frekfencja*0.05 or glosyC<ilosc_uprawnionych*frekfencja*0.05):
    print("funkcja korwin")
    print("nie przekroczyles progu wyborczego")
    time.sleep(5)
    webbrowser.open('https://youtu.be/j4AtJ_xrrH8?t=22s')



