X = int(input())
cnt = 0
for i in range(1, X + 1):
    if X % i == 0:
        cnt = cnt+1
        print(cnt)