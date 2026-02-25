#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# Plot y as a solid red line
plt.plot(np.arange(0, 11), y, 'r-', label='y = x^3')

# Set the x-axis range
plt.xlim(0, 10)

# Add labels and title (optional)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x^3')

# Show legend
plt.legend()

# Display the plot
plt.show()
