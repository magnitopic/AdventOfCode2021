import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.stats import poisson
import seaborn as sns
import math


def generateArray(mean):
    x, sum, acumulado = 1, 0, []

    while sum != 1:
        sum += math.exp(-mean)*(mean ^ x)/math.factorial(x)
        acumulado.append(sum)
        x += 1
    print(acumulado)

    for i in acumulado:
        if random.random() < i:
            return acumulado.index(i)


def generateArrayLib(mean):
    x = 1_000_000
    return poisson.rvs(mu=mean, size=x)


if __name__ == "__main__":

    """ sns.distplot(generateArray(5), hist=True, kde=False, label='Custom')
    sns.distplot(generateArrayLib(7), hist=True, kde=False, label='Library') """
    """ for i in range(3, 23, 5):
        sns.distplot(generateArrayLib(i), hist=True, kde=False)

    plt.show() """
    generateArray(1)
