A, B = map(int, input().split())

if A != 0 and B >=45:
    print(A , B-45)
elif A !=0 and B <45:
    print(A-1,15+B)
elif A ==0 and B>=45:
    print(0, B-45)
else:
    print(23,15+B)