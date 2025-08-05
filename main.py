Creating a "Smart Energy Dashboard" involves several components including data collection, real-time data visualization, and recommendations for optimizing energy consumption. Below is a simplified version of a Python program that focuses on the core functionality of this project. For the sake of example, we'll simulate real-time data and visualization, as actual implementation would require integrating hardware sensors or APIs to fetch data.

Ensure you have the required libraries installed:
```bash
pip install matplotlib numpy
```

Here's a Python script with simulated data:

```python
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated Data Generator
def generate_energy_data():
    # Simulates hourly energy consumption for a day (in kilowatt-hours)
    try:
        data = np.random.uniform(low=0.5, high=5.0, size=24)
        logging.info("Generated energy data successfully.")
        return data
    except Exception as e:
        logging.error(f"Error in generating energy data: {e}")
        return np.zeros(24)

# Real-time Data Visualization
def visualize_energy_data(data):
    try:
        plt.figure(figsize=(10, 5))
        plt.plot(data, marker='o')
        plt.title('Home Energy Consumption')
        plt.xlabel('Hour')
        plt.ylabel('Energy (kWh)')
        plt.xticks(range(24), [f'{x}:00' for x in range(24)])
        plt.grid(True)
        plt.show()
        logging.info("Data visualization successful.")
    except Exception as e:
        logging.error(f"Error in data visualization: {e}")

# Recommendations based on data
def energy_recommendations(data):
    try:
        avg_consumption = np.mean(data)
        peak_hour = np.argmax(data)
        logging.info("Analysis for recommendations complete.")

        recommendations = [
            f"Your average daily energy consumption is {avg_consumption:.2f} kWh.",
            f"Peak energy consumption occurs at {peak_hour}:00 with {data[peak_hour]:.2f} kWh."
        ]

        if avg_consumption > 3.5:
            recommendations.append("Consider reducing your energy usage during peak hours.")
        if np.max(data) > 4.0:
            recommendations.append("Look into why consumption spikes above 4.0 kWh during peak times.")

        return recommendations
    except Exception as e:
        logging.error(f"Error in generating recommendations: {e}")
        return ["Unable to generate recommendations due to an error."]

# Main Function
def main():
    try:
        data = generate_energy_data()
        visualize_energy_data(data)
        recommendations = energy_recommendations(data)
        for recommendation in recommendations:
            print(recommendation)
    except Exception as e:
        logging.critical(f"Critical error in main execution: {e}")

if __name__ == "__main__":
    main()
```

### Explanation:

1. **Data Simulation**: The energy data is simulated using a random number generator that creates energy consumption values for every hour of a day. This is a placeholder for real sensor data.

2. **Visualization**: The program uses `matplotlib` to visualize the hourly energy consumption.

3. **Recommendations**: Basic statistical analysis is performed to generate energy-saving recommendations based on average usage and peak consumption.

4. **Logging and Error Handling**: The program uses Python’s built-in logging module to report the status and handle any errors in the data generation, visualization, and recommendations steps.

For real-world applications, this program would need to interface with actual hardware or APIs to fetch and react to real-time data. Additional functionalities like scheduling, remote access, and integration with external data sources might also be required.