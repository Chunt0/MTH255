import matplotlib.pyplot as plt
import numpy as np

# Define the parameter t and the corresponding x and y values
t = np.linspace(-2*np.pi, 2*np.pi, 100)
x = t
y = x**2

# Plot the curve
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Curve of x^2')
plt.show()

# Define the parameter t and the corresponding x and y values
t = np.linspace(-2*np.pi, 2*np.pi, 100)
y = t
x = y**2

# Plot the curve
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Curve of y^2')
plt.show()

# Define the parameter t and the corresponding r and theta values
t = np.linspace(0, 2*np.pi, 100)
r = 2
theta = t

# Convert the polar coordinates to cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the curve
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_aspect('equal')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Parametric Curve of x^2+y^2 = 4')
plt.show()