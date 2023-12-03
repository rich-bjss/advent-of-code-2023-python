
import utils

file = open("input.txt", "r")

number_map = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

with open('input.txt') as file:
    i = 0
    for string in file:
        matches = utils.get_matches(string)
        first = matches.pop(0)
        last = matches.pop(len(matches) -1)
        first_number = number_map.get(first)
        last_number = number_map.get(last)
        number = int("%s%s" % (first_number, last_number))
        print(string.replace("\n", ""))
        print("=%s" % number)

        i = i + number

        

print(i)