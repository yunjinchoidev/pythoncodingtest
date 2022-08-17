# 1	5086	 배수와 약수
# while True:
#     N, M = map(int, input().split())
#     if N == 0 and M == 0:
#         break
#     if M % N == 0:
#         print("factor")
#     elif N % M == 0:
#         print("multiple")
#     else:
#         print("neither")


# 2	1037	 약수
# T = int(input())
# input_list = list(map(int, input().split()))
# max_value = max(input_list)
# min_value = min(input_list)
# print(max_value*min_value)


# 3	2609	 최대공약수와 최소공배수
# a, b = map(int, input().split())
#
# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a
#
# def lcm(a, b):
#     return a * b // gcd(a, b)
#
# print(gcd(a, b))
# print(lcm(a, b))

# 4	1934	 최소공배수
# N = int(input())
# for i in range(N):
#     a, b = map(int, input().split())
#
#     def gcd(a, b):
#         while b > 0:
#             a, b = b, a % b
#         return a
#
#     def lcm(a, b):
#         return a * b // gcd(a, b)
#
#     print(lcm(a, b))




# 5	2981	 검문	다국어
# from math import gcd
# from math import sqrt
#
# n = int(input())
# ns = list(int(input()) for _ in range(n))
# ns.sort()
# interval = list()
# ans = list()
#
# for i in range(1, n):
#     interval.append(ns[i] - ns[i - 1])
#
# prev = interval[0]
# for i in range(1, len(interval)):
#     prev = gcd(prev, interval[i])
#
# for i in range(2, int(sqrt(prev)) + 1): #제곱근까지만 탐색
#     if prev % i == 0:
#         ans.append(i)
#         ans.append(prev//i)
# ans.append(prev)
# ans = list(set(ans)) #중복이 있을수 있으니 제거
# ans.sort()
# print(*ans)


# 6	3036	 링	다국어
# def gcd(a, b):
#     while(b != 0):
#         n = a%b
#         a = b
#         b = n
#     return a
#
# n = int(input())
# li = list(map(int, input().split()))
# for i in range(1, n):
#     g = gcd(li[0], li[i])
#     print('{0}/{1}'.format(li[0]//g, li[i]//g))


# 7	11050	 이항 계수 1
# from math import factorial
# n, k = map(int, input().split())
# b = factorial(n) // (factorial(k) * factorial(n - k))
# print(b)



# 8	11051	 이항 계수 2
# n, k = map(int, input().split())
# dp = [[0] * 1 for i in range(1001)]
# dp[1].append(1)
# for i in range(2, 1001):
#     for j in range(1, i + 1):
#         if j == 1:
#             dp[i].append(1)
#         elif j == i:
#             dp[i].append(1)
#         else:
#             dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
# print(dp[n + 1][k + 1] % 10007)


# 9	1010	 다리 놓기
# from math import factorial
# N = int(input())
# for i in range(N):
#     k, n = map(int, input().split())
#     b = factorial(n) // (factorial(k) * factorial(n - k))
#     print(b)


# 10	9375	 패션왕 신해빈	다국어
# t = int(input())
#
# for i in range(t):
#     n = int(input())
#     weardict = {}
#     for j in range(n):
#         wear = list(input().split())
#         if wear[1] in weardict:
#             weardict[wear[1]].append(wear[0])
#         else:
#             weardict[wear[1]] = [wear[0]]
#
#     cnt = 1 # 각 종류마다 항목의 개수
#
#     for k in weardict:
#         cnt *= (len(weardict[k])+1)
#     print(cnt-1)


# 11	1676	 팩토리얼 0의 개수
# from math import factorial
# N = factorial(int(input()))
#
# n = 10
# cnt = 0
# while True:
#     if N % n == 0:
#        cnt += 1
#     else:
#         break
#     n *= 10
# print(cnt)



# 12	2004	 조합 0의 개수
# n, m = map(int, input().split())
#
#
# def two_count(n):
#     two = 0
#     while n != 0:
#         n = n // 2
#         two += n
#     return two
#
# def five_count(n):
#     five = 0
#     while n != 0:
#         n = n // 5
#         five += n
#     return five
#
# print(min(two_count(n) - two_count(n - m) - two_count(m), five_count(n) - five_count(n - m) - five_count(m)))

