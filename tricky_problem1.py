def decode_string(s):
    result = ""  # This will store the final decoded string
    i = 0       # This is our index to traverse the string

    while i < len(s):
        # If the character is a digit, find the full number
        if s[i].isdigit():
            num = 0
            while s[i].isdigit():  # Handle multi-digit numbers like "10", "20", etc.
                num = num * 10 + int(s[i])
                i += 1

        # If the character is '[', skip it
        elif s[i] == '[':
            i += 1

        # If the character is ']', skip it
        elif s[i] == ']':
            i += 1

        # If the character is a letter, add it to the result
        else:
            # Find the substring to repeat
            substring = ""
            while i < len(s) and s[i].isalpha():  # Collect all letters
                substring += s[i]
                i += 1
            # Repeat the substring 'num' times and add to the result
            result += substring * num

    return result

# Example usage
input_str = "3[a]2[bc]"
output = decode_string(input_str)
print(output)  # Output: aaabcbc