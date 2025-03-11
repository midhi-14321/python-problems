# iterate over each digit in a list and check it is strict increasing or not 
#method 1
def check_digit_increasing(lst):
    result = []
    for num in lst:
        str_num = str(num)  
        increasing = all(str_num[i] < str_num[i + 1] for i in range(len(str_num) - 1))  
        result.append(increasing)
    return result

numbers = [123, 135, 321, 245, 789, 987, 56789, 468, 102, 469]
output = check_digit_increasing(numbers)
print(output)  

# method 2 concise code
numbers = [123, 135, 245, 779]
output = [all(str(num)[i] < str(num)[i+1] for i in range(len(str(num)) - 1)) for num in numbers]
print(output) 

