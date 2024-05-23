import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Function to plot the leg in 2D
def plot_leg(ax, hip, knee, ankle):
    ax.plot([hip[0], knee[0]], [hip[1], knee[1]], 'r-', linewidth=3)
    ax.plot([knee[0], ankle[0]], [knee[1], ankle[1]], 'b-', linewidth=3)

# Function to simulate gait in 2D
def simulate_gait(gait_angles, ax):
    for angles in gait_angles:
        hip = np.array([0, 1])
        knee = hip + np.array([np.cos(np.radians(angles[0])), -np.sin(np.radians(angles[0]))])
        ankle = knee + np.array([np.cos(np.radians(angles[1])), -np.sin(np.radians(angles[1]))])
        plot_leg(ax, hip, knee, ankle)
        plt.pause(0.2)
        ax.clear()
        set_axes_limits(ax)
    plt.show()

# Function to set axes limits
def set_axes_limits(ax):
    ax.set_xlim([-1, 2])
    ax.set_ylim([-1, 2])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Human Gait Simulation')

# Define gait angles for different activities with realistic frequencies
gait_data = {
    'walking': {
        'angles': [[0, 0], [10, 20], [20, 30], [30, 40], [20, 30], [10, 20], [0, 0]],
        'frequency': 1.5  # Hz
    },
    'running': {
        'angles': [[0, 0], [20, 40], [40, 60], [60, 80], [40, 60], [20, 40], [0, 0]],
        'frequency': 3.0  # Hz
    },
    'standing_up': {
        'angles': [[0, 0], [10, 30], [20, 40], [30, 50], [20, 40], [10, 30], [0, 0]],
        'frequency': 0.5  # Hz
    },
    'sitting_down': {
        'angles': [[0, 0], [-10, -30], [-20, -40], [-30, -50], [-20, -40], [-10, -30], [0, 0]],
        'frequency': 0.5  # Hz
    },
    'bending_down': {
        'angles': [[0, 0], [15, 30], [30, 45], [45, 60], [30, 45], [15, 30], [0, 0]],
        'frequency': 0.5  # Hz
    },
    'jumping': {
        'angles': [[0, 0], [20, 40], [40, 60], [60, 80], [40, 60], [20, 40], [0, 0]],
        'frequency': 2.0  # Hz
    },
    'trotting': {
        'angles': [[0, 0], [10, 20], [20, 30], [30, 40], [20, 30], [10, 20], [0, 0]],
        'frequency': 2.5  # Hz
    },
    'walking_high_speed': {
        'angles': [[0, 0], [15, 30], [30, 45], [45, 60], [30, 45], [15, 30], [0, 0]],
        'frequency': 2.0  # Hz
    }
}

# Function to update the GUI and start the simulation
def update_simulation():
    activity = activity_var.get()
    angles = gait_data[activity]['angles']
    fig, ax = plt.subplots()
    set_axes_limits(ax)
    simulate_gait(angles, ax)

# Function to create the frequency plot
def plot_frequency():
    activity = activity_var.get()
    frequency = gait_data[activity]['frequency']
    time = np.linspace(0, 2, len(gait_data[activity]['angles']))
    frequency_lower_leg = frequency * np.sin(2 * np.pi * frequency * time)
    frequency_thigh = frequency * np.cos(2 * np.pi * frequency * time)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(time, frequency_lower_leg, 'r')
    plt.title(f'Frequency of Lower Leg Motion - {activity.capitalize()}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')

    plt.subplot(2, 1, 2)
    plt.plot(time, frequency_thigh, 'b')
    plt.title(f'Frequency of Thigh Motion - {activity.capitalize()}')
    plt.xlabel('Time (s)')
    plt.ylabel('Frequency (Hz)')

    plt.tight_layout()
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Human Gait Simulation")
root.geometry("300x200")

# Create a label and combobox for selecting the activity
activity_label = tk.Label(root, text="Select Activity:")
activity_label.pack(pady=5)
activity_var = tk.StringVar(value='walking')
activity_combobox = ttk.Combobox(root, textvariable=activity_var, values=list(gait_data.keys()))
activity_combobox.pack(pady=5)

# Create a button to start the simulation
simulate_button = tk.Button(root, text="Start Simulation", command=update_simulation)
simulate_button.pack(pady=10)

# Create a button to plot the frequency graph
frequency_button = tk.Button(root, text="Plot Frequency", command=plot_frequency)
frequency_button.pack(pady=10)

# Run the application
root.mainloop()
