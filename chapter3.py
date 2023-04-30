# This is a comment.
'''This is a multi-line comment.'''

# Create a list of games
# A list is a collection of items, in this case strings
games = ["Pokemon", "Valorant", "Roblox", "Hallow Knight", "Chess"]
print(games)
print("Game at index 1 " + games[1])
print("Game at index 0 " + games[0])
print("Game at index -1 " + games[-1])
print("Game at index -2 " + games[-2])

# Append a new game to the end of list
games.append("Chess2")
print(games)

# Add a game to the 1 index of list
games.insert(1, "Rocket League")
print(games)

# Remove chess from the list of games
games.remove("Chess")
print(games)

# sort the games alphabetically
games.sort()
print(games)

# Reverse the sort
reverse_order_games = list(reversed(games))
print(reverse_order_games)

# The length of the list
list_size = len(games)
'''
You must first cast list_size as a string to concatenate it using str(VARIABLE)
because it is of type int.
'''
print("There are " + str(list_size) + " items in the list.")
