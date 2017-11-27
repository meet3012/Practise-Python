if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scor1 = student_marks[query_name]
    scor1=list(scor1)
    avg = 0
    for i in range(3):
        avg += scor1[i]
    avg=avg/3;
    print('{0:.2f}'.format(avg))
