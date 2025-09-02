import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

spect_df = pd.DataFrame({
    'Test Tube': [1, 2, 3, 4, 5, 6, 7],
    'Standard Solution (mL)': [0.0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0],
    'Distilled Water (mL)': [1.0, 0.9, 0.8, 0.8, 0.4, 0.2, 0.0],
    'Protein Conc. (final, mg/dL)': [0, 1, 2, 4, 6, 8, 10],
    'Absorbance (OD) at 550 nm': [0.000, 0.050, 0.086, 0.174, 0.270, 0.351, 0.415]
})

spect_df.set_index('Test Tube', inplace=True)

fig, ax = plt.subplots()

x = spect_df['Absorbance (OD) at 550 nm']
y = spect_df['Protein Conc. (final, mg/dL)']

ax.scatter(x, y, label='OD')

ax.set(
    xlabel='Absorbance (OD) at 550 nm',
    ylabel='Protein Conc. (final, mg/dL)',
    facecolor='whitesmoke'
)

ax.grid(True, color='green', alpha=0.3)

slope, intercept = np.polyfit(x, y, 1)
y_fit = slope * x + intercept

plt.plot(x, y_fit, color='red', label=f'y={slope:.2f}x + {intercept:.2f}')

plt.legend(fontsize=14)

plt.show()
