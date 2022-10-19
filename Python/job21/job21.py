def mySort(myList):
        N = len(myList)
        for n in range(1,N):
            cle = myList[n]
            j = n-1
            while j>=0 and myList[j] > cle:
                myList[j+1] = myList[j] #decalage
                j = j-1
            myList[j+1] = cle
        return myList

def myDysplay(myList):
    print(myList)

liste = [5,1,3,2,4]

liste = mySort(liste)

liste = myDysplay(liste)

