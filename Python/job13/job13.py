fichier = open("C:/Users/justi/OneDrive/Bureau/Python/data.txt", "r")

lignes = fichier.readlines()

saisi = int(input("Saisir la longueur du mot souhaité : "))

compteur = 0
#Pour la ligne(i) dans les lignes
for ligne in lignes:
    #Séparer la phrase pour en faire un tableau de mot
    mot = ligne.split()
    #Pour i dans la longeur du tableau
    for i in range(len(mot)):
        #caractere va stocker un mot
        caractere = mot[i]
        #Si la longueur du mot est égal a la saisi de l'utilisateur compteur + 1
        if len(caractere) == saisi:
            compteur += 1

print("Il y a", compteur ,"mots qui sont de longueur", saisi)