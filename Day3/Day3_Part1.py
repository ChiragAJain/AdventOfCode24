from input import problem_input
import regex as re
def mul(x,y):
    return x*y
def scrape(input):
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)",input)
    sum = 0
    for i in matches:
        sum += mul(int(i[0]),int(i[1]))
    return sum
print(scrape(problem_input))