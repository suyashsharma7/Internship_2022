# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m = map(int,input().split())
numpy.set_printoptions(legacy='1.13')
print(numpy.eye(n, m))
