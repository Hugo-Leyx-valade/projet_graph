# Python program to demonstrate
# main() function
from functions import *

print("Hello")

# Defining main function
def main():
    graph = graph_import("graphes.txt")
    print_graph_to_matrix_of_values(graph)



# Using the special variable
# __name__
if __name__=="__main__":
    main()



