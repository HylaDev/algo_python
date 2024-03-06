import pandas as pd
import os

# fonction pour ajouter un étudiant à la liste d'étudiant  
def ajouter_nom(nom,etudiants):
    if nom != "":
        print(etudiants.append(nom))
       
        
    else:
        print('Erreur')

# fonction pour afficher la liste d'étudiant  
def afficher_tableau(etudiants):
    
    for i in range(len(etudiants)):
        print(etudiants[i])

# fonction pour rechercher un étudiant  
def rechercher_nom(nom,etudiants):
    for i in range(len(etudiants)):
        if nom not in etudiants[i]:
            print("L étudiant ", nom, "n existe pas")
        else:
            
            print("L étudiant ", nom, "existe")
            break

# fonction pour supprimer un étudiant       
def supprimer_nom(nom,etudiants):
    for i in range(len(etudiants)-1):
        if etudiants[i] ==  nom:
            del etudiants[i]
            print(etudiants)
            break
        else:
            print("Ton ", nom, "n existe pas dans notre base")

# fonction principale
def main():
    etudiants = []

    while True:
        # Définition du menu
        print('\n Manipulation de donnée ')
        print('1. Ajouter un étudiant')
        print('2. Afficher étudiant')
        print('3. Rechercher élement')
        print('4. Supprimer ')
        print('5. Sortie')

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

        elif choix == '4':
            nom = input('Entrer nom à supprimer: ')
            print(supprimer_nom(nom, etudiants))

        elif choix == '5':
            print("Bye bye bro")
            break
    
#  Création d'une instance de la fonction principale
if __name__ == '__main__':
    main()
