from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(str, numbers))
    newnumber = ''
    answer = list()
    for i in range(len(numbers)):
        number = numbers.copy()
        del number[i]
        newnumber = numbers[i]
        for n in number:
            print(n)
            newnumber += n
            print(newnumber)
        answer.append(newnumber)
        number.reverse()
        newnumber = numbers[i] 
        for n in number:
            newnumber += n
        answer.append(newnumber)
    answer.sort()
    return answer

numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
