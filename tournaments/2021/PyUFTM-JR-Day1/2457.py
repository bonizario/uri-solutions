letter = input()
text = input().split()
total = sum(1 for word in text if letter in word)
print(f'{(total / len(text) * 100):.1f}')
