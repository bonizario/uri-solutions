def main():
    while True:
        n = int(input())
        if not n:
            break
        d = dict()
        for _ in range(n):
            message, year, time_to_receive = input().split()
            message = message.strip()
            year, time_to_receive = int(year), int(time_to_receive)
            d[year - time_to_receive] = message
        print(d[min(d)])
main()
