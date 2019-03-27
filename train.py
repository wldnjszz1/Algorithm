import sys

train = list()
train = [[0]*2 for a in range(4)]
recent = 0
ppl = 0
for i in range(len(train)):
    train[i][0], train[i][1] = sys.stdin.readline().split()    
    if recent == 0:
        recent = int(train[i][1]) - int(train[i][0])
    else:
        recent = recent + int(train[i][1]) - int(train[i][0])
    ppl = max(recent, ppl)
print(ppl)    