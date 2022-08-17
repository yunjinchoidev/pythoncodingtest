# 11654
# a = input()
# print(ord(a))

# 11720
# n = input()
#
# print(sum(map(int,input())))

# 10809
# word = input()
# alphabet = list(range(97,123))  # 아스키코드 숫자 범위
#
# for x in alphabet :
#     print(word.find(chr(x)), end=' ')

# 2675
# N = int(input())
#
# for i in range(N):
#     A, B = input().split()
#     A = int(A)
#     B = list(B)
#     text = ""
#     for j in B:
#         text += A * j
#     print(text)

# 1157
# word = input().upper()
# unique_list = list(set(word))
# top = []
# for i in unique_list:
#     cnt = word.count(i)
#     top.append(cnt)
#
# if top.count(max(top)) > 1:
#     print('?')
# else :
#     max_indx = top.index(max(top))
#     print(unique_list[max_indx])

# 1152
# word_list = list(map(str, input().split()))
# print(len(word_list))

# 2908
# A, B = input().split()
# A = int(A[::-1])
# B = int(B[::-1]) # 역순으로 바꿔주기
# if A > B:
#     print(A)
# else:
#     print(B)


# 5622
# words = list(input())
# dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# time = 0
# for i in words:
#     for j in dial:
#         if i in j:
#             time += dial.index(j)+3
# print(time)

# 2941
# words = input()
# croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# count = 0
#
# for i in croatia:
#     words = words.replace(i, '*')
# print(len(words))


# 1316
# n = int(input())
#
# group_word = 0
# for _ in range(n):
#     word = input()
#     error = 0
#     for index in range(len(word)-1):
#         if word[index] != word[index+1]:
#             new_word = word[index+1:]
#             if new_word.count(word[index]) > 0:
#                 error += 1
#     if error == 0:
#         group_word += 1
# print(group_word)










