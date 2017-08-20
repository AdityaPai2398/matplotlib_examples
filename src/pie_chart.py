import matplotlib.pyplot as plt

transport_methodes = ['Car', 'Train', 'Bus', 'Walk']

transport_count = [23, 25, 10, 2] # e.g. total count of random survey

col = ['r', 'b', 'y', 'g'] 

plt.pie(transport_count, labels=transport_methodes, colors=col)

plt.title('Pie Chart')

plt.show()