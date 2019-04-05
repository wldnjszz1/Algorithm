def solution(phone_book):
    f = 0
    pb = phone_book.copy()
    for i in range(len(pb)):
        del pb[i]
        for number in pb:
            if phone_book[i] in number:
                print(phone_book[i], number)
                f += 1
        pb = phone_book.copy()
    if f !=0 :
        answer = False
    else:
        answer = True
    return answer
a = ['12','123','1235','567','88']
print(solution(a))

# 정확성 60


