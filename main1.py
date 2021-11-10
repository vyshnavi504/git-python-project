import math
n=int(input("enter number")
root=math.sqrt(n)
if int(root+0.5)**2==n:
    print(n,"Given no is perfect square...")
else:
    print(n,"is not perfect")