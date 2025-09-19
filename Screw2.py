import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

# Define the calculation function (assuming this is the correct one based on previous interactions)
def calculate_screw_flight_size(outer_diameter_mm, inner_diameter_mm, pitch_mm):
    """
    Calculates the dimensions of the flat pattern for a screw flight.

    Args:
        outer_diameter_mm: The outer diameter of the screw flight in millimeters.
        inner_diameter_mm: The inner diameter of the screw flight in millimeters.
        pitch_mm: The pitch of the screw flight in millimeters.
        # Note: Thickness (t) is included as an input in the app but not used in this specific calculation function.

    Returns:
        A dictionary containing the calculated dimensions in millimeters and degrees, or an error message.
    """
    # Input validation
    if not all(isinstance(i, (int, float)) for i in [outer_diameter_mm, inner_diameter_mm, pitch_mm]):
        return {"error": "All inputs must be numerical values."}
    if outer_diameter_mm <= 0 or inner_diameter_mm <= 0 or pitch_mm <= 0:
        return {"error": "Outer diameter, inner diameter, and pitch must be positive values."}
    if inner_diameter_mm >= outer_diameter_mm:
        return {"error": "Inner diameter must be less than outer diameter."}

    # Calculate the width of the screw flight (h)
    h_mm = outer_diameter_mm - inner_diameter_mm

    # Calculate the length of the outer edge (L_outer) and inner edge (L_inner) of the developed blank in millimeters.
    L_outer_mm = np.sqrt((np.pi * outer_diameter_mm)**2 + pitch_mm**2)
    L_inner_mm = np.sqrt((np.pi * inner_diameter_mm)**2 + pitch_mm**2)

    # Calculate the inner and outer radii (R_inner and R_outer) using the provided formulas:
    # R_inner = (L_inner * h) / (L_outer - L_inner)
    # R_outer = (L_outer * h) / (L_outer - L_inner)
    # Add a check to prevent division by zero or near-zero in the denominator
    denominator = L_outer_mm - L_inner_mm
    if abs(denominator) < 1e-9: # Use a small tolerance for floating point comparison
         return {"error": "Calculation error: L_outer is too close to L_inner."}

    R_inner_mm = (L_inner_mm * h_mm) / denominator
    R_outer_mm = (L_outer_mm * h_mm) / denominator

    # Calculate the angle of the sector to be removed from the annular blank (theta) in degrees.
    # Using the cone development method formula based on the new R_outer_mm:
    theta_removed_deg = np.degrees(np.arctan(pitch_mm / (np.pi * R_outer_mm)))
    theta_segment_deg = 360 - theta_removed_deg


    return {
        "R_outer_mm": R_outer_mm,
        "R_inner_mm": R_inner_mm,
        "L_outer_mm": L_outer_mm,
        "L_inner_mm": L_inner_mm,
        "theta_removed_deg": theta_removed_deg, # Include the removed angle for reference
        "theta_segment_deg": theta_segment_deg, # Include the segment angle for visualization
        "h_mm": h_mm # Include h in the output for clarity
    }

def visualize_screw_flight(calculated_results):
    """
    Generates a visual representation of the flat pattern of the screw flight segment.

    Args:
        calculated_results: A dictionary containing the calculated dimensions.

    Returns:
        A matplotlib figure.
    """
    R_outer_mm = calculated_results['R_outer_mm']
    R_inner_mm = calculated_results['R_inner_mm']
    theta_segment_deg = calculated_results['theta_segment_deg'] # Use the segment angle for visualization

    # Convert angle from degrees to radians for plotting
    theta_segment_rad = np.deg2rad(theta_segment_deg)

    # Create a figure and axes for the plot
    fig, ax = plt.subplots(1)

    # Plot the inner arc
    inner_arc = patches.Arc((0, 0), 2 * R_inner_mm, 2 * R_inner_mm,
                            angle=0, theta1=0, theta2=theta_segment_deg, color='blue', lw=2)
    ax.add_patch(inner_arc)

    # Plot the outer arc
    outer_arc = patches.Arc((0, 0), 2 * R_outer_mm, 2 * R_outer_mm,
                            angle=0, theta1=0, theta2=theta_segment_deg, color='red', lw=2)
    ax.add_patch(outer_arc)

    # Connect the endpoints of the arcs to form the radial edges
    # Starting point (at angle 0)
    x_inner_start = R_inner_mm * np.cos(0)
    y_inner_start = R_inner_mm * np.sin(0)
    x_outer_start = R_outer_mm * np.cos(0)
    y_outer_start = R_outer_mm * np.sin(0)
    ax.plot([x_inner_start, x_outer_start], [y_inner_start, y_outer_start], color='green', lw=2)

    # Ending point (at angle theta_segment_rad)
    x_inner_end = R_inner_mm * np.cos(theta_segment_rad)
    y_inner_end = R_inner_mm * np.sin(theta_segment_rad)
    x_outer_end = R_outer_mm * np.cos(theta_segment_rad)
    y_outer_end = R_outer_mm * np.sin(theta_segment_rad)
    ax.plot([x_inner_end, x_outer_end], [y_inner_end, y_outer_end], color='green', lw=2)

    # Add labels for key dimensions on the plot
    # Label for R_outer (on the outer arc)
    outer_label_angle = theta_segment_rad / 4 # Position the label along the arc
    ax.text(R_outer_mm * np.cos(outer_label_angle), R_outer_mm * np.sin(outer_label_angle),
            f'R_outer: {R_outer_mm:.2f} mm', color='red', fontsize=10, ha='center', va='bottom')

    # Label for R_inner (on the inner arc)
    inner_label_angle = theta_segment_rad / 4
    ax.text(R_inner_mm * np.cos(inner_label_angle), R_inner_mm * np.sin(inner_label_angle),
            f'R_inner: {R_inner_mm:.2f} mm', color='blue', fontsize=10, ha='center', va='top')

    # Label for h (flight width)
    mid_radius = (R_outer_mm + R_inner_mm) / 2
    mid_angle = theta_segment_rad * 0.9 # Position towards the end of the segment
    ax.text(mid_radius * np.cos(mid_angle), mid_radius * np.sin(mid_angle),
            f'h: {calculated_results["h_mm"]:.2f} mm', color='purple', fontsize=10, ha='center', va='center')

    # Label for the segment angle
    ax.text(R_outer_mm * np.cos(theta_segment_rad * 0.5) * 0.8 , R_outer_mm * np.sin(theta_segment_rad * 0.5) * 0.8,
            f'{theta_segment_deg:.2f}°', color='darkgreen', fontsize=10, ha='center', va='center')


    # Set plot limits and aspect ratio
    max_radius = max(R_outer_mm, R_inner_mm)
    # Adjust limits to accommodate the full segment visualization and labels
    padding = max_radius * 0.2
    ax.set_xlim(-max_radius - padding, max_radius + padding)
    ax.set_ylim(-max_radius - padding, max_radius + padding)
    ax.set_aspect('equal', adjustable='box')

    # Add title and labels
    ax.set_title('Flat Pattern of Screw Flight Segment with Dimensions')
    ax.set_xlabel('X (mm)')
    ax.set_ylabel('Y (mm)')
    ax.grid(True)

    return fig


# --- Streamlit Application Interface ---
st.title('Screw Flight Size Calculator and Visualizer')

st.write("Enter the dimensions of the screw flight to calculate the flat pattern size.")

# Input widgets for D, d, P, and t
outer_diameter = st.number_input('Outer Diameter (D) (mm)', min_value=0.1, format="%.2f")
inner_diameter = st.number_input('Inner Diameter (d) (mm)', min_value=0.1, format="%.2f")
pitch = st.number_input('Pitch (P) (mm)', min_value=0.1, format="%.2f")
thickness = st.number_input('Thickness (t) (mm)', min_value=0.1, format="%.2f") # Input for thickness

# Calculation and Visualization Button
if st.button('Calculate and Visualize'):
    # Perform calculation using D, d, and P
    results = calculate_screw_flight_size(outer_diameter, inner_diameter, pitch)

    # Display results or error
    if "error" in results:
        st.error(results["error"])
    else:
        st.subheader("Calculated Dimensions:")
        # Display results in a table format using a DataFrame
        results_df = pd.DataFrame({
            'Dimension': ['Outer Radius (mm)', 'Inner Radius (mm)', 'Outer Edge Length (mm)',
                          'Inner Edge Length (mm)', 'Sector Angle (degrees)', 'Flight Width (mm)'],
            'Value': [results['R_outer_mm'], results['R_inner_mm'], results['L_outer_mm'],
                      results['L_inner_mm'], results['theta_segment_deg'], results['h_mm']]
        })
        st.dataframe(results_df.set_index('Dimension'))

        # Display thickness separately as it's not in the calculation output dictionary
        st.write(f"Input Thickness (t): {thickness:.2f} mm")


        st.subheader("Flat Pattern Visualization:")
        # Generate and display the visualization
        fig = visualize_screw_flight(results)
        st.pyplot(fig)
     
