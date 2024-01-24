from collections import Counter

def topKFrequent(nums, k):
  '''
  Instead of heap or sort which is O(nlogn) bucketSort algo counts 
  takes Frequency as index then add element of same frequent number
  
  Returns the top k frequent elements in the given list of numbers.
  
  Parameters:
    nums (list): A list of integers.
    k (int): The number of top frequent elements to be returned.
    
  Returns:
    list: A list of the top k frequent elements.
  '''
  # Count the frequency of each number
  freq_map = Counter(nums)
  
  # Create a list of lists to store numbers with the same frequency
  arr = [[] for _ in range(len(nums)+1)]
  
  # Store numbers in the corresponding frequency index
  for num, freq in freq_map.items():
    arr[freq].append(num)
  
  # Retrieve the top k frequent elements
  ans = []
  for i in range(1, len(arr)+1):
    for j in range(len(arr[-i])):
      ans.append(arr[-i][j])
      if len(ans) == k:
        break
    if len(ans) == k:
      break
  
  return ans

nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))


