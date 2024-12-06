from Input import input
xmas_matrix = [list(line) for line in input.splitlines()]
rows = len(xmas_matrix)
cols = len(xmas_matrix[0])
def count_xmas(matrix):
    count = 0
    mas= {"M", "S"}
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if matrix[i][j] == "A":
                    if {matrix[i - 1][j - 1], matrix[i + 1][j + 1]} == mas and {matrix[i - 1][j + 1], matrix[i + 1][j - 1]} == mas:
                        count += 1
    return count
occurrences = count_xmas(xmas_matrix)
print("Number of 'X-MAS' patterns:", occurrences)