def hourglassSum(arr):
    max_hourglass = -10000
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            hourglass = arr[i][j]+ arr[i][j+1] + arr[i][j+2]+ arr[i+1][j+1]+arr[i+2][j]+ arr[i+2][j+1] + arr[i+2][j+2]   

            if(hourglass > max_hourglass):
                max_hourglass = hourglass  
    
    return max_hourglass