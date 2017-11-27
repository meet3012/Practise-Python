if __name__ == '__main__':
    N = int(input())
    A = list()
    for i in range(N):
        a = input().split()
        if a[0] == "insert":
            A.insert(int(a[1]),int(a[2]))
        elif a[0] == "print":
            print(A)
        elif a[0] == "remove":
            A.remove(int(a[1]));
        elif a[0] == "append":
            A.append(int(a[1]));
        elif a[0] == "sort":
            A.sort();
        elif a[0] == "pop":
            A.pop();
        else:
            A.reverse();
