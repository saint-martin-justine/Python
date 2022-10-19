def fonctionIndefini(*args):
    myList = []
    for n in args :
        myList += [n]
        N = len(myList)
        for n in range(1,N):
            #La range()fonction renvoie une séquence de nombres,
            #commençant par 0 par défaut, et incrémentée de 1 (par défaut),
            #et s'arrête avant un nombre spécifié.
            cle = myList[n]
            j = n-1
            while j>=0 and myList[j] > cle:
                myList[j+1] = myList[j] # decalage
                j = j-1
            myList[j+1] = cle
    print(myList)

fonctionIndefini(5,1,3,2,4)