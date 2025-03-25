import requests
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# OpenWeatherMap API configuration
API_KEY = "c53c3c8d8feeffeb3e9d4a17493ccf1f"  
CITY = "Pune"  # Change city as needed
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# Fetch data from the API
response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
else:
    print("Failed to fetch data. Check your API key and internet connection.")
    exit()

# Extract relevant data
dates = []
temps = []
humidities = []

for entry in data.get("list", []):
    dates.append(entry["dt_txt"])
    temps.append(entry["main"]["temp"])
    humidities.append(entry["main"]["humidity"])

# Create DataFrame
df = pd.DataFrame({"Date": dates, "Temperature": temps, "Humidity": humidities})
df["Date"] = pd.to_datetime(df["Date"])

# Plot data
plt.figure(figsize=(10, 5))
sns.set_style("whitegrid")
sns.lineplot(x=df["Date"], y=df["Temperature"], label="Temp (°C)", color="red", marker="o")
sns.lineplot(x=df["Date"], y=df["Humidity"], label="Humidity (%)", color="blue", marker="s")

plt.xlabel("Date & Time", fontsize=12)
plt.ylabel("Values", fontsize=12)
plt.title(f"Weather Forecast for {CITY}", fontsize=14)
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.legend()
plt.show()
