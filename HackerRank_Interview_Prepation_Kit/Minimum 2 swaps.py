def minimumSwaps(arr):
    swap = 0
    dict = {}
    
    for i in range(len(arr)):
       dict[arr[i]] = i
    
    arr = sorted(arr)
    
    for k,v in dict.items():
        if arr[v] != k:
            swap_val = arr[v]
            arr[arr.index(k)] = swap_val
            arr[v] = k 
            swap += 1
    return swap