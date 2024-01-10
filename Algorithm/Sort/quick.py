

# Time complexity: O(nlogn)
# Space complexity: O(1)
# Stable: No
def quicksort(arr,l,r):
    # If the left index is less than the right index, proceed with the sorting
    if l<r:
        # Choose the last element as the pivot
        pivot = arr[r]
        # Initialize the left pointer at the first element
        left = l

        # Start the loop from the left index and go up to the second last element
        for i in range(l,r):
            # If the current element is smaller than pivot, swap it with the element at 'left' index
            if pivot>arr[i]:
                arr[i],arr[left] = arr[left], arr[i]
                # Move the 'left' index to the right
                left+=1

        # Swap the pivot element with the element at 'left' index
        arr[r] = arr[left]
        arr[left] = pivot

        # Recursively apply the same logic to the left and right subarrays
        quicksort(arr,l,left-1)
        quicksort(arr,left+1,r)
    # If the array is sorted, return it
    return arr
  

import numpy as np 

a = np.random.randint(0,9,20).tolist()


quicksort(a,0,len(a)-1)
print(a)
