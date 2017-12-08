import os

def format_data():
    file_dir = "data\\Day07_data.txt"
    script_dir = os.path.dirname(__file__)
    file_object = open(os.path.join(script_dir, file_dir), "r")

    tree_graph = {}

    for line in file_object:        
        no_newline = line.replace("\n", "")
        split = no_newline.split(" -> ")
        
        children = []

        if len(split) > 1:
            children = split[1].split(", ")
        
        name_weight = split[0].split(" ")

        tree_graph[name_weight[0]] = (int(name_weight[1].strip("()")), children)

    return tree_graph