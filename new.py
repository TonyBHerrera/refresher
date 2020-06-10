# def sum(num_one, num_two):
#     print(num_one + num_two)

# sum(2,4)

# def hello_world():
#     print("Hello World")

# hello_world()

# post_count = 42
# name = 'Kristine'

# print(name)
# print(post_count)

# players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

# for player in players:
#     print(player)

players = {
    '2b': "Altuve",
    '3b': 'Bregman',
    'ss': 'Bregman',
    'dh': 'Gattis'
}

for position, player in players.items():
    print('Position', position)
    print('Player', player)