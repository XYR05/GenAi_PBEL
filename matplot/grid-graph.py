import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([0,1,2,3,4,5])
y1 = np.array([30,60,90,120,150,180])
plt.title(" Sports Watch data")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.plot(x1, y1, "-o")
plt.grid()
plt.show()