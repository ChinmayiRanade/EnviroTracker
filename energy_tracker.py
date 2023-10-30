import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#random data
data = {
    'Energy Consumption Time': pd.date_range(start='2023-10-01 00:00', periods=72, freq='H'),
    'Electricity (kWh)': np.random.uniform(5, 25, 72),
    'Gas (Cubic Feet)': np.random.uniform(10, 25, 72)
}

df = pd.DataFrame(data)

total_electricity_used = df['Electricity (kWh)'].sum()
total_gas = df['Gas (Cubic Feet)'].sum()
total_electricity_used_avg = df['Electricity (kWh)'].mean()
total_gas_avg = df['Gas (Cubic Feet)'].mean()

plt.figure(figsize=(10, 6))
plt.plot(df['Energy Consumption Time'], df['Electricity (kWh)'], label='Electricity (kWh)', marker='o')
plt.plot(df['Energy Consumption Time'], df['Gas (Cubic Feet)'], label='Gas (Cubic Feet)', marker='o')
plt.xlabel('Time')
plt.ylabel('Consumption')
plt.title('Energy Consumption Over Time')
plt.legend()
plt.grid()

#websites don't work, can't implement through matplotlib
if total_electricity_used_avg > 15:
    plt.text(df['Energy Consumption Time'].iloc[0], 7.5, "Your electricity consumption is high. Consider energy-efficient products like solar chargers.", fontsize=14, color='red', fontname='Times New Roman')
    
    
if total_gas_avg > 20:
    plt.text(df['Energy Consumption Time'].iloc[0], 7.5, "Your gas consumption is high. Check for any gas leaks to optimize usage. Explore gas-saving products", fontsize=14, color='red', fontname='Times New Roman')
   


plt.show()
