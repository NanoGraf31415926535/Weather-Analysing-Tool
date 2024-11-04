```markdown
# Weather Data Analysis Project

This project analyzes weather data retrieved from the [Open Meteo API](https://open-meteo.com/). It provides insights into temperature, humidity, and wind speed trends using various data analysis techniques, smoothing functions, and frequency analysis. Visualizations include line charts, smoothed data trends, and frequency (Fourier) analysis for temperature.

## Features
- **Data Retrieval**: Fetches hourly weather data for a specified location (Berlin, Germany).
- **Data Smoothing**: Applies a Savitzky-Golay filter to smooth temperature, humidity, and wind speed data.
- **Statistical Analysis**: Calculates basic statistical metrics like maximum, minimum, mean, median, and mode for temperature and wind speed.
- **Visualizations**:
  - Temperature, humidity, and wind speed over time with smoothed trend lines.
  - Daily and monthly summaries, including range and average wind speed.
  - Fourier Transform analysis of temperature data to identify periodic trends.

## Setup and Installation

### Prerequisites
- Python 3.x
- The following Python packages:
  - `requests`
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `scipy`

To install the required packages, run:
```bash
pip install requests numpy pandas matplotlib scipy
```

### Running the Project
1. **Clone this repository** (or download the code files).
2. **Run the main analysis script**:
    ```bash
    python Weather.py
    ```
3. **View the output**: The script will fetch data from the Open Meteo API, perform statistical analyses, and display a series of graphs for temperature, humidity, and wind speed.

### API Information
The script retrieves data using the Open Meteo API. The specific endpoint used provides hourly temperature, humidity, and wind speed data for Berlin (latitude: 52.52, longitude: 13.41).

## Code Structure

- **Data Retrieval**: Fetches weather data for temperature, humidity, and wind speed over a 24-hour period.
- **Data Processing**:
  - **Smoothing**: Uses the Savitzky-Golay filter to smooth time series data for better trend visualization.
  - **Fourier Transform**: Analyzes the frequency components of temperature data to detect periodic trends.
- **Visualizations**:
  - Line plots showing raw and smoothed data over time.
  - Bar charts and line graphs for data summaries.
  - Frequency analysis plot for temperature.

## Visualization Details

1. **Temperature, Humidity, and Wind Speed**: Displays hourly measurements with a trend line for each variable.
2. **Daily Wind Speed Range**: Shows daily wind speed fluctuations.
3. **Monthly Climograph**: Combines average monthly temperature and wind speed in one chart for high-level insights.
4. **Fourier Analysis**: Temperature frequency analysis identifies any cyclical patterns in the data.

## Example Output
The code produces visualizations such as:
- Line graphs with trend lines for temperature, humidity, and wind speed.
- A Fourier Transform graph showing frequency components of temperature data.

## Notes and Future Enhancements

- **Extended Data Collection**: This script currently fetches limited data due to API constraints. Future iterations could store daily data for long-term trend analysis.
- **Additional Weather Metrics**: Incorporate other weather parameters like precipitation, atmospheric pressure, and UV index for a more comprehensive climate analysis.
- **Forecasting**: Implement a predictive model using historical data and time-series forecasting techniques.

## License
This project is licensed under the MIT License.

## Acknowledgments
- **Open Meteo API**: For providing open-access weather data.
- **Python**: Core libraries used for data handling and visualization.

---

Enjoy analyzing your weather data!
