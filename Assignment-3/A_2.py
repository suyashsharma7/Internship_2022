# Enter your code here. Read input from STDIN. Print output to STDOUT\
import math
AB = int(input())
BC= int(input())
CA = math.sqrt(AB**2+BC**2)
angle = math.acos(BC/CA)
theta = round(math.degrees(angle))
print(str(theta)+chr(176))
