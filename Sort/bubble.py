a = list()

for _ in range(int(input())): 
    a.append(input())

for i in range(len(a)):
    for j in range(len(a)-i-1):
        if int(a[j]) > int(a[j+1]):
            a[j], a[j+1] = a[j+1], a[j]

for i in range(len(a)):
    print(a[i])


    
# append는 str type만 가능. str끼리 비교하면 제대로 비교 안됨
