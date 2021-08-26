print('Y' if [a + b for a, b in zip(map(int, input().split()), map(int, input().split()))] == [1,1,1,1,1] else 'N')
