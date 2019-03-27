import sys

n = int(sys.stdin.readline())
a = list()
c = list()
for i in range(n):
    a = [0]*(i+1)
    c = [0]*(i+1)

for i in range(n):
    a[i] = int(sys.stdin.readline())

for i in a:
    counting = 0
    for b in a:
        if i > b:
            counting += 1        
    if c[counting]:
        c[counting+1] = i
    c[counting] = i

for i in c:
    print(i)
    
