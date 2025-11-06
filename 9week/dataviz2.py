import matplotlib.pyplot as plt

height = [156.9,159.9,153.5,151.2,154.6,168.3,165,154.7,146,152.4]
weight = [48.7,58.5,48.4,39,58.9,80.8,59.3,49.4,35.3,51.8]
gender = ['f','f','f','f','f','m','m','m','m','m']

plt.figure(figsize=(5,3))
colors = ['r' if g == 'f' else 'b' for g in gender]
plt.scatter(height, weight, c=colors)
plt.xlabel('height')
plt.ylabel('weight')
plt.show()

