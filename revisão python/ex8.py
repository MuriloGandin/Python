def twosum(lst, target):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] + lst[j] == target and i != j:
                return [i, j]
            
print(twosum([1, 2, 5, -1], 4))
