# 2739
# A = int(input())
# for i in range(1,10):
#     print(A, "*", i, "=", A * i)

# 10950
# N = int(input())
#
# for i in range(N):
#     A, B = map(int, input().split())
#     print(A+B)

# 8393
# N = int(input())
# sum = 0
# for i in range(1,N+1):
#     sum += i
#
# print(sum)


# 25304
# total = int(input())
# N = int(input())
#
# sum = 0
# for _ in range(N):
#     A, B = map(int, input().split())
#     sum += A*B
#
# if total == sum:
#     print("Yes")
# else:
#     print("No")

# 15552
# import sys
#
# inp = int(input())
# for i in range(inp):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a + b)

# 11021
# import sys
#
# N = int(input())
#
# for i in range(1, N + 1):
#     A, B = map(int, sys.stdin.readline().split())
#     print(f"Case #{i}: {A+B}")

# 11022
# import sys
#
# N = int(input())
#
# for i in range(1, N + 1):
#     A, B = map(int, sys.stdin.readline().split())
#     print(f"Case #{i}: {A} + {B} = {A+B}")


# 2438
# N = int(input())
#
# for i in range(1, N+1):
#     print("*"*i)

# 2439
# N = int(input())
#
# for i in range(1, N + 1):
#     print(" " * (N - i)+ "*" * i)

# 10871
# A, B = map(int, input().split())
# input__list = list(map(int, input().split()))
#
# for i in range(A):
#     if input__list[i] < B:
#         print(input__list[i], end=" ")

# 10952
# while True:
#     try:
#         A, B = map(int, input().split())
#         print(A+B)
#     except:
#         break

# 1110
A = int(input())
B = 0
C = 0
count = 0

while True:
     if count == 0:
         B=A
     C1 = (B//10) + B % 10
     C2 = (B%10)*10 + C1%10
     count += 1
     B = C2
     if A == C2 :
         break
print(count)


