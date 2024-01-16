
arr=[0,0,0,0,0,1,1,1,1,1,1]
arr.sort()

def ok(m):
    return True if arr[m] == 1 else False

def range_based_binary_search(arr):
    l ,r= 0,len(arr)-1
    while l<=r:
        m = (l+r)//2
        if ok(m):
            r = m - 1
        else :
            l = m + 1
    return r+1 # return index where 1 start and all are 1

print(range_based_binary_search(arr)) 