from random import randrange
from math import ceil


def saisie():
    """

    :rtype: int
    :return:
    """
    test = True
    while test:
        try:
            num: int = int(input("donner un numéro:"))
            money = int(input("donner votre somme d'argent:"))
            assert (0 <= num <= 49) and money > 0
            test = False
        except ValueError:
            print("Ce n'est pas un numéro")
        except AssertionError:
            print("le numéro n'est pas compris entre 0 et 49 ou la somme d'argent n'est pas positive")

    return num, money


def Zcasino():
    num, money = saisie()
    roulette = randrange(50)
    print("roulette =", roulette)
    if roulette == num:
        print(("félicitaions!"))
        money += 3 * money
        return (print("money =" + str(money)))
    elif ((roulette % 2) == 0 and (num % 2) == 0) or ((roulette % 2) != 0 and (num % 2) != 0):
        money += ceil(money / 2)
        return (print("money =" + str(money)))
    else:
        print("jouez de nouveau")
        money = 0
        return (print("money=" + str(money)))


Zcasino()
