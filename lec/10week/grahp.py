import numpy as np
import matplotlib.pyplot as plt

nation = ['Korea', 'USA', 'Japan', 'France']
men = [175.5, 176.9, 172.1, 178.6]
women = [163.2, 163.3, 158.5, 164.5]
ind = np.arange(len(nation))

plt.figure(figsize=(5, 3))
plt.bar(ind-0.2, men, color='b', label='men', width=0.4)
plt.bar(ind+0.2, women, color='r', label='women', width=0.4)
plt.ylim(130, 190)
plt.xticks(ind, nation)
plt.legend()
plt.show()