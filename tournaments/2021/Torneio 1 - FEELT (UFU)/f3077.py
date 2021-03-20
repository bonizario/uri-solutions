def main():
    n, k = map(int, input().split())
    s = tuple(map(int, input().split()))

    full_sums_quantity = k // n

    rest = (k % n) if full_sums_quantity else 1

    base_sum = full_sums_quantity * sum(s)

    remain = k if not full_sums_quantity else rest

    s = tuple(reversed(s * (rest + 2)))

    workers = [base_sum] * n

    for i in range(n):
        workers[i] += sum(s[i:i+remain])

    print(' '.join(map(str, reversed(workers))))

main()
