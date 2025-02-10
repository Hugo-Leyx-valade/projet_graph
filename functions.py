import sys
import copy
from collections import deque
import heapq



def test_no_circuit_in_graph(graph):
    print("debut test circuit")
    graph_for_test = copy.deepcopy(graph)
    node_in_graph = set()
    for i in range(len(graph_for_test)):
        node_in_graph.add(i+1)
    for line in graph_for_test:
        if len(line) < 3:
            graph_for_test[graph_for_test.index(line)] = []
            node_in_graph.discard(line[0])
        else:
            for p in line[2:]:
                if p not in node_in_graph:
                    line.pop(line.index(p))
            if len(line) < 3:
                graph_for_test[graph_for_test.index(line)] = []
                node_in_graph.discard(line[0])
    for i in range(len(graph_for_test)):
        if graph_for_test[i] != []:
            return -1
        else :
            return 1





def graph_import(link):
    with open(link, 'r') as f:
        lines = f.readlines()

    graph = []  # Liste pour stocker le graphe
    parents = set()  # Stocke les nœuds qui sont des parents (prédécesseurs)
    predecessors = set()  # Stocke tous les nœuds existants

    # Lire et structurer les données du fichier
    for line in lines:
        values = list(map(int, line.split()))  # fais un vecteur avec les valeurs de la ligne (1 1 => [1,1])

        if values[1] < 0 : # Test si la valeur de liens ne sont pas négatifs
            return -1 # Doit etre pris en charge dans le main avec une comparaison

        predecessors.update(values[2:])  # Noeuds parents

        graph.append(values)  # Stocker la ligne
        # Ajouter les prédécesseurs à l'ensemble des parents

    # implémenter la fonction de test circuit
    if test_no_circuit_in_graph(graph) == -1 :
        return -2

    for line in graph:
        if len(line) < 3:
            line.append(0)

    # Déterminer les nœuds sans successeur (ceux qui ne sont jamais parents)
    omega = [len(graph) + 1, 0]  # initialisation d'oméga [dernier_noeud + 1, 0]
    for i in range(len(graph)):
        if i+1 not in predecessors:  # S'il n'est jamais parent, il va vers omega
            omega.append(i+1)

    # Déterminer les nœuds sans prédécesseur (ceux qui ne sont jamais enfants)
    alpha = [0, 0]  # α est toujours [0, 0]

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
    header = "    " + "  ".join(str(i) for i in range(n))
    col_width = max(len(str(n)), 2)  # Largeur minimale de 2
    separator = "   " + "-" * (n * (col_width + 1))

    print(header)
    print(separator)

    # Affichage des lignes
    for i in range(n):
        row = f"{i} | " + "  ".join(matrice[i][j] if j < len(matrice[i]) else ' * ' for j in range(n))
        print(row)


def compute_rank_of_node(graph):

    # Initialisation des rangs des sommets
    ranks = {node[0]: 0 for node in graph}

    # Création d'un dictionnaire des degrés entrants (nombre de prédecesseurs)
    in_degree = {node[0]: 0 for node in graph}
    for node in graph:
        for pred in node[2:]:
            in_degree[node[0]] += 1

    # File des sommets sans prédécesseurs (rang 0)
    queue = deque([node[0] for node in graph if in_degree[node[0]] == 0])

    while queue:
        node = queue.popleft()
        current_rank = ranks[node]  # Récupération du rang du sommet actuel

        for succ in graph:
            if node in succ[2:]:  # Si le sommet est un prédécesseur de succ
                in_degree[succ[0]] -= 1  # On enlève un prédécesseur
                if in_degree[succ[0]] == 0:
                    queue.append(succ[0])
                ranks[succ[0]] = max(ranks[succ[0]], current_rank + 1)

    return ranks


def display_rank_of_each_node(ranks):
    for node, rank in ranks.items():
        print(f"Rang du sommet {node}: {rank}")

def invert_graph(graph):
    """Inverse le graphe donné."""
    inverted_graph = {node: [] for node in graph}
    for node in graph:
        for neighbor, weight in graph[node]:
            if neighbor not in inverted_graph:
                inverted_graph[neighbor] = []
            inverted_graph[neighbor].append((node, weight))
    return inverted_graph


def create_adjacency_list(graph):
    adjacent_list = {node[0]: [] for node in graph}
    task_duration = {node[0]: node[1] for node in graph}
    for node in graph:
        for pred in node[2:]:
            adjacent_list[pred].append((node[0], task_duration[pred]))
    return adjacent_list


def calculate_earliest_date(graph, start):
    """
    Implémente l'algorithme de Dijkstra modifié pour trouver le chemin le plus long.
    :param graph: Dictionnaire représentant le graphe d'ordonnancement {sommet: [(successeur, poids)]}
    :param start: Sommet source (0 pour ES, N+1 pour LS)
    :return: Dictionnaire des distances maximales depuis la source
    """
    dist = {node: float('-inf') for node in graph}
    dist[start] = 0
    heap = [(-0, start)]  # Utilisation d'un tas pour maximiser la distance (inversion des poids)

    while heap:
        current_dist, node = heapq.heappop(heap)
        current_dist = -current_dist  # Conversion en valeur positive

        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist > dist[neighbor]:  # Maximisation de la distance
                dist[neighbor] = new_dist
                heapq.heappush(heap, (-new_dist, neighbor))

    return dist


def compute_earliest_date(graph):
    adjacent_list = create_adjacency_list(graph)
    earliest_date = calculate_earliest_date(adjacent_list, 0)
    return earliest_date



def draw_dict(dictionnaire, titre=""):
    # Vérifier si le dictionnaire est vide
    if not dictionnaire:
        print("Le dictionnaire est vide.")
        return

    # Récupérer les clés du dictionnaire
    cles = list(dictionnaire.keys())

    # Calculer la largeur maximale des colonnes
    largeurs = [max(len(str(cle)), len(str(dictionnaire[cle]))) for cle in cles]

    # Calculer la largeur totale du tableau
    largeur_totale = sum(largeurs) + 3 * (len(cles) - 1) + 2

    # Afficher la bordure supérieure avec le titre centré
    if titre:
        titre_formate = f"| {titre} |"
        espace_disponible = largeur_totale - len(titre_formate)
        espace_gauche = espace_disponible // 2
        espace_droite = espace_disponible - espace_gauche
        print("+" + "-" * espace_gauche + titre_formate + "-" * espace_droite + "+")
    else:
        print("+" + "-" * (largeur_totale - 2) + "+")

    # Afficher les clés en haut
    for i, cle in enumerate(cles):
        print("| " + str(cle).ljust(largeurs[i]), end=" ")
    print("|")  # Nouvelle ligne

    # Afficher une ligne de séparation
    for largeur in largeurs:
        print("+-" + "-" * largeur, end=" ")
    print("+")  # Nouvelle ligne

    # Afficher les valeurs
    for i, cle in enumerate(cles):
        print("| " + str(dictionnaire[cle]).ljust(largeurs[i]), end=" ")
    print("|")  # Nouvelle ligne

    # Afficher la bordure inférieure
    print("+" + "-" * (largeur_totale) + "+")

def create_reversed_adjacency_list(graph):
    """
    Crée une liste d'adjacence inversée (successeurs -> prédécesseurs) avec les poids (durées des tâches).
    :param graph: Liste de tâches [[numéro, durée, prédécesseurs], ...]
    :return: Dictionnaire {sommet: [(prédécesseur, poids)]}
    """
    reversed_list = {node[0]: [] for node in graph}
    task_duration = {node[0]: node[1] for node in graph}

    for node in graph:
        for pred in node[2:]:
            reversed_list[node[0]].append((pred, task_duration[pred]))  # (prédécesseur, durée)

    return reversed_list


def calculate_latest_dates(graph, end_node):
    """
    Implémente Dijkstra inversé pour calculer la date au plus tard (LS - Latest Start).
    :param graph: Dictionnaire représentant le graphe inversé {sommet: [(prédécesseur, poids)]}
    :param end_node: Dernier nœud du graphe (Ω)
    :return: Dictionnaire des dates au plus tard (LS)
    """
    dist = {node: float('-inf') for node in graph}
    dist[end_node] = 0  # On commence à la fin

    heap = [(-0, end_node)]  # Inversion des poids pour maximiser

    while heap:
        current_dist, node = heapq.heappop(heap)
        current_dist = -current_dist  # Conversion en valeur positive

        for predecessor, weight in graph[node]:
            new_dist = current_dist + weight
            if new_dist > dist[predecessor]:  # Maximisation de la distance inverse
                dist[predecessor] = new_dist
                heapq.heappush(heap, (-new_dist, predecessor))

    return dist


def compute_latest_date(graph, project_duration):
    """
    Calcule la date au plus tard (LS) en ajustant les valeurs obtenues avec Dijkstra inversé.
    :param graph: Liste d'adjacence
    :param project_duration: Durée totale du projet (max(ES))
    :return: Dictionnaire contenant LS pour chaque sommet
    """
    reversed_graph = create_reversed_adjacency_list(graph)
    latest_dates = calculate_latest_dates(reversed_graph, max(reversed_graph.keys()))  # Ω (dernier sommet)

    # Ajustement de LS pour respecter la contrainte de fin du projet
    for node in latest_dates:
        latest_dates[node] = project_duration - latest_dates[node]

    return latest_dates


def calculate_margins(earliest, latest):
    margins = {node: latest[node] - earliest[node] for node in earliest}
    return margins


def find_critical_path(margins):
    list = []
    for node in margins:
        if margins[node] == 0:
            list.append(node)
    return list

def print_critical_path(tab):
    # Vérifie si la liste n'est pas vide
    if not tab:
        print("Le chemin critique est vide")
        return
    print("Le chemin critique:")
    # Itère sur les éléments de la liste et les affiche
    for i in range(len(tab) - 1):
        print(f"{tab[i]} => ", end="")

    # Affiche le dernier élément sans "=>"
    print(tab[-1])

