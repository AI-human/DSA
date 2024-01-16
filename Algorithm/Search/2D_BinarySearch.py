
''' TC: O(log(m*n)) or O(log(n^2)) MC: O(1)
It uses binary search twice: first, to find the potential
 row where the target could be, and second, to find the 
 target in that row. If the target is found, it returns True; otherwise, it returns False.
'''

def twoD_binary_search(mat, target: int) -> bool:

    li ,ri = 0, len(mat)-1
    while li<=ri:
        midi = (li+ri)//2
        if mat[midi][0]<=target and mat[midi][-1]>=target:
            lj , rj = 0, len(mat[midi])-1
            while lj<=rj:
                midj = (lj+rj)//2
                
                if mat[midi][midj] == target:
                    return True
                elif mat[midi][midj]<target:
                    lj = midj + 1
                else:
                    rj = midj - 1
            return False
        elif mat[midi][0]<target :
            li = midi + 1
        else:
            ri= midi - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(twoD_binary_search(matrix,target))

