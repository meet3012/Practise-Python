if __name__ == '__main__':
    A = list()
    s=list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l = list()
        l.append(name)
        l.append(score)
        if score not in s:
            s.append(score)
        A.append(l)
    s.sort()
    A.sort()
    for i in range(len(A)):
        if(s[1]==A[i][1]):
            print(A[i][0])
