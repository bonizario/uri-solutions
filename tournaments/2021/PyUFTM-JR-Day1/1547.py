for _ in range(int(input())):
    qt, s = map(int, input().split())
    raffle = list(map(lambda x: abs(int(x) - s), input().split()))
    print(raffle.index(min(raffle)) + 1)
