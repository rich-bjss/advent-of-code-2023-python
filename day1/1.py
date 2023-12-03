
file = open("input.txt", "r")


with open('input.txt') as file:
    i = 0
    for string in file:
        first_number = None
        last_number = None
        chars = [*string]
        for char in chars:
            if char.isnumeric():
                if not first_number:
                    first_number = char
                last_number = char

        number = int("%s%s" % (first_number, last_number))
        i = i + number

print(i)



        
       