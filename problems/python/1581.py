def main():
    for _ in range(int(input())):
        languages = set()
        for _ in range(int(input())):
            languages.add(input())
        print(languages.pop() if len(languages) == 1 else 'ingles')
main()
