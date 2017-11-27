# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input());
A = set()
B = set()
sum1=0;
A = input();
#print(A)
A = A.split(" ");
#print(A)

for i in range(n):
    A[i]=int(A[i]);
A = set(A)
#print(A)


#print(A);

op = int(input());
for i in range(op):
    a = input().split(' ');
    B = input();
    B = B.split(" ");

    for i in range(int(a[1])):
        B[i]=int(B[i]);
    B = set(B)
    #print(B)
    
    #print(a);
    b=a[0];
    if( b == "intersection_update"):
        A.intersection_update(B);
        
    elif(b == "update"):
        A.update(B);
    elif(b == "symmetric_difference_update"):
        A.symmetric_difference_update(B);
    else:
        A.difference_update(B);
    #print(A)
    
for i in range(len(A)):
    #sum = sum + int(A[i])
    sum1 = sum(A);
print(sum1);
