saisi = str(input("saisir un texte \n>"))
#permet de lire e ecrire dans le fichier
fichier = open("C:/Users/justi/OneDrive/Bureau/Python/output.txt", "a")
fichier.write("\n" + saisi)
fichier.close()