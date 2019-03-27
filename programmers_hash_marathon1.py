def solution(participant, completion):
    completion.append('z'*5)
    completion.sort()
    participant.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p