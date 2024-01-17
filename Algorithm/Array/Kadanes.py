'''O(n)'''

def kadanes(arr):

  maxSum = arr[0]
  curSum = 0

  for i in arr[1:]:
    print(curSum,maxSum)
    curSum = max(0,curSum)
    curSum+=i
    maxSum = max(maxSum,curSum)
    print(curSum,maxSum)
  return maxSum


a = [10,-2,2,3,4,-1]
print(kadanes(a))