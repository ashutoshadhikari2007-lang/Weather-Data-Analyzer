Weather Data Analyzer 🌤️📊
A lightweight, high-performance weather data analytics engine built using Python and NumPy. This project analyzes multi-dimensional temperature datasets across multiple cities and months to extract statistical insights such as averages, extreme temperatures, fluctuations, threshold masks, and month-over-month trends.

🚀 GitHub Repository Description
Short Description (for GitHub About section): A hands-on Weather Data Analyzer built with Python & NumPy demonstrating 2D array manipulation, axis-wise aggregations, boolean masking, and data trends.

📌 Project Overview & Objectives
In real-world data science and scientific computing, geospatial and climate metrics are stored in multi-dimensional grids. This project demonstrates how to manipulate, filter, and analyze multi-dimensional matrix data without using heavy data-frame libraries, leveraging pure vectorized NumPy operations.

✨ Features
Multi-Dimensional Matrix Representation: Encapsulate multi-city, multi-month data in 2D NumPy arrays (Cities × Months).
Axis-Wise Aggregations:
Overall mean temperature across all datapoints.
City-wise mean temperature (axis=1).
Monthly mean temperature (axis=0).
Extrema Detection:
Hottest & Coldest cities using np.argmax() and np.argmin().
Peak temperature month lookup.
Temperature Fluctuation Analysis:
Calculates temperature range (Max - Min) per city to identify the region with the largest variation.
Threshold Filtering (Boolean Masking):
Filters out exact cities, months, and temperatures exceeding custom thresholds (e.g. > 20°C) using np.where().
Month-Over-Month Trend Calculation:
Vectorized adjacent differences using np.diff().
🛠️ Data Blueprint & Structure
The core temperature dataset is structured as a 2D NumPy array with dimensions (3, 3):

City / Month	Jan	Feb	March
Kathmandu	10°C	12°C	16°C
Pokhara	12°C	14°C	18°C
Chitwan	18°C	21°C	25°C
axis=0 (Vertical): Operates down columns (Month-by-Month across cities).
axis=1 (Horizontal): Operates across rows (City-by-City across months).
💻 Tech Stack
Language: Python 3.x
Library: NumPy (numpy)
