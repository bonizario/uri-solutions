while True:
    try:
        first, *middle, last = list(map(len, input().split('x')))
    except EOFError:
        break
    print(max(first, last, *map(lambda length: length // 2, middle)))
