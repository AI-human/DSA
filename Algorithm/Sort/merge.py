def mergesort(arr, l,r):
  if l<r:
    mid = (l+r)//2
    print(arr)
    mergesort(arr,l,mid)
    mergesort(arr,mid+1,r)
    print(arr)
    merge(arr,l,mid,r)
    return arr

def merge(arr,l,mid,r):
  l_arr = arr[l:mid+1]
  r_arr = arr[mid+1:r+1]
  print(l_arr," ",r_arr)


  i = 0
  j = 0
  k = l

  while i<len(l_arr) and j<len(r_arr):
    if l_arr[i]<=r_arr[j]:
      arr[k] = l_arr[i]
      i+=1
    else:
      arr[k] = r_arr[j]
      j+=1
    k+=1
  print(arr)
  
  while i<len(l_arr):
    arr[k]= l_arr[i]
    i+=1
    k+=1
  print(arr)


  while i<len(r_arr):
    arr[k]= r_arr[j]
    j+=1
    k+=1
  print(arr)




a = [5,1,1,2,0,0]
mergesort(a,0,len(a))
print(a)