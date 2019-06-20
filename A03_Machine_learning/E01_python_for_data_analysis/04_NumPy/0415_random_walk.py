import numpy as np
import random
import matplotlib.pyplot as plt

position = 0
walk = [position]
steps = 1000

for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100])
plt.show()



nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
print(draws)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

print(walk.min())
print(walk.max())
print((np.abs(walk) >= 10).argmax())
