import matplotlib.pyplot as plt
import numpy as np
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

x=np.array([1,2,3,4])
y=np.array([1,4,9,16])
plt.plot(x,y, '--o')
plt.show()


y=np.array([1,4,9,16])
plt.plot(y, 'o:r')  
plt.show()

x=np.array([1,2,3,4])
plt.plot(x,  label='x squared')
plt.show()