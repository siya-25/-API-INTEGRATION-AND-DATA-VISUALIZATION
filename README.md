API-INTEGRATION-AND-DATA-VISUALIZATION


This project is designed to fetch weather forecast data from the OpenWeatherMap API and visualize temperature and humidity trends using Python. It incorporates essential programming techniques such as API integration, data extraction, data visualization, and error handling. The script is ideal for students learning how to work with real-world data using Python.

Libraries and Tools Used
The project makes use of the following Python libraries:

Requests: This library is used to make HTTP requests and fetch weather data from the OpenWeatherMap API. It is essential for communicating with web-based services.

Matplotlib: A widely used Python library for plotting graphs and visualizing data. It provides powerful tools for creating static, animated, and interactive visualizations.

Seaborn: A high-level data visualization library built on Matplotlib. It is particularly useful for statistical graphics and makes visualization more visually appealing and easier to interpret.

Pandas: Used for data manipulation and analysis, particularly for handling structured data such as time-series information. It simplifies the process of organizing and analyzing weather data fetched from the API.

How the Code Works
Fetching Data from OpenWeatherMap API

The script defines an API key and a city (Pune by default) to request weather data.

A request is sent to the OpenWeatherMap API using the requests.get() function.

The API response is returned in JSON format, containing weather forecasts for multiple timestamps.

If the API request is unsuccessful (e.g., due to an invalid API key or network issues), an error message is displayed, and the script exits.

Extracting Relevant Data

The script iterates through the JSON response to extract important weather details, such as date, temperature, and humidity.

This extracted data is stored in lists for further processing.

Storing Data in a Pandas DataFrame

The extracted data is structured using a Pandas DataFrame, making it easier to analyze and manipulate.

The Date column is converted into a proper datetime format to ensure accurate time-based plotting.

Visualizing the Data with Matplotlib and Seaborn

The script uses Matplotlib and Seaborn to plot two line graphs:

Temperature (°C) – Red Line with circular markers

Humidity (%) – Blue Line with square markers

The x-axis represents time, while the y-axis represents the values of temperature and humidity.

The graph is customized with labels, titles, legends, and rotated x-axis values for improved readability.

Where This Project Can Be Used
This script can be executed in different development environments, including:

Jupyter Notebook: Best for interactive coding and data visualization.

VS Code / PyCharm: Ideal for running Python scripts and debugging.

Google Colab: A cloud-based solution that allows execution without requiring local installations.

Why This Project is Useful for Students
This project is an excellent learning exercise for students who want to understand API integration, JSON data processing, and visualization techniques. It helps build practical programming skills that are essential for real-world applications such as weather monitoring, IoT analytics, and data science projects. By working with actual weather data, students can develop hands-on experience with external data sources and enhance their understanding of Python libraries used for data analysis.



#OUTPUT : ![Image](https://github.com/user-attachments/assets/99b8b3f1-c749-45f2-981c-27420342ce2e)
