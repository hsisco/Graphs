import random
import math
from queue import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        users = []
        for user in range(num_users):
            self.add_user(user)
            users.append(self.last_id)

        # Create friendships
        for user_id in users:
            num_friends = round(avg_friendships - avg_friendships * random.random() / 2)

            existing_friends = self.friendships[user_id]
            num_friends -= len(existing_friends)

            friends_to_choose = set(users)
            friends_to_choose.remove(user_id)
            friends_to_choose -= existing_friends

            for i in range(num_friends):
                if (len(friends_to_choose) == 0):
                    break
                new_friend = random.choice(list(friends_to_choose))
                self.add_friendship(user_id, new_friend)
                friends_to_choose.remove(new_friend)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        to_visit = Queue()
        to_visit.put([user_id])

        while not to_visit.empty():
            path = to_visit.get()
            if path[-1] not in visited:
                visited[path[-1]] = path
                for friend in self.friendships[path[-1]]:
                    to_visit.put([*path, friend])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)

    num_edges = 0
    for user in sg.friendships:
        num_edges += len(sg.friendships[user])
    print(f"avg friendships: {num_edges / len(sg.users)}")

    connections = sg.get_all_social_paths(1)
    print(connections)