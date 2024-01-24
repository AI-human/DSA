''' Frequency of item in list '''

from collections import Counter

nums = [...]  # your list of numbers
mp = Counter(nums)
#__________________________
nums = [...]  # your list of numbers
mp = {}

for x in nums:
    if x in mp:
        mp[x] += 1
    else:
        mp[x] = 1
#__________________________
from collections import defaultdict

nums = [...]  # your list of numbers
mp = defaultdict(int)

for x in nums:
    mp[x] += 1
#__________________________
    
nums = [...]  # your list of numbers
mp = {}

for x in nums:
    mp[x] = mp.get(x, 0) + 1

