## PALINDROOM ##

woord = input("Voer woord in om te checken of het een palindroom is: ")
check = woord [::-1]
print(check)

if woord == check : 
    print(woord + " is een palindroom.")

else :
    print(woord + " is geen palindroom.")