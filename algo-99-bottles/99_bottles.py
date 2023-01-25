def bottle_song(num=100):
    
    bottles = num +1
    
    # while (bottles:=bottles-1) != 0:  # welcome to the walrus operator 
    #     print (f"{bottles} bottles of beer on the wall\n{bottles} bottles of beer\nTake one down, pass it around\n{bottles-1} bottles of beer on the wall\n")

    while bottles != 0:  # What do you think the result of this will be? 
        print (f"{bottles} bottles of beer on the wall\n{bottles} bottles of beer\nTake one down, pass it around\n{(bottles:=bottles-1)} bottles of beer on the wall\n")

def walrus_test(num=10):
	bottles = num
	while bottles <= 500:
		print (f"""Testing Walrus Expressions: 
		 base: {bottles}
         walrus: {(bottles := bottles*2)} """)  # prints the result and updates the variable.

		# bottles *= 2
		# print(bottles)

bottle_song(10) 
#walrus_test(3)