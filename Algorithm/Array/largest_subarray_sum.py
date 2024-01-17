
'''O(n^2) for optimal solution please check Kadane's Algo'''

def bruteforce(arr):
  maxsum = arr[0]

  for i in range(len(arr)):
    cursum = 0
    for j in range(i,len(arr)):
      cursum += arr[j]
      maxsum = max(maxsum,cursum)

  return maxsum

a = [2,3,4,-1]

print(bruteforce(a))