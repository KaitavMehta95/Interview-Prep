print("Jump Search program.")
import math
arr = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
find = 54

m = int(math.sqrt(len(arr)))
index = 0
while index < len(arr):
    if arr[index] >= find:
        index = index - m
        for index in range(index,index+m):
            if arr[index] == find:
                print(find," found at index: ",index)
                break
        print(find," not found. index: ",-1)
        break
    else: 
        index = index + m
