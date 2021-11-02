import numpy as np
import pandas as pd
from numpy.random import randn

from scipy import stats

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

dataset1 = randn(100)

plt.hist(dataset1)
plt.show()