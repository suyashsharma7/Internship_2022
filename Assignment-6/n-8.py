# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
n = int(input())
a=[]
b=[]
a = np.array([input().split() for _ in range(n)],dtype=np.int)
b = np.array([input().split() for _ in range(n)],dtype=np.int)
    
    
a=np.matrix(a)
b=np.matrix(b)
print(a*b)
