import sys

def graph_import(link):
    f= open(link,'r')
    actual_line = f.readline()
    graph = []
    while actual_line != "":
        graph.append(list(map(int,actual_line.split())))
        actual_line = f.readline()

    for line in graph:
        print(line)

    return graph


def print_graph_to_matrix_of_values(liste_adjacence):
    # Déterminer la taille de la matrice
    n = len(liste_adjacence)

    # Créer une matrice remplie de '*'
    matrice = [['*' for _ in range(n)] for _ in range(n)]
    print("taille de la matrice d'adjacsence : " + str(n))
    # Remplir la matrice avec les valeurs données
    for i in range(n):
        for j in range(len(liste_adjacence[i])-2):
            matrice[int(liste_adjacence[i][j+2])-1][i] = str(liste_adjacence[i][j+2])  # Stocker en tant que chaîne pour l'affichage

    # Affichage de l'en-tête des colonnes
    header = "  " + " ".join(str(i+1) for i in range(n))
    print(header)

    # Affichage des lignes
    for i in range(n):
        row = f"{i+1} " + " ".join(matrice[i][j] if j < len(matrice[i]) else '*' for j in range(n))
        print(row)

