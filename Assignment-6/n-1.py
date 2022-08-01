# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
l = list(map(int,input().split()))
my_array = np.array(l)
print(np.reshape(my_array,(3,3)))
