from itertools import permutations
def main():
    arr=[]
    for x in permutations(input('Введите список формата [x1,x2,x3]: ')[1:-1].split(',')):
        if list(map(int,x)) not in arr:
            arr.append(list(map(int,x)))
    print(arr)
if __name__=='__main__':
    main()