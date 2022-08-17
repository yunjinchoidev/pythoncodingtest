# 1	2750	 수 정렬하기
# N = int(input())
#
# input_list = []
# for i in range(N):
#     input_list.append(int(input()))
#
# input_list.sort()
# for i in range(N):
#     print(input_list[i])


# 2	2751	 수 정렬하기 2
# N = int(input())
#
# input_list = []
# for i in range(N):
#     input_list.append(int(input()))
#
# input_list.sort()
# for i in range(N):
#     print(input_list[i])

# 3	10989	 수 정렬하기 3
# import sys
#
# n = int(sys.stdin.readline())
# num_list = [0] * 10001
#
# for _ in range(n):
#     num_list[int(sys.stdin.readline())] += 1
#
# for i in range(10001):
#     if num_list[i] != 0:
#         for j in range(num_list[i]):
#             print(i)
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            sys.stdout.write(str(i) + '\n')

# 4	25305	 커트라인
# N, k = map(int, input().split())
# score_list = list(map(int, input().split()))
# score_list.sort(reverse=True)
# print(score_list[k-1])


# 5	2108	 통계학
# import sys
# from collections import Counter
# N = int(sys.stdin.readline())
#
# input_list=[]
# for i in range(N):
#     input_list.append(int(sys.stdin.readline()))
#
# input_list.sort()
# avg = round(sum(input_list)/N)
# center_value = input_list[N//2]
# cnt = Counter(input_list).most_common(2)
#
# if len(input_list) > 1:
#     if cnt[0][1] == cnt[1][1]:
#         many_value = cnt[1][0]
#     else:
#         many_value = cnt[0][0]
# else:
#         many_value = cnt[0][0]
#
# range = max(input_list) - min(input_list)
#
# print(avg)
# print(center_value)
# print(many_value)
# print(range)


# 6	1427	 소트인사이드
# input_list = list(map(int, input()))
# input_list.sort(reverse=True)
# r = ""
# for i in input_list:
#     r += str(i)
# print(r)


# 7	11650	 좌표 정렬하기
# N = int(input())
#
# input_list = [[0]*2 for _ in range(N)]
# for i in range(N):
#     input_list[i] = list(map(int, input().split()))
# input_list.sort()
# for i in range(N):
#     print(input_list[i][0], input_list[i][1])


# 8	11651	 좌표 정렬하기 2
# N = int(input())
#
# input_list = [[0]*2 for _ in range(N)]
# for i in range(N):
#     x, y = map(int, input().split())
#     input_list[i] = [y, x]
# input_list.sort()
#
# for i in range(N):
#     print(input_list[i][1], input_list[i][0])


# 9	1181	 단어 정렬
# import sys
#
# n = int(sys.stdin.readline())
# lst = []
#
# for i in range(n):
#     lst.append(sys.stdin.readline().strip())
# set_lst = set(lst)
# lst = list(set_lst)
# lst.sort()
# lst.sort(key = len)
#
# for i in lst:
#     print(i)


# 10	10814	 나이순 정렬
# N = int(input())
# input_list = []
# for i in range(N):
#     age, name = input().split()
#     input_list.append([int(age), name])
#
# input_list.sort(key=lambda x: x[0])
#
# for i in input_list:
#     print(i[0], i[1])



# 11	18870	 좌표 압축 dict 의 시간 복잡도
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# arr = list(map(int, input().split()))
#
# arr2 = sorted(list(set(arr)))
# dic = {arr2[i] : i for i in range(len(arr2))}
# for i in arr:
#     print(dic[i], end = ' ')






