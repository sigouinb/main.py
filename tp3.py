#Benjamin Sigouin, 404
#TP3

from random import randint

def jeu():
    choix = str(input("""Vous tombez face à un monstre. Vous avez 4 options: 
    1. Combattre"
    2. Contourner
    3. Afficher les règles du jeu
    4. Quitter la partie"""))
    if choix == "1":
        def adversaire():
            global winstreak
            global playerhp
            winstreak = 0
            enemyhp = 4
            playerhp = 20
            dice = randint(1, 6)
            print("Vous tombez face à un adversaire.")
            print("Vous avez roulé", dice)
            if dice > enemyhp:
                winstreak += 1
                print("Vous avez gagné. Votre nombre de victoires consécutives est", winstreak)
                print("Points de vie:", playerhp + dice)
                jeu()
            elif dice < enemyhp:
                print("Vous avez perdu.")
                print("Points de vie:", playerhp - dice)
                jeu()

        adversaire()


jeu()