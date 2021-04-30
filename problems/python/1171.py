def main():
    from collections import defaultdict

    n = int(input())

    d = defaultdict(int)

    for _ in range(n):
        x = int(input())
        d[x] += 1

    for num in sorted(d):
        print(f'{num} aparece {d[num]} vez(es)')
main()
