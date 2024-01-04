

a = [1,5,3,2,1]

''' O(2^n) Stable '''
for i in range(0,len(a)):
  print("i",i)
  j = i-1
  print("j",j)  
  while j>=0 and a[j] > a[j+1] :
    print(a)
    print("before swap",a[j],a[j+1])
    a[j+1],a[j] = a[j],a[j+1]
    print("after swap",a[j],a[j+1])
    print(a)
    j-=1
    print("j",j)  
print(a)


