def fonctionIndefini(*args):
# [] pour faire un tableau 
    mylist = []
    for n in args :
        mylist += [n]
        #+= Ajoute une valeur et la variable et affecte le résultat à cette variable.
    for i in range(len(mylist)):
            #range quand on veut itérer une action un certain nombre de fois.
            # len() sur des strings, tuples, listes, dictionnaires, ensembles et range.
        if (mylist[i] % 2) == 0:
            # Modulo: Il renvoie le reste de la division de l'opérande de gauche par l'opérande de droite. 
            print(mylist[i])

#affiche les nombres pairs de la list

fonctionIndefini(1,2,3,4,)