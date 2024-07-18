#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 19:09:40 2024

@author: johannes
"""

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Function definitions
vector = lambda ang: np.array([np.cos(ang), np.sin(ang)])
angles = lambda num: np.random.uniform(0, 2*np.pi, size=(num))
distan = lambda num: np.array([vector(angles(num)), vector(angles(num))])
avrg_l = lambda arr: np.sum(np.linalg.norm(arr[0,:,:] - arr[1,:,:], axis=0)) / len(arr[0,0])

#%%
'''
Calculate
'''
# Number of lines
num = 100_000

# Generate the data
d = distan(num)

# Compute ratio between average length and 4/pi
print(f'Average length over 4/pi: {avrg_l(d) * np.pi / 4}')

#%%
'''
Plot
'''
# Create the plot
fig, ax = plt.subplots()

# Set limits and hide the axes
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1.3)
ax.axis('off')

# Set aspect ratio to equal
ax.set_aspect('equal')

# Initialize the label and line
label = ax.text(-1, 1.05, '')
line, = ax.plot([], [], 'k-', linewidth=0.1)

# Animation function
def animate(i):
    # Set line data
    x_data = d[:, 0, :i]
    y_data = d[:, 1, :i]
    line.set_data(x_data, y_data)
    
    # Update the label with the average length
    average_length = avrg_l(d[:,:,:i+1])
    label.set_text(f'Average length over 4/pi: {average_length * np.pi / 4:.6f}\nIteration: {i+1}')
    
    return line, label

# Create the animation
ani = FuncAnimation(fig, animate, frames=num, interval=0, blit=True)

# Display the animation
plt.show()
