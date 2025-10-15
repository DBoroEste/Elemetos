import random
elementos = [
    ["Hidrógeno","H","G1 P1"],["Litio","Li","G1 P2"],["Sodio","Na","G1 P3"],["Potasio","K","G1 P4"],["Rubidio","Rb","G1 P5"],["Cesio","Cs","G1 P6"],["Francio","Fr","G1 P7"],["Berilio","Be","G2 P2"],["Magnesio","Mg","G2 P3"],["Calcio","Ca","G2 P4"],["Estroncio","Sr","G2 P5"],["Bario","Ba","G2 P6"],["Radio","Ra","G2 P7"],["Boro","B","G13 P2"],["Aluminio","Al","G13 P3"],["Galio","Ga","G13 P4"],["Indio","In","G13 P5"],["Talio","Tl","G13 P6"],["Carbono","C","G14 P2"],["Silicio","Si","G14 P3"],["Germanio","Ge","G14 P4"],["Estaño","Sn","G14,P5"],["Plomo","Pb","G14 P6"],["Nitrógeno","N","G15 P2"],["Fósforo","P","G15 P3"],["Arsénico","As","G15 P4"],["Antimonio","Sb","G15 P5"],["Bismuto","Bi","G15 P6"],["Oxígeno","O","G16 P2"],["Azufre","S","G16 P3"],["Selenio","Se","G16 P4"],["Telurio","Te","G16 P5"],["Polonio","Po","G16 P6"],["Flúor","F","G17 P2"],["Cloro","Cl","G17 P3"],["Bromo","Br","G17 P4"],["Yodo","I","G17 P5"],["Astato","At","G17 P6"],["Helio","He","G18 P1"],["Neón","Ne","G18 P2"],["Argón","Ar","G18 P3"],["Kriptón","Kr","G18 P4"],["Xenón","Xe","G18 P5"],["Radón","Rn","G18 P6"
]
print("Este es el tests de los elementos, en la posición pon El grupo y el periodo así: (Hidrógeno) G1 P1")
a = 0
while a == 0:
    elección = random.choice(elementos)
    print(random.choice(elección))
    elemento = input("Elemento: ")
    símbolo = input("Símbolo: ")
    Posición = input("Posición: ")
    if(elemento.lower() == elección[0].lower() ):
     print(elemento," ✔️")
    else:
        print(elemento," ❌")
    if(símbolo == elección[1]):
      print(símbolo," ✔️")
    else:
       print(símbolo," ❌")
    if(Posición == elección [2]):
       print(Posición," ✔️")
    else:
      print(Posición," ❌")
    r = input("¿Quieres continuar?")
    if(r.lower() == "no"):
       a = 1