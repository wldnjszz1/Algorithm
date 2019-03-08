for _ in range(int(input())):
    h, w, n = map(int, input().split())

    if n%h == 0:
        y = h * 100
        x = n//h
    else:    
        y = (n % h) * 100
        x = ( n // h ) + 1

    print(y+x)

