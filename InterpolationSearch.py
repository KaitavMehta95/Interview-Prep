print ("Interpolation Sorting..")
"""
Binary search - O(logn)
Jump search - O(sqrt(n))
linear search - O(n)

BS- Middle
IS- May go to different locations
probe position = lo + (x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo])
lo- start index
hi- end index
x= element to be found

Works on SORTED ARRAY!

"""

def helper(lo,hi):
		return int(lo + (x-arr[lo])*(hi-lo) / (arr[hi]-arr[lo]))
def interpolationSort(arr,x):

	lo = 0
	hi = len(arr)-1
	pos = helper(lo,hi)
	while lo < hi:
		if(arr[pos] == x):
			return pos
		elif arr[pos] < x:
			pos = helper(pos+1,hi)
		elif arr[pos] > x:
			pos = helper(lo,pos+1)


	return pos

arr = [2,3,4,6,7,9,12,19]
x = 4
print(interpolationSort(arr,x))
