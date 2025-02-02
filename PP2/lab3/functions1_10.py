def unique_list(lst):
    unique = []
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique

print(unique_list([1, 2, 3, 2, 1, 4]))