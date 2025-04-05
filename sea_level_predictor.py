import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x,y)
    print(f'R-squared:{res.rvalue**2:.6f}')
    x_extended = np.append(x, np.arange(x.max() + 1, 2051))
    line1, = plt.plot(x_extended, res.intercept + res.slope*x_extended, 'r', label='Line of best fit (1880-2050)')

    # Create second line of best fit
    mask = df['Year'] >= 2000
    x_2000 = df['Year'][mask]
    y_2000 = df['CSIRO Adjusted Sea Level'][mask]
    res_2000 = linregress(x_2000,y_2000)
    print(f'R-squared:{res_2000.rvalue**2:.6f}')
    x_2000_extended = np.append(x_2000, np.arange(x_2000.max() + 1, 2051))  
    line2, = plt.plot(x_2000_extended,res_2000.intercept + res_2000.slope*x_2000_extended,'g', label = 'Line of best fit(2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend(handles=[line1, line2])
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()