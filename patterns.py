# pattern 1
row=int(input('enter a no of rows: '))
for i in range(1,row+1):
    print(row*' * ')
print()

# pattern 2
row=int(input('enter a number of rows: '))
count=0
for i in range(1,row+1):
    for j in range(1,i+1):
        count=count+1
        print(count,end=' ')
    print()

#pattern 3
row=int(input('enter a number of rows:'))
for i in range(1,row+1):
    spaces=(row-i)*' '
    stars=i*' *'
    print(spaces+stars)

#pattern 4
row=int(input('enter a number of rows:'))
for i in range(1,row+1):
    spaces=(row-i)*'  '
    stars=(2*i-1)*' *'
    print(spaces+stars)

#pattern 5
row=int(input('enter a no of rows: '))
for i in range(1,row+1):
    spaces=(row-i)*'  '
    stars=(2*i-1)*' *'
    print(spaces+stars)
for j in range(row,-1,-1):
    spaces=(row-j)*'  '
    stars=(2*j-1)*' *'
    print(spaces+stars)

#pattern 6
row=int(input('enter a no of rows: '))
for i in range(1,row+1):
    spaces=(row-i)*' '
    print(spaces,end='')
    for j in range(1,i+1):
        if i==1 or j==1 or j==i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for j in range(row,-1,-1):
    spaces=(row-j)*' '
    print(spaces,end='')
    for k in range(1,j+1):
        if j==1 or k==1 or k==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()