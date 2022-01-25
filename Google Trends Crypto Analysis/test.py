import numpy as np 

x = [1,2,3,4,5,6,7,8]
y = [11,22,35,4,75,68,70,81]

w = np.corrcoef(x,y)
print(w)