def solution(numbers):
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            if int(numbers[j][0]) == int(numbers[j+1][0]):
                if int(numbers[j][-1]) < int(numbers[j+1][-1]):
                    (numbers[j], numbers[j+1]) = (numbers[j+1], numbers[j])
            elif int(numbers[j][0]) < int(numbers[j+1][0]):
                (numbers[j], numbers[j+1]) = (numbers[j+1], numbers[j])
    n = "".join(numbers)
    return n

numbers = [9, 5, 34, 3, 30]
print(solution(numbers))
