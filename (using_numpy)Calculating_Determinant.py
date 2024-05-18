import numpy as np
a=np.array([[3,2,1],
            [6,2,1],
            [7,4,8]],dtype=np.dtype(float))
print(f"Determinant for {a} is : {np.linalg.det(a):3f}")
