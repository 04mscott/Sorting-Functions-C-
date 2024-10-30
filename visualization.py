import numpy as np
import matplotlib.pyplot as plt

num = 15

lst = np.random.randint(0, 100, num)
x = np.arange(0, num, 1)

n = len(lst)
for i in range(n):
  for j in range(0, n - i - 1):
    plt.bar(x, lst)
    plt.pause(0.01)
    plt.clf()
    if lst[j] > lst[j + 1]:
      lst[j], lst[j + 1] = lst[j + 1], lst[j]
plt.show()