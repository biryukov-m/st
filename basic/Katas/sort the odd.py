def sort_array(source_array):
    insertion = [e for e in source_array if e % 2 != 0]
    insertion.sort()
    insertion = iter(insertion)
    for i in range((len(source_array))):
        if source_array[i] % 2 != 0:
            source_array[i] = int(next(insertion))
    return source_array
print(sort_array([5, 3, 2, 8, 1, 4]))