import matplotlib.pyplot as plt

x = [1.1, 1.7, 1.3, 1.4, 1.2, 2.7, 2.3, 2.2]
y = [4, 6, 10, 3, 2, 10, 11, 5]

x0 = [3.2, 3.3, 3.7, 4, 4.2, 4.3]
y0 = [5, 7, 3, 9, 3, 12]

plt.scatter(x, y, label='Red', color='r')
plt.scatter(x0, y0, label='Blue', color='b')

plt.xlabel('x')
plt.xlabel('y')
plt.title('Scatter Pot')
plt.legend()
plt.show()