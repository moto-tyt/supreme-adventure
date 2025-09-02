def selection_sort_sth(list):
    new_list = []
    while list:
        smallest = find_smallest(list)
        new_list.append(list[smallest])
        del list[smallest]
        
    return new_list

def find_smallest(list):
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index



my_list = [3, 1, 7, 8]
print(find_smallest(my_list))
print(selection_sort_sth(my_list))

