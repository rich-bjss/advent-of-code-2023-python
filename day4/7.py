with open('input.txt') as file:
    count = 0
  
    for string in file:
        full_numbers_string = string.replace("\n", "").replace("  ", " ").split(": ")
        numbers_string = full_numbers_string[1].split(" | ")
        winning_numbers = numbers_string[0].split(" ")
        my_numbers = numbers_string[1].split(" ")

        
        points = 0
        print(winning_numbers)
        print(my_numbers)
        for number in my_numbers:
            if number in winning_numbers:
                points = 1 if points == 0 else points * 2
        
        print(points)
        count = count + points

    
        
       
    print(count)


 