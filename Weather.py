import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import stats

# Step 1: Fetch Data from Open Meteo API
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}
response = requests.get(url, params=params)
data = response.json()

# Step 2: Parse Data into DataFrames
times = [datetime.fromisoformat(t) for t in data['hourly']['time']]
temperature = np.array(data['hourly']['temperature_2m'])
humidity = np.array(data['hourly']['relative_humidity_2m'])
wind_speed = np.array(data['hourly']['wind_speed_10m'])

# Create a DataFrame for easy data handling
df = pd.DataFrame({
    "Time": times,
    "Temperature (°C)": temperature,
    "Humidity (%)": humidity,
    "Wind Speed (m/s)": wind_speed
})

# Step 3: Statistical Analysis
try:
    temperature_mode = stats.mode(temperature, keepdims=True).mode[0]
except IndexError:
    temperature_mode = None

try:
    wind_speed_mode = stats.mode(wind_speed, keepdims=True).mode[0]
except IndexError:
    wind_speed_mode = None

temperature_stats = {
    "Max Temp": np.max(temperature),
    "Min Temp": np.min(temperature),
    "Range Temp": np.ptp(temperature),
    "Mean Temp": np.mean(temperature),
    "Median Temp": np.median(temperature),
    "Mode Temp": temperature_mode
}

wind_speed_stats = {
    "Max Wind Speed": np.max(wind_speed),
    "Min Wind Speed": np.min(wind_speed),
    "Range Wind Speed": np.ptp(wind_speed),
    "Mean Wind Speed": np.mean(wind_speed),
    "Median Wind Speed": np.median(wind_speed),
    "Mode Wind Speed": wind_speed_mode
}

# Print summary statistics
print("\nTemperature Statistics:")
print(pd.DataFrame(temperature_stats, index=[0]).T)
print("\nWind Speed Statistics:")
print(pd.DataFrame(wind_speed_stats, index=[0]).T)

# Step 4: Visualization
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Weather Data Analysis")

# Line Graph - Temperature and Wind Speed Over Time
axs[0, 0].plot(df["Time"], df["Temperature (°C)"], label="Temperature (°C)", color="orange")
axs[0, 0].plot(df["Time"], df["Wind Speed (m/s)"], label="Wind Speed (m/s)", color="blue")
axs[0, 0].set_title("Temperature and Wind Speed Over Time")
axs[0, 0].set_xlabel("Time")
axs[0, 0].set_ylabel("Value")
axs[0, 0].legend()
axs[0, 0].tick_params(axis='x', rotation=45)

# Bar Graph - Daily Wind Speed Range
daily_wind_speed_range = df.resample('D', on="Time")["Wind Speed (m/s)"].apply(np.ptp)
axs[0, 1].bar(daily_wind_speed_range.index, daily_wind_speed_range, color="cyan")
axs[0, 1].set_title("Daily Wind Speed Range")
axs[0, 1].set_xlabel("Day")
axs[0, 1].set_ylabel("Wind Speed Range (m/s)")
axs[0, 1].tick_params(axis='x', rotation=45)

# Monthly Climograph (Average Temperature and Wind Speed)
monthly_avg = df.resample('M', on="Time")[["Temperature (°C)", "Wind Speed (m/s)"]].mean()
ax2 = axs[1, 0]
ax2.bar(monthly_avg.index, monthly_avg["Wind Speed (m/s)"], color="lightblue", label="Avg Wind Speed (m/s)")
ax2.set_ylabel("Avg Wind Speed (m/s)", color="blue")
ax2.tick_params(axis="y", labelcolor="blue")
ax2.set_title("Monthly Climograph: Avg Temp and Wind Speed")

# Adding Temperature on the same axis but different y-axis
ax3 = ax2.twinx()
ax3.plot(monthly_avg.index, monthly_avg["Temperature (°C)"], color="red", marker="o", label="Avg Temperature (°C)")
ax3.set_ylabel("Avg Temperature (°C)", color="red")
ax3.tick_params(axis="y", labelcolor="red")

# Add legends for both y-axes in climograph subplot
ax2.legend(loc="upper left")
ax3.legend(loc="upper right")

# Summary Table in the last subplot
axs[1, 1].axis("off")
table_data = pd.DataFrame({
    "Temperature Stats": list(temperature_stats.values()),
    "Wind Speed Stats": list(wind_speed_stats.values())
}, index=list(temperature_stats.keys()))
axs[1, 1].table(cellText=table_data.values, colLabels=table_data.columns, rowLabels=table_data.index, loc="center")

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()