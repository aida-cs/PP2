def has_33(nums):
    return "33" in ''.join(map(str, nums))

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))  