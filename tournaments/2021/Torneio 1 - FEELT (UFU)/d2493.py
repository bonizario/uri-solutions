def main():
    while True:
        try:
            t = int(input())
        except Exception:
            break

        players = dict()
        expressions = []

        for i in range(t):
            entry = input()
            x, y, z = int(entry[0]), int(entry[2]), int(entry[4])
            expressions.append((x, y, z))

        for _ in range(t):
            name, index, operation = input().split()
            expression = expressions[int(index) - 1]
            players[name] = False
            if operation == '+':
                if expression[0] + expression[1] == expression[2]:
                    players[name] = True
            elif operation == '-':
                if expression[0] - expression[1] == expression[2]:
                    players[name] = True
            elif operation == '*':
                if expression[0] * expression[1] == expression[2]:
                    players[name] = True
            elif operation == 'I':
                if expression[0] + expression[1] != expression[2] and \
                   expression[0] - expression[1] != expression[2] and \
                   expression[0] * expression[1] != expression[2]:
                    players[name] = True

        if sum(players.values()) == t:
            print('You Shall All Pass!')
        else:
            losers = []
            for name in players:
                if not players[name]:
                    losers.append(name)
            if len(losers) == t:
                print('None Shall Pass!')
            else:
                print(' '.join(sorted(losers)))

main()
