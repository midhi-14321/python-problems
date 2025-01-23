# highest number in the nested list
my_lst=[[1,2,3],[4,5,6]]
highest=0
for i in my_lst:
    greater=0
    for j in i:
        if j>greater:
            greater=j
    highest=greater
    # print(greater)
print(highest) 