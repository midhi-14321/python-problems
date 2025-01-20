lst=[1,2,3,4,5,6,7]
target=9
found=False
for i in range(0,len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]+lst[j]==target:
            found=True
            print(i,j)
            
if not found:
    print('no')