def main():
    from operator import itemgetter
    while True:
        try:
            n = int(input())
        except EOFError:
            break
        meats = []
        for _ in range(n):
            meat, date = input().split()
            meats.append((meat, int(date)))
        meats.sort(key=itemgetter(1))
        print(' '.join(map(itemgetter(0), meats)))
main()
