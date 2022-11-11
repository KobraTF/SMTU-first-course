from itertools import combinations
def main():
    N=int(input()[4:])
    del N
    arr=[[sum(list(map(int,x))),list(map(int,x))] for x in combinations(input()[1:-1].split(','),4)]
    C=int(input()[4:])
    res=[2*100,[]]
    #print(N,C,arr[])
    for x in arr:
        if res[0]>abs(C-x[0]):
            res=[abs(C-x[0]),x]
    print(res[1][1])
    print(res[1][0])

if __name__=='__main__':
    main()