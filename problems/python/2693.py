def main():
    from operator import itemgetter
    while True:
        try:
            total_students = int(input())
        except EOFError:
            break
        students = []
        for _ in range(total_students):
            name, region, distance = input().split()
            students.append((name, region, int(distance)))
        students.sort(key=itemgetter(2, 1, 0))
        print('\n'.join(map(itemgetter(0), students)))
main()
