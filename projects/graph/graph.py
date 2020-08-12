"""
Simple graph implementation
"""
# from util import Stack, Queue  # These may come in handy
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """
    Represent a graph as a dictionary of vertices mapping labels to edges.
    """
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            return None

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        queue = Queue()# make a queue
        queue.enqueue([starting_vertex])# enqueue our start node into a list
        visited = set()# make a set to track visited nodes
        
        while queue.size() > 0:# while queue still has things in it
            curr = queue.dequeue()# dq path from front of the line, this is our current node
            if curr not in visited:# check if we've visited, if not:
                visited.add(curr)# mark it as visited
                print(curr)

                for neighbor in self.get_neighbors(curr):# iterate over neighbors
                    queue.enqueue(neighbor)# add to queue

    def dft(self, starting_vertex):
        stack = Stack()# make a stack
        stack.push([starting_vertex])# push our starting node onto the stack
        visited = set()# make a set to track the nodes we've visited

        while stack.size() > 0:# as long as our stack isn't empty
            curr = stack.pop()# pop off the top, this is our current node
            if curr not in visited:# check if we have visited this before, and if not:
                visited.add(curr)# mark it as visited
                print(curr)

                for neighbor in self.get_neighbors(curr):# iterate over neighbors
                    stack.push(neighbor)# and add them to our stack

    def dft_recursive_helper(self, curr, visited):
        visited.add(curr)# mark it as visited
        print(curr)
        
        for neighbor in self.get_neighbors(curr):# iterate over neighbors
            if neighbor not in visited:
                self.dft_recursive_helper(neighbor, visited)

    def dft_recursive(self, starting_vertex):
        visited = set()# make a set to track visited nodes
        self.dft_recursive_helper(starting_vertex, visited)# If we do have neighbors, iterate over them and recurse for each one

    def bfs(self, starting_vertex, destination_vertex):
        queue = Queue()# make a queue
        queue.enqueue([starting_vertex])# Enqueue a path starting with the starting index
        visited = set()# make a set to track visited nodes

        while queue.size() > 0:# while queue still has things in it
            curr_path = queue.dequeue()# Grab the first path and the last vertex in that path
            curr = curr_path[-1]

            if curr not in visited:# check if we've visited
                if curr == destination_vertex: return curr_path# Check to see if this vertex matches our destination vertex
                visited.add(curr)# mark it as visited
            
            for neighbor in self.get_neighbors(curr):# iterate over neighbors,
                next_path = curr_path[:]
                next_path.append(neighbor)# Add the current vertex's neighbors to the current path
                if neighbor == destination_vertex:# Check to see if the neighbor matches our destination vertex
                    return next_path
                else:
                    queue.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        stack = Stack()# make a stack
        stack.push([starting_vertex])# push our starting node onto the stack
        visited = set()# make a set to track the nodes we've visited

        while stack.size() > 0:# as long as our stack isn't empty
            curr_path = stack.pop()# pop off the top, this is our current node
            curr = curr_path[-1]

            if curr not in visited:# check if we have visited this before, and if not:
                visited.add(curr)# mark it as visited

            for neighbor in self.get_neighbors(curr):# iterate over neighbors,
                next_path = curr_path[:]
                next_path.append(neighbor)# Add the current vertex's neighbors to the current path

                if neighbor == destination_vertex:# Check to see if the neighbor matches our destination vertex
                    return next_path
                else:
                    stack.push(next_path)


    def dfs_recursive_helper(self, curr, destination, visited):
        if curr == destination:
            return [curr]
        
        for neighbor in self.get_neighbors(curr):# iterate over neighbors,
            if neighbor not in visited:
                visited.add(neighbor)# mark it as visited
                path = self.dfs_recursive_helper(neighbor, destination, visited)

                if path is not None:
                    path.insert(0, curr)
                    return path

    def dfs_recursive(self, starting_vertex, destination_vertex):
        visited = set()# make a set to track the nodes we've visited
        visited.add([starting_vertex])# mark it as visited
        return self.dfs_recursive_helper(starting_vertex, destination_vertex, visited)


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
