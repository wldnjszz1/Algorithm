import sys

def merge(a):

    if len(a) <= 1:
        return a

    mid = len(a)//2
    left = merge(a[:mid])
    right = merge(a[mid:])

    i, j, k = 0, 0, 0
    while len(left) > i and len(right) > j:
        if left[i] >= right[j]:
            a[k] = right[j]
            j+=1
        elif left[i] < right[j]:
            a[k] = left[i]
            i+=1
        k+=1
    while len(left) > i:
        a[k] = left[i]
        k +=1
        i +=1
    while len(right) > j:
        a[k] = right[j]
        k +=1
        j +=1
    return a

a = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    a.append(num)

merge(a)
for _ in range(len(a)):
    sys.stdout.
