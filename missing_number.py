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

#missing number in a number
def missing(num):
    temp=num
    digit_list=[]
    missing_list=[]
    while temp!=0:
        digit=temp%10
        digit_list.append(digit)
        temp//=10
    minimum_num=min(digit_list)
    maximum_num=max(digit_list)
    for i in range(minimum_num,maximum_num+1):
        if i not in digit_list:
            missing_list.append(i)
    return missing_list
            
num=632718
print(missing(num))

# missing numbers in a list that is even number
def missing_even_numbers(lst):
    minimum=float("inf")
    maximum=float("-inf")
    missing_numbers=[]
    for i in lst:
        if i>maximum:
            maximum=i
        if i<minimum:
            minimum=i
    for i in range(minimum,maximum+1):
        if i not in lst and i%2==0:
            missing_numbers.append(i)
    return missing_numbers
lst=[-4,6,10,12]
print(missing_even_numbers(lst))