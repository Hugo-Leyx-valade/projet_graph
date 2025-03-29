from functions import *

print("Hello")

def main():
    graph = graph_import("graphe2.txt") #Ajouter table*.txt
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
    earliest_date = compute_earliest_date(graph)
    project_duration = max(earliest_date.values())
    draw_dict(earliest_date,"Calendrier le plus court")

    print("Date au plus tard:")
    latest_date = compute_latest_date(graph,project_duration) #MARCHE PAS
    draw_dict(latest_date,"Calendrier le plus tard")

    margins = calculate_margins(earliest_date,latest_date)
    draw_dict(margins,"marges")
    path = find_critical_path(margins)
    print_critical_path(path)


if __name__=="__main__":
    main()



