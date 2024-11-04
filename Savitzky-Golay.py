import requests
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from datetime import datetime

# Step 1: Fetch data from Open Meteo API
url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 52.52,
    "longitude": 13.41,
    "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}
response = requests.get(url, params=params)
data = response.json()

# Step 2: Parse data into arrays
times = [datetime.fromisoformat(t) for t in data['hourly']['time']]
temperature = np.array(data['hourly']['temperature_2m'])
humidity = np.array(data['hourly']['relative_humidity_2m'])
wind_speed = np.array(data['hourly']['wind_speed_10m'])

# Step 3: Data Processing
# Apply a Savitzky-Golay filter for smoothing
temperature_smooth = signal.savgol_filter(temperature, window_length=11, polyorder=2)
humidity_smooth = signal.savgol_filter(humidity, window_length=11, polyorder=2)
wind_speed_smooth = signal.savgol_filter(wind_speed, window_length=11, polyorder=2)

# Fourier Transform to analyze frequency components of temperature
temp_fft = fft(temperature)
freqs = fftfreq(len(temperature), d=1)  # Assuming hourly data

# Step 4: Plotting

# Create a new figure with subplots for smoothed data and Fourier Transform
fig, axs = plt.subplots(3, 1, figsize=(14, 12))
fig.suptitle("Weather Data Analysis with Smoothing and Frequency Analysis")

# Subplot 1: Temperature with smoothed line
axs[0].plot(times, temperature, label="Temperature (°C)", color="orange")
axs[0].plot(times, temperature_smooth, label="Smoothed Temperature", color="red", linestyle="--")
axs[0].set_title("Temperature Over Time")
axs[0].set_xlabel("Time")
axs[0].set_ylabel("Temperature (°C)")
axs[0].legend()
axs[0].tick_params(axis='x', rotation=45)

# Subplot 2: Humidity with smoothed line
axs[1].plot(times, humidity, label="Humidity (%)", color="blue")
axs[1].plot(times, humidity_smooth, label="Smoothed Humidity", color="cyan", linestyle="--")
axs[1].set_title("Relative Humidity Over Time")
axs[1].set_xlabel("Time")
axs[1].set_ylabel("Humidity (%)")
axs[1].legend()
axs[1].tick_params(axis='x', rotation=45)

# Subplot 3: Wind Speed with smoothed line
axs[2].plot(times, wind_speed, label="Wind Speed (m/s)", color="green")
axs[2].plot(times, wind_speed_smooth, label="Smoothed Wind Speed", color="lime", linestyle="--")
axs[2].set_title("Wind Speed Over Time")
axs[2].set_xlabel("Time")
axs[2].set_ylabel("Wind Speed (m/s)")
axs[2].legend()
axs[2].tick_params(axis='x', rotation=45)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()