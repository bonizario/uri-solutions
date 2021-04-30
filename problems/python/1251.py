def main():
    from collections import defaultdict
    from operator import itemgetter

    ascii_codes = [-ord(char) for char in input().strip()]

    while True:
        counter = defaultdict(int)
        for ascii_code in ascii_codes:
            counter[ascii_code] += 1

        sorted_characters = sorted(counter.items(), key=(itemgetter(1, 0)))

        for ascii_code, frequency in sorted_characters:
            print(f'{-ascii_code} {frequency}')

        try:
            ascii_codes = [-ord(char) for char in input().strip()]
            print()
        except Exception:
            break

main()
