# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m = map(int,input().split())
l = []
for i in range(n):
    a = list(map(int,input().split()))
    l.append(a)

my_array = numpy.array(l)
print(numpy.transpose(my_array))
print(my_array.flatten())    
