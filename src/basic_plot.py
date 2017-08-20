import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 4, 9, 16, 25, 36, 49]
y1 = [1, 2, 3, 4, 5, 6, 7]

plt.plot(x, y, label='x^2')
plt.plot(x, y1, label='x')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.title('function plots')
plt.legend()
plt.show()
