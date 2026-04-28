def find_max(lst):
    max = lst[0]
    for number in lst:
        if max < number:
            max = number
    return max

numbers = [3, 5, 10, 50, -40, 120]

print(find_max(numbers))