cards = list(map(int, input().split()))
if cards == sorted(cards):
    print('C')
elif cards == sorted(cards, reverse=True):
    print('D')
else:
    print('N')
