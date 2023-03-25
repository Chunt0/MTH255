import numpy as np
import matplotlib.pyplot as plt
  
# creating an array containing the radian values
time = np.linspace(0, (2 * np.pi), 100)
r = 3-np.cos(time)
phi = time

ax = plt.subplot(111, projection='polar')

ax.plot(phi,r)
plt.show()
