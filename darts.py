from tabulate import tabulate
from itertools import zip_longest


def print_points(game_type):
    if game_type == '0' or game_type == '1':
        table = zip_longest(*scores.values(), fillvalue='')
        print(tabulate(table,headers=names.values(),missingval=0))

num_of_players = int(input('Number of Players: '))
game_types = {'1':301, '2':501}
game_choice = input('Type of Game: \n 1 - 301 \n 2 - 501 \n Choice: ')
while True:
    try:
        points = game_types[game_choice]
    except KeyError:
        print('Invalid Choice. \n Stupid Dax, try again.')
    else:
        break


scores = {}
names = {}
for i in range(num_of_players):
    name = input("Enter Name for Player {0}: ".format(i+1))
    scores[i] = [points]
    names[i] = name
current_player = 0
while True:
    print_points(game_choice)
    while True:
        try:
            round_score = input('Enter Score for {0}: '.format(names[current_player]))
        except ValueError:
            print("Invalid Input!")
        else: break
    if ' ' in round_score:
        round_score = sum([int(i) for i in round_score.split(' ')])
    else:
        round_score = int(round_score)
    new_score = scores[current_player][-1] - round_score
    if not new_score < 0:
        scores[current_player].append(new_score)
    if new_score == 0:
        break
    current_player = (current_player + 1)%num_of_players

print('{0} Wins!'.format(names[current_player]))
if names[current_player] != 'Dax' and names[current_player] != 'dax':
    if 'dax' in names.values() or 'Dax' in names.values():
        print('Suck it Dax!!!! In your fucking Face!!!!!')