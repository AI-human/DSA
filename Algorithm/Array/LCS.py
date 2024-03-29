'''Approach HashSet and Intelligent Sequence Building
Intuition

It turns out that our initial brute force solution was on the right track, but missing
a few optimizations necessary to reach O(n) time complexity.

Algorithm

This optimized algorithm contains only two changes from the brute force
approach: the numbers are stored in a HashSet (or Set, in Python) to
allow O(1) lookups, and we only attempt to build sequences from numbers
that are not already part of a longer sequence. This is accomplished by first
ensuring that the number that would immediately precede the current number in
a sequence is not present, as that number would necessarily be part of a
longer sequence
Complexity Analysis

Time complexity : O(n).

Although the time complexity appears to be quadratic due to the while
loop nested within the for loop, closer inspection reveals it to be
linear. Because the while loop is reached only when currentNum marks
the beginning of a sequence (i.e. currentNum-1 is not present in
nums), the while loop can only run for nnn iterations throughout the
entire runtime of the algorithm. This means that despite looking like
O(n⋅n) complexity, the nested loops actually run in O(n+n)=O(n)
time. All other computations occur in constant time, so the overall
runtime is linear.

Space complexity : O(n).

In order to set up O(1) containment lookups, we allocate linear space
for a hash table to store the O(n) numbers in nums. Other than that,
the space complexity is identical to that of the brute force solution.
'''

nums = [1,100,200,3,4,2]
numset = set(nums)

ans = 0
for i in nums:
    if i-1 not in numset:
        length = 1
        while i+length in numset:
            length +=1
        ans = max(ans,length)

