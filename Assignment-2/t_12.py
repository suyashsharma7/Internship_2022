# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    n = int(input())
    a = set(map(int,input().split()))
    m = int(input())
    b = set(map(int,input().split()))   
    if len(a)>len(b):
        print('False')
    elif len(a.difference(b))==0:
        print('True')
    else:
        print('False')
