import streamlit as st
import numpy as npModuleNotFoundError: This app has encountered an error in the logs (if you're on Streamlit Cloud, click on 'Manage app' in the lower right of your app).
Traceback:
File "/mount/src/calculate-screw-flight-dimensions/screw_flight_app.py", line 3, in <module>
    import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

# Define the calculation function (assuming this is the correct one based on previous interactions)
def calculate_screw_flight_size(outer_diameter_mm, inner_diameter_mm, pitch_mm, thickness_mm):
    """
    Calculates the dimensions of the flat pattern for a screw flight,
    using updated formulas for R_inner and R_outer.

    Args:
        outer_diameter_mm: The outer diameter of the screw flight in millimeters.
        inner_diameter_mm: The inner diameter of the screw flight in millimeters.
        pitch_mm: The pitch of the screw flight in millimeters.
        thickness_mm: The thickness of the screw flight material in millimeters.

    Returns:
        A dictionary containing the calculated dimensions in millimeters and degrees, or an error message.
    """
    # Input validation
    if not all(isinstance(i, (int, float)) for i in [outer_diameter_mm, inner_diameter_mm, pitch_mm, thickness_mm]):
        return {"error": "All inputs must be numerical values."}
    if outer_diameter_mm <= 0 or inner_diameter_mm <= 0 or pitch_mm <= 0 or thickness_mm < 0:
        return {"error": "Outer diameter, inner diameter, and pitch must be positive values. Thickness must be non-negative."}
    if inner_diameter_mm >= outer_diameter_mm:
        return {"error": "Inner diameter must be less than outer diameter."}
    # The check for thickness being too large needs to be adjusted based on the new definition of h
    if (thickness_mm * 2) >= (outer_diameter_mm - inner_diameter_mm): # This check is still valid as it relates to the full width
         return {"error": "Thickness is too large for the given inner and outer diameters."}


    # Calculate the width of the screw flight (h) using the formula: h = (D - d) / 2
    h_mm = (outer_diameter_mm - inner_diameter_mm) / 2

    # Calculate the length of the outer edge (L_outer) and inner edge (L_inner) of the developed blank in millimeters.
    L_outer_mm = np.sqrt((np.pi * outer_diameter_mm)**2 + pitch_mm**2)
    L_inner_mm = np.sqrt((np.pi * inner_diameter_mm)**2 + pitch_mm**2)

    # Calculate the inner radius (R_inner) using the NEW formula: R_Inner = ((L_inner * h) / (L_outer - L_inner)) - t
    denominator = (L_outer_mm - L_inner_mm)
    if abs(denominator) < 1e-9: # Use a small tolerance for floating point comparison
         return {"error": "Calculation error: denominator for R_inner calculation is too close to zero."}
    R_inner_mm = ((L_inner_mm * h_mm) / denominator) - thickness_mm


    # Calculate the outer radius (R_outer) using the NEW formula: R_outer = R_inner + h
    R_outer_mm = R_inner_mm + h_mm

    # Calculate the angle of the sector to be removed from the annular blank (theta) in degrees.
    # The angle calculation depends on R_outer and pitch. Using the cone development method formula:
    if R_outer_mm <= 0: # Prevent division by zero or log of zero/negative in degrees calculation
         return {"error": "Calculated outer radius is not positive, cannot calculate angle."}
    theta_removed_deg = np.degrees(np.arctan(pitch_mm / (np.pi * R_outer_mm)))
    theta_segment_deg = 360 - theta_removed_deg


    return {
        "outer_diameter_mm": outer_diameter_mm, # Include original inputs in the results
        "inner_diameter_mm": inner_diameter_mm,
        "pitch_mm": pitch_mm,
        "R_outer_mm": R_outer_mm,
        "R_inner_mm": R_inner_mm,
        "L_outer_mm": L_outer_mm, # Note: L_outer and L_inner are based on original D and d, not derived from the new R_outer and R_inner
        "L_inner_mm": L_inner_mm,
        "theta_removed_deg": theta_removed_deg, # Include the removed angle for reference
        "theta_segment_deg": theta_segment_deg, # Include the segment angle for visualization
        "h_mm": h_mm, # Include the new h in the output
        "thickness_mm": thickness_mm # Include thickness in output
    }

def visualize_screw_flight(calculated_results):
    """
    Generates a visual representation of the flat pattern of the screw flight segment with dimensions listed.

    Args:
        calculated_results: A dictionary containing the calculated dimensions.

    Returns:
        A matplotlib figure.
    """
    R_outer_mm = calculated_results['R_outer_mm']
    R_inner_mm = calculated_results['R_inner_mm']
    theta_segment_deg = calculated_results['theta_segment_deg'] # Use the segment angle for visualization
    thickness_mm = calculated_results['thickness_mm'] # Get thickness for display
    h_mm = calculated_results['h_mm'] # Get the new h for visualization purposes


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

    # Add dimensions as text in a column on the right side with colors
    # Use ax.text for each line with specific color and position
    text_x = 1.02 # right edge of the axes, slightly outside
    text_y_start = 0.5 # vertical center of the axes
    line_height = 0.05 # spacing between lines in axes coordinates

    ax.text(text_x, text_y_start + line_height * 3, f'Outer Diameter: {R_outer_mm * 2:.2f} mm.', # Use calculated D
            verticalalignment='center', horizontalalignment='left',
            transform=ax.transAxes, color='red', fontsize=10)

    ax.text(text_x, text_y_start + line_height * 2, f'Inner Diameter: {R_inner_mm * 2:.2f} mm.', # Use calculated d
            verticalalignment='center', horizontalalignment='left',
            transform=ax.transAxes, color='blue', fontsize=10)

    ax.text(text_x, text_y_start + line_height * 1, f'Flight Width: {h_mm:.2f} mm.', # Changed label to Flight Width
            verticalalignment='center', horizontalalignment='left',
            transform=ax.transAxes, color='purple', fontsize=10) # Use purple for flight width

    ax.text(text_x, text_y_start + line_height * 0, f'Segment Angle: {theta_segment_deg:.2f}°',
            verticalalignment='center', horizontalalignment='left',
            transform=ax.transAxes, color='darkgreen', fontsize=10) # Use darkgreen for segment angle

    ax.text(text_x, text_y_start - line_height * 1, f'Removed Angle: {calculated_results["theta_removed_deg"]:.2f}°',
            verticalalignment='center', horizontalalignment='left',
            transform=ax.transAxes, color='gray', fontsize=10) # Use gray for removed angle

    ax.text(text_x, text_y_start - line_height * 2, f'Thickness: {thickness_mm:.2f} mm.', # Moved mm. after value
            verticalalignment='center', horizontalalignment='left',
            transform=ax.transAxes, color='orange', fontsize=10) # Use orange for thickness


    # Add visual representation of h (dashed line and arrow) between arcs
    mid_angle_rad = theta_segment_rad * 0.5
    arrow_start_x = R_inner_mm * np.cos(mid_angle_rad)
    arrow_start_y = R_inner_mm * np.sin(mid_angle_rad)
    arrow_end_x = R_outer_mm * np.cos(mid_angle_rad)
    arrow_end_y = R_outer_mm * np.sin(mid_angle_rad)

    ax.annotate('', xy=(arrow_end_x, arrow_end_y), xytext=(arrow_start_x, arrow_start_y),
                arrowprops=dict(arrowstyle='<->', color='purple', lw=1.5))


    # Set plot limits and aspect ratio
    max_radius = max(R_outer_mm, R_inner_mm)
    # Adjust limits to accommodate the full segment visualization and labels
    padding = max_radius * 0.6 # Increased padding to make space for text on the right
    ax.set_xlim(-max_radius - padding * 0.1, max_radius + padding) # More padding on the right
    ax.set_ylim(-max_radius - padding * 0.1, max_radius + padding * 0.1)
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
thickness = st.number_input('Thickness (t) (mm)', min_value=0.0, format="%.2f") # thickness can be 0 or positive

# Calculation and Visualization Button
if st.button('Calculate and Visualize'):
    # Perform calculation using D, d, P, and t
    results = calculate_screw_flight_size(outer_diameter, inner_diameter, pitch, thickness)

    # Display results or error
    if "error" in results:
        st.error(results["error"])
    else:
        st.subheader("Calculated Dimensions:")
        # Display results in a table format using a DataFrame
        results_df = pd.DataFrame({
            'Dimension': ['Outer Diameter (mm)', 'Inner Diameter (mm)', 'Outer Edge Length (mm)',
                          'Inner Edge Length (mm)', 'Sector Angle (Segment) (degrees)', 'Sector Angle (Removed) (degrees)', 'Flight Width (mm)', 'Thickness (mm)'],
            'Value': [results['R_outer_mm'] * 2, results['R_inner_mm'] * 2, results['L_outer_mm'],
                      results['L_inner_mm'], results['theta_segment_deg'], results['theta_removed_deg'], results['h_mm']*2, results['thickness_mm']] # Display diameters and h*2 here
        })
        # Apply formatting to the 'Value' column after creating the DataFrame
        results_df['Value'] = results_df['Value'].map('{:.2f}'.format)
        st.dataframe(results_df.set_index('Dimension'))


        st.subheader("Flat Pattern Visualization:")
        # Generate and display the visualization
        fig = visualize_screw_flight(results)
        st.pyplot(fig)
