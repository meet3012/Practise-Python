if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l = list(set(arr))
    
    maximum = max(l)
    for i in l:
        if i == maximum:
            l.remove(i)
            continue
    
    print(max(l))
