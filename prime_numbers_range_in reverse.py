start=20
end=1
for i in range(start,end-1,-1):
    if i>=1:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        
        if count==2:
            print(i)
    else:
        pass