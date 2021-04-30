def main():
    from sys import stdin, stdout

    def is_valid(str1, str2):
        diff = 0
        for c1, c2 in zip(str1, str2):
            if c1 != c2:
                diff += 1
            if diff > 1:
                return False
        return True

    def build_dict(size):
        d = dict()
        for _ in range(size):
            key, value = stdin.readline().split()
            d[key] = value
        return d


    while True:
        n = int(stdin.readline())
        if n == 0:
            break

        original_signatures = build_dict(n)
        m = int(stdin.readline())
        class_signatures = build_dict(m)

        cheaters = 0
        for student in class_signatures:
            if not is_valid(original_signatures[student],class_signatures[student]):
                cheaters += 1

        stdout.write(f'{cheaters}\n')

main()
