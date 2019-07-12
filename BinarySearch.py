
arr = [1,12,43,54,65,70,115] 
x = 43


def binarySearch(arr,x):
    l = 0
    r = len(arr)-1
    
    while l<=r:
        
        mid = int((l+ r)/2)
        
        if arr[mid] == x:
            return mid
        
        if arr[mid] < x:
            l= mid+1
          
        
        if arr[mid] > x:
            r = mid-1
            
   
    return -1
    
index = binarySearch(arr,x)
print("Element %d found at index %d" % (x,index))
