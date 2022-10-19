#trier un tableau
def fonctionIndefini(*args):
    mylist = []
    for n in args :
        mylist += [n]
    mylist.sort()
    print(mylist)

fonctionIndefini(5,1,2,3,4)  
