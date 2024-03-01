def ajouter_nom(nom,etudiants):
    if nom != " ":
        print (etudiants.append(nom))
    else:
        print('Erreur')

def afficher_tableau(etudiants):
    for i in range(len(etudiants)):
        print(etudiants[i])


def rechercher_nom(nom,etudiants):
    for i in range(len(etudiants)):
        if nom ==  etudiants[i]:
            print("Ton ", nom, "existe")
        else:
            print("Ton ", nom, "n existe pas")
         
def supprimer_nom(nom,etudiants):
    for i in range(len(etudiants)-1):
        if nom ==  etudiants[i]:
            del etudiants[i]
            print(etudiants)
            break
        else:
            print("Ton ", nom, "n existe pas dans notre base")

def main():
    etudiants = ["Andil","Franck","Roxane"]

    while True:

        print('\Manipulation de donnée ')
        print('1. Ajouter un étudiant')
        print('2. Afficher étudiant')
        print('3. Rechercher élement')
        print('4. Supprimer ')
        print('5. Sortie ')

        choix = input('Entrer votre choix: ')

        if choix == '1':
            nom = input('Entrer le nom de l etudiant: ')
            print(ajouter_nom(nom, etudiants))
            print(afficher_tableau(etudiants))
            
        elif choix == '2':
            print(afficher_tableau(etudiants))

        elif choix == '3':
            nom = input('Entrer nom à rechercher: ')
            print(rechercher_nom(nom, etudiants))
            # print(afficher_tableau(etudiants))

        elif choix == '4':
            nom = input('Entrer nom à supprimer: ')
            print(supprimer_nom(nom, etudiants))
            print(afficher_tableau(etudiants))

        elif choix == '5':
            print("Bye bye bro")
            break
    
   
if __name__ == '__main__':
    main()
