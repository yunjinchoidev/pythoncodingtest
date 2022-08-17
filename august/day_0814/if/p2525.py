A, B = map(int, input().split())
plus = int(input())

sum = B + plus

if(sum >= 60):
    A += sum/60
    B = sum%60
else:
    B = sum

print(int(A)%24, B, end=' ')
