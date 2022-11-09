def santa_users(array):
    d={x[0]: x[1] for x in array}
    return d
def formating(strin):
    strsplit= lambda x: x.strip().split(',')
    if len(strsplit(strin))>1:
        return strsplit(strin)[0],int(strsplit(strin)[1])
    else:
        return strin.strip(),None
def main():
    inp=list(input().split('],'))
    inp[-1]=inp[-1][:-2];  inp[0]=inp[0][1:]
    inp=[tuple([formating(x)[0][2:-1],formating(x)[1]]) for x in inp]
    print(santa_users(inp))
## как же геморно обрабатывать ввод массивов 
if __name__ =="__main__":
    main()
