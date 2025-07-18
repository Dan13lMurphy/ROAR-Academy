import matplotlib.pyplot as plt
import numpy as np

x1 = [-1, 6, 11]
y1 = [2, 4, 1]
x2 = np.linspace(0, 4 * np.pi, 100)  # add sin function
y2 = np.sin(x2)

plt.plot(x1, y1, 'b')
plt.plot(x2, y2, 'r')

plt.title("Sample graph!")
plt.xlabel("x - axis")
plt.ylabel("y - axis")

plt.show()
