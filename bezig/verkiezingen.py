## VERKIEZINGEN ##

stemlijst = []

lijstlengte = 100000

for i in range(lijstlengte):
    item = input("Voor wie stem jij: ")
    stemlijst.append(item)
    if item == "uitslag":
        stemlijst.remove("uitslag")
        break


print(stemlijst)
print(stemlijst.count(""))