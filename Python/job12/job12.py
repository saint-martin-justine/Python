fichier = open("C:/Users/justi/OneDrive/Bureau/Python/data.txt", "r")

lignes = fichier.readlines()

compteurCarSpe = 0
compteurMot = 0

for ligne in lignes:

    caractereSpeciaux = ['.', '^', '$', '*', '+', '?', '{', '}', '[', ']', '\\', '|', '(', ')']
     
    #split sert à séparer chaque mot dans la liste
    mot = ligne.split()
    #Permet de calculer le nombre de mot de chaque lignes
    for i in range (len(mot)):
        compteurMot += 1
    #Permet de calculer le nombre de mot avec des caractères spéciaux de chaque lignes
    for i in range (len(caractereSpeciaux)):
        #Si il trouve un caractère spécial suivant i
        if ligne.find(caractereSpeciaux[i])> 0:
            compteurCarSpe += 1

print("Il y'a ", (compteurMot - compteurCarSpe), "mot ")