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

    # Looping while the number is greater than zero.
    while num > 0:
        for _ in range(num // values[pointer]):
            result += symbols[pointer]
            num -= values[pointer]
        pointer += 1

    return result

debug = True

if debug:
    print (bool(4 // 5))
    print (bool(11 // 5))
    print (bool(10 // 2))
