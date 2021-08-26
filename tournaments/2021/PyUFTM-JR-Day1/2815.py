text = input().split()
for i, word in enumerate(text):
    if len(word) >= 4 and word[0:2] == word[2:4]:
        text[i] = word[2:]
print(' '.join(text))
