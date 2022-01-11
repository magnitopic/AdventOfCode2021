import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import poisson
import random, math


def generateArray(mean):
    x, sum, acumulado, array = 0, 0, [], []

    while sum < 1 and x < 170:  # the factorial of 170 or more gives an error because it is too large
        sum += math.exp(-mean)*(mean ** x)/math.factorial(x)
        #print("x:", x, "sum:", sum)
        acumulado.append(sum)
        x += 1

    for j in range(1_000_000):
        for i in acumulado:
            if random.random() < i:
                array.append(acumulado.index(i))
                break
    return array


def generateArrayLib(mean):
    x = 1_000_000
    return poisson.rvs(mu=mean, size=x)


if __name__ == "__main__":
    for i in range(1, 25, 7):
        sns.distplot(generateArray(i), hist=True, kde=False)
    plt.show()
