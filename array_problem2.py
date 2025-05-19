"""Given an array of digits, e.g., arr = [1, 2, 3],
treat it as a whole number (123), increment it by 1,
and return the result as an array of digits: [1, 2, 4].
"""

arr = [1, 2, 3]
new_arr = []
new = ""

for i in arr:
    new += str(i)

new = int(new) + 1

while new != 0:
    new_arr.append(new % 10)
    new //= 10

new_arr.reverse()
print(new_arr)  # Output: [1, 2, 4]
