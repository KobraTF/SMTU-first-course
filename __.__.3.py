def main():
    s=input()
    flag=True
    arr=[]
    arr2=[]
    opening='([{'
    closing=')]}'

    if flag:
        x=0
        o=''
        f=True
        right=''
        while True:
            if s=='':
                break
            elif s[x] in opening:
                o+=closing[opening.find(s[x])]
                f=True
            elif o!='' and s[x]==o[-1]:
                if f:
                    right+=opening[closing.find(s[x])]+s[x]
                else:
                    right=opening[closing.find(s[x])]+right+s[x]
                s=s[:x-1]+s[x+1:]
                o=o[:len(o)-1]
                f=False
                x-=2
            else:
                arr.append(right)
                arr2.append(len(right))
                s=s[x+1:]
                o=''
                right=''
                x=0
                flag=False
                continue
            x+=1
            if x==len(s):
                break
        if flag:
            print(right)
        else:
            print(arr[arr2.index(max(arr2))])

if __name__=='__main__':
    main()