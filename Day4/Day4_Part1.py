from Input import input

xmas_matrix = [list(line) for line in input.splitlines()]
word = 'XMAS'
directions = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(-1, -1),(1, -1),(-1, 1)]
rows = len(xmas_matrix)
cols = len(xmas_matrix[0])
def count_xmas(matrix, word):
    count = 0
    word_len = len(word)
    for row in range(rows):
        for col in range(cols):
            for dr, dc in directions:
                found = True
                for i in range(word_len):
                    nr, nc = row + dr * i, col + dc * i
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or matrix[nr][nc] != word[i]:
                        found = False
                        break
                if found:
                    count += 1
    return count
occurrences = count_xmas(xmas_matrix, word)
print("Number of occurrences of 'XMAS':", occurrences)