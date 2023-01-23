def to_roman(num):
    # write your code here!

    values = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 
        1
    ]
    symbols = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    result = ''  #final output string
    pointer = 0  #list starting location

    while num > 0:  # Looping while the number is greater than zero.
        
        for _ in range(num // values[pointer]):  
        # Checks the boolean value of the operation 
        
            result += symbols[pointer]  # Append the Symbol to the string

            num -= values[pointer]  # Subtract the value from the original number

        pointer += 1  # Increase the pointer by 1, aka, look at the next number in line. 

    return result  # Send the result to where this function was called.

# Extra debug code
debug = False
if debug:
    print (bool(4 // 5))
    print (bool(11 // 5))
    print (bool(10 // 2))
