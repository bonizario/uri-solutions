for _ in range(int(input())):
    m = int(input())
    grades = list(map(int, input().split()))
    ordered = sorted(grades, reverse=True)
    print(sum(1 for i in range(m) if grades[i] == ordered[i]))
