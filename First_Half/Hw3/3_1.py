from itertools import combinations
def main():
    N=int(input("N = "))
    del N
    arr=[
        [sum(list(map(int,x))),    list(map(int,x))] 
        for x in combinations(input().strip()[1:-1].split(','),4)
        ]
    C=int(input("C = "))
    res=[2*100,[]]
    #print(C,arr)
    for x in arr:
        if res[0]>abs(C-x[0]):
            res=[abs(C-x[0]),x]
    print(res[1][1])
    print(res[1][0])

if __name__=='__main__':
    main()