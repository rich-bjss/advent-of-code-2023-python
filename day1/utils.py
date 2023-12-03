import re

def get_matches(string):
    matches = re.findall(r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))', string)
    if (len(matches) == 1):
        matches.append(matches.copy().pop(0))
    return matches