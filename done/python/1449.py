def main():
    for _ in range(int(input())):
        total_dictionary_words, total_song_lines = map(int, input().split())
        dictionary = dict()

        for _ in range(total_dictionary_words):
            line = input()
            translated_line = input()
            dictionary[line] = translated_line

        for _ in range(total_song_lines):
            line = input().split()
            words = [dictionary[word] if word in dictionary else word for word in line]
            print(' '.join(words))

        print()
main()
