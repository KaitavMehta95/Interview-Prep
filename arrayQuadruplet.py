/*
Array Quadruplet
Given an unsorted array of integers arr and a number s, write a function findArrayQuadruplet that finds four numbers (quadruplet) in arr that sum up to s. Your function should return an array of these numbers in an ascending order. If such a quadruplet doesn’t exist, return an empty array.

Note that there may be more than one quadruplet in arr whose sum is s. You’re asked to return the first one you encounter (considering the results are sorted).
*/

def find_array_quadruplet(arr, s):
  arr.sort()  

  print(range(0,len(arr)-3))
  i=0
  for i in range(len(arr)-3):
    for j in range(i+1,len(arr)-2):    
      k = j+1
      l = len(arr)-1
      r = s - (arr[i]+arr[j])
      while k < l:
      	if arr[l]+arr[k] < r:
          k = k+1 
      	elif arr[l]+arr[k] >  r:
          l = l-1
      	else:
      		return [arr[i],arr[j],arr[k],arr[l]]
  return []
