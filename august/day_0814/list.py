# 10818
# A = int(input())
#
# input_list = list(map(int, input().split()))
#
# print(min(input_list), max(input_list))


# 2562
# input_list = []
# for i in range(9):
#     input_list.append(int(input()))
#
# print(max(input_list))
# print(input_list.index(max(input_list))+1)

# 3052
# input_list = []
# for i in range(10):
#     input_list.append(int(input())%42)
#
# print(len(set(input_list)))


# 1546
N = int(input())
input_list = list(map(int, input().split()))
max = max(input_list)
for i in range(len(input_list)):
    input_list[i] = input_list[i]/max*100


avg = sum(input_list)/N
print(avg)











# 8958
# N = int(input())
#
# for i in range(N):
#     input_list = list((input().split("X")))
#     sum = 0
#     for indi in input_list :
#         count=0
#         size = len(indi)+1
#         for j in range(size):
#             count += j
#         sum += count
#     print(sum)


# 4344
# N = int(input())
#
# for i in range(N):
#     count =0
#     input_list = list(map(int, input().split()))
#     avg = sum(input_list[1:])/input_list[0]
#     for indi in input_list[1:]:
#         if indi > avg:
#             count +=1
#     rate = count/input_list[0]*100
#     print(f'{rate:.3f}%')
