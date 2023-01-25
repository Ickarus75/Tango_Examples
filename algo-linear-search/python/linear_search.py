array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    for item in array_to_search_through:
        # print(item)
        if array_to_search_through[item-1] == value_to_find:
            return item-1
    return None

def linear_search_global(value_to_find, array_to_search_through):
    array_of_hits = []
    for item in array_to_search_through:
        # print(item)
        if item == value_to_find:
            array_of_hits.append(array_to_search_through.index(item)) # grabs the location of the item
        pass
    # print(array_of_hits)
    return array_of_hits