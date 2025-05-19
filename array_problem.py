"""Given a list of integers, determine whether any value appears more than once.
Return True if any duplicate is found, otherwise return False"""

arr = [1, 2, 3, 1]
freq = {}
for i in arr:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
for key, value in freq.items():
    if value > 1:
        print("True")
        break
else:
    print("False")
