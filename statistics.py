import sys
from collections import Counter

a = []
avg = 0

n = int(sys.stdin.readline())

for _ in range(n):
    temp = int(sys.stdin.readline())
    a.append(temp)

if len(a) == 1:
    print(a[0])
    print(a[0])
    print(a[0])
    print(0)
else:
    a.sort(reverse = False)

    # 산술평균
    avg = sum(a) / len(a)
    print(int(round(avg, 0)))

    # 중앙값
    b = int(len(a)/2)
    print(a[b])

    # 최빈값
    c = Counter(a)
    mode = c.most_common()
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])

    # 범위
    ran = max(a)-min(a)
    print(ran)

# 알고리즘 풀 때, input()보다는 sys.stdin.read()를 써서 시간초과 문제 해결할 것