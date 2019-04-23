from datetime import datetime, timedelta

file_numbers = [61, 62, 63, 64, 65, 66, 67, 68, 70, 71, 72]
file_beginning = "DS3500"
file_location = "C:/kool/thesis/sphere_1m_env/2018_02_06_annotations_for_andreas/"
output_directory = "C:/kool/thesis/sphere_1m_env/edited_annotations/"
date_format = "%Y-%m-%dT%H:%M:%S.%fZ"


def convert_annotations():
	for file_number in file_numbers:
		# Taking the starting time
		file = file_location + file_beginning + str(file_number) + "_start.txt"
		with open(file) as f:
			start_time = datetime.strptime(f.readline().strip(), date_format)

		# Converts the location labels
		file = file_location + file_beginning + str(file_number) + "_loc.txt"
		with open(file) as f:
			content = f.readlines()
		loc_fail = open(output_directory + file_beginning + str(file_number) + "_loc.txt", 'w')
		for line in content:
			split_line = line.strip().split("\t")
			time_from_start = float(split_line[0])
			label = split_line[1]
			loc_fail.write(str(start_time + timedelta(0, time_from_start)) + "\t" + label + "\n")
		loc_fail.close()

		# Converts the activity labels
		file = file_location + file_beginning + str(file_number) + ".txt"
		with open(file) as f:
			content = f.readlines()
		activity_fail = open(output_directory + file_beginning + str(file_number) + ".txt", 'w')
		for line in content:
			split_line = line.strip().split("\t")
			time_from_start = float(split_line[0])
			label = split_line[2]
			activity_fail.write(str(start_time + timedelta(0, time_from_start)) + "\t" + label + "\n")
		activity_fail.close()


convert_annotations()
