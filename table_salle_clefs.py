""" 
VARIABLES
   
    tabl: tableau à trois dimensions contenant des noms, des numéros de clés et des noms de salles
    tabl = [
            ["Alice", "clef-123", "Salle A"],
            ["Bob", "clef-321", "Salle B"],
            ["Alice", "clef-213", "Salle C"],
            ["Bob", "clef-123", "Salle A"],
            ["Alice", "clef-321", "Salle B"],
            ["Bob", "clef-987", "Salle C"],
            ["Bob", "clef-123", "Salle D"]
        ]

afficher_tableau:
    POUR chaque entrée DANS tabl FAIRE
        AFFICHER "Nom :", entrée[0], " - Numéro de clé :", entrée[1], " - Salle :", entrée[2]
    FIN POUR
FIN afficher_tableau

afficher_salles_et_clefs_par_nom(nom_recherche: CHAINE):
    ok <- FAUX
    POUR chaque el DANS tabl FAIRE
        SI el[0] == nom_recherche ALORS
            AFFICHER "Nom :", el[0], " - Numéro de clé :", el[1], " - Salle :", el[2]
            ok <- VRAI
        FIN SI
    FIN POUR
    SI NON ok ALORS
        AFFICHER "Le nom ", nom_recherche, " n'a pas été trouvé."
    FIN SI
FIN afficher_salles_et_clefs_par_nom

afficher_nom_et_salle_par_clef(clef_recherche: CHAINE):
    ok <- FAUX
    POUR chaque el DANS tabl FAIRE
        SI el[1] == clef_recherche ALORS
            AFFICHER "Nom :", el[0], " - Numéro de clé :", el[1], " - Salle :", el[2]
            ok <- VRAI
        FIN SI
    FIN POUR
    SI NON ok ALORS
        AFFICHER "La clef ", clef_recherche, " n'a pas été trouvée."
    FIN SI
FIN afficher_nom_et_salle_par_clef

ajouter_entree:
    nom <- DEMANDER "Entrez le nom : "
    clef <- DEMANDER "Entrez le numéro de clé : "
    salle <- DEMANDER "Entrez la salle : "
    AJOUTER [nom, clef, salle]                                                                                                                                                                                                                     À tabl
    AFFICHER "Nouvelle entrée ajoutée :", [nom, clef, salle]
FIN ajouter_entree

menu_principal:
    TANT QUE VRAI FAIRE
        AFFICHER "Menu Principal :"
        AFFICHER "A. Afficher le tableau."
        AFFICHER "B. Afficher les salles et les clés par nom."
        AFFICHER "C. Afficher les noms et les salles par clefs."
        AFFICHER "D. Alimenter le tableau."
        AFFICHER "E. Quitter"
        
        choix <- DEMANDER "Choisissez une option : "

        SI choix == "A" ALORS
            afficher_tableau()
        SINON SI choix == "B" ALORS
            nom_recherche <- DEMANDER "Entrez le nom à rechercher : "
            afficher_salles_et_clefs_par_nom(nom_recherche)
        SINON SI choix == "C" ALORS
            clef_recherche <- DEMANDER "Entrez le nom de la clef à rechercher : "
            afficher_nom_et_salle_par_clef(clef_recherche)
        SINON SI choix == "D" ALORS
            ajouter_entree()
        SINON SI choix == "E" ALORS
            AFFICHER "Au revoir !"
            ARRÊTER_PROGRAMME
        SINON
            AFFICHER "Option invalide ! Veuillez choisir à nouveau."
        FIN SI
    FIN TANT QUE
FIN menu_principal

DÉBUT
    menu_principal()
FIN
 """
'''

tabl = [["Alice", "clef-123", "Salle A"],
        ["Bob", "clef-321", "Salle B"],
        ["Alice", "clef-213", "Salle C"],
        ["Bob", "clef-123", "Salle A"],
        ["Alice", "clef-321", "Salle B"],
        ["Bob", "clef-987", "Salle C"],
        ["Bob", "clef-123", "Salle D"]]

def afficher_tableau():
    for entrée in tabl:
        print("Nom :", entrée[0], "- Numéro de clé :", entrée[1], "- Salle :", entrée[2])

def afficher_salles_et_clefs_par_nom(nom_recherche):
    ok = False
    for el in tabl:
        if el[0] == nom_recherche:
            print("Nom :", el[0], "- Numéro de clé :", el[1], "- Salle :", el[2])
            ok = True
    if not ok:
        print("Le nom", nom_recherche, "n'a pas été trouvé.")

def afficher_nom_et_salle_par_clef(clef_recherche):
    ok = False
    for el in tabl:
        if el[1] == clef_recherche:
            print("Nom :", el[0], "- Numéro de clé :", el[1], "- Salle :", el[2])
            ok = True
    if not ok:
        print("La clef", clef_recherche, "n'a pas été trouvée.")

def ajouter_entree():
    nom = input("Entrez le nom : ")
    clef = input("Entrez le numéro de clé : ")
    salle = input("Entrez la salle : ")
    tabl.append([nom, clef, salle])
    print("Nouvelle entrée ajoutée :", [nom, clef, salle])

def menu_principal():
    while True:
        print("Menu Principal :")
        print("A. Afficher le tableau.")
        print("B. Afficher les salles et les clés par nom.")
        print("C. Afficher les noms et les salles par clefs.")
        print("D. Alimenter le tableau.")
        print("E. Quitter")
        
        choix = input("Choisissez une option : ")

        if choix == "A":
            afficher_tableau()
        elif choix == "B":
            nom_recherche = input("Entrez le nom à rechercher : ")
            afficher_salles_et_clefs_par_nom(nom_recherche)
        elif choix == "C":
            clef_recherche = input("Entrez le nom de la clef à rechercher : ")
            afficher_nom_et_salle_par_clef(clef_recherche)
        elif choix == "D":
            ajouter_entree()
        elif choix == "E":
            print("Au revoir !")
            break
        else:
            print("Option invalide ! Veuillez choisir à nouveau.")

# Appel du menu principal pour démarrer le programme
menu_principal()

'''

import tkinter as tk

tabl = [["Alice", "clef-123", "Salle A"],
        ["Bob", "clef-321", "Salle B"],
        ["Alice", "clef-213", "Salle C"],
        ["Bob", "clef-123", "Salle A"],
        ["Alice", "clef-321", "Salle B"],
        ["Bob", "clef-987", "Salle C"],
        ["Bob", "clef-123", "Salle D"]]

def afficher_tableau():
    for entrée in tabl:
        print("Nom :", entrée[0], "- Numéro de clé :", entrée[1], "- Salle :", entrée[2])
    print("=================================================")

def afficher_salles_et_clefs_par_nom(nom_recherche):
    ok = False
    for el in tabl:
        if el[0] == nom_recherche:
            print("Nom :", el[0], "- Numéro de clé :", el[1], "- Salle :", el[2])
            ok = True
    print("=================================================")

    if not ok:
        print("Le nom", nom_recherche, "n'a pas été trouvé.")
    print("=================================================")


def afficher_nom_et_salle_par_clef(clef_recherche):
    ok = False
    for el in tabl:
        if el[1] == clef_recherche:
            print("Nom :", el[0], "- Numéro de clé :", el[1], "- Salle :", el[2])
            ok = True
    print("=================================================")
    if not ok:
        print("La clef", clef_recherche, "n'a pas été trouvée.")
    print("=================================================")


def ajouter_entree(nom, clef, salle):
    tabl.append([nom, clef, salle])
    print("Nouvelle entrée ajoutée :", [nom, clef, salle])
    print("=================================================")


def menu_principal():
    root = tk.Tk()
    root.title("Gestionnaire de tableau")
    root.geometry("800x350")  


    label = tk.Label(root, text="Menu Principal :")
    label.pack()

    button_tableau = tk.Button(root, text="Afficher le tableau", command=afficher_tableau)
    button_tableau.pack()

    frame_nom = tk.Frame(root)
    label_nom = tk.Label(frame_nom, text="Entrez le nom à rechercher :")
    label_nom.pack(side="left")
    entry_nom = tk.Entry(frame_nom)
    entry_nom.pack(side="left")
    frame_nom.pack()

    button_salles_clefs_nom = tk.Button(root, text="Afficher les salles et les clés par nom",
                                        command=lambda: afficher_salles_et_clefs_par_nom(entry_nom.get()))
    button_salles_clefs_nom.pack()

    frame_clef = tk.Frame(root)
    label_clef = tk.Label(frame_clef, text="Entrez le numéro de clé à rechercher :")
    label_clef.pack(side="left")
    entry_clef = tk.Entry(frame_clef)
    entry_clef.pack(side="left")
    frame_clef.pack()

    button_noms_salles_clef = tk.Button(root, text="Afficher les noms et les salles par clef",
                                         command=lambda: afficher_nom_et_salle_par_clef(entry_clef.get()))
    button_noms_salles_clef.pack()

    frame_ajout = tk.Frame(root)
    label_nom_ajout = tk.Label(frame_ajout, text="Nom :")
    label_nom_ajout.pack(side="left")
    entry_nom_ajout = tk.Entry(frame_ajout)
    entry_nom_ajout.pack(side="left")
    label_clef_ajout = tk.Label(frame_ajout, text="Numéro de clé :")
    label_clef_ajout.pack(side="left")
    entry_clef_ajout = tk.Entry(frame_ajout)
    entry_clef_ajout.pack(side="left")
    label_salle_ajout = tk.Label(frame_ajout, text="Salle :")
    label_salle_ajout.pack(side="left")
    entry_salle_ajout = tk.Entry(frame_ajout)
    entry_salle_ajout.pack(side="left")
    button_ajouter = tk.Button(frame_ajout, text="Ajouter", command=lambda: ajouter_entree(entry_nom_ajout.get(),
                                                                                            entry_clef_ajout.get(),
                                                                                            entry_salle_ajout.get()))
    button_ajouter.pack(side="left")
    frame_ajout.pack()

    button_quitter = tk.Button(root, text="Quitter", command=root.destroy, bg="red")
    button_quitter.pack()

    root.mainloop()

# Appel du menu principal pour démarrer le programme
menu_principal()