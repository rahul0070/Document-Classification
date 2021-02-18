import matplotlib.pyplot as plt

plt.semilogx([0.00001,0.0001,0.001,0.01, 0.1], [0.86527,0.87009,0.86839,0.86042,0.82785], 'ro', linestyle='--')
plt.ylabel('Beta values')
plt.xlabel('Accuracy - [0.00001,0.0001,0.001,0.01, 0.1]')
plt.xticks([0.00001,0.0001,0.001,0.01, 0.1])
plt.show()