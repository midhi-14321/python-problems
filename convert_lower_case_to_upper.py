string="MidHiLesH"
res=""
lower='abcdefghijklmnopqrstuvwxyz'
upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(len(string)):
    is_lower=False
    for j in range(len(lower)):
        if string[i]==lower[j]:
            res=res+upper[j]
            is_lower=True
    if string[i] not in lower:
        res=res+string[i]
print(res)

