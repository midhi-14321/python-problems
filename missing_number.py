#method 1
lst=[1,2,5]
min_value=min(lst)
max_value=max(lst)
for i in range(min_value,max_value+1):
    if i not in lst:
        print(i,'is the missing number')
        
# find a single missing number in a list
#method 2
def missingNumber(lst):
    start,end=min(lst),max(lst)
    expected_sum=sum(range(start,end+1))
    actual_sum=sum(lst)
    return expected_sum-actual_sum
lst=[7,1,4,6,3,2]
print(missingNumber(lst),"is the missing number")

#multiple missing numbers in a list
def find_missing_numbers(lst):
    start, end = min(lst), max(lst)
    missing_numbers = []
    
    for num in range(start, end + 1):
        if num not in lst:
            missing_numbers.append(num)
    
    return missing_numbers

lst = [6, 7, 9, 11, 12]  
print(find_missing_numbers(lst)) 
