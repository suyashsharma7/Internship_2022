# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
a = np.array(input().split(), int)
b = np.array(input().split(), int)
print(np.inner(a,b), np.outer(a,b), sep='\n')
