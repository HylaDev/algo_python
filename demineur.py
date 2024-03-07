import random
from colorama import Back, Fore, Style

# creation de la grille avec des lignes, colonnes et le nombre de bombes à placer
def creation_grille(lignes, colonnes, bombes):
    # initialisation de la grille
    grille = [['0' for _ in range(colonnes)] for _ in range(lignes)]
    bombe_placer = 0
    while bombe_placer <= bombes:
        ligne = random.randint(0, lignes - 1)
        colonne = random.randint(0, colonnes - 1)
        if bombes <= lignes*colonnes:
            if grille[ligne][colonne] != 'x':
                b = Fore.RED + 'x' + Style.RESET_ALL
                grille[ligne][colonne] = b
                
                bombe_placer += 1
        else:
            print('Nombre de bombes doit être inférieur au nombre de case, ciao')
            break

    return grille

# calcul du nombre des côtés adjacents
def calcul_adjacent(grille):
    lignes = len(grille)
    colonnes = len(grille[0])

    for i in range(lignes):
        for j in range(colonnes):
            if grille[i][j] != 'x':
                bombe_autour = 0
                for ligne in range(max(0, i-1),min(lignes,i + 2 )):
                    for colonne in range(max(0, j-1),min(colonnes, j + 2)):
                        if grille[ligne][colonne] == 'x':
                            bombe_autour += 1
                    grille[ligne][colonne] = bombe_autour
            else:
                print('Il y a déjà une bombe dans cette case')


# fonction principale
def main():

    # retourne le menu tant que l'utilisateur est toujours dans le programme
    while True:
        # menu principal du programmme
        print(Fore.WHITE + Back.GREEN +'####### MENU PRINCIPAL ########'+ Style.RESET_ALL)
        print('1. Créer un démineur')
        print('2. Quitter le programme')

        choix = input('Quelle est votre choix: ')

        # verification du choix de l'utilisateur
        if choix == '1':
            
            lignes = input('Combien de ligne?: \n')
            colonnes = input('Combien de colonne?: \n')
            
            n_bombe = input('Combien de bombe?: \n')
            if int(n_bombe) <= 0 or int(lignes) <= 0 or int(colonnes) <= 0:
                print(Fore.RED + Back.BLACK + 'Vos nombres doit être supérieur à 0'+ Style.RESET_ALL)
                print('\n================================')
            else:
                if int(lignes) <= 50 or int(colonnes) <= 50:
                    grille = creation_grille(int(lignes),int(colonnes),int(n_bombe))
                    calcul_adjacent(grille)
                    for lignes in grille:
                        print("|".join(str(case) for case in lignes))
                else:
                    print(Fore.RED + Back.BLACK + 'Nombre de ligne ou de colonnes ne pas dépassé 50'+ Style.RESET_ALL)
        elif choix == '2':
            print(Fore.RED + Back.BLACK + 'À bientôt ------->'+ Style.RESET_ALL)
            break

# creation d'une instance de la fonction principale
if __name__ == '__main__':
    main()