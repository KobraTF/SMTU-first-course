from math import factorial,comb
def main():
    n,k=map(int,input().split(","))
    ## n-конфет по k-пакетам
    S=0
    for j in range(k+1):
        S+=((-1)**(k+j))*comb(k,j)*(j**n)
    print(S//factorial(k))
if __name__ =='__main__':
    main()