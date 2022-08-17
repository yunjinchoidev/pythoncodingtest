A = int(input())
N = int(input())
sum = 0

for i in range(N):
    x, y = map(int, input().split())
    sum += x*y

if sum == A:
    print("Yes")
else:
    print("No")

