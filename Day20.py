import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.stats import poisson
import seaborn as sns


def generateArray(mean):
    x = 1_000_000
    pass


def generateArrayLib(mean):
    x = 1_000_000
    return poisson.rvs(mu=mean, size=x)


if __name__ == "__main__":

    """ sns.distplot(generateArray(5), hist=True, kde=False, label='Custom')
    sns.distplot(generateArrayLib(7), hist=True, kde=False, label='Library') """
    for i in range(3, 23,5):
        sns.distplot(generateArrayLib(i), hist=True, kde=False)

    plt.show()
