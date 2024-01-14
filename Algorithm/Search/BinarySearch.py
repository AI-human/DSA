

n = int(input())
arr = list(map(int,input().split()))

arr.sort()
x = int(input())

def binary_search(arr,x):

  l , r = 0,len(arr)-1

  while l<=r:
    mid = l+r//2 

    if arr[mid] == x:
      return mid 
    elif arr[mid]> x:
      r = mid- 1 
    else :
      l = mid + 1
print(arr)
print(binary_search(arr,x))