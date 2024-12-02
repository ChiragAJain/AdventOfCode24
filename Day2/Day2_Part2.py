from Day2_Part1 import problem_input,is_safe
def is_safe_with_dampener(line):
    if is_safe(line):
        return True
    for i in range(len(line)):
        modified_line = line[:i] + line[i + 1:]
        if len(modified_line) > 1 and is_safe(modified_line):
            return True
    return False
def safe_lines(string):
    lines = string.strip().split("\n")
    count = 0
    for line in lines:
        numbers = list(map(int, line.split()))
        if len(numbers) > 1 and is_safe_with_dampener(numbers):
            count += 1
    return count
print(safe_lines(problem_input))