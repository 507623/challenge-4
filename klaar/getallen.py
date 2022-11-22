## GETALLEN ##

#n1 = int(input("Vul je eerste nummer in: "))
#n2 = int(input("Vul je tweede nummer in: "))
#n3 = int(input("Vul je derde nummer in: "))
#n4 = int(input("Vul je vierde nummer in: "))
#n5 = int(input("Vul je vijfde nummer in: "))

#n1, n2, n3, n4, n5 = input("Vul hier de 5 getallen in die je wilt sorteren van groot naar klein, zet een komma na ieder nummer: ")

#print(sorted(n1, n2, n3, n4, n5))

print("Typ 5 getallen gescheiden door een spatie. De getallen zullen gesorteerd worden.: ")
try:
    getallen = list(map(int, input().split()))
    getallen.sort()
    getallen.reverse()
    print("Na het sorteren van deze getallen: ")
    print(*getallen)
except ValueError:
    print("Het is fout gegaan. Probeer opnieuw.")
