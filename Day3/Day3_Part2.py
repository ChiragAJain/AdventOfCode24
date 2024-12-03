from input import problem_input
import regex as re

def mul(x, y):
    return x * y
def scrape(input):
    flag = True
    sum = 0
    instructions = re.split(r"(?=mul\(|do\(\)|don't\(\))", input)
    for instruction in instructions:
        if re.match(r"do\(\)", instruction):
            flag = True
            continue
        if re.match(r"don't\(\)", instruction):
            flag = False
            continue
        match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", instruction)
        if match and flag:
            num1, num2 = map(int, match.groups())
            sum += mul(num1, num2)
    return sum
print(scrape(problem_input))