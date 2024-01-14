
'''
Average Case (O(n)): On average, each recursive call processes a list that
  is half the size of the previous list, leading to a linear number of operations overall.
    This is similar to the logic behind the average-case analysis of QuickSort.


Worst Case (O(n2)): The worst-case scenario occurs when the pivot is consistently the
  smallest or largest element, resulting in very skewed partitions. In this case, 
    each recursive call only eliminates one element, leading to a quadratic number of operations overall.
'''


def findKthLargest(nums, k: int) -> int:
    k = len(nums) - k

    def quickSelect(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k: return quickSelect(l, p - 1)
        elif p < k: return quickSelect(p + 1, r)
        else: return nums[p]

    return quickSelect(0, len(nums) - 1)

nums = [3,5,4,2,7] 
k = 2
print(findKthLargest(nums, k))

'''
let’s walk through the code with the array [3,5,4,2,7] and k=2. Remember, 
  we’re looking for the 2nd largest element, which is 5 in this case.

Here are the steps:

Initialization: We start by adjusting k to account for 0-indexing and the fact that
 we’re looking for the kth largest element, not the kth smallest. So k = len(nums) - k = 5 - 2 = 3.

First Call to quickSelect: We call quickSelect(0, len(nums) - 1), which is quickSelect(0, 4).

First Partition: We choose 7 as the pivot (the last element in the current subarray). 
  We initialize p to the start of the subarray, which is 0. We then iterate over the subarray,
    swapping elements that are less than or equal to the pivot with the element at position p, 
      and incrementing p each time we make a swap. After this step, the array looks like this: [3, 5, 4, 2, 7], and p=4.

First Recursive Call: Since p > k, we recurse on the left subarray and call quickSelect(0, p - 1), which is quickSelect(0, 3).

Second Partition: We choose 2 as the pivot. After partitioning, the array looks like this: [2, 3, 4, 5, 7], and p=1.

Second Recursive Call: Since p < k, we recurse on the right subarray and call quickSelect(p + 1, r), which is quickSelect(2, 3).

Third Partition: We choose 5 as the pivot. After partitioning, the array looks like this: [2, 3, 4, 5, 7], and p=3.

Termination: Since p == k, we have found the kth largest element and return nums[p], which is 5.

So, the 2nd largest element in the array [3,5,4,2,7] is 5'''