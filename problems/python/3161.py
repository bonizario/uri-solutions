def main():
    n, m = map(int, input().split())
    fruits = dict()

    for _ in range(n):
        fruits[input().strip().lower()] = False

    hacked_list = [input().strip().lower() for _ in range(m)]

    for line in hacked_list:
        for fruit in fruits:
            if fruit in line or fruit in line[::-1]:
                fruits[fruit] = True

    for fruit in fruits:
        print(f'Sheldon {"come" if fruits[fruit] else "detesta"} a fruta {fruit}')

main()
