def nthRow(mat,n):
    if n>=len(mat):
        return -1
    row = []
    for i in range(len(mat)):
        row.append(mat[n-1][i])
    return row

def nthCol(mat,n):
    if n>=len(mat):
        return -1
    col = []
    for i in range(len(mat)):
        col.append(mat[i][n-1])
    return col


mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
      ]

n = 2
row = nthRow(mat,n)
print(row)
col = nthCol(mat,n)
print(col)