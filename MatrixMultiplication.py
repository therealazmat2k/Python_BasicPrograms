def matrix_multiplication():
    m1, m2 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # Take first matrix as input
    for i in range(3):
        row = input(f"Please input row {i+1} of first matrix : ").split()
        for j in range(3):
            row[j] = int(row[j])
        m1[i] = row

    print("\n")

    # Take second matrix as input
    for i in range(3):
        row = input(f"Please input row {i+1} of second matrix : ").split()
        for j in range(3):
            row[j] = int(row[j])
        m2[i] = row

    # Calculate the result
    for i in range(3):
        for j in range(3):
            temp = 0
            for k in range(3):
                temp += m1[i][k] * m2[k][j]

            result[i][j] = temp

    # Print output in a matrix form
    print("\nOutput = ")
    for i in range(3):
        print(f"         {result[i][0]} {result[i][1]} {result[i][2]}")

matrix_multiplication()
