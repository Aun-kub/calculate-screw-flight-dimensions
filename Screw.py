Requirement already satisfied: altair!=5.4.0,!=5.4.1,<6,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.0)
Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (1.9.0)
Requirement already satisfied: cachetools<7,>=4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.5.2)
Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.2.1)
Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.0.2)
Requirement already satisfied: packaging<26,>=20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (25.0)
Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.2.2)
Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (11.3.0)
Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.12/dist-packages (from streamlit) (5.29.5)
Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (18.1.0)
Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.12/dist-packages (from streamlit) (2.32.4)
Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (8.5.0)
Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.12/dist-packages (from streamlit) (0.10.2)
Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.12/dist-packages (from streamlit) (4.15.0)
Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.0.0)
Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.12/dist-packages (from streamlit) (3.1.45)
Requirement already satisfied: tornado!=6.5.0,<7,>=6.0.3 in /usr/local/lib/python3.12/dist-packages (from streamlit) (6.4.2)
Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.3.3)
Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (0.12.1)
Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (4.59.2)
Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (1.4.9)
Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (3.2.3)
Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.12/dist-packages (from matplotlib) (2.9.0.post0)
Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.1.6)
Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (4.25.1)
Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.12/dist-packages (from altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2.4.0)
Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.12/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)
Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.7->matplotlib) (1.17.0)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.4.3)
Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2.5.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3,>=2.27->streamlit) (2025.8.3)
Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.12/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (3.0.2)
Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (25.3.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.36.2)
Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.12/dist-packages (from jsonschema>=3.0->altair!=5.4.0,!=5.4.1,<6,>=4.0->streamlit) (0.27.1)
import streamlit as st
import numpy as np
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
    if (thickness_mm * 2) >= (outer_diameter_mm - inner_diameter_mm):
         return {"error": "Thickness must be less than half of the difference between outer and inner diameters."}

    try:
        # Calculate radii considering thickness
        R_outer = outer_diameter_mm / 2
        R_inner = inner_diameter_mm / 2

        # Calculate circumference at the mean radius (R_mean)
        R_mean = (R_outer + R_inner) / 2
        circumference_mean = 2 * np.pi * R_mean

        # Calculate the slant height (h)
        h = np.sqrt(pitch_mm**2 + circumference_mean**2)

        # Calculate the total angle (theta) for the full flight turn in degrees
        theta = 360 * (h / R_mean) / (circumference_mean / R_mean) # This simplifies to 360 * h / circumference_mean
        theta = 360 * h / circumference_mean

        # Calculate the outer arc length (S_outer)
        S_outer = (theta / 360) * (2 * np.pi * R_outer)

        # Calculate the inner arc length (S_inner)
        S_inner = (theta / 360) * (2 * np.pi * R_inner)

        return {
            "R_outer_flat": R_outer * (theta / 360) * (2 * np.pi / theta),  # This simplifies to R_outer
            "R_inner_flat": R_inner * (theta / 360) * (2 * np.pi / theta),  # This simplifies to R_inner
            "theta_degrees": theta,
            "S_outer_arc_length": S_outer,
            "S_inner_arc_length": S_inner,
            "slant_height": h,
            "mean_radius": R_mean,
            "circumference_mean": circumference_mean
        }
    except Exception as e:
        return {"error": f"An error occurred during calculation: {e}"}


# Function to draw the flat pattern
def draw_flat_pattern(R_outer_flat, R_inner_flat, theta_degrees):
    """
    Draws the flat pattern of the screw flight using Matplotlib.

    Args:
        R_outer_flat: The outer radius of the flat pattern.
        R_inner_flat: The inner radius of the flat pattern.
        theta_degrees: The angle of the flat pattern in degrees.
    """
    fig, ax = plt.subplots(1)
    ax.set_aspect('equal', adjustable='box')

    # Convert angle to radians
    theta_radians = np.deg2rad(theta_degrees)

    # Draw the arcs
    outer_arc = patches.Arc((0, 0), 2 * R_outer_flat, 2 * R_outer_flat,
                            angle=0, theta1=0, theta2=theta_degrees, linewidth=2, fill=False)
    inner_arc = patches.Arc((0, 0), 2 * R_inner_flat, 2 * R_inner_flat,
                            angle=0, theta1=0, theta2=theta_degrees, linewidth=2, fill=False)

    ax.add_patch(outer_arc)
    ax.add_patch(inner_arc)

    # Draw the connecting lines
    x_outer_end = R_outer_flat * np.cos(theta_radians)
    y_outer_end = R_outer_flat * np.sin(theta_radians)
    x_inner_end = R_inner_flat * np.cos(theta_radians)
    y_inner_end = R_inner_flat * np.sin(theta_radians)

    ax.plot([R_inner_flat, R_outer_flat], [0, 0], 'k-', linewidth=2)
    ax.plot([x_inner_end, x_outer_end], [y_inner_end, y_outer_end], 'k-', linewidth=2)

    # Set plot limits
    max_dim = max(R_outer_flat, R_outer_flat * np.sin(theta_radians)) * 1.1
    ax.set_xlim(-max_dim, max_dim)
    ax.set_ylim(-max_dim, max_dim)

    st.pyplot(fig)

# Streamlit app layout
st.title("Screw Flight Dimension Calculator")

st.sidebar.header("Input Parameters (in mm)")
outer_diameter = st.sidebar.number_input("Outer Diameter", min_value=0.1, value=100.0)
inner_diameter = st.sidebar.number_input("Inner Diameter", min_value=0.1, value=50.0)
pitch = st.sidebar.number_input("Pitch", min_value=0.1, value=75.0)
thickness = st.sidebar.number_input("Thickness", min_value=0.0, value=3.0)

if st.sidebar.button("Calculate"):
    results = calculate_screw_flight_size(outer_diameter, inner_diameter, pitch, thickness)

    if "error" in results:
        st.error(results["error"])
    else:
        st.subheader("Calculated Dimensions (Flat Pattern)")
        st.write(f"Outer Radius (R_outer_flat): {results['R_outer_flat']:.2f} mm")
        st.write(f"Inner Radius (R_inner_flat): {results['R_inner_flat']:.2f} mm")
        st.write(f"Total Angle (theta): {results['theta_degrees']:.2f} degrees")
        st.write(f"Outer Arc Length (S_outer): {results['S_outer_arc_length']:.2f} mm")
        st.write(f"Inner Arc Length (S_inner): {results['S_inner_arc_length']:.2f} mm")
        st.write(f"Slant Height (h): {results['slant_height']:.2f} mm")
        st.write(f"Mean Radius (R_mean): {results['mean_radius']:.2f} mm")
        st.write(f"Circumference Mean: {results['circumference_mean']:.2f} mm")

        st.subheader("Flat Pattern Visualization")
        draw_flat_pattern(results['R_outer_flat'], results['R_inner_flat'], results['theta_degrees'])
