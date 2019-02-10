def brute_force(h):
    max_width = 0
    total_length = len(h)
    for left in range(total_length):
        min_height = h[left]
        for right in range(left,total_length):
            min_height = min(min_height,h[right])
            max_width = max(min_height*(right-left+1),max_width)
    return max_width


if __name__ == "__main__":
    h = []
    for _ in range(int(input('테스트 케이스의 수를 입력하세요 : '))):
        wood_num = int(input('판자의 개수를 입력하세요 : '))
        h = (','.join(input('판자의 각 높이를 입력하세요 : ')).split(','))
        for a in range(len(h)):
            h[a] = int(h[a])
    print(brute_force(h))
        

            
            
