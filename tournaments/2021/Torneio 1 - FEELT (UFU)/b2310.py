def main():
    total = [0, 0, 0]
    successful = [0, 0, 0]
    for _ in range(int(input())):
        input().strip()
        total = [x + y for x, y in zip(total, map(int, input().split()))]
        successful = [x + y for x, y in zip(successful, map(int, input().split()))]
    print(f'Pontos de Saque: {(successful[0] / total[0] * 100):.2f} %.')
    print(f'Pontos de Bloqueio: {(successful[1] / total[1] * 100):.2f} %.')
    print(f'Pontos de Ataque: {(successful[2] / total[2] * 100):.2f} %.')
main()
