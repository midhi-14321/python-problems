# reverse a string
def reverse_string(word):
    if len(word)==0:
        return ""
    return word[-1]+reverse_string(word[:-1])

word='midhilesh'
print(reverse_string(word))

# factorial of number
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
    
n=5
print(factorial(n))

#