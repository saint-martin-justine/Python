i = 1

#Tant que i n'est pas égal a 100
while i != 100:
    #Si i modulo 3 (le reste de 3 par exemple 6 / 3 ça fait 2 et il reste 0) = 0 et modulo 5 = 0 alors afficher FizzBuzz
    if (((i % 3) == 0) and (i % 5) == 0):
        print("FizzBuzz")
        i += 1
    #et si i % 5 = 0 alors afficher Buzz
    elif(i % 5) == 0:
        print("Buzz")
        i += 1
    #et si i % 3 = 0 alors afficher Fizz
    elif(i % 3) == 0:
        print("Fizz")
        i += 1
    #Sinon afficher i
    else:
        print(i)
        i += 1