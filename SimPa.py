import sys
from collections import defaultdict

ulazniZnakovi = sys.stdin.readline().strip().split("|")
skupStanja = sys.stdin.readline().strip().split(",")
skupZnakova = sys.stdin.readline().strip().split(",")
skupZnakovaStoga = sys.stdin.readline().strip().split(",")
skupPrihStanja = sys.stdin.readline().strip().split(",")
pocetnoStanje = sys.stdin.readline().strip()
pocetniZnakStoga = sys.stdin.readline().strip()

fjePrijelaza = defaultdict(str)

while True:
    izraz = sys.stdin.readline().strip()
    if not izraz:
        break
    lista = izraz.split("->")
    stanja1 = lista[0].split(",")
    stanja2 = lista[1].split(",")
    fjePrijelaza[tuple(stanja1)] = stanja2

for niz in ulazniZnakovi:
    listaZnakova = niz.split(",")
    stog = pocetniZnakStoga
    prethodnoStanje = pocetnoStanje
    print(pocetnoStanje + "#" + stog + "|", end = "")
    i = 0
    while(i < len(listaZnakova)):
        znak = listaZnakova[i]
        provjera = False
        krivo = False
        if(len(stog) >= 1):
            pom = stog[0]
        else:
            pom = "$"
        if(pom != "$"):
            for key, value in fjePrijelaza.items():
                if((key[0] == prethodnoStanje) and (key[1] == znak or key[1] == "$") and (key[2] == pom)):
                    provjera = True
                    prethodnoStanje = value[0]
                    if(value[1] != "$"):
                        stog = value[1] + stog[1:]
                    elif(value[1] == "$" and len(stog) == 1):
                        stog = str()
                    elif(value[1] == "$" and len(stog) > 1):
                        stog = stog[1:]
                    if(key[1] == znak):
                        i = i + 1
                    if(len(stog) > 0):
                        print(prethodnoStanje + "#" + stog + "|", end = "")
                    else:
                        print(prethodnoStanje + "#" + "$" + "|", end = "")
                    break
        if((provjera == False)):
           print("fail" + "|", end = "")
           krivo = True
           break
    if(krivo != True and prethodnoStanje not in skupPrihStanja):
        provjera2 = True
        while(provjera2):
            provjera2 = False
            if(len(stog) > 0):
                pom = stog[0]
            else:
                pom = "$"
            if(pom != "$"):
                for key, value in fjePrijelaza.items():
                    if((key[0] == prethodnoStanje) and ( key[1] == "$") and (key[2] == pom)):
                        prethodnoStanje = value[0]
                        if(value[1] != "$"):
                            stog = value[1] + stog[1:]
                        elif(value[1] == "$" and len(stog) == 1):
                            stog = str()
                        elif(value[1] == "$" and len(stog) > 1):
                            stog = stog[1:]
                        if(key[1] != "$"):
                            i = i + 1
                        if(len(stog) > 0):
                            print(prethodnoStanje + "#" + stog + "|", end = "")
                        else:
                            print(prethodnoStanje + "#" + "$" + "|", end = "")
                        if(prethodnoStanje in skupPrihStanja):
                            provjera2 = False
                        else:
                            provjera2 = True
                        break
    if((prethodnoStanje in skupPrihStanja) and (krivo == False)):
        print("1")
    else:
        print("0")