from random import randrange
from math import ceil

continuerlejeu = True
total : int= 100
while continuerlejeu:




    def saisie():
        """

        :rtype: int
        """
        test = False

        while test == False:
            try:
                num: int = int(input("donner un numéro:"))

                assert 0 <= num <= 49
                test = True
            except ValueError:
                print("Ce n'est pas un numéro")
            except AssertionError:
                print("Le numéro n'est pas compris entre 0 et 49 ")

        return num


    def saisiemoney() -> int:
        test = False
        while test == False:
            try:
                money = int(input("donner votre somme d'argent:"))
                assert 0 <= money <= total
                test = True
            except ValueError:
                print("Ce n'est pas un numéro")
            except AssertionError:
                print("La somme d'argent n'est pas positive")
        return money



    num = saisie()
    money = saisiemoney()
    roulette = randrange(50)

    print("Roulette =", roulette)
    # resultat
    if roulette == num:
        print("Félicitaions!")
        total += money*3
        print("Total money =" + str(total))
    elif (roulette % 2) == (num % 2):
        print("Bonne couleur")
        total += ceil(money / 2)
        print("Total money =" + str(total))
    else:
        print("Loser!")
        total -= money
        print("Total money=" + str(total))
    # continuer le jeu
    if total <= 0:
        print("Vous n'avez plus d'argent")
        continuerlejeu = False
    else:
        print("vous avez :", total)
        quitter = str(input("Voulez-vous quitter le jeux o/n ?"))
        if quitter == 'o' or quitter == 'O':
            continuerlejeu = False



