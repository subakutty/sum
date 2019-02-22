def largest(arr,x): 
    max = arr[0] 
    for i in range(1,x): 
        if arr[i] > max: 
            max = arr[i] 
    return max
arr = [10, 324, 45, 90, 9808] 
x = len(arr) 
b = largest(arr,x) 
print (b)
