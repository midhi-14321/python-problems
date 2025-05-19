arr=[5,4,-1,7,8]
n=len(arr)
res=arr[0]
cur=arr[0]
for i in range(1,n):
    cur=max(arr[i],arr[i]+cur)
    res=max(res,cur)
print(res)