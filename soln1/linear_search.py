def linear_search(num_list, item):
    size = len(num_list)
    for i in range(size):
        if(num_list[i] == item):
            return i

input_list = [50, 30, 20 , 10, 60]
item = 20
index = linear_search(input_list , item)
print('{} is at index {}'.format(item , index))