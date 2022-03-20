def upperTri(mat):
    tri = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            if i<=j:
                row.append(mat[i][j])
        tri.append(row)
    return tri

def lowerTri(mat):
    tri = []
    for i in range(len(mat)):
        row = []
        for j in range(len(mat[0])):
            if i>=j:
                row.append(mat[i][j])
        tri.append(row)
    return tri

mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
      ]

tri = upperTri(mat)
print(tri)

tri = lowerTri(mat)
print(tri)