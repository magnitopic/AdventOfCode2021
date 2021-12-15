import random as rnd, numpy as np
x, y = rnd.randint(1, 5), rnd.randint(1, 5)
array = np.array([[rnd.randint(0, 9) for i in range(x)]for j in range(y)])
print(np.max(np.min(array, axis=1)))
