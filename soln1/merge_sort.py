def merge_sort(num_list):   
    if len(num_list)>1: 
        mid = len(num_list)//2
        left = merge_sort(num_list[:mid]) 
        right = merge_sort(num_list[mid:] ) 
  
        num_list =[] 
  
        while len(left)>0 and len(right)>0: 
            if left[0]<right[0]: 
                num_list.append(left[0]) 
                left.pop(0) 
            else: 
                num_list.append(right[0]) 
                right.pop(0) 
  
        for i in left: 
            num_list.append(i) 
        for i in right: 
            num_list.append(i) 
                  
    return num_list 
  
# Input list 
a = [1, 8, 2, 5, 9, 7] 
print("Given array is") 
print(*a) 
  
a = merge_sort(a) 
  
# Print output 
print("Sorted array is : ") 
print(*a) 
