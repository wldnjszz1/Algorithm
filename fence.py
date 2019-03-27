def solve(left, right):
    if (left == right) : 
        return h[left]
    mid = (left + right) // 2
    max_width = max( solve(left, mid), solve(mid+1, right) )
    lo , hi = mid , mid+1
    height = min(h[lo],h[hi])
    max_width = max(max_width, height*2) # [mid,mid+1]만 포함하는 너비 2인 사각형 고려
    while(left < lo or hi < right):
        if(hi < right and (lo == left or h[lo-1] < h[hi+1])):
            hi += 1
            height = min(height,h[hi])
        else:
            lo -= 1
            height = min(height,h[lo])
        max_width = max(max_width,height*(hi-lo+1))
    return max_width

if __name__ == "__main__":
    h = []
    for _ in range(int(input('테스트 케이스의 수를 입력하세요 : '))):
        wood_num = int(input('판자의 개수를 입력하세요 : '))
        h = (','.join(input('판자의 각 높이를 입력하세요 : ')).split(','))
        for a in range(len(h)):
            h[a] = int(h[a])
    print(solve(0,len(h)-1))
        
