## RIJBEWIJS 2 ##

leeftijd = int(input("Vul hier je leeftijd in: "))

if leeftijd >= 0 and leeftijd <= 16 :
    print("Je mag nog niet op voor theorie of rijles voor je motorrijbewijs.")
if leeftijd >= 17 and leeftijd <= 17 :
    print("Je mag rijles doen op een lichte motor en theorie-examen doen, praktijk examen mag je nog niet!")
if leeftijd >= 18 and leeftijd <= 19 :
    print("Je mag op voor je praktijkexamen! Als je dit haalt krijg je je A1 rijbewijs (125cc en max vermogen 11 kW).")
if leeftijd >= 20 and leeftijd <= 20 :
    print("Je mag op voor je praktijkexamen! Als je dit haalt krijg je je A2 rijbewijs (max vermogen 35 kW).")
if leeftijd >= 21 and leeftijd <= 23 :
    print("Je mag op voor je praktijkexamen! Als je dit haalt krijg je je A1 Code 80 rijbewijs onbeperkt vermogen op voertuigen met 3 wielen, na 2 jaar kan je ook met 2 wielen (aanbevolen! onbeperkt vermogen).")
if leeftijd >= 24 and leeftijd <= 99 :
    print("Je mag op voor je praktijkexamen! Als je dit haalt krijg je je A1 rijbewijs (onbeperkt vermogen).")
