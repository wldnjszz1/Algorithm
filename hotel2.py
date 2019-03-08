for _ in range(int(input())):
    h, w, n = map(int, input().split())

    room = [[0]*h for i in range(w)]

    for i in range(w):
        for j in range(h):
            room[i][j] = (j+1)*100 + (i+1)


    if n%h == 0:
        print(room[n//h-1][5])
    else:
        print(room[n//h][n%h-1])
