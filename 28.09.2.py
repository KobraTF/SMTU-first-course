def main():
    s=input().strip().split()
    print(str(s[len(s)-1]).capitalize().replace(' ',''),end=' ')
    for x in range(2,len(s)):
        print(str(s[-x]).lower().replace(' ',''), end=' ')
    if len(s)>1:
        print(str(s[0]).lower().replace(' ',''))
if __name__=='__main__':
    main()