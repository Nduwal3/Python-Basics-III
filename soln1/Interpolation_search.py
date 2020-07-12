def interpolation_search(num_list, size, item):
    low = 0
    high = size - 1

    while low <= high and item >= num_list[low] and item <= num_list[high]:
        if low == high:
            if num_list[low] == item:
                return low
            return -1
        position  = low + int(((float(high - low) / ( num_list[high] - num_list[low])) * ( item - num_list[low]))) 
        if num_list[position] == item:
            return position        
        if num_list[position] < item:
            low = position + 1
        else:
            high = position - 1
    return -1

input_list =[1, 5, 7, 9, 12, 15, 22]
size = len(input_list)
item = 9
index = interpolation_search(input_list, size, item)
print(index)

