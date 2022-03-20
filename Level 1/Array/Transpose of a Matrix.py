def transpose1(mat):
    l = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            row.append(-1)
        l.append(row)

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            l[i][j] = mat[j][i]

    return l

mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

l = transpose1(mat)
print(l)

def transpose2(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i>j:
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

transpose2(mat)
print(mat)