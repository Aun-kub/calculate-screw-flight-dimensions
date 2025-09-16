{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Aun-kub/calculate-screw-flight-dimensions/blob/main/Screw2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": Null,
      "metadata": {
        "id": "e7JBNYz3Ok4r"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "0a1322d9"
      },
      "source": [
        "**Reasoning**:\n",
        "Combine the input gathering and calculation code into a single script and execute it with valid inputs.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": Null,
      "metadata": {
        "id": "f16125eb"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd # Import pandas for Excel output\n",
        "from google.colab import drive # Import drive for saving to Google Drive\n",
        "\n",
        "def calculate_flighting_development():\n",
        "    \"\"\"Calculates the development of a screw conveyor flighting based on user input and saves to Excel.\"\"\"\n",
        "    try:\n",
        "        outer_diameter_str = input(\"Enter Outer Diameter (mm): \")\n",
        "        inner_diameter_str = input(\"Enter Inner Diameter (mm): \")\n",
        "        pitch_str = input(\"Enter Pitch (mm): \")\n",
        "        material_thickness_str = input(\"Enter Material Thickness (mm): \")\n",
        "\n",
        "        target_outer_diameter = float(outer_diameter_str) # This is the target outer diameter\n",
        "        target_inner_diameter = float(inner_diameter_str) # This is the target inner diameter (pipe OD)\n",
        "        pitch = float(pitch_str)\n",
        "        material_thickness = float(material_thickness_str)\n",
        "\n",
        "        # --- General Adjustment for Inner Diameter in Flat Pattern ---\n",
        "        # Increase the inner diameter of the flat pattern based on material thickness.\n",
        "        # This is a general adjustment and may need empirical tuning for specific materials/processes.\n",
        "        inner_diameter_flat_pattern = target_inner_diameter + material_thickness\n",
        "        print(\"\\n--- Using General Adjustment for Inner Diameter for Flat Pattern ---\")\n",
        "        print(f\"  (Target Inner Diameter + Material Thickness)\")\n",
        "        # ----------------------------------------------------\n",
        "\n",
        "        # --- Outer Diameter for Flat Pattern ---\n",
        "        # Use the target outer diameter for the flat pattern calculation.\n",
        "        # Note: Empirical testing may be needed for outer diameters as well to refine this.\n",
        "        outer_diameter_flat_pattern = target_outer_diameter\n",
        "        print(\"--- Using Target Outer Diameter for Flat Pattern ---\")\n",
        "        # ----------------------------------------------------------\n",
        "\n",
        "\n",
        "        # 1. Calculate outer radius for the FLAT PATTERN (R_outer_flat_pattern)\n",
        "        R_outer_flat_pattern = outer_diameter_flat_pattern / 2\n",
        "\n",
        "        # 2. Calculate inner radius for the FLAT PATTERN (R_inner_flat_pattern)\n",
        "        R_inner_flat_pattern = inner_diameter_flat_pattern / 2\n",
        "\n",
        "        # 3. Calculate outer circumference for the FLAT PATTERN (C_outer_flat_pattern)\n",
        "        C_outer_flat_pattern = 2 * np.pi * R_outer_flat_pattern\n",
        "\n",
        "        # 4. Calculate outer arc length (L_outer) - This is calculated based on the FLAT PATTERN outer circumference and the PITCH\n",
        "        L_outer = np.sqrt(C_outer_flat_pattern**2 + pitch**2)\n",
        "\n",
        "        # 5. Calculate inner circumference for the FLAT PATTERN (C_inner_flat_pattern)\n",
        "        C_inner_flat_pattern = 2 * np.pi * R_inner_flat_pattern\n",
        "\n",
        "        # 6. Calculate inner arc length for the FLAT PATTERN (L_inner_flat_pattern) - This is calculated based on the FLAT PATTERN inner circumference and the PITCH\n",
        "        L_inner_flat_pattern = np.sqrt(C_inner_flat_pattern**2 + pitch**2)\n",
        "\n",
        "\n",
        "        # 7. Calculate the width of the developed blank (Width)\n",
        "        # Width is the difference between outer and inner radii of the FLAT PATTERN\n",
        "        Width = R_outer_flat_pattern - R_inner_flat_pattern\n",
        "\n",
        "        # 8. Calculate the angle of the developed blank (Angle) in degrees\n",
        "        # Using the formula: (L_outer / R_outer) * (180 / pi)\n",
        "        # Note: Use R_outer_flat_pattern for this calculation as L_outer was based on it\n",
        "        Angle = (L_outer / R_outer_flat_pattern) * (180 / np.pi)\n",
        "\n",
        "        print(\"\\n--- Calculation Results for Flat Pattern ---\")\n",
        "        print(f\"Target Outer Diameter: {target_outer_diameter:.2f} mm\")\n",
        "        print(f\"Target Inner Diameter (Pipe OD): {target_inner_diameter:.2f} mm\")\n",
        "        print(f\"Material Thickness: {material_thickness:.2f} mm\")\n",
        "        print(\"-\" * 30)\n",
        "        print(f\"Flat Pattern Outer Diameter: {outer_diameter_flat_pattern:.2f} mm\")\n",
        "        print(f\"Flat Pattern Inner Diameter: {inner_diameter_flat_pattern:.2f} mm\")\n",
        "        print(f\"Developed Width: {Width:.2f} mm\")\n",
        "        print(f\"Developed Angle: {Angle:.2f} degrees\")\n",
        "\n",
        "        # Store the results in a dictionary\n",
        "        results = {\n",
        "            \"Input Outer Diameter (mm)\": [target_outer_diameter],\n",
        "            \"Input Inner Diameter (Pipe OD) (mm)\": [target_inner_diameter],\n",
        "            \"Input Pitch (mm)\": [pitch],\n",
        "            \"Input Material Thickness (mm)\": [material_thickness],\n",
        "            \"Flat Pattern Outer Diameter (mm)\": [outer_diameter_flat_pattern],\n",
        "            \"Flat Pattern Inner Diameter (mm)\": [inner_diameter_flat_pattern],\n",
        "            \"Developed Width (mm)\": [Width],\n",
        "            \"Developed Angle (degrees)\": [Angle]\n",
        "        }\n",
        "\n",
        "        # Ask user if they want to save to Excel\n",
        "        save_to_excel = input(\"\\nDo you want to save the results to an Excel file? (yes/no): \").lower()\n",
        "\n",
        "        if save_to_excel == 'yes':\n",
        "            # Define the path in Google Drive\n",
        "            excel_filepath = \"/content/drive/MyDrive/screw_conveyor_flighting_development.xlsx\"\n",
        "            df_results = pd.DataFrame(results)\n",
        "            df_results.to_excel(excel_filepath, index=False)\n",
        "            print(f\"Results saved to {excel_filepath}\")\n",
        "\n",
        "        # Return the calculated values for the flat pattern for plotting\n",
        "        return {\n",
        "            \"R_outer_flat_pattern\": R_outer_flat_pattern,\n",
        "            \"R_inner_flat_pattern\": R_inner_flat_pattern,\n",
        "            \"Angle\": Angle\n",
        "        }\n",
        "\n",
        "    except ValueError:\n",
        "        print(\"Invalid input. Please enter numeric values for all parameters.\")\n",
        "        return None # Return None in case of error\n",
        "    except Exception as e:\n",
        "        print(f\"An error occurred: {e}\")\n",
        "        return None # Return None in case of error\n",
        "\n",
        "# The function is now defined to return values, we will call it and plot in a separate cell\n",
        "# calculate_flighting_development()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8db6f37c",
        "outputId": "ad08d6ab-22a6-4d5e-97a9-97c7a77c58d8"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter Outer Diameter (mm): 450\n",
            "Enter Inner Diameter (mm): 118\n",
            "Enter Pitch (mm): 350\n",
            "Enter Material Thickness (mm): 6\n",
            "\n",
            "--- Using General Adjustment for Inner Diameter for Flat Pattern ---\n",
            "  (Target Inner Diameter + Material Thickness)\n",
            "--- Using Target Outer Diameter for Flat Pattern ---\n",
            "\n",
            "--- Calculation Results for Flat Pattern ---\n",
            "Target Outer Diameter: 450.00 mm\n",
            "Target Inner Diameter (Pipe OD): 118.00 mm\n",
            "Material Thickness: 6.00 mm\n",
            "------------------------------\n",
            "Flat Pattern Outer Diameter: 450.00 mm\n",
            "Flat Pattern Inner Diameter: 124.00 mm\n",
            "Developed Width: 163.00 mm\n",
            "Developed Angle: 370.87 degrees\n",
            "\n",
            "Do you want to save the results to an Excel file? (yes/no): yes\n",
            "An error occurred: Cannot save file into a non-existent directory: '/content/drive/MyDrive'\n"
          ]
        }
      ],
      "source": [
        "# Run the calculation function again\n",
        "calculate_flighting_development()"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": Null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1lGtQ6zrVqG9",
        "outputId": "b686b87e-9c00-4de7-fc93-bfbd69971b61"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": Null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 824
        },
        "id": "a2a041f2",
        "outputId": "dc8ad9d3-5b5a-452b-ed6f-53b5947fc84b"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Enter Outer Diameter (mm): 450\n",
            "Enter Inner Diameter (mm): 118\n",
            "Enter Pitch (mm): 350\n",
            "Enter Material Thickness (mm): 6\n",
            "\n",
            "--- Using General Adjustment for Inner Diameter for Flat Pattern ---\n",
            "  (Target Inner Diameter + Material Thickness)\n",
            "--- Using Target Outer Diameter for Flat Pattern ---\n",
            "\n",
            "--- Calculation Results for Flat Pattern ---\n",
            "Target Outer Diameter: 450.00 mm\n",
            "Target Inner Diameter (Pipe OD): 118.00 mm\n",
            "Material Thickness: 6.00 mm\n",
            "------------------------------\n",
            "Flat Pattern Outer Diameter: 450.00 mm\n",
            "Flat Pattern Inner Diameter: 124.00 mm\n",
            "Developed Width: 163.00 mm\n",
            "Developed Angle: 370.87 degrees\n",
            "\n",
            "Do you want to save the results to an Excel file? (yes/no): yes\n",
            "Results saved to /content/drive/MyDrive/screw_conveyor_flighting_development.xlsx\n"
          ]
        },
        {
          "data": {
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAqQAAAG6CAYAAADeclTfAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQABAABJREFUeJzsnXdYVMfXx793l6UtvRdpgtJEECyxd0k0tmhsiWJi1FhiS0z5xZLEGE1MYknRmGI0lqhRo7E3xIYFURQQEKQo0nvfdt4/NntflgUEpWc+z3Mf2Jm5M+fObeeemXOGIyICg8FgMBgMBoPRTAiaWwAGg8FgMBgMxn8bppAyGAwGg8FgMJoVppAyGAwGg8FgMJoVppAyGAwGg8FgMJoVppAyGAwGg8FgMJoVppAyGAwGg8FgMJoVppAyGAwGg8FgMJoVppAyGAwGg8FgMJoVppAyGAwGg8FgMJqVNquQJiUlgeM4/P77780tSq0MGDAAAwYMaG4xGP9Bql57z3PPqPb9+uuvn0smjuPwySefPFcdTUFT3LfTp0+HgYHBc9Uxd+5cDB06tIEkal5a47Pyk08+AcdxzS0GoxZayzPnaUyfPh3Ozs7NLQYmTZqECRMmPNO+9VJIf//9d3Acx2+6urqws7NDYGAgNm3ahKKiomcSgvF0JBIJNm7ciC5dusDIyAgmJibw9vbGrFmzEBMT09ziNQgXLlzAK6+8AhsbG2hra8PKygojR47EwYMHm1u0VsWFCxfU7tPK26RJk5pbPBw/frzFvQBUCnXlzcjICH5+fvj+++8hl8v5sj/88AOuXbuGixcvokePHrhx4wafFxsbi969e6Ndu3b4/PPPm+NQeBITE/HLL7/gf//7H59Wn+Nk1E5N95iNjU2D1P/jjz/W6+OwsgwCgQB2dnYYNmwYLly4UO+2a7pHS0tL8cknnzxTnU2Bs7OzWh+YmJjAx8cHs2bNwvXr15tbvP8EH3zwAQ4cOICIiIh676v1LA1+9tlncHFxgVQqRXp6Oi5cuIBFixbh22+/xZEjR9C5c+dnqZZRC+PGjcOJEycwefJkzJw5E1KpFDExMTh69Ch69eoFDw+P5hbxuVi5ciU+++wzdOjQAbNnz4aTkxNycnJw/PhxjBs3Drt27cKUKVOaW8xWxYIFC9CtWze1tNq+oJ2cnFBWVgaRSNSoch0/fhw//PBDtS+8srIyaGk902OpQZg8eTKGDx8OACgoKMDx48fxzjvvIDk5GevWrcPevXuxZMkSuLi4wMjICL6+vggMDERsbCysrKwwf/58vP766+jevTvefvttDBo0CL169WqWY9m4cSNcXFwwcOBAjbynHSejbgwdOhTTpk1TS9PT02uQun/88UdYWFhg+vTp9ZaHiJCYmIgff/wRgwYNwrFjx/DSSy/VuZ6a7tHS0lJ8+umnANBirdV+fn549913AQBFRUW4f/8+9u/fj59//hmLFy/Gt99+q1a+uZ85DcXPP/8MhULR3GKgS5cu6Nq1K7755hvs2LGjfjtTPdi2bRsBoJs3b2rknTt3jvT09MjJyYlKS0vrU22jkJiYSABo27ZtzS1KrfTv35/69+9fa5kbN24QAFq9erVGnkwmo+zs7OeWo7i4+LnreFb2799PAGj8+PEkkUg08k+ePEn//PNPM0jWcqntfAUHBxMA2r9/f6111OXaqyuq+23dunVPLTtv3jyq56On0alJfoVCQd26dSM7OzsiIurevTvNmzeP7zu5XE52dna0Zs0aIiIKCAig69evk0QioVGjRtGxY8eeWaagoCASi8XPtK9EIiELCwtatmyZWnpdj7Ml0pDXa0MAgObNm1drmZUrVz7zte7t7V2v461Onrt37xIAGjZsWL3arukezcrKIgC0cuXKetX3NBrq/ePk5EQjRozQSC8tLaUxY8YQAPrxxx8bpC1GzXz99dckFoupqKioXvs12BzSQYMGYfny5UhOTsbOnTvV8mJiYjB+/HiYmZlBV1cXXbt2xZEjR/j8sLAwcByH7du3a9R76tQpcByHo0eP8mmpqal48803YW1tDR0dHXh7e+O3336rk5znz59H3759IRaLYWJigtGjR+P+/ftqZVTzfmJiYjBhwgQYGRnB3NwcCxcuRHl5uUadO3fuREBAAPT09GBmZoZJkybh0aNHGuW2bt0KV1dX6OnpoXv37rh06VKdZE5ISAAA9O7dWyNPKBTC3NxcLS01NRUzZsyAnZ0ddHR04OLigjlz5kAikQD4/6kXISEhmDt3LqysrNCuXTt+/xMnTvB9ZGhoiBEjRiAqKorPP3LkCDiOw927d/m0AwcOgOM4vPLKK2qyeHp6YuLEibUe3/Lly2FmZobffvutWutcYGAgXn75Zf53ZmYmZsyYAWtr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jx6lY8eONcJ6v379aH2r7SQgInIFCqQi0mhdvHiRPXv2kJubWx3ODhw4QGFhIV5eXoSFhVUH1LCwMIKDgwkMDCQoKIjWrVvfkMB6IwOpaZqcO3eO0tJSSkpKKC0t5fDhwzXC59mzZwkODq4Rvnv16kW/fv20O5KINFoKpCJy23E4HBQWFtYIcocOHaoOeWfPnsVutxMQEEBgYGB1SA0ICKBFixY0b94cPz8/mjdvXuPXfn5++Pn5YbfbsdlsWK1WDMMgPT2dkSNHYrPZcLvdGIZBRUUF5eXllJeXc/78+Rqfl4+TJ09SWlpaI4BevHgRHx+f6nZ17ty5RvgMCwu7aS97iYh4igKpiNxxKioqqoPgjwPhiRMnOHfuXK0h0uFwXNPPsdlstYbb5s2b84tf/KI6DF8OoIGBgfj7+98SL2+JiDQUBVIRkXpyOBxcuHABwzBwu901jss9ppePpk2b4uPjo2ApIlIPCqQiIiIi4lFa+0NEREREPEqBVEREREQ8SoFURERERDxKgVREREREPEqBVEREREQ8SoFURERERDxKgVREREREPEqBVEREREQ8SoFURERERDxKgVREREREPEqBVEREREQ8SoFURATIzs4mLi6OoKAgLBYLa9asqXH+/PnzPP3004SEhODr60v37t35+9//XuOaS5cuMWvWLFq3bo2fnx8TJ07kxIkTNa5JTU0lPDyciIgIPvvss5tdlohIo6BAKiICXLhwgd69e7NgwYIrnp8zZw7r1q0jKSmJ/fv38/zzz/P000+Tmppafc3s2bNJS0vjX//6F1lZWZSUlDBhwoTq85WVlcyaNYuFCxeSmJjIU089hcPhuOm1iYjc6uyeboCIyK1g1KhRjBo1qtbzX375JdOmTSM6OhqAhIQEFi9ezI4dOxg7dixnz55l6dKlrFy5ktjYWACWLVtGt27d2L59OwMGDKCyshKbzUafPn0AsNvtVFZW4u3tfbPLExG5pamHVESkHgYNGkRqairHjx/HNE02bdpEQUEBI0aMACAnJwen08mwYcOq7+natSvt27dn27ZtALRo0YLf/va3BAYGEhQUxFNPPUXz5s09Uo+IyK1EPaQiIvUwf/58EhISCAkJwW63Y7VaWbJkCUOHDgWgrKwMb29v7rrrrhr3tW3blrKysurvb7zxBs8//zxWq1VhVETkfxRIRUTqYf78+Wzfvp3U1FRCQ0PJzs5m1qxZBAUF1egVrQ9/f/+b1EoRkcZJgVRE5CouXrzIq6++SkpKCg8++CAAvXr1Yvfu3bz33nsMGzaMgIAAHA4H33//fY1e0hMnThAQEOChlouINA6aQyoichVOpxOn04nVWvOvTJvNhtvtBiAyMhIvLy82btxYff7AgQMcO3aMgQMHNmh7RUQaG/WQiohQtc7ooUOHqr8XFhaye/duWrVqRfv27YmKiuKll17C19eX0NBQsrKyWLFiBe+//z5QNQw/ffp05syZQ6tWrWjRogXPPPMMAwcOZMCAAZ4qS0SkUbCYpml6uhEiIp6WmZlJTEzMT35/2rRpLF++nLKyMl555RXWr1/PmTNnCA0NJSEhgdmzZ2OxWICqhfFfeOEFVq1aRWVlJSNHjmThwoUashcRuQoFUhERERHxKM0hFRERERGPUiAVEREREY9SIBURERERj1IgFRERERGPUiAVEREREY9SIBURERERj1IgFRERERGPUiAVEREREY9SIBURERERj1IgFRERERGPUiAVEREREY9SIBURERERj/o/8IWSUWPCHgYAAAAASUVORK5CYII=\n",
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "# Call the calculation function to get the latest values\n",
        "calculated_results = calculate_flighting_development()\n",
        "\n",
        "if calculated_results:\n",
        "    R_outer_flat_pattern = calculated_results[\"R_outer_flat_pattern\"]\n",
        "    R_inner_flat_pattern = calculated_results[\"R_inner_flat_pattern\"]\n",
        "    Angle = calculated_results[\"Angle\"]\n",
        "\n",
        "    # Ensure Angle is in radians for plotting\n",
        "    angle_rad = np.deg2rad(Angle)\n",
        "\n",
        "    # Create a polar plot\n",
        "    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})\n",
        "\n",
        "    # Plot the outer arc\n",
        "    theta_outer = np.linspace(0, angle_rad, 100)\n",
        "    r_outer = np.full_like(theta_outer, R_outer_flat_pattern)\n",
        "    ax.plot(theta_outer, r_outer, color='blue', label=f'Flat Pattern Outer Radius ({R_outer_flat_pattern:.2f} mm)')\n",
        "\n",
        "    # Plot the inner arc\n",
        "    theta_inner = np.linspace(0, angle_rad, 100)\n",
        "    r_inner = np.full_like(theta_inner, R_inner_flat_pattern)\n",
        "    ax.plot(theta_inner, r_inner, color='red', label=f'Flat Pattern Inner Radius ({R_inner_flat_pattern:.2f} mm)')\n",
        "\n",
        "    # Plot the connecting lines (sides of the segment)\n",
        "    ax.plot([0, 0], [R_inner_flat_pattern, R_outer_flat_pattern], color='black')\n",
        "    ax.plot([angle_rad, angle_rad], [R_inner_flat_pattern, R_outer_flat_pattern], color='black')\n",
        "\n",
        "    # Set plot properties\n",
        "    ax.set_title(\"Developed Screw Conveyor Flighting Blank (Based on Flat Pattern Dimensions)\", va='bottom')\n",
        "    ax.set_theta_zero_location(\"N\")\n",
        "    ax.set_theta_direction(-1)\n",
        "    # Adjust rticks based on the new inner/outer radii\n",
        "    max_radius = max(R_outer_flat_pattern, R_inner_flat_pattern)\n",
        "    min_radius = min(R_outer_flat_pattern, R_inner_flat_pattern)\n",
        "    ax.set_rticks(np.linspace(min_radius, max_radius, num=5)) # Adjust num as needed for clarity\n",
        "    ax.set_rlabel_position(-22.5)\n",
        "    ax.grid(True)\n",
        "    ax.legend(loc='upper right')\n",
        "\n",
        "    plt.show()\n",
        "else:\n",
        "    print(\"Calculation failed. Plotting skipped.\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "1d22e209"
      },
      "source": [
        "# Task\n",
        "สร้างแอปพลิเคชันสำหรับคำนวณงานตัดแผ่นคลี่ใบ Screw conveyor โดยใช้ Gradio เพื่อให้ผู้ใช้สามารถป้อนค่า Outer Diameter, Inner Diameter, Pitch, และ Material Thickness และแสดงผลลัพธ์การคำนวณพร้อมรูปภาพประกอบ"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "6adc0ae4"
      },
      "source": [
        "## ติดตั้งไลบรารี gradio (install gradio library)\n",
        "\n",
        "### Subtask:\n",
        "เพิ่มโค้ดเพื่อติดตั้ง Gradio ใน Colab.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "8fa4193e"
      },
      "source": [
        "**Reasoning**:\n",
        "The subtask is to install the Gradio library. This requires adding a new code cell with the pip install command.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": Null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3c2693e1",
        "outputId": "39f11497-6244-4489-d274-f3c688deef9e"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Requirement already satisfied: gradio in /usr/local/lib/python3.12/dist-packages (5.44.1)\n",
            "Requirement already satisfied: aiofiles<25.0,>=22.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (24.1.0)\n",
            "Requirement already satisfied: anyio<5.0,>=3.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (4.10.0)\n",
            "Requirement already satisfied: brotli>=1.1.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (1.1.0)\n",
            "Requirement already satisfied: fastapi<1.0,>=0.115.2 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.116.1)\n",
            "Requirement already satisfied: ffmpy in /usr/local/lib/python3.12/dist-packages (from gradio) (0.6.1)\n",
            "Requirement already satisfied: gradio-client==1.12.1 in /usr/local/lib/python3.12/dist-packages (from gradio) (1.12.1)\n",
            "Requirement already satisfied: groovy~=0.1 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.1.2)\n",
            "Requirement already satisfied: httpx<1.0,>=0.24.1 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.28.1)\n",
            "Requirement already satisfied: huggingface-hub<1.0,>=0.33.5 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.34.4)\n",
            "Requirement already satisfied: jinja2<4.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (3.1.6)\n",
            "Requirement already satisfied: markupsafe<4.0,>=2.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (3.0.2)\n",
            "Requirement already satisfied: numpy<3.0,>=1.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (2.0.2)\n",
            "Requirement already satisfied: orjson~=3.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (3.11.3)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.12/dist-packages (from gradio) (25.0)\n",
            "Requirement already satisfied: pandas<3.0,>=1.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (2.2.2)\n",
            "Requirement already satisfied: pillow<12.0,>=8.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (11.3.0)\n",
            "Requirement already satisfied: pydantic<2.12,>=2.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (2.11.7)\n",
            "Requirement already satisfied: pydub in /usr/local/lib/python3.12/dist-packages (from gradio) (0.25.1)\n",
            "Requirement already satisfied: python-multipart>=0.0.18 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.0.20)\n",
            "Requirement already satisfied: pyyaml<7.0,>=5.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (6.0.2)\n",
            "Requirement already satisfied: ruff>=0.9.3 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.12.12)\n",
            "Requirement already satisfied: safehttpx<0.2.0,>=0.1.6 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.1.6)\n",
            "Requirement already satisfied: semantic-version~=2.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (2.10.0)\n",
            "Requirement already satisfied: starlette<1.0,>=0.40.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.47.3)\n",
            "Requirement already satisfied: tomlkit<0.14.0,>=0.12.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.13.3)\n",
            "Requirement already satisfied: typer<1.0,>=0.12 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.17.3)\n",
            "Requirement already satisfied: typing-extensions~=4.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (4.15.0)\n",
            "Requirement already satisfied: uvicorn>=0.14.0 in /usr/local/lib/python3.12/dist-packages (from gradio) (0.35.0)\n",
            "Requirement already satisfied: fsspec in /usr/local/lib/python3.12/dist-packages (from gradio-client==1.12.1->gradio) (2025.3.0)\n",
            "Requirement already satisfied: websockets<16.0,>=10.0 in /usr/local/lib/python3.12/dist-packages (from gradio-client==1.12.1->gradio) (15.0.1)\n",
            "Requirement already satisfied: idna>=2.8 in /usr/local/lib/python3.12/dist-packages (from anyio<5.0,>=3.0->gradio) (3.10)\n",
            "Requirement already satisfied: sniffio>=1.1 in /usr/local/lib/python3.12/dist-packages (from anyio<5.0,>=3.0->gradio) (1.3.1)\n",
            "Requirement already satisfied: certifi in /usr/local/lib/python3.12/dist-packages (from httpx<1.0,>=0.24.1->gradio) (2025.8.3)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx<1.0,>=0.24.1->gradio) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx<1.0,>=0.24.1->gradio) (0.16.0)\n",
            "Requirement already satisfied: filelock in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<1.0,>=0.33.5->gradio) (3.19.1)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<1.0,>=0.33.5->gradio) (2.32.4)\n",
            "Requirement already satisfied: tqdm>=4.42.1 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<1.0,>=0.33.5->gradio) (4.67.1)\n",
            "Requirement already satisfied: hf-xet<2.0.0,>=1.1.3 in /usr/local/lib/python3.12/dist-packages (from huggingface-hub<1.0,>=0.33.5->gradio) (1.1.9)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas<3.0,>=1.0->gradio) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3.0,>=1.0->gradio) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3.0,>=1.0->gradio) (2025.2)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from pydantic<2.12,>=2.0->gradio) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.33.2 in /usr/local/lib/python3.12/dist-packages (from pydantic<2.12,>=2.0->gradio) (2.33.2)\n",
            "Requirement already satisfied: typing-inspection>=0.4.0 in /usr/local/lib/python3.12/dist-packages (from pydantic<2.12,>=2.0->gradio) (0.4.1)\n",
            "Requirement already satisfied: click>=8.0.0 in /usr/local/lib/python3.12/dist-packages (from typer<1.0,>=0.12->gradio) (8.2.1)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.12/dist-packages (from typer<1.0,>=0.12->gradio) (1.5.4)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.12/dist-packages (from typer<1.0,>=0.12->gradio) (13.9.4)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas<3.0,>=1.0->gradio) (1.17.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.12/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (4.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.12/dist-packages (from rich>=10.11.0->typer<1.0,>=0.12->gradio) (2.19.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests->huggingface-hub<1.0,>=0.33.5->gradio) (3.4.3)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests->huggingface-hub<1.0,>=0.33.5->gradio) (2.5.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.12/dist-packages (from markdown-it-py>=2.2.0->rich>=10.11.0->typer<1.0,>=0.12->gradio) (0.1.2)\n"
          ]
        }
      ],
      "source": [
        "%pip install gradio"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "d640add4"
      },
      "source": [
        "## ปรับโครงสร้างโค้ดคำนวณ (refactor calculation code)\n",
        "\n",
        "### Subtask:\n",
        "ปรับฟังก์ชันคำนวณ `calculate_flighting_development` ให้รับค่าอินพุตเป็นอาร์กิวเมนต์ของฟังก์ชัน แทนการใช้ `input()`.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "f1b1b874"
      },
      "source": [
        "**Reasoning**:\n",
        "Modify the `calculate_flighting_development` function to accept parameters instead of using `input()`, remove the Excel saving prompt, and update the function calls in other cells.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "fce176e8"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd # Import pandas for Excel output\n",
        "from google.colab import drive # Import drive for saving to Google Drive\n",
        "\n",
        "def calculate_flighting_development(outer_diameter_str, inner_diameter_str, pitch_str, material_thickness_str):\n",
        "    \"\"\"Calculates the development of a screw conveyor flighting based on user input and returns the results.\n",
        "\n",
        "    Args:\n",
        "        outer_diameter_str: String input for Outer Diameter (mm).\n",
        "        inner_diameter_str: String input for Inner Diameter (mm).\n",
        "        pitch_str: String input for Pitch (mm).\n",
        "        material_thickness_str: String input for Material Thickness (mm).\n",
        "\n",
        "    Returns:\n",
        "        A dictionary containing the calculated flat pattern radii and angle, or None if input is invalid.\n",
        "    \"\"\"\n",
        "    try:\n",
        "        target_outer_diameter = float(outer_diameter_str) # This is the target outer diameter\n",
        "        target_inner_diameter = float(inner_diameter_str) # This is the target inner diameter (pipe OD)\n",
        "        pitch = float(pitch_str)\n",
        "        material_thickness = float(material_thickness_str)\n",
        "\n",
        "        # --- General Adjustment for Inner Diameter in Flat Pattern ---\n",
        "        # Increase the inner diameter of the flat pattern based on material thickness.\n",
        "        # This is a general adjustment and may need empirical tuning for specific materials/processes.\n",
        "        inner_diameter_flat_pattern = target_inner_diameter + material_thickness\n",
        "        # print(\"\\n--- Using General Adjustment for Inner Diameter for Flat Pattern ---\")\n",
        "        # print(f\"  (Target Inner Diameter + Material Thickness)\")\n",
        "        # ----------------------------------------------------\n",
        "\n",
        "        # --- Outer Diameter for Flat Pattern ---\n",
        "        # Use the target outer diameter for the flat pattern calculation.\n",
        "        # Note: Empirical testing may be needed for outer diameters as well to refine this.\n",
        "        outer_diameter_flat_pattern = target_outer_diameter\n",
        "        # print(\"--- Using Target Outer Diameter for Flat Pattern ---\")\n",
        "        # ----------------------------------------------------------\n",
        "\n",
        "\n",
        "        # 1. Calculate outer radius for the FLAT PATTERN (R_outer_flat_pattern)\n",
        "        R_outer_flat_pattern = outer_diameter_flat_pattern / 2\n",
        "\n",
        "        # 2. Calculate inner radius for the FLAT PATTERN (R_inner_flat_pattern)\n",
        "        R_inner_flat_pattern = inner_diameter_flat_pattern / 2\n",
        "\n",
        "        # 3. Calculate outer circumference for the FLAT PATTERN (C_outer_flat_pattern)\n",
        "        C_outer_flat_pattern = 2 * np.pi * R_outer_flat_pattern\n",
        "\n",
        "        # 4. Calculate outer arc length (L_outer) - This is calculated based on the FLAT PATTERN outer circumference and the PITCH\n",
        "        L_outer = np.sqrt(C_outer_flat_pattern**2 + pitch**2)\n",
        "\n",
        "        # 5. Calculate inner circumference for the FLAT PATTERN (C_inner_flat_pattern)\n",
        "        C_inner_flat_pattern = 2 * np.pi * R_inner_flat_pattern\n",
        "\n",
        "        # 6. Calculate inner arc length for the FLAT PATTERN (L_inner_flat_pattern) - This is calculated based on the FLAT PATTERN inner circumference and the PITCH\n",
        "        L_inner_flat_pattern = np.sqrt(C_inner_flat_pattern**2 + pitch**2)\n",
        "\n",
        "\n",
        "        # 7. Calculate the width of the developed blank (Width)\n",
        "        # Width is the difference between outer and inner radii of the FLAT PATTERN\n",
        "        Width = R_outer_flat_pattern - R_inner_flat_pattern\n",
        "\n",
        "        # 8. Calculate the angle of the developed blank (Angle) in degrees\n",
        "        # Using the formula: (L_outer / R_outer) * (180 / pi)\n",
        "        # Note: Use R_outer_flat_pattern for this calculation as L_outer was based on it\n",
        "        Angle = (L_outer / R_outer_flat_pattern) * (180 / np.pi)\n",
        "\n",
        "        # print(\"\\n--- Calculation Results for Flat Pattern ---\")\n",
        "        # print(f\"Target Outer Diameter: {target_outer_diameter:.2f} mm\")\n",
        "        # print(f\"Target Inner Diameter (Pipe OD): {target_inner_diameter:.2f} mm\")\n",
        "        # print(f\"Material Thickness: {material_thickness:.2f} mm\")\n",
        "        # print(\"-\" * 30)\n",
        "        # print(f\"Flat Pattern Outer Diameter: {outer_diameter_flat_pattern:.2f} mm\")\n",
        "        # print(f\"Flat Pattern Inner Diameter: {inner_diameter_flat_pattern:.2f} mm\")\n",
        "        # print(f\"Developed Width: {Width:.2f} mm\")\n",
        "        # print(f\"Developed Angle: {Angle:.2f} degrees\")\n",
        "\n",
        "        # Store the results in a dictionary\n",
        "        results = {\n",
        "            \"Input Outer Diameter (mm)\": target_outer_diameter,\n",
        "            \"Input Inner Diameter (Pipe OD) (mm)\": target_inner_diameter,\n",
        "            \"Input Pitch (mm)\": pitch,\n",
        "            \"Input Material Thickness (mm)\": material_thickness,\n",
        "            \"Flat Pattern Outer Diameter (mm)\": outer_diameter_flat_pattern,\n",
        "            \"Flat Pattern Inner Diameter (mm)\": inner_diameter_flat_pattern,\n",
        "            \"Developed Width (mm)\": Width,\n",
        "            \"Developed Angle (degrees)\": Angle\n",
        "        }\n",
        "\n",
        "        # Return the calculated values for the flat pattern for plotting and display\n",
        "        return {\n",
        "            \"R_outer_flat_pattern\": R_outer_flat_pattern,\n",
        "            \"R_inner_flat_pattern\": R_inner_flat_pattern,\n",
        "            \"Angle\": Angle,\n",
        "            \"Display_Results\": results # Include all results for display\n",
        "        }\n",
        "\n",
        "    except ValueError:\n",
        "        print(\"Invalid input. Please enter numeric values for all parameters.\")\n",
        "        return None # Return None in case of error\n",
        "    except Exception as e:\n",
        "        print(f\"An error occurred: {e}\")\n",
        "        return None # Return None in case of error\n",
        "\n",
        "# Update the function call in the next cell\n",
        "# calculate_flighting_development()\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "dbcce50b"
      },
      "source": [
        "**Reasoning**:\n",
        "Update the function call in the plotting cell to pass example values to the modified `calculate_flighting_development` function.\n",
        "\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "28ede7ca"
      },
      "source": [
        "## สร้างส่วนติดต่อผู้ใช้ด้วย gradio (create gradio interface)\n",
        "\n",
        "### Subtask:\n",
        "ใช้ Gradio เพื่อสร้างอินเทอร์เฟซที่ประกอบด้วยช่องป้อนข้อมูลสำหรับ Outer Diameter, Inner Diameter, Pitch, Material Thickness และแสดงผลลัพธ์การคำนวณและรูปภาพ.\n"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ddb533a4"
      },
      "source": [
        "**Reasoning**:\n",
        "Import the gradio library and define the Gradio interface with inputs for the required parameters and outputs for the calculation results and the plot.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "963663a5",
        "outputId": "5bf3e730-7951-45b0-b395-2ef8578561f4"
      },
      "outputs": [
        {
          "name": "stderr",
          "output_type": "stream",
          "text": [
            "/usr/local/lib/python3.12/dist-packages/gradio/interface.py:414: UserWarning: The `allow_flagging` parameter in `Interface` is deprecated. Use `flagging_mode` instead.\n",
            "  warnings.warn(\n"
          ]
        }
      ],
      "source": [
        "import gradio as gr\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "def calculate_and_plot_flighting(outer_diameter_str, inner_diameter_str, pitch_str, material_thickness_str):\n",
        "    \"\"\"Calculates the development of a screw conveyor flighting, generates a plot, and returns the results and plot.\n",
        "\n",
        "    Args:\n",
        "        outer_diameter_str: String input for Outer Diameter (mm).\n",
        "        inner_diameter_str: String input for Inner Diameter (mm).\n",
        "        pitch_str: String input for Pitch (mm).\n",
        "        material_thickness_str: String input for Material Thickness (mm).\n",
        "\n",
        "    Returns:\n",
        "        A tuple containing a formatted string of calculation results and a matplotlib figure,\n",
        "        or an error message and None if input is invalid.\n",
        "    \"\"\"\n",
        "    calculated_results = calculate_flighting_development(outer_diameter_str, inner_diameter_str, pitch_str, material_thickness_str)\n",
        "\n",
        "    if calculated_results:\n",
        "        R_outer_flat_pattern = calculated_results[\"R_outer_flat_pattern\"]\n",
        "        R_inner_flat_pattern = calculated_results[\"R_inner_flat_pattern\"]\n",
        "        Angle = calculated_results[\"Angle\"]\n",
        "        display_results = calculated_results[\"Display_Results\"]\n",
        "\n",
        "        # Format the results for display\n",
        "        results_string = (\n",
        "            f\"--- Calculation Results for Flat Pattern ---\\n\"\n",
        "            f\"Target Outer Diameter: {display_results['Input Outer Diameter (mm)']:.2f} mm\\n\"\n",
        "            f\"Target Inner Diameter (Pipe OD): {display_results['Input Inner Diameter (Pipe OD) (mm)']:.2f} mm\\n\"\n",
        "            f\"Material Thickness: {display_results['Input Material Thickness (mm)']:.2f} mm\\n\"\n",
        "            f\"------------------------------\\n\"\n",
        "            f\"Flat Pattern Outer Diameter: {display_results['Flat Pattern Outer Diameter (mm)']:.2f} mm\\n\"\n",
        "            f\"Flat Pattern Inner Diameter: {display_results['Flat Pattern Inner Diameter (mm)']:.2f} mm\\n\"\n",
        "            f\"Developed Width: {display_results['Developed Width (mm)']:.2f} mm\\n\"\n",
        "            f\"Developed Angle: {display_results['Developed Angle (degrees)']:.2f} degrees\"\n",
        "        )\n",
        "\n",
        "\n",
        "        # Ensure Angle is in radians for plotting\n",
        "        angle_rad = np.deg2rad(Angle)\n",
        "\n",
        "        # Create a polar plot\n",
        "        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})\n",
        "\n",
        "        # Plot the outer arc\n",
        "        theta_outer = np.linspace(0, angle_rad, 100)\n",
        "        r_outer = np.full_like(theta_outer, R_outer_flat_pattern)\n",
        "        ax.plot(theta_outer, r_outer, color='blue', label=f'Flat Pattern Outer Radius ({R_outer_flat_pattern:.2f} mm)')\n",
        "\n",
        "        # Plot the inner arc\n",
        "        theta_inner = np.linspace(0, angle_rad, 100)\n",
        "        r_inner = np.full_like(theta_inner, R_inner_flat_pattern)\n",
        "        ax.plot(theta_inner, r_inner, color='red', label=f'Flat Pattern Inner Radius ({R_inner_flat_pattern:.2f} mm)')\n",
        "\n",
        "        # Plot the connecting lines (sides of the segment)\n",
        "        ax.plot([0, 0], [R_inner_flat_pattern, R_outer_flat_pattern], color='black')\n",
        "        ax.plot([angle_rad, angle_rad], [R_inner_flat_pattern, R_outer_flat_pattern], color='black')\n",
        "\n",
        "        # Set plot properties\n",
        "        ax.set_title(\"Developed Screw Conveyor Flighting Blank (Based on Flat Pattern Dimensions)\", va='bottom')\n",
        "        ax.set_theta_zero_location(\"N\")\n",
        "        ax.set_theta_direction(-1)\n",
        "        # Adjust rticks based on the new inner/outer radii\n",
        "        max_radius = max(R_outer_flat_pattern, R_inner_flat_pattern)\n",
        "        min_radius = min(R_outer_flat_pattern, R_inner_flat_pattern)\n",
        "        ax.set_rticks(np.linspace(min_radius, max_radius, num=5)) # Adjust num as needed for clarity\n",
        "        ax.set_rlabel_position(-22.5)\n",
        "        ax.grid(True)\n",
        "        ax.legend(loc='upper right')\n",
        "\n",
        "\n",
        "        return results_string, fig\n",
        "    else:\n",
        "        return \"Calculation failed. Please check your inputs.\", None\n",
        "\n",
        "\n",
        "# Define Gradio inputs and outputs\n",
        "inputs = [\n",
        "    gr.Textbox(label=\"Outer Diameter (mm)\"),\n",
        "    gr.Textbox(label=\"Inner Diameter (mm)\"),\n",
        "    gr.Textbox(label=\"Pitch (mm)\"),\n",
        "    gr.Textbox(label=\"Material Thickness (mm)\")\n",
        "]\n",
        "\n",
        "outputs = [\n",
        "    gr.Textbox(label=\"Calculation Results\"),\n",
        "    gr.Plot(label=\"Developed Flighting Blank\")\n",
        "]\n",
        "\n",
        "# Create the Gradio interface\n",
        "iface = gr.Interface(\n",
        "    fn=calculate_and_plot_flighting,\n",
        "    inputs=inputs,\n",
        "    outputs=outputs,\n",
        "    title=\"Screw Conveyor Flighting Development Calculator\",\n",
        "    description=\"Enter the dimensions to calculate the developed blank for a screw conveyor flighting and see the flat pattern.\",\n",
        "    allow_flagging=\"never\" # Disable flagging\n",
        ")\n",
        "\n",
        "# To launch the interface, you would typically add:\n",
        "# iface.launch()"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "fc4e8736"
      },
      "source": [
        "**Reasoning**:\n",
        "Launch the Gradio interface to allow user interaction with the calculation and plotting functionality.\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true,
          "base_uri": "https://localhost:8080/",
          "height": 625
        },
        "id": "MaCydckBa1Qc",
        "outputId": "2af07bac-0274-4f46-9dd4-06d4f8af8252"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "It looks like you are running Gradio on a hosted Jupyter notebook, which requires `share=True`. Automatically setting `share=True` (you can turn this off by setting `share=False` in `launch()` explicitly).\n",
            "\n",
            "Colab notebook detected. This cell will run indefinitely so that you can see errors and logs. To turn off, set debug=False in launch().\n",
            "* Running on public URL: https://877f970518f9b09667.gradio.live\n",
            "\n",
            "This share link expires in 1 week. For free permanent hosting and GPU upgrades, run `gradio deploy` from the terminal in the working directory to deploy to Hugging Face Spaces (https://huggingface.co/spaces)\n"
          ]
        },
        {
          "data": {
            "text/html": [
              "<div><iframe src=\"https://877f970518f9b09667.gradio.live\" width=\"100%\" height=\"500\" allow=\"autoplay; camera; microphone; clipboard-read; clipboard-write;\" frameborder=\"0\" allowfullscreen></iframe></div>"
            ],
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ]
          },
          "metadata": {},
          "output_type": "display_data"
        }
      ],
      "source": [
        "iface.launch(debug=True)"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOW1G1XRK4bMPo4aP9k0H6h",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
