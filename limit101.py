import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, num=100)
y = x**2

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of f(x) = x^2')
# plt.grid()
plt.show()
