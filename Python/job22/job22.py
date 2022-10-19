#Importer la bibliothèque time
import time

def myUpper(phrase):
    lowercase_characters =  [chr(i) for i in range(97 , 122)]
    # on peut donc obtenir un caractère majuscule à partir d'un caractère minuscule 
    #en soustrayant 32 à son code ascii
    
    # initialisation de la liste qu'on cherche
    s_upper = ""
    for x in phrase:
        if x in lowercase_characters:
            # on transforme le caractère minuscule en majuscule
            x = chr(ord(x) -32)
            # on ajoute le caractère à la liste 
            s_upper = s_upper + x
        else:
            s_upper = s_upper + x
            
    return s_upper

def myLower(phrase):

    uppercase_characters = [chr(i) for i in range(65 , 91)]
    # on peut donc obtenir un caractère majuscule à partir d'un caractère minuscule 
    
    # initialisation de la liste qu'on cherche
    s_lower = ""
    for x in phrase:
        if x in uppercase_characters:
            # on transforme le caractère minuscule en majuscule
            x = chr(ord(x) +32)
            # on ajoute le caractère à la liste 
            s_lower = s_lower + x
        else:
            s_lower = s_lower + x
            
    return s_lower
    
def myTitle(phrase):
    result = []
    mot = phrase.split()

    for i in range (len(mot)):
        caractere = mot[i][0]

        result.append(myUpper(caractere) + mot[i][1:])

    return (' '.join(result))

def myClean(phrase):

    return (' '.join(phrase.split()))

    
saisi1 = str(input("Saisir une chaine de caractère : "))
saisi2 = str(input("Veuillez saisir parmis ces options : \n -upper \n -lower \n -title \n -clean \n -exit \n>" ))

while saisi2 != "Exit":
    match saisi2:
        case "upper":
            print(myUpper(saisi1))
        case "lower":
            print(myLower(saisi1))
        case "title":
            print(myTitle(saisi1))
        case "clean":
            print(myClean(saisi1))

    #Permet de stoper le programme pendant 1.5s avant de passer a la suite
    # cela permet un meilleur affichage et une meilleure utilisation du programme
    time.sleep(1.5)

    saisi2 = str(input("\nVeuillez saisir parmis ces options : \n -upper \n -lower \n -title \n -clean \n -Exit \n>" ))



     
    