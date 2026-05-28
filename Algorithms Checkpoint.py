# Question 1

def binary_search(data_list, target):
    low = 0
    high = len(data_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data_list[mid] == target:
            return True
        elif data_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False

print(binary_search([1, 2, 3, 5, 8], 6))  
print(binary_search([1, 2, 3, 5, 8], 5))  


# Question 2

def power(a, b):
    if b == 0:
        return 1
    elif b < 0:
        return 1 / power(a, -b)
    
    result = 1
    for _ in range(b):
        result *= a
    return result

print(power(3, 4)) 

# Question 3

def bubble_sort(data_list):
    n = len(data_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if data_list[j] > data_list[j + 1]:
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                swapped = True
        if not swapped:
            break
    return data_list

sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(bubble_sort(sample_data))  

# Question 4

def merge_sort(data_list):
    if len(data_list) <= 1:
        return data_list
        
    mid = len(data_list) // 2
    left_half = merge_sort(data_list[:mid])
    right_half = merge_sort(data_list[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    sorted_list = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(merge_sort(sample_data))  

# Question 5

def quick_sort(data_list):
    if len(data_list) <= 1:
        return data_list
    else:
        pivot = data_list[len(data_list) // 2]
        left = [x for x in data_list if x < pivot]
        middle = [x for x in data_list if x == pivot]
        right = [x for x in data_list if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

sample_data = [29, 13, 22, 37, 52, 49, 46, 71, 56]
print(quick_sort(sample_data))  




