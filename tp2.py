#Benjamin Sigouin, 404
#TP2
from random import randint

print("J'ai choisi un nombre entre 1 et 100. À vous de deviner.")

nombre = randint(0,100)
guess = int(input(("Entre un nombre.")))
if guess == nombre:
    print("Tu as bien deviné!")


elif guess > nombre:
    print("Incorrect. Ton choix est plus grand que le nombre que j'ai choisi." + guess)


elif guess < nombre:
    print("Incorrect. Ton choix est plus petit que le nombre que j'ai choisi." + guess)