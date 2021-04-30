def main():
    longest_word, longest_word_size = '', 0
    while True:
        words = input()
        if words == '0':
            break
        lengths = tuple(map(lambda w: str(len(w)), words.split()))
        curr_word = max(words.split(), key=len)
        curr_size = len(curr_word)
        if curr_size >= longest_word_size:
            longest_word, longest_word_size = curr_word, curr_size
        print('-'.join(lengths))
    print(f'\nThe biggest word: {longest_word}')
main()
