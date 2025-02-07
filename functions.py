import sys

def graph_import(link):
    f= open(link,'r')
    actual_line = f.readline()
    graph = []
    alpha = [0, 0]
    while actual_line != "":
        if len(list(map(int,actual_line.split()))) == 2 :
            line_to_insert = list(map(int,actual_line.split())) + [0]
            graph.append(line_to_insert)
            actual_line = f.readline()
        else:
            graph.append(list(map(int,actual_line.split())))
            actual_line = f.readline()

    graph.insert(0,alpha)

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
            matrice[int(liste_adjacence[i][j+2])][i] = str(liste_adjacence[i][j+2])  # Stocker en tant que chaîne pour l'affichage

    # Affichage de l'en-tête des colonnes
    header = "  " + " ".join(str(i) for i in range(n))
    print(header)

    # Affichage des lignes
    for i in range(n):
        row = f"{i} " + " ".join(matrice[i][j] if j < len(matrice[i]) else '*' for j in range(n))
        print(row)

