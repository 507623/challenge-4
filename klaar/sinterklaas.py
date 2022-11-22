## VERLANGLIJSTJE ##

## VERLANGLIJSTJE ##

verlanglijst = []

lijstlengte = 100000

for i in range(lijstlengte):
    item = input("Wat wil jij van Sinterklaas: ")
    verlanglijst.append(item)
    if item == "KLAAR!":
        verlanglijst.remove("KLAAR!")
        break


print(verlanglijst)