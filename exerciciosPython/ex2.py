# Find and return the most common character in a list
def findMode(itens):
    item_count = {}
    for item in itens:
        item_count[item] = item_count.get(item, 0) + 1
    
    result = None
    max_count = 0

    for item, count in item_count.items():
        if count > max_count:
            max_count = count
            result = item

    return result

test = [2, 2, 2, 2, 3, 3, 3, 4, 5]
print(findMode(test))


