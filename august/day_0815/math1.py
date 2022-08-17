# 1712
# A, B, C = map(int, input().split())
#
# if B >= C:
#     print(-1)
# else:
#     print(int(A/(C-B))+1)


# 2292
# N = int(input())
#
# room_count =1
# six_check = 6
# total = 1
# while N > total:
#     room_count += 1
#     total += six_check
#     six_check += 6
# print(room_count)

# 1193
# n = int(input())
#
# line = 0
# end = 0
# while n > end:
#     line += 1
#     end += line
#
# diff = end - n
# if line%2 == 0: #짝수 라인 일때
#     top = line - diff
#     bottom = diff + 1
# else:
#     top = diff + 1
#     bottom = line - diff
#
# print("%d/%d"%(top,bottom))


# 2869
# A, B, V = map(int, input().split())
#
# n = (V - B)/(A-B)
# if int(n) < n:
#
#     print(int(n)+1)
# else:
#     print(int(n))


# 10250
# T = int(input())
#
# for i in range(T):
#     H, W, N = map(int, input().split())
#
#     height = H*100 if N % H == 0 else (N % H)*100
#
#     horizon = N // H if N % H == 0 else N // H + 1
#     print(height+horizon)

# 2775 # 부녀 회장이 될꺼야
# def knho(k, n):
#     if k == 0:
#         return n
#
#     r = 0
#     for i in range(1, n + 1):
#         r += knho(k - 1, i)
#     return r
#
#
# T = int(input())
# for i in range(T):
#     K = int(input())
#     N = int(input())
#     print(knho(K,N))

# 2839

sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :
        bag += (sugar // 5)
        print(bag)
        break
    sugar -= 3
    bag += 1
else :
    print(-1)

# 10757
