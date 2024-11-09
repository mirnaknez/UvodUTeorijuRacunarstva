import sys
from collections import defaultdict

def nedohvatljiva(fjePrijelaza, skup):
    provjera = False
    skupSt = skup.copy()
    for stanje in skup:
        for k, v in fjePrijelaza.items():
            if k[0] == stanje:
                if v not in skup:
                    skupSt.append(v)
                    provjera = True
    if provjera:
        return nedohvatljiva(fjePrijelaza, skupSt)
    else:
        for i in skupStanja.copy():
            if i not in skupSt:
                skupStanja.remove(i)
        for drugo in skupPrihStanja.copy():
            if drugo not in skupSt:
                skupPrihStanja.remove(drugo)
        for key in list(fjePrijelaza.keys()):
            if key[0] not in skupSt:
                del fjePrijelaza[key]
        return fjePrijelaza

skupStanja = sys.stdin.readline().strip().split(",")
skupSimbola = sys.stdin.readline().strip().split(",")
skupPrihStanja = sys.stdin.readline().strip().split(",")
pocetnoStanje = sys.stdin.readline().strip()

fjePrijelaza = defaultdict(str)

while True:
    izraz = sys.stdin.readline().strip()
    if not izraz:
        break
    lista = izraz.split("->")
    stanja1 = lista[0].split(",")
    stanja2 = lista[1]
    fjePrijelaza[tuple(stanja1)] = stanja2

skup = list([pocetnoStanje])
fjePrijelaza = nedohvatljiva(fjePrijelaza, skup)

grupe = []
prihvatljiva = set()
neprihvatljiva = set()

for key, value in fjePrijelaza.items():
    if key[0] in skupPrihStanja:
        prihvatljiva.add(key[0])
    else:
        neprihvatljiva.add(key[0])


grupe.append(sorted(list(prihvatljiva)))
grupe.append(sorted(list(neprihvatljiva)))

promjena = True
pomocna = []
while(promjena) :
        promjena = False
        for trenutna in grupe.copy():
            trenutna.sort()
            if len(trenutna) > 1:
                prvi = trenutna[0]
                a = 0
                b = 0
                pomocna = []
                for znak in skupSimbola:
                    for stanje in trenutna.copy():
                        for k,v in fjePrijelaza.items():
                            for grupa in grupe.copy():
                                if (k[0] == prvi) and (v in grupa):
                                    a = grupe.index(grupa)
                                if (k[0] == stanje) and (v in grupa):
                                    b = grupe.index(grupa)
                        if a != b:
                            if stanje not in pomocna:
                                pomocna.append(stanje)
                                promjena = True
                                grupe[grupe.index(trenutna)].remove(stanje)
            if len(pomocna) > 0 and promjena:
                grupe.append(pomocna)
                pomocna = []

pomocni = defaultdict(str)

for k,v in fjePrijelaza.items():
    for grupa in grupe:
        grupa.sort()
        if len(grupa) > 0:
            prvi = grupa[0]
            if k[0] in grupa:
                if k[0] == prvi:
                    pomocni[k] = v
for grupa in grupe:
    if len(grupa) > 0:
        prvi = grupa[0]
        for k,v in pomocni.items():
            if v in grupa:
                if v != prvi:
                    pomocni[k] = prvi

for grupa in grupe:
    if len(grupa) > 0:
        prvi = grupa[0]
        if pocetnoStanje in grupa:
            if pocetnoStanje != prvi:
                pocetnoStanje = prvi

krajnjaStanja = []
for k, v in pomocni.items():
    krajnjaStanja.append(k[0])

for i in skupStanja.copy():
    if i not in krajnjaStanja:
        skupStanja.remove(i)
for drugo in skupPrihStanja.copy():
    if drugo not in krajnjaStanja:
        skupPrihStanja.remove(drugo)

print(*skupStanja, sep=",")
print(*skupSimbola, sep=",")
print(*skupPrihStanja, sep=",")
print(pocetnoStanje)
for key, value in pomocni.items():
    print(key[0] + "," + key[1] + "->" + value)
