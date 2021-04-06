def main():
    from re import compile
    pattern = compile('[^a-zA-Z]+')

    words = set()
    while True:
        try:
            line = input().strip().lower()
            line = pattern.sub(' ', line)
            for word in line.split():
                words.add(word)
        except Exception:
            break

    print('\n'.join(sorted(words)))

main()
