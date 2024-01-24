n = int(input())
arr = list(map(int,input().split()))


def bucketSort(list):
    mx = max(list)    
    if mx>1e5:
        return 'range is to big'
    cnts = [0]*(mx+1)
    print(cnts)

    for i in range(len(list)):
        cnts[list[i]]+=1

    k = 0
    for i in range(len(cnts)):
        for j in range(cnts[i]):
            list[k] = i
            k+=1

bucketSort(arr)
print(arr)