import pandas as pd


all_truck = pd.read_csv('wassup.csv')
all_truck['time_y'] = pd.to_datetime(all_truck['time'], format = "%Y-%m-%d %H:%M:%S.%f")
all_truck = all_truck.set_index('time_y')
seconds_resampled_data = all_truck.resample('1S').interpolate()

print(seconds_resampled_data.head())
seconds_resampled_data.to_csv('new_data.csv')