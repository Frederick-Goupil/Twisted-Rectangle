# libraries

import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
 
begin_time = datetime.datetime.now()

import Equation
dictionary = Equation.calculate()
# Make a data frame
df=pd.DataFrame(dictionary)
 
# Initialize the figure style
plt.style.use('seaborn-darkgrid')
 
# create a color palette
palette = plt.get_cmap('Set1')
 
# multiple line plot
num=0
for column in df.drop('x', axis=1):
    num+=1
 
    # Find the right spot on the plot
    plt.subplot(9,9, num)
 
    # plot every group, but discrete
    for v in df.drop('x', axis=1):
        plt.plot(df['x'], df[v], marker='', color='grey', linewidth=0.6, alpha=0.3)
 
    # Plot the lineplot
    plt.plot(df['x'], df[column], marker='', color=palette(0), linewidth=2.4, alpha=0.9, label="")
 
    # Same limits for every chart
    plt.xlim(0,3000)
    plt.ylim(0,2000)
 
    # Not ticks everywhere
    if num in range(7) :
        plt.tick_params(labelbottom='off')
    if num not in [1,4,7] :
        plt.tick_params(labelleft='off')
 
    # Add title
    

# general title

 
# Axis titles


print(datetime.datetime.now() - begin_time)
# Show the graph
plt.show()
