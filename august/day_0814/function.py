# 15596
# def solve(a):
#     return sum(a)

# 4673
# def self_number(a):
#     a_sum = a + sum(map(int, str(a)))
#     return a_sum
#
#
# non_self = set()
#
# for i in range(1, 10001):
#     non_self.add(self_number(i))
#
# for j in range(1, 10001):
#     if j not in non_self:
#         print(j)


# 1065
def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu_cnt += 1
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu_cnt += 1
    return hansu_cnt

num = int(input())
print(hansu(num))