from Day1_Part1 import left_list,right_list
def similarity_score(left_list,right_list):
    sum = 0
    for i in left_list:
        count = right_list.count(i)
        sum+=i*count
    return sum
print(similarity_score(left_list,right_list))
