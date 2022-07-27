# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int,input().split()))
n = int(input())
ans = True
for i in range(n):
    b = set(map(int,input().split())) 
    
    if b.issubset(a) and not a.issubset(b):
        flag = True
    else:
        flag = False
    ans=ans&flag
print(ans)