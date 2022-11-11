from itertools import permutations
def main():
    print([list(map(int,x)) for x in permutations(input()[1:-1].split(','))])
if __name__=='__main__':
    main()