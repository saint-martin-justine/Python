fichier = open("C:/Users/justi/OneDrive/Bureau/Python/domains.xml", "r")

lignes = fichier.readlines()

compteur = 0

for ligne in lignes:
    if ligne.find("domain") != -1:
        compteur += 1

print("Il y'a ", compteur, "domain")