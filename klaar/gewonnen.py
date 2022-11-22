## WIE HEEFT ER GEWONNEN##

lijst1 = []
lijst2 = []
aantal_spelers = input("Hoeveel spelers zitten er in het team: ")
for i in range(int(aantal_spelers)):
    lijst1.append(input("Naam speler: "))
    lijst2.append(input("Aantal punten: "))

lijst2.sort(reverse = True)
print(lijst2)