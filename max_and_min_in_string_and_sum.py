# method 1
str='123'
num=int(str)
largest=float('-inf') # for lowest value
smallest=float('inf') #for highest value
while num!=0:
    digit=num%10
    if digit>largest:
        largest=digit
    elif digit<smallest:
        smallest=digit
    num=num//10
sum=largest+smallest
print(sum)

#method 2
num_str = "123"  # Example input (string)
largest = '0'  # Set to the smallest possible digit (as a string)
smallest = '9'  # Set to the largest possible digit (as a string)

for digit in num_str:
    if digit > largest:
        largest = digit  # Update largest
    if digit < smallest:
        smallest = digit  # Update smallest

# Convert to integers before summing
print(int(largest) + int(smallest))  # Sum and output the result


        