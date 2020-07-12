# def partition(num_list, low, high):
#     i = (low - 1)
#     # print(i)
#     pivot = num_list[high]

#     for j in range (low, high):
#         if num_list[j] <= pivot:
#             i += 1
#             num_list[j], num_list[i] = num_list[i], num_list[j]
#     num_list[j + 1], num_list[high] = num_list[high], num_list[j + 1]
#     return j + 1

def partition(num_list, start, end):
    pivot = num_list[start]
    low = start + 1
    high = end

    while True:
        while low <= high and num_list[high] >= pivot:
            high = high - 1
        while low <= high and num_list[low] <= pivot:
            low = low + 1
        if low <= high:
            num_list[low], num_list[high] = num_list[high], num_list[low]
        else:
            break
    num_list[start], num_list[high] = num_list[high], num_list[start]
    return high

def quick_sort(num_list, low, high):
    if low < high:
        result = partition(num_list, low, high)
        quick_sort(num_list, low, result-1)
        quick_sort(num_list, result + 1, high)
        
        
    
input_list = [5, 9, 2, 7, 1, 0]
quick_sort(input_list , 0 , (len(input_list) - 1))
print(input_list)

