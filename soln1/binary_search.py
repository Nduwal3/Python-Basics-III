def binary_search(num_list, high, low, item):
    if item in num_list:
        mid_index = (high + low)//2
        if num_list[mid_index] == item:
            return mid_index
        elif num_list[mid_index] < item:
            return binary_search(num_list , high , mid_index + 1 , item)
        elif num_list[mid_index] > item:
            return binary_search(num_list, mid_index - 1, low, item)
    else:
        return -1


input_list = [5, 6, 2, 1, 8, 9, 0]
sorted_list = sorted(input_list)
print(sorted_list)
result_index = binary_search(sorted_list, len(sorted_list), 0, 9)
print(result_index)