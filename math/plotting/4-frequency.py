#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# your code here
bins = np.arange(0, student_grades.max(), 10)
plt.hist(student_grades, bins)
plt.show()