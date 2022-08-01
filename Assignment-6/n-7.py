# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
arr=[]
n,m=map(int,input().split())
for i in range(n):
    l=list(map(int,input().split()))
    arr.append(l)
my_array=numpy.array(arr)
result=numpy.min(my_array, axis = 1)
print(max(result))
