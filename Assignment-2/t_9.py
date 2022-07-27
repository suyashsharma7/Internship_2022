# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = set(map(int,input().split()))
b = int(input())
m = set(map(int,input().split()))
x = l.difference(m)
y = m.difference(l)
z=l.intersection(m)
print(len(x)+len(y)+len(z))