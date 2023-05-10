def main():
    N=int(input("Длина квадрата спирали: "))
    C=1
    n=1
    arr=[]
    for x in range(N):
        arr.append([])
        for j in range(N):
            arr[x].append(0)
    for x in range(N//2+1):
        for j in range(N):
            if arr[x][j]==0:
                arr[x][j]=n
                n+=1
        for j in range(N):
            if arr[j][N-x-1]==0:
                arr[j][N-x-1]=n
                n+=1
        for j in range(N):
            if arr[N-x-1][N-j-1]==0:
                arr[N-x-1][N-j-1]=n
                n+=1
        for j in range(N):
            if arr[N-j-1][x]==0:
                arr[N-j-1][x]=n
                n+=1
    for x in range(N):
        print(*arr[x])

if __name__=='__main__':
    main()