import re


max_green = 13
max_red = 12
max_blue = 14

with open('input.txt') as file:
    i = 0
    map
    for string in file:
        game_no = int(re.findall("Game (\d+)", string).pop(0))
        
        games = re.split(":", string).pop(1)
        allowed = True
        for game in re.split(";", games):
            green_match = re.findall("(\d+)\sgreen", game)
            green = int(green_match.pop(0)) if (len(green_match) > 0) else 0
            red_match = re.findall("(\d+)\sred", game)
            red = int(red_match.pop(0)) if (len(red_match) > 0) else 0
            blue_match = re.findall("(\d+)\sblue", game)
            blue = int(blue_match.pop(0)) if (len(blue_match) > 0) else 0

            if (green > max_green or red > max_red or blue > max_blue):
                allowed = False

        if(allowed): 
            i = i + game_no

    print(i)
            

        