from audioop import reverse


def main():
    arr=list(*[[list(z) for z in list(set([tuple(sorted([s[i] for i in range(len(s)) if all ([char in s[i] and (len(s[n])==len(s[i])) and all([char2 in s[n] for char2 in (' '.join(s[i]).split())]) for char in (' '.join(s[n]).split())])])) for n in range(len(s))]))] for s in [[x[1:-1] for x in list(input()[1:-1].split(','))]]])
    for x in range(len(arr)):
        if '' in arr[x]:
            c=arr[x].count('')
            while arr[x].count('')==c:
                arr[x].pop()
            arr[x].append('')
    print(arr)

if __name__=="__main__":
    main()