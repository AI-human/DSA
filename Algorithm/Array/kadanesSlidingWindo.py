

def kadanesSlidingWindow(arr):
  maxSum = arr[0]
  curSum, maxL,maxR = 0,0,0
  L = 0 

  for R in range(len(arr)):
    if curSum < 0:
      curSum = 0
      L = R
    
    curSum += arr[R]
    
    if curSum>maxSum:
      maxSum = curSum 
      maxL,maxR = L,R

  return [maxL,maxR]


a = [2,3,4,-1]

print(kadanesSlidingWindow(a))