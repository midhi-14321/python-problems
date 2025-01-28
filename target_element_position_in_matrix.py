#print position of a target element
matrix=[[1,2,3,7,6],[4,5,6,11],[7,8,9,11]]
target=int(input('enter a number: '))
found=False
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if target==matrix[i][j]:
            print('row',i,'column',j)
            found=True
            break
    
if not found:
    print('not found')