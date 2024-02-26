import numpy as np

# Define constants
radius = 0.3
center = (0.45, 0.15, 0)  # Center of the hemisphere

# File path for saving the output
file_path = 'coordinates.txt'

# Open the file to write the coordinates
with open(file_path, 'w') as file:
    # Write the very top point (north pole of the hemisphere)
    top_point = (center[0], center[1], center[2] + radius)
    file.write(f"xyz = ({top_point[0]}, {top_point[1]}, {top_point[2]})\n")
    file.write("robot.move_to_target_in_cartesian(xyz, rpy)\n")
    file.write("time.sleep(1)\n")
    file.write("\n")
    
    # Loop through latitudes from +80 to +30 degrees in 10-degree decrements
    for latitude in range(80, 29, -10):
        # Convert latitude to polar angle theta in radians (90 - latitude)
        theta = np.radians(90 - latitude)
        
        # Generate 36 longitude points at 10-degree increments
        phi = np.radians(np.linspace(0, 360, 36, endpoint=False))
        
        # Calculate XYZ positions
        x = center[0] + radius * np.sin(theta) * np.cos(phi)
        y = center[1] + radius * np.sin(theta) * np.sin(phi)
        z = np.full_like(x, center[2] + radius * np.cos(theta))
        
        # Combine x, y, z into a list of coordinates
        coordinates = np.vstack((x, y, z)).T
        
        # Write the coordinates in the specified format
        for coord in coordinates:
            file.write(f"xyz = ({coord[0]}, {coord[1]}, {coord[2]})\n")
            file.write("robot.move_to_target_in_cartesian(xyz, rpy)\n")
            file.write("time.sleep(1)\n")
            file.write("\n")

print(f"Coordinates including the top point and latitudes from +80 to +30 degrees have been written to {file_path}.")
