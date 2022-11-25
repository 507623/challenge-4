## FACULTEIT ##
import math

nummer = int(input("Voer een getal in: "))

faculteit = math.factorial(nummer)

if nummer <= 0 :
    print("Faculteit bestaat niet voor negatieve getallen.")
    
elif nummer == 0 :
    print("De faculteit van 0 is 1.")

else :
    for i in range(nummer) :
        print(faculteit)