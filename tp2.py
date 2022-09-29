#Benjamin Sigouin, 404
#TP2
from random import randint


def jeux():
    print("J'ai choisi un nombre entre 1 et 1000. À vous de deviner.")

    nombre = randint(0,10)
    guess = int(input("Entre un nombre."))
    def game():
        if guess != nombre:
            print("Mauvaise réponse! Essaye encore.")
            if guess > nombre:
                print("Ton choix de nombre est plus grand que mon nombre.")
            elif guess < nombre:
                print("Ton choix de nombre est plus petit que mon nombre.")
        elif guess == nombre:
            print("Tu as bien deviné! Ton nombre d'essais est:")

    while guess != nombre:
        guess = int(input("Entre un nombre."))
        game()
jeux()
quitte = str(input("Voulez-vous quitter? (y/n)"))
if quitte == "n":
    jeux()

countWord = def count():