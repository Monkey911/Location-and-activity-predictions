import pandas as pd
import time
from datetime import timedelta, datetime

data = pd.read_csv("C:/kool/thesis/sphere_1m_env/ENV_all.csv", index_col=0)
data['datetime'] = pd.to_datetime(data['datetime'], format="%Y-%m-%d %H:%M:%S")
data.sort_values(["datetime"], ascending=False)

pir = data[data.sensor == "PIR_TRIGS"]
without_pir = data[data.sensor != "PIR_TRIGS"]

datetimes = []
device_id = []
value = []
sensors = []

for d_id in ["fd00::212:4b00:0:80", "fd00::212:4b00:0:81", "fd00::212:4b00:0:82", "fd00::212:4b00:0:83",
			"fd00::212:4b00:0:84", "fd00::212:4b00:0:85", "fd00::212:4b00:0:86", "fd00::212:4b00:0:87"]:
	print(d_id)
	sensor_data = pir[pir.device_id == d_id]
	sensor_data = sensor_data.reset_index(drop=True)
	sensor_length = len(sensor_data)

	start = time.time()
	for index, row in sensor_data.iterrows():
		current_datetime = row['datetime'] - timedelta(0, 30)
		if index + 1 < sensor_length:
			next_datetime = sensor_data.iloc[index + 1]['datetime'] - timedelta(0, 30)
		else:
			next_datetime = sensor_data.iloc[0]['datetime'] - timedelta(0, 30)

		values = row['value']
		values = values.replace("[", "")
		values = values.replace("]", "")
		values = values.split(", ")
		for i in range(30):
			if current_datetime == next_datetime:
				break
			datetimes.append(current_datetime)
			device_id.append(d_id)
			value.append(int(values[i]))
			current_datetime = current_datetime + timedelta(0, 1)
	end = time.time()
	print("selleks kulus: " + str(end-start))

df = pd.DataFrame({'device_id' : device_id,
				   'datetime' : datetimes,
					'sensor' : "PIR_TRIGS",
					'value' : value})
result = pd.concat([without_pir, df])
result.to_csv("ENV_all_edited.csv")



