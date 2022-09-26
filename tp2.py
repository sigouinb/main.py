#Benjamin Sigouin, 404
#TP2
from random import randint

print("J'ai choisi un nombre entre 1 et 100. À vous de deviner.")

nombre = randint(0,100)
guess = int(input("Entre un nombre."))

def(game):
    if guess == nombre:
        guess = True
        print("Tu as bien deviné!")
    elif guess != nombre:
        guess = False
        print("Mauvaise réponse! Essaye encore.")
while guess == False:
    guess = int(input("Entre un nombre."))
    run(game)
