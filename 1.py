X = int(input()) # N целых чисел
cnt = 0
for i in range(1, X + 1):
    N = int(input()) # целое число
    if N == 0:
        cnt += 1
        print(cnt, "чисел равных нулю")