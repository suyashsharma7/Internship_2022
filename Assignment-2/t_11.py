# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
k = int(input())
l = list(map(int,input().split()))
ans=0
d = Counter(l)
for i in d:
    if d[i]==1:
        print(i)