import math
n=int(input("enter number")
root=math.sqrt(n)
if int(root+0.5)**2==n:
    print(n,"is a perfect")
else:
    print(n,"is not perfect")