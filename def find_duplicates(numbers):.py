def find_duplicates(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    
    new_list = []
    for number, count in counts.items():
        if count > 1:
            new_list.append(number)
    
    return (new_list)

numbers = [1, 1, 2, 3, 3, 4, 5, 5, 5]
print (find_duplicates(numbers))