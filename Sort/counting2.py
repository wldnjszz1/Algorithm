import sys

n = int(sys.stdin.readline())
cache = [0]*10001

for i in range(n):
    a = int(sys.stdin.readline())
    cache[a] += 1

for i in range(len(cache)):
    if cache[i] > 0:
        for c in range(cache[i]):
            print(i)