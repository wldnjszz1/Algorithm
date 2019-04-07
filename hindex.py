def solution(citations):
    if len(citations) == 1 and citations[0] == 0:
        return 0
    cache = [[0]*2 for i in range(len(citations))]
    for i in range(len(cache)):
        count = 0
        ccount = 0
        for j in range(len(cache)):
            if i+1 <= citations[j]:
                count += 1
            else:
                ccount += 1
        cache[i][0] = count
        cache[i][1] = ccount
    for i in range(len(cache)):
        if i+1 == cache[i][0]:
            return cache[i][0]

citations = [3, 3, 3, 4, 4, 5, 5, 5]
print(solution(citations))


# 정확성 : 87.5
