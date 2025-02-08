# Python program to demonstrate
# main() function
from functions import *

print("Hello")

# Defining main function
def main():
    graph = graph_import("graphes.txt")
    if graph == -1:
        print("il y a au moins un arc à valeur négative !")
        return
    if graph == -2:
        print("le graphe comporte un circuit !")
        return
    else:
        print_graph_to_matrix_of_values(graph)
        display_rank_of_each_node(compute_rank_of_node(graph))
    print("Date au plus tot:")
    print(compute_earliest_date(graph)) #MARCHE PAS BIEN
    print("Date au plus tard:")
    print(compute_latest_date(graph))  #MARCHE PAS



# Using the special variable
# __name__
if __name__=="__main__":
    main()



