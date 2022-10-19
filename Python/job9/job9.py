hauteur = int(input("saisir chiffre : "))

a = 0 
for j in range(hauteur,1, -1):


    print(" " * j + "/" + " " * a * 2 + "\\")
    a += 1

print(" /" + "__" * (hauteur - 1) + "\\")