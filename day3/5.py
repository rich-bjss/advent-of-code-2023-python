import re

def create_symbols_map(file):
    y = 0
    symbols = {}
    for string in file:
        x = 0
        symbols[y] = []
        for char in string:
            if (char != "." and char != "\n" and not char.isnumeric()):
                symbols[y].append(x)
            x += 1
        y += 1
    return symbols

def current_pos_in_symbols(x, y, symbols):
    return (y in symbols and symbols[y].count(x) > 0)

def possible_adjacent_positions(y, x_list):
    start_pos = x_list[0]
    end_pos = x_list[len(x_list) -1]
    return {
        (y-1): [*range(start_pos - 1, end_pos + 2)],
        y: [start_pos - 1, end_pos + 1],
        (y+1): [*range(start_pos - 1, end_pos + 2)]
    }

def find_match_of_postions_in_symbols(positions, symbols):
    match = False
    for y in positions:
        for x in positions[y]:
            if(current_pos_in_symbols(x, y, symbols)):
                match = True
    return match

with open('input.txt') as file:
    i = 0
    symbols = create_symbols_map(file)
    file.seek(0)
    y = 0
    for string in file:
        x = 0
        current_part = ""
        current_part_positions = [] 
        for char in string:
            if(char.isnumeric()):
                current_part = current_part + char
                current_part_positions.append(x)
            if(((x == len(string) -1) or not char.isnumeric()) and current_part != ""):
                # Work out if adjacent items exist at the end of line, or when hitting a new dot.
                print(  "%s ====" % (y))
                print(current_part_positions)
                possible_positions = possible_adjacent_positions(y, current_part_positions)
                print(possible_positions)
                if(find_match_of_postions_in_symbols(possible_positions, symbols)):
                    print(current_part)
                    i = i + int(current_part)

                current_part = ""
                current_part_positions = []


            x += 1
        y += 1

    print(i)