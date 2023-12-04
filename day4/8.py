def run_card(winning_numbers, my_numbers):
    i = 0
    for number in my_numbers:
        if(number in winning_numbers):
            i += 1
    return i

def run_game(map, games):
    for game in games:
        if game in map:
            [winning_numbers, my_numbers, points_won] = map[game]
            number_of_matches = run_card(winning_numbers, my_numbers)
            cards_won = [*range(game + 1, game + number_of_matches + 1)]
            map[game][2] += 1 
            map = run_game(map, cards_won)
    return map


with open('input.txt') as file:
    games = {}
  
    for string in file:
        game = string.replace("Card ", "").split(":")[0]
        full_numbers_string = string.replace("\n", "").replace("  ", " ").split(": ")
        numbers_string = full_numbers_string[1].split(" | ")
        winning_numbers = numbers_string[0].split(" ")
        my_numbers = numbers_string[1].split(" ")
        games[int(game)] = [winning_numbers, my_numbers, 0]

    map = run_game(games, list(games.keys()))
    i = 0
    for game in map:
        i = i + map[game][2]
    
print(map)
print(i)