#print highest number in the maxtrix
matrix=[[1,2,3,7,6],[4,5,6,11],[7,8,9,11]]
maximum=[]
for i in range(len(matrix)):
    highest=0
    for j in range(len(matrix[i])):
        if matrix[i][j]>highest:
            highest=matrix[i][j]
    maximum.append(highest)
print(max(maximum))