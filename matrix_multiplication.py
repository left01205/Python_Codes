# Given code works only for 2x2  and 3x3 resulting inputs
# Wrote this code when was quite new to the language.
r1=int(input("Enter number of rows of first matrix = "))
r2=int(input("Enter number of rows of second matrix = "))
c1=int(input("Enter number of columns of first matrix = "))
c2=int(input("Enter number of columns of second matrix = "))

if c1 == r2:
    if r1*c2 == 4:
        result=[[0,0],
                [0,0]]
        x=[]
        y=[]
        for i in range (r1):
            a=eval(input("Enter row of matrix x (in form of [a1,a2]="))
            x.append(a)
        for j in range(r2):
            b=eval(input("Enter row of matrix y (in form of [b1,b2]="))
            y.append(b)
        # iterate through rows of X
        for i in range(len(x)):
            # iterate through columns of Y
            for j in range(len(y[0])):
                # iterate through rows of Y
                for k in range(len(y)):
                    result[i][j] += x[i][k] * y[k][j]
        print(result)
    elif r1*c2== 9:
        result = [[0, 0 ,0],
                  [0, 0, 0],
                  [0, 0, 0]]
        x = []
        y = []
        for i in range(r1):
            a = eval(input("Enter row of matrix x (in form of [a1,a2,a3]="))
            x.append(a)
        for j in range(r2):
            b = eval(input("Enter row of matrix y (in form of [b1,b2,b3]="))
            y.append(b)
        # iterate through rows of X
        for i in range(len(x)):
            # iterate through columns of Y
            for j in range(len(y[0])):
                # iterate through rows of Y
                for k in range(len(y)):
                    result[i][j] += x[i][k] * y[k][j]
        #printing result
        print('[')
        for t in result:
            print(t"\n")
        print(']')
else:
    print("matrix multiplication can't be done \n Please enter valid matrices for operation")
