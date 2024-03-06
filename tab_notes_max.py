'''
DEBUT
    // Initialisation du tableau à deux dimensions avec des noms et des notes
    tableau_notes = [["Alice", 15], ["Bob", 12], ["Claire", 8], ["David", 18], ["Emma", 10]]

    // Parcours du tableau pour afficher les noms et les notes supérieurs à 10
    POUR chaque entrée DANS tableau_notes FAIRE
        SI entrée[1] > 10 ALORS
            AFFICHER "Nom :", entrée[0], " - Note :", entrée[1]
        FINSI
    FINPOUR
FIN
'''

# Initialisation du tableau à deux dimensions avec des noms et des notes
notes = [["Raphael   ", 15], ["Mirabelle ", 12], ["Louis     ", 9], ["Faty      ", 12], ["Arnold    ", 14], ["Christian ", 17], ["Anja      ", 6],["Dexter    ", 19], ["Roxanne   ", 7], ["Franck    ", 13]]

print("  Notes au dessus de 10 : \n||==============================||")
for el in notes:
    if el[1] > 10:
        print("|| Nom :", el[0], "| Note :", el[1], "||")
        print("||------------------------------||")
print("||==============================||")

