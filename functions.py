import sys


def graph_import(link):
    with open(link, 'r') as f:
        lines = f.readlines()

    graph = []  # Liste pour stocker le graphe
    parents = set()  # Stocke les nœuds qui sont des parents (prédécesseurs)
    all_nodes = set()  # Stocke tous les nœuds existants

    # Lire et structurer les données du fichier
    for line in lines:
        values = list(map(int, line.split()))
        node = values[0]  # Numéro du nœud
        duration = values[1]  # Durée de la tâche
        predecessors = values[2:]  # Noeuds parents

        graph.append([node, duration] + predecessors)  # Stocker la ligne
        all_nodes.add(node)

        # Ajouter les prédécesseurs à l'ensemble des parents
        for p in predecessors:
            parents.add(p)

    # Déterminer les nœuds sans successeur (ceux qui ne sont jamais parents)
    omega = [len(all_nodes) + 1, 0]  # Ω commence par [dernier_noeud + 1, 0]
    for node in all_nodes:
        if node not in parents:  # S'il n'est jamais parent, il va vers omega
            omega.append(node)

    # Déterminer les nœuds sans prédécesseur (ceux qui ne sont jamais enfants)
    alpha = [0, 0]  # α est toujours [0, 0]
    referenced_nodes = set(p for _, _, *ps in graph for p in ps)  # Tous les prédécesseurs cités
    for node in all_nodes:
        if node not in referenced_nodes:  # Si un nœud n'a pas de prédécesseur, c'est un départ
            alpha.append(node)

    # Insérer alpha au début du graphe
    graph.insert(0, alpha)

    # Ajouter omega à la fin du graphe
    graph.append(omega)

    print("Graphe final :")
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

