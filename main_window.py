
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Import the Hohmann transfer calculation
from calculations.hohmann_transfer import hohmann_transfer

def visualize_trajectory():
    # Create a new window for trajectory visualization
    traj_window = tk.Toplevel()
    traj_window.title("Trajectory Visualization")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Sample distances for the Hohmann transfer (in meters)
    r1 = 6671e3  # Low Earth orbit (6671 km from Earth's center)
    r2 = 384400e3  # Distance to the Moon (384,400 km from Earth's center)

    # Get delta_v values
    delta_v1, delta_v2 = hohmann_transfer(r1, r2)

    # Example trajectory data (simplified for demo purposes)
    x = np.linspace(0, 1000, 100)
    y = np.sin(x / 100) * 1000
    z = np.cos(x / 100) * 1000

    ax.plot(x, y, z)
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    
    # Plot title displaying delta-v values
    ax.set_title(f"Hohmann Transfer:  = \u0394v1 = {delta_v1:.2f} m/s, \u0394v2 = {delta_v2:.2f} m/s")


    # Embed Matplotlib plot into Tkinter window 
    canvas = FigureCanvasTkAgg(fig, master=traj_window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create the main application window
root = tk.Tk()
root.title("Space Mission GUI")

# Add a button to visualize the trajectory
visualize_button = tk.Button(root, text="Visualize Trajectory", command=visualize_trajectory)
visualize_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
