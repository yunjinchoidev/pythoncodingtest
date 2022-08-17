# 10814
# import sys
#
# n = int(input())
# card = list(map(int, sys.stdin.readline().split()))
# m = int(input())
# check = list(map(int, sys.stdin.readline().split()))
#
# card.sort()
#
# def binary_search(array, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#
#         if array[mid] == target:
#             return mid
#         elif array[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None
#
# for i in range(m):
#     if binary_search(card, check[i], 0, n-1) is not None:
#         print(1, end=' ')
#     else:
#         print(0, end=' ')

# 14425
# N, M = map(int, input().split())
#
# s = set(input() for _ in range(N))
# cnt = 0
# for _ in range(M):
#     t = input()
#     if t in s:
#         cnt += 1
# print(cnt)


# 1620
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# dict = {}
#
# for i in range(1, n + 1):
#     a = input().rstrip()
#     dict[i] = a
#     dict[a] = i
#
# for i in range(m):
#     quest = input().rstrip()
#     if quest.isdigit():
#         print(dict[int(quest)])
#     else:
#         print(dict[quest])


# 10816	 숫자 카드 2
# from collections import Counter
# from sys import stdin
#
# n = stdin.readline().rstrip()
# card = list(map(int,stdin.readline().split()))
# m = stdin.readline().rstrip()
# test = list(map(int,stdin.readline().split()))
#
# count = Counter(card)
#
# for i in range(len(test)):
#     if test[i] in count:
#         print(count[test[i]], end=' ')
#     else:
#         print(0, end=' ')

# 1764	 듣보잡
# n, m = map(int, input().split())
#
# a = set()
# for i in range(n):
#     a.add(input())
#
# b = set()
# for i in range(m):
#     b.add(input())
#
# result = sorted(list(a & b))
#
# print(len(result))
#
# for i in result:
#     print(i)


# 1269	 대칭 차집합
# A, B = map(int, input().split())
#
# A_list = list(map(int, input().split()))
# B_list = list(map(int, input().split()))
#
# A_and_B = set(set(A_list) & set(B_list))
#
# return_A = [i for i in A_list if i not in A_and_B]
# return_B = [i for i in B_list if i not in A_and_B]
# print(len(return_A)+len(return_B))

# 11478	 서로 다른 부분 문자열의 개수
# S = input()
# ans = set()
#
# for i in range(len(S)):
#     for j in range(i, len(S)):
#         temp=S[i:j+1]
#         ans.add(temp)
# print(len(ans))