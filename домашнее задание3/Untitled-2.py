def selection_sort(lst):
    
    result = lst.copy()
    n = len(result)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        if min_idx != i:
            result[i], result[min_idx] = result[min_idx], result[i]
    return result

print(selection_sort([5, 2, 9, 1, 7]))       
print(selection_sort([3, 3, 1, 2]))          
print(selection_sort([]))