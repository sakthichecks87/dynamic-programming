# Dynamic programming Python implementation  of LIS problem 
  
# lis returns length of the longest
def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and  
    # initialize LIS values for all indexes 
    lis = [1]*n 
   
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get  
    # the maximum of all LIS 
    maximum = 0
  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
  
    return maximum 
  
# Driver program to test above function 
arr = [100, 10, 22, 9, 33, 21, 20, 50, 41, 60] 
print "Length of lis is", lis(arr) 