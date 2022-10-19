largeur = int(input("saisir la largeur :"))
hauteur = int(input("saisir la hauteur :"))


tiret = "-"
espace = " "

largeur -= 2

print("|" + (tiret * largeur) + "|")

i = 1

while i != hauteur - 1:
    print("|" + (espace * largeur) + "|") 
    i += 1


print("|" + (tiret * largeur) + "|") 