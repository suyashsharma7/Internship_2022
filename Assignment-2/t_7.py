# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().split())
l = list(map(int,input().split()))
a = set(map(int,input().split()))
b= set(map(int,input().split()))
c = 0 


for i in l:
    if i in a:
        c+=1
    elif i in b:
        c-=1
print(c)
