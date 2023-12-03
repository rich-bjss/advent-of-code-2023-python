import re

with open('input.txt') as file:
    i = 0
    map
    for string in file:
        game_no = int(re.findall("Game (\d+)", string).pop(0))
        
        games = re.split(":", string).pop(1)
        max_green = 0
        max_red = 0
        max_blue = 0
        for game in re.split(";", games):
            green_match = re.findall("(\d+)\sgreen", game)
            if (len(green_match) > 0):
                green = int(green_match.pop(0))
                if(green > max_green):
                    max_green = green
            red_match = re.findall("(\d+)\sred", game)
            if (len(red_match) > 0):
                red = int(red_match.pop(0))
                if(red > max_red):
                    max_red = red
            blue_match = re.findall("(\d+)\sblue", game)
            if (len(blue_match) > 0):
                blue = int(blue_match.pop(0))
                if(blue > max_blue):
                    max_blue = blue

         
        i = i + (max_blue * max_red * max_green)

    print(i)
            

        