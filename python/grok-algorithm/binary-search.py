def binary_search(list, target):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid -1
        else:
            low = mid + 1
    return None

my_list = [1, 2, 3, 4, 5, 6, 7, 8]

print(binary_search(my_list, 5))

#what if I added this
#whill it be changed?