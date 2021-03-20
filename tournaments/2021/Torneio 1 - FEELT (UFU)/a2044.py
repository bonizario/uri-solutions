def main():
    while True:
        n = int(input())
        if n == -1:
            break
        prices = list(map(int, input().split()))
        visits = 0
        current_debt = 0
        for price in prices:
            current_debt += price
            if current_debt % 100 == 0:
                visits += 1
                current_debt = 0
        print(visits)
main()
