import re
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

text = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

i = 0
for string in text.splitlines():
    matches = re.findall("(one|two|three|four|five|six|seven|eight|nine|[\d])", string)
    if (len(matches) == 1):
        matches.append(matches.copy().pop(0))
    first = matches.pop(0)
    last = matches.pop(len(matches) -1)
    first_number = number_map.get(first)
    last_number = number_map.get(last)
    print(string)
    print(first_number)
    print(last_number)
    number = int("%s%s" % (first_number, last_number))
    print(number)

    i = i + number
    print(i)

print(i)