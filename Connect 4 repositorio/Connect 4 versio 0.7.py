#Connect 4 pelissä on 6 riviä ja 7 jonoa.
jonot = [0,0,0,0,0,0,0]
täysijono = 6
leveys = 7
#Tuossa tarkistetaan kuinka monta kussakin jonossa on ja määritellään kuinka iso on isoin jono.
#_ esittää tyhjää tilaa R esittää punaisen pelaajan siirtoa ja S sinisen
Lauta = [
["_","_","_","_","_","_","_"],
["_","_","_","_","_","_","_"],
["_","_","_","_","_","_","_"],
["_","_","_","_","_","_","_"],
["_","_","_","_","_","_","_"],
["_","_","_","_","_","_","_"],
]

#merkitsemme pelaajien nappulat näin peli alkaa sinisellä pelaajalla
nykyinenpelaaja = "S"
pelaaja1 = "S"
pelaaja2 = "R"
#merkataan sallitut siirrot
sallitutsiirrot = [1,2,3,4,5,6,7]
#jokaisen siirron jälkeen tarkistamme olemmeko saavuttanut 4 putkeen.

def voitonTarkistaminen(pelaaja, paikkax, paikkay):
    #print(pelaaja, paikkax,paikkay)
    mahdolliset = []
    if (paikkay > 0):
        mahdolliset.append((paikkay-1,paikkax))
    if (paikkay <täysijono-1):
        mahdolliset.append((paikkay+1,paikkax))
    #katsomme löydämmekö neljän jonoa ylöspäinsuunnassa.
    lasku = 1
    käydyt = [(paikkay,paikkax)]
    while len(mahdolliset) > 0:
        nykyinen = mahdolliset[0]
        #print(nykyinen)
        #print("tämä on nappula", Lauta[nykyinen[0]][nykyinen[1]], lasku)
        if (Lauta[nykyinen[0]][nykyinen[1]] == pelaaja):
            #print("tapa")
            lasku +=1
            if (lasku >= 4):
                return True
            käydyt.append(nykyinen)
            if (nykyinen[0] <5):
                if ((nykyinen[0]+1,nykyinen[1]) not in käydyt):
                    mahdolliset.append((nykyinen[0]+1,nykyinen[1]))
                    #print("alaspäin")
            if (nykyinen[0] >0):
                if ((nykyinen[0]-1,nykyinen[1]) not in käydyt):
                    mahdolliset.append((nykyinen[0]-1,nykyinen[1]))
                    #print("ylöspäin")
        mahdolliset = mahdolliset[1:]
        #print(käydyt)
    
    #nyt tarkistamme toisen akselin eli sivuttais suunnassa
    #teemme tämän vielä kahdelle muulle akselille
    mahdolliset = []
    if (paikkax > 0):
        mahdolliset.append((paikkay,paikkax-1))
    if (paikkax <leveys-1):
        mahdolliset.append((paikkay,paikkax+1))
    lasku = 1
    käydyt = [(paikkay,paikkax)]
    while len(mahdolliset) > 0:
        nykyinen = mahdolliset[0]
        #print(nykyinen)
        #print("tämä on nappula", Lauta[nykyinen[0]][nykyinen[1]])
        if (Lauta[nykyinen[0]][nykyinen[1]] == pelaaja):
            lasku +=1
            if (lasku >= 4):
                return True
            käydyt.append(nykyinen)
            if (nykyinen[1] <leveys-1):
                if ((nykyinen[0],nykyinen[1]+1) not in käydyt):
                    mahdolliset.append((nykyinen[0],nykyinen[1]+1))
            if (nykyinen[1] >0):
                if ((nykyinen[0],nykyinen[1]-1) not in käydyt):
                    mahdolliset.append((nykyinen[0],nykyinen[1]-1))
        mahdolliset = mahdolliset[1:]
    
    #teemme samana tarkistuksen luode-kaakko suunnassa(eli alkaen vasemmalta ylhäältä)
    mahdolliset = []
    if (paikkax > 0 and paikkay >0):
        mahdolliset.append((paikkay-1,paikkax-1))
    #print(paikkax,"<",leveys-1,"and",paikkay,"<", täysijono-1)
    if (paikkax <leveys-1 and paikkay <täysijono-1):
        mahdolliset.append((paikkay+1,paikkax+1))
    lasku = 1
    käydyt = [(paikkay,paikkax)]
    #print(mahdolliset)
    while len(mahdolliset) > 0:
        nykyinen = mahdolliset[0]
        #print(nykyinen)
        #print("tämä on nappula", Lauta[nykyinen[0]][nykyinen[1]], lasku)
        if (Lauta[nykyinen[0]][nykyinen[1]] == pelaaja):
            #print("tapa")
            lasku +=1
            if (lasku >= 4):
                return True
            käydyt.append(nykyinen)
            if (nykyinen[1] <leveys-1 and nykyinen[0] < täysijono-1):
                if ((nykyinen[0]+1,nykyinen[1]+1) not in käydyt):
                    mahdolliset.append((nykyinen[0]+1,nykyinen[1]+1))
            if (nykyinen[1] >0 and nykyinen[0] > 0):
                if ((nykyinen[0]-1,nykyinen[1]-1) not in käydyt):
                    mahdolliset.append((nykyinen[0]-1,nykyinen[1]-1))
        mahdolliset = mahdolliset[1:]
    


    #teemme samana tarkistuksen koilinen-lounas suunnassa(eli alkaen oikealta ylhäältä)
    mahdolliset = []
    #print(paikkax,">",0,"and",paikkay,"<", täysijono-1)
    if (paikkax <leveys-1 and paikkay > 0):
        mahdolliset.append((paikkay-1,paikkax+1))
    if (paikkax > 0 and paikkay < täysijono-1):
        mahdolliset.append((paikkay+1,paikkax-1))
    lasku = 1
    käydyt = [(paikkay,paikkax)]
    #print(mahdolliset)
    while len(mahdolliset) > 0:
        nykyinen = mahdolliset[0]
        #print(nykyinen)
        #print("tämä on nappula", Lauta[nykyinen[0]][nykyinen[1]], lasku)
        if (Lauta[nykyinen[0]][nykyinen[1]] == pelaaja):
            #print("tapa")
            lasku +=1
            if (lasku >= 4):
                return True
            käydyt.append(nykyinen)
            if (nykyinen[1] >0 and nykyinen[0] < täysijono-1):
                if ((nykyinen[0]+1,nykyinen[1]-1) not in käydyt):
                    mahdolliset.append((nykyinen[0]+1,nykyinen[1]-1))
            if (nykyinen[1] <leveys-1 and nykyinen[0] >0):
                if ((nykyinen[0]-1,nykyinen[1]+1) not in käydyt):
                    mahdolliset.append((nykyinen[0]-1,nykyinen[1]+1))
        mahdolliset = mahdolliset[1:]


    
while True:

    for rivi in Lauta:
        print(rivi)
    print("  1","   2","   3","   4","   5","   6","   7")
    siirto = int(input("Tee siirto "+nykyinenpelaaja+" :"  ))
    if (siirto == "pois"):
        break
    if (siirto in sallitutsiirrot):
        #print("tapa")
        if (jonot[siirto-1] < 6):
            korkeus = 6-jonot[siirto-1]-1
            Lauta[korkeus][siirto-1] = nykyinenpelaaja
            jonot[siirto-1]+=1
            lasku = voitonTarkistaminen(nykyinenpelaaja, (siirto-1), korkeus)
            if (lasku):
                print(nykyinenpelaaja, "voitit pelin")
                print("WOHOOO")
                break
            if (nykyinenpelaaja == "S"):
                nykyinenpelaaja=pelaaja2
            else:
                nykyinenpelaaja = pelaaja1
            


for rivi in Lauta:
        print(rivi)
print("  1","   2","   3","   4","   5","   6","   7")