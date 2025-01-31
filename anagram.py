str1='silent'
str2='listen'
freq1={}
freq2={}
if len(str1)==len(str2):
    for ch in str1:
        if ch not in freq1:
            freq1[ch]=1
        else:
            freq1[ch]+=1
    for ch in str2:
        if ch not in freq2:
            freq2[ch]=1
        else:
            freq2[ch]+=1
    for key in freq1:
        if key not in freq2 and freq1[key]!=freq2[key]:
            print('not a anagram')
            break
    else:
        print('anagram')
else:
    print('not a anagram')
        