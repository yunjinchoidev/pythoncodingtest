# 1085	 직사각형에서 탈출
# x, y, w, h = map(int, input().split())
# print(min(x, y, w-x, h-y))

# 3009	 네 번째 점	다국어
# x_ = []
# y_ = []
# for i in range(3):
#         x, y = map(int, input().split())
#         x_.append(x)
#         y_.append(y)
# for i in range(3):
#         if x_.count(x_[i]) == 1:
#                 x = x_[i]
#         if y_.count(y_[i]) == 1:
#                 y = y_[i]
# print(x, y)


# 4153	 직각삼각형	다국어
# while True:
#     input_list = list(map(int, input().split()))
#     if input_list[0]==0 and input_list[1]==0 and input_list[2]==0:
#         break
#
#     max_num = max(input_list)
#     input_list.remove(max_num)
#
#     if max_num**2 == input_list[0]**2 + input_list[1]**2:
#         print("right")
#     else:
#         print("wrong")

# 2477	 참외밭
# K = int(input())
# max_height = 0  # 가장 긴 높이를 저장할 변수
# max_width = 0  # 가장 긴 가로길이를 저장할 변수
# max_width_index = 0  # 가장 긴 가로길이의 인덱스를 저장할 변수
# max_height_index = 0  # 가장 긴 높이의 인덱스를 저장할 변수
# info = []  # 변의 정보들을 저장할 리스트
# for i in range(6):
#     temp = list(map(int, input().split()))
#     info.append(temp)
#     if temp[0] == 1 or temp[0] == 2:  # 만약 가로 길이라면
#         if max_width < temp[1]:  # 해당 길이가 가장 길다면
#             max_width = temp[1]  # 그 길이를 가장긴 가로로 저장한 후
#             max_width_index = i  # 그에 해당하는 인덱스를 저장
#     else:
#         if max_height < temp[1]:  # 해당 길이가 가장 길다면
#             max_height = temp[1]  # 그 길이를 가장긴 세로로 저장한 후
#             max_height_index = i  # 그에 해당하는 인덱스를 저장
#
# # 그 후 가장 긴 가로 및 세로와 인접한 변 2개와 가장긴 가로와 세로 총 4개를 새로운 리스트에 저장한다.
# index_list = [info[max_height_index - 1], info[(max_height_index + 1) % 6], info[max_width_index - 1],
#               info[(max_width_index + 1) % 6]]
#
# product = 1  # 곱을 저장할 변수
# for i in info:  # 입력받은 변들 중에
#     if i not in index_list:  # 만약 새로운 리스트에 저장한 변 4개 중에 없다면 빈 사각형이므로
#         product *= i[1]  # 그 넓이를 변수에 저장한다.
#
# result = (max_width * max_height - product) * K  # 전체 큰 직사각형 넓이에서 빈 사각형 넓이를 빼준 후 K를 곱한다.
# print(result)


# 3053	택시 기하학
# import math
#
# r = int(input())
# print(r*r*math.pi)
# print(r*r*2)

# 1002	 터렛
# import math
#
# n = int(input())
#
# for _ in range(n):
#     x1, y1, r1, x2, y2, r2 = map(int, input().split())
#     distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)  # 두 원의 거리 (원의방정식활용)
#     if distance == 0 and r1 == r2 :  # 두 원이 동심원이고 반지름이 같을 때
#         print(-1)
#     elif abs(r1-r2) == distance or r1 + r2 == distance:  # 내접, 외접일 때
#         print(1)
#     elif abs(r1-r2) < distance < (r1+r2) :  # 두 원이 서로다른 두 점에서 만날 때
#         print(2)
#     else:
#         print(0)  # 그 외에

# 1004	 어린 왕자
# t = int(input())
# for i in range(t):
#     cnt = 0
#     x1, y1, x2, y2 = map(int, input().split())
#     n = int(input())
#     for i in range(n):
#         px, py, pr = map(int, input().split())
#         d1 = (((x1 - px) ** 2) + ((y1 - py) ** 2)) ** 0.5
#         d2 = (((x2 - px) ** 2) + ((y2 - py) ** 2)) ** 0.5
#         if (d1 < pr and d2 > pr) or (d1 > pr and d2 < pr):
#             cnt += 1
#     print(cnt)

# 1358	 하키
# import sys
#
# input = sys.stdin.readline
#
# W, H, X, Y, P = map(int, input().split())
# count = 0
# for _ in range(P):
#     x, y = map(int, input().split())
#
#     # 가운데 직사각형 내부에 있는 경우(둘레 포함)
#     if (X <= x <= X + W) and (Y <= y <= Y + H):
#         count += 1
#         continue
#
#     # 왼쪽 반원, 오른쪽 반원 내부에 있는 경우(둘레 포함)
#     R = H / 2
#     d1 = ((x - X) ** 2 + (y - (Y + R)) ** 2) ** 0.5
#     d2 = ((x - (X + W)) ** 2 + (y - (Y + R)) ** 2) ** 0.5
#     if d1 <= R or d2 <= R:
#         count += 1
#
# print(count)



