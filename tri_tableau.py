# Tri ordre decroissant avec la fonction sorted de python
def tri_tableau_decroissant(tabl):
    print(sorted(tabl, reverse=True))

# Tri ordre croissant sorted de python
def tri_tableau_croissant(tabl):
    print(sorted(tabl))

# tri par selection 
def tri_selection_croissant(tableau):
    for i in range(len(tableau)):
        index_min = i
        for j in range(i + 1, len(tableau)):
            if tableau[j] < tableau[index_min]:
                index_min = j
        if index_min != i:
            tableau[i], tableau[index_min] = tableau[index_min], tableau[i]

#tri_tableau_croissant([5,1,3,2,8,9,4])
#tri_tableau_decroissant([5,1,3,2,8,9,4])
tab = [5,1,-3,2,8,-9,4]
tri_selection_croissant(tab)
print("Tri par selection du tableau",tab)


# tri à bulle
def tri_a_bulle_croissant(tableau):
    n = len(tableau)
    for i in range(n):
        for j in range(0, n-i-1):
            if tableau[j] > tableau[j+1]:
                tableau[j], tableau[j+1] = tableau[j+1], tableau[j]


tableau = [5,1,-3,2,8,-9,4]
tri_a_bulle_croissant(tableau)
print("Tri à bulle :", tableau)
