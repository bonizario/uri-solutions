def main():
    encoded = input().split()
    print(' '.join((word[1::2] for word in encoded)))
main()
