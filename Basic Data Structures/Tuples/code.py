if __name__ == '__main__':
    n = int(input())
    a = input().split();
    for i in range(len(a)):
        a[i]=int(a[i]);
    print(hash(tuple(a)))
