import json
import pandas as pd
from datetime import datetime


def env_data_to_csv():
	with open("C:/kool/thesis/sphere_1m_env/ENV.bson.dump") as f:
		content = f.readlines()

	devices = []
	datetimes = []
	sensors = []
	values = []

	for line in content:
		line = json.loads(line.strip())
		device_id = line['uid']
		dt = line['bt']['$date']
		for e in line['e']:
			n = e['n']
			v = e['v']
			devices.append(device_id)
			datetimes.append(datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S"))
			sensors.append(n)
			values.append(v)

	df = pd.DataFrame({'device_id' : devices,
						'datetime' : datetimes,
						'sensor' : sensors,
						'value' : values})

	df.to_csv("ENV_all.csv")


def minimize_video_data():
	with open("C:/kool/thesis/sphere_1m_env/VID.bsondump_without_silhouettes.txt") as f:
		content = f.readlines()

	file = open("C:/kool/thesis/sphere_1m_env/VID.min_bsondump_without_silhouettes.txt", "w")
	i = 0
	for line in content:
		file.write(str(line))
		i += 1
		if i >= 20000:
			break
	file.close()


def video_data_to_csv():
	devices = []
	datetimes = []
	keys = []
	values = []

	f = open("C:/kool/thesis/sphere_1m_env/VID.bsondump_without_silhouettes.txt")
	line = f.readline()

	while line != "":
		try:
			line = line.replace("+Infinity", "10")
			line = json.loads(line.strip())
			device_id = line['uid']
			datetime = line['bt']['$date']
			for e in line['e']:
				key = e['n']
				if key not in ['frameID', 'userID', 'FeaturesREID']:
					v = e['v']
					devices.append(device_id)
					datetimes.append(datetime)
					keys.append(key)
					values.append(v)
		except json.decoder.JSONDecodeError:
			print("error on line:")
			print(line)
		line = f.readline()
	f.close()

	df = pd.DataFrame({'device_id' : devices,
						'datetime' : datetimes,
						'key' : keys,
						'value' : values})

	df.to_csv("C:/kool/thesis/sphere_1m_env/video_all.csv")



#minimize_video_data()
video_data_to_csv()
#sth()
#env_data_to_csv()

#print(datetime.datetime.now())

