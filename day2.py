# Day 2 : Cube Conundrum

# Loop through the game (in each line)
def is_possible(red, green, blue, game):
    for subset in game:
        subset_colors = subset.split()
        for color_count in subset_colors[1:]:
            color_count = color_count.strip().split()
            if len(color_count) != 2:
                continue
            color, count = color_count
            count = int(count)
            if color == 'red' and count > red:
                return False
            elif color == 'green' and count > green:
                return False
            elif color == 'blue' and count > blue:
                return False
    return True

def possible_games(red, green, blue, games):
    possible_game_ids = []
    for game in games:
        game_info = game.split(':')
        game_id = int(game_info[0].split()[1])
        subsets = game_info[1].strip().split(';')
        if is_possible(red, green, blue, subsets):
            possible_game_ids.append(game_id)
    return possible_game_ids

with open('input.txt', 'r') as file:
    game_data = file.readlines()

possible_ids = possible_games(12, 13, 14, game_data)

sum_possible_ids = sum(possible_ids)

print("Sum of possible game IDs:", sum_possible_ids)
