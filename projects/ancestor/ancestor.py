def earliest_ancestor(ancestors, starting_node):
    graph = {}                  # Store parents and children in graph where, key=child and value=parent

    for ancestor in ancestors:  # Add each child as the key in for each entry
        if ancestor[1] in graph:
            graph[ancestor[1]].append(ancestor[0])
        else:
            graph[ancestor[1]] = [ancestor[0]]

    curr = starting_node
    if curr not in graph:       # If the input individual is not in the graph, it has no parents
        return -1

    curr = starting_node        # Set the current individual

    while True:
        path = []               # Array to store the current path of ancestors
        for ancestor in graph[curr]:    # Check the array of parents for each child in the graph
            if ancestor in graph:       # If the the parent is also a child, add it to the path
                path = path + graph[ancestor]
        
        if len(path) == 0:
            return graph[curr][0]
        else:
            graph[curr] = path