diameter = int(input())
print('S' if all(side >= diameter for side in map(int, input().split())) else 'N')
