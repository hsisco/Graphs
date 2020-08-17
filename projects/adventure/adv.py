from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []



def walk_directions(current_room): 
    visited=set()
    path=list()

    def walk_recur(current_room, opposite_direction=None): 
        # Check if we have been visited and if so add it to visited
        if current_room not in visited:
            visited.add(current_room)

        # Base case: if no neighbors
        neighbors = current_room.get_exits()
        if len(neighbors) == 0:
            return visited

        # If we do have neighbors, iterate over them and get each direction
        for neighbor in neighbors:
            next_room=current_room.get_room_in_direction(neighbor)
            if next_room in visited: 
                continue 
            else: 
                # If we haven't been to the room, add the room to visited and append neighbor to path
                visited.add(next_room)
                path.append(neighbor) 
            # Recurse for each room until rooms are all visited and neighbors appended
            walk_recur(next_room, opposite_direction=neighbor)

        # If we've been though an exit, find the opposite direction and append it to walk through
        if opposite_direction is not None: 
            back={"n": "s", "e": "w", "s": "n", "w": "e"}
            previous=back[opposite_direction]
            path.append(previous)
    walk_recur(current_room)
    return path

traversal_path=walk_directions(player.current_room)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")