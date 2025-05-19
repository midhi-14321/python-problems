#find the longest string in the list
str_list=['hi','hello','hey']
greater=len(str_list[0])
for i in str_list:
    length=len(i)
    if length>greater:
        greater=length

for j in str_list:
    if len(j)==greater:
        print(j)
