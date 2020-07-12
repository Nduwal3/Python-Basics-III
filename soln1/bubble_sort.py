def bubble_sort(list_input):
    size = len(list_input)
    for i in range(size):        
        for j in range(0, size-i- 1):            
            if(list_input[j]> list_input[j + 1]):                
                list_input[j], list_input[j + 1] = list_input[j + 1], list_input[j]

    return list_input

print(bubble_sort([ 5, 1, 4, 8, 9]))

