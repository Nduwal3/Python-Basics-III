def insertion_sort(num_list):
    size = len(num_list)
    for i in range(1, size):
        key = num_list[i]
        j = i 
        while j > 0 and  key < num_list[j - 1]:
            num_list[j]= num_list[j - 1]
            j -= 1 
        num_list[j] = key
    return num_list

sorted_list = insertion_sort([5, 3 , 2 , 10, 4 , 4])
print(sorted_list)
