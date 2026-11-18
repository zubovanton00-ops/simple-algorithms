def bubble_sort(lst):

    result = lst.copy()  
    n = len(result)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped: 
            break
    return result


print(bubble_sort([5, 2, 9, 1, 7]))          
print(bubble_sort([3, 3, 1, 2]))            
print(bubble_sort([]))  