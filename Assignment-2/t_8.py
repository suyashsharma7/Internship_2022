# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int,input().split()))
n = int(input())
b =  set(map(int,input().split()))

x = a.difference(b)
y=b.difference(a)
z = x.union(y)
z = list(z)
z.sort()
for i in z:
    print(i)
