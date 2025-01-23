my_lst=['classroom','students','laptops']
max=-1
for i in my_lst:
    count=0
    for j in i:
        if j in 'aeiou':
            count+=1
    if count>max:
        max=count
        print(i,'has highest number of vowels')