# 1978
# N = int(input())
#
# input_list = list(map(int, input().split()))
# prime_count = 0
# for prime in input_list:
#     k = 0
#     if prime == 1:
#         continue
#
#     for j in range(2, prime):
#         if prime % j == 0:
#             k = 1
#
#     if k == 0:
#         prime_count += 1
# print(prime_count)

# 2581
# def prime_dis(a):
#     k = 0
#
#     if a == 1:
#         return 0
#
#     for j in range(2, a):
#         if a % j == 0:
#             k = 1
#
#     if k == 0:
#         return 1
#     else:
#         return 0
#
#
# M = int(input())
# N = int(input())
#
# prime_list = []
# for i in range(M, N + 1):
#     if prime_dis(i) == 1:
#         prime_list.append(i)
#
# if len(prime_list) == 0:
#     print(-1)
# else:
#     print(sum(prime_list))
#     print(min(prime_list))

# 11653
# def prime_dis(a):
#     k = 0
#     if a == 1:
#         return 0
#     for j in range(2, a):
#         if a % j == 0:
#             k = 1
#     if k == 0:
#         return 1  # 소수
#     else:
#         return 0  # 합성수
#
#
# N = int(input())
# soinsu = []
# while prime_dis(N) == 0:
#     for i in range(2, N):
#         if N % i == 0:
#             soinsu.append(i)
#             N = N // i
#             break
# soinsu.append(N)
# for i in soinsu:
#     print(i)

# 2) 간 단 한 풀 이
# N = int(input())
# m = 2
# while N != 1:
#     if N % m == 0:
#         print(m)
#         N = N/m
#     else:
#         m += 1


# 1929
# def is_prime(a):
#     if a == 1:
#         return 0
#     else:
#         for j in range(2, int(a ** 0.5) + 1):
#             if a % j == 0:
#                 return 1
#         return 0
#
#
# M, N = map(int, input().split())
#
# prime_list = []
# for i in range(M, N + 1):
#     if is_prime(i) == 1:
#         print(i)

# 4948
# def sosu(n):
#     if n ==1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True							#소수 구하는 방식은 위와 같다
#
# all_list = list(range(2,246912))		#문제에서 제한한 범위
# memo = []								#for문 밖에 리스트 정의
#
# for i in all_list:						#2부터 2*123,456 범위
#     if sosu(i):							#sosu함수에 해당하면
#         memo.append(i)					#리스트에 추가
#
# n = int(input())
#
# while True:
#     count=0					#갯수를 세야하는 조건 때문에 카운트
#     if n == 0 :
#             break
#     for i in memo:			#memo리스트 중에서
#         if n < i <=2*n:		#입력한 값의 범위 내에서 값이 있으면
#             count+=1		#있을 때 마다 카운트 +1
#     print(count)
#     n = int(input())		#0 입력받기 전까지 계속 해야하므로 입력 받음



# 9020
# def isPrime(n):
#     if n ==1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
#
# for _ in range(int(input())):
#     num = int(input())
#
#     a, b = num//2, num//2
#     while a > 0:
#         if isPrime(a) and isPrime(b):
#             print(a, b)
#             break
#         else:
#             a -= 1
#             b += 1