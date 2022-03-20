def diagonal_left1(mat):
    dia = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i==j:
                dia.append(mat[i][j])
    return dia

def diagonal_right1(mat):
    dia = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i+j==len(mat)-1:
                dia.append(mat[i][j])
    return dia

mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
       ]
    
dia = diagonal_left1(mat)
print(dia)

dia = diagonal_right1(mat)
print(dia)


def diagonal_left(mat):
    dia = []
    for i in range(len(mat)):
        dia.append(mat[i][i])
    return dia

def diagonal_right(mat):
    dia = []
    j = len(mat)-1
    for i in range(len(mat)):
        dia.append(mat[i][j])
        j-=1
    return dia

mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
       ]
    
dia = diagonal_left(mat)
print(dia)

dia = diagonal_right(mat)
print(dia)