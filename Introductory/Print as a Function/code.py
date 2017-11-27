if __name__ == '__main__':
    n = int(input())
    m = list()
    for i in range(n):
        m.append(i+1);
    print(*m,sep='')
