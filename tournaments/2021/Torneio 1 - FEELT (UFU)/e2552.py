def main():
    while True:
        try:
            n, m = map(int, input().split())
        except Exception:
            break

        board = [list(map(int, input().split())) for _ in range(n)]
        cheesebreads = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if board[i][j]:
                    cheesebreads[i][j] = 9
                    continue
                cheesebreads[i][j] += 1 if j > 0     and board[i][j - 1] else 0
                cheesebreads[i][j] += 1 if j < m - 1 and board[i][j + 1] else 0
                cheesebreads[i][j] += 1 if i > 0     and board[i - 1][j] else 0
                cheesebreads[i][j] += 1 if i < n - 1 and board[i + 1][j] else 0

        for i in range(n):
            print(''.join(map(str, cheesebreads[i])))

main()
