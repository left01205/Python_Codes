def submatrix(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i] + m[i+1:])]

def determinant(m):
    if len(m) == 1:
        return m[0][0]
    elif len(m) == 2:
        return m[0][0]*m[1][1] - m[0][1]*m[1][0]
    else:
        det = 0
        for j in range(len(m)):
            det += (-1)**j * m[0][j] * determinant(submatrix(m, 0, j))
        return det

m = [[3,2,1],
        [6,2,1],    
        [7,4,8]]
det = determinant(m)
print("Determinant:", det)
