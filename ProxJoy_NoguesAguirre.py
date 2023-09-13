# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:14:20 2023

@author: escor
"""


import pandas as pd
import matplotlib.pyplot as plt
import re
import numpy as np


#To open the file and its path:
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def open_file():
    Tk().withdraw()  
    file = askopenfilename()  
    if file:
        print("Selected File:", file)
    else:
        print("File not selected")

    return file  


#To extract the depth from each sample:
def extract_depth(column_name):
    match = re.search(r'\d+\.\d+', column_name)
    if match:
        return float(match.group())
    else:
        return 0.0
    
  
# For usage:
df = pd.read_csv(open_file(), delimiter=';')#change for "," if your CSV file is "," separated

#Must create the figure first:
fig, ax = plt.subplots(figsize=(6, 20))#dimensions of the figsize can be changed as desired
  
#Loop through the dataframe:
data_columns = df.columns[2:]#change the number if your sample columns beguin elsewhere
for column in data_columns:       
    depth_offset = extract_depth(column)
    y = np.array(df[column])  
    # Reduce non-zero values to 10% of their original values to adjust the curves better:
    y = y*0.1 #this number can be changed if you want another adjustment
    y = y - depth_offset  # Adjust the curve between current and previous depth        
    x = df["um"]
    ax.plot(x, y, label=column)  
    
# Plot settings:
ax.set_ylim(-4.9, -3.6)  # Adjust the y-axis limit as needed
ax.set_xlim(0.3, 3000)
ax.set_yticks([-4.9,-4.8,-4.7,-4.6, -4.5,-4.4,-4.3,-4.2,-4.1,-4.0,-3.9,-3.8,-3.7, -3.6])  # Set your ticks as needed
ax.set_title("Spaced Curves Plot")
ax.set_xscale('log')
# ax.legend()  # Uncomment if you want the legend

# Save the figure as a PDF
plt.savefig("my_figure.pdf", format="pdf", bbox_inches="tight")

plt.show()  # Display the plot on the screen
