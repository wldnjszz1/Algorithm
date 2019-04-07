def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        for j in range(len(numbers)-i-1):
            if numbers[j] < 10 and numbers[j+1] < 10:
                if numbers[j] > numbers[j+1]:
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            elif numbers[j] >= 10 or numbers[j+1] >= 10:
                if numbers[j] >= 10 and numbers[j+1] >= 10:
                    if (numbers[j]//10) > (numbers[j+1]//10):
                        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    elif (numbers[j]//10) == (numbers[j+1]//10):
                        if (numbers[j]%10) > (numbers[j+1]%10):
                            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                elif numbers[j] >= 10:
                    if (numbers[j]//10) > numbers[j+1]:
                        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    elif (numbers[j]//10) == numbers[j+1]:
                        if (numbers[j]%10) > numbers[j+1]:
                            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]                        
                elif numbers[j+1] >= 10:
                    if numbers[j] > (numbers[j+1]//10):
                        numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                    elif numbers[j] == (numbers[j+1]//10):
                        if numbers[j] > (numbers[j+1]%10):
                            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]                        

    numbers.reverse()
    numbers = list(map(str, numbers))
    answer = ''.join(numbers)
    return answer

numbers = [6, 10, 2]
print(solution(numbers))
