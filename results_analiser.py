from datetime import datetime, timedelta

list_of_prediction_times1 = ["2017-04-30 09:46:39", "2017-04-30 09:49:48",
							 "2017-04-30 09:49:49", "2017-04-30 09:50:09", "2017-04-30 09:50:12",
							 "2017-04-30 09:50:21", "2017-04-30 09:50:27", "2017-04-30 10:01:20",
							 "2017-04-30 10:01:25", "2017-04-30 10:01:32", "2017-04-30 10:01:37",
							 "2017-04-30 10:01:48", "2017-04-30 10:01:52", "2017-04-30 10:04:11",
							 "2017-04-30 10:04:13", "2017-04-30 10:04:20", "2017-04-30 10:04:23",
							 "2017-04-30 10:04:35", "2017-04-30 10:04:37", "2017-04-30 10:04:46",
							 "2017-04-30 10:04:50", "2017-04-30 10:05:23", "2017-04-30 10:05:26",
							 "2017-04-30 10:16:01", "2017-04-30 10:16:06", "2017-04-30 10:17:02",
							 "2017-04-30 10:17:08",  # "2017-04-30 10:17:33",
							 "2017-04-30 10:17:47"]

list_of_annotation_times1 = ["2017-04-30 09:46:37.320618", "2017-04-30 09:49:46.640034",
							 "2017-04-30 09:49:48.522860", "2017-04-30 09:50:08.578691", "2017-04-30 09:50:11.863269",
							 "2017-04-30 09:50:19.220391", "2017-04-30 09:50:26.635575", "2017-04-30 10:01:21.419480",
							 "2017-04-30 10:01:24.654292", "2017-04-30 10:01:32.932091", "2017-04-30 10:01:36.307907",
							 "2017-04-30 10:01:49.238859", "2017-04-30 10:01:52.639558", "2017-04-30 10:04:12.234115",
							 "2017-04-30 10:04:14.921497", "2017-04-30 10:04:19.682476", "2017-04-30 10:04:22.369858",
							 "2017-04-30 10:04:35.591113", "2017-04-30 10:04:38.394616", "2017-04-30 10:04:45.527790",
							 "2017-04-30 10:04:49.260265", "2017-04-30 10:05:22.835949", "2017-04-30 10:05:26.518658",
							 "2017-04-30 10:16:01.603391", "2017-04-30 10:16:05.518342", "2017-04-30 10:17:02.625206",
							 "2017-04-30 10:17:06.415742",  # "2017-04-30 10:17:42.645631",
							 "2017-04-30 10:17:46.195629"]

list_of_prediction_times2 = ["2017-04-30 14:23:51", "2017-04-30 14:23:55",
"2017-04-30 14:24:02",
"2017-04-30 14:24:11",
"2017-04-30 14:26:14",
"2017-04-30 14:26:24",
"2017-04-30 14:26:35",
"2017-04-30 14:26:37",
"2017-04-30 14:26:46",
"2017-04-30 14:26:50",
"2017-04-30 14:34:00",
"2017-04-30 14:34:04",
"2017-04-30 14:34:17",
"2017-04-30 14:34:21",
"2017-04-30 14:40:49",
"2017-04-30 14:40:55",
"2017-04-30 14:41:25",
"2017-04-30 14:41:35"]

list_of_annotation_times2 = ["2017-04-30 14:23:51.102989",
"2017-04-30 14:23:53.543973",
"2017-04-30 14:24:01.671645",
"2017-04-30 14:24:13.822916",
"2017-04-30 14:26:12.425225",
"2017-04-30 14:26:22.712228",
"2017-04-30 14:26:34.407492",
"2017-04-30 14:26:37.975084",
"2017-04-30 14:26:45.324859",
"2017-04-30 14:26:50.260475",
"2017-04-30 14:34:00.892945",
"2017-04-30 14:34:03.776525",
"2017-04-30 14:34:17.054404",
"2017-04-30 14:34:21.024356",
"2017-04-30 14:40:49.918685",
"2017-04-30 14:40:54.130053",
"2017-04-30 14:41:25.205655",
"2017-04-30 14:41:34.942766"]

list_of_annotation_times3 = ["2017-04-30 12:30:53.122857",
"2017-04-30 12:30:57.685578",
"2017-04-30 12:32:18.845125",
"2017-04-30 12:32:36.605488",
"2017-04-30 12:32:41.687755",
"2017-04-30 12:32:44.398685",
"2017-04-30 12:33:09.331111",
"2017-04-30 12:33:10.364399",
"2017-04-30 12:36:39.227891",
"2017-04-30 12:36:40.679138",
"2017-04-30 12:37:21.697188",
"2017-04-30 12:37:31.623719",
"2017-04-30 12:37:39.483673",
"2017-04-30 12:37:41.782449",
"2017-04-30 12:37:48.469796",
"2017-04-30 12:37:53.938095"]

list_of_prediction_times3 = [
"2017-04-30 12:30:53",
"2017-04-30 12:30:58",
"2017-04-30 12:32:18",
"2017-04-30 12:32:36",
"2017-04-30 12:32:43",
"2017-04-30 12:32:45",
"2017-04-30 12:33:09",
"2017-04-30 12:33:11",
"2017-04-30 12:36:39",
"2017-04-30 12:36:40",
"2017-04-30 12:37:21",
"2017-04-30 12:37:32",
"2017-04-30 12:37:40",
"2017-04-30 12:37:41",
"2017-04-30 12:37:50",
"2017-04-30 12:37:54"]


list_of_annotation_times4 = [
"2017-04-30 17:59:07.146965",
"2017-04-30 17:59:12.856629",
"2017-04-30 17:59:48.611326",
"2017-04-30 17:59:52.805804",
"2017-04-30 18:00:00.973027",
"2017-04-30 18:00:06.654975",
"2017-04-30 18:02:05.042747",
"2017-04-30 18:02:11.907280",
"2017-04-30 18:02:33.249230",
"2017-04-30 18:02:41.550544",
"2017-04-30 18:03:31.932041",
"2017-04-30 18:03:39.223107",
"2017-04-30 18:03:44.958435",
"2017-04-30 18:06:06.797528",
"2017-04-30 18:06:19.881973",
"2017-04-30 18:06:32.432358",
"2017-04-30 18:06:36.234626",
"2017-04-30 18:06:46.973855",
#"2017-04-30 18:06:50.242063",
"2017-04-30 18:07:10.507279",
"2017-04-30 18:07:13.769683",
"2017-04-30 18:07:56.593084",
"2017-04-30 18:08:00.598526",
"2017-04-30 18:08:10.188367",
"2017-04-30 18:08:12.278163"
]

list_of_prediction_times4 = [
"2017-04-30 17:59:07",
"2017-04-30 17:59:12",
"2017-04-30 17:59:48",
"2017-04-30 17:59:54",
"2017-04-30 18:00:01",
"2017-04-30 18:00:08",
"2017-04-30 18:02:05",
"2017-04-30 18:02:12",
"2017-04-30 18:02:34",
"2017-04-30 18:02:43",
"2017-04-30 18:03:31",
"2017-04-30 18:03:40",
"2017-04-30 18:03:46",
"2017-04-30 18:06:07",
"2017-04-30 18:06:20",
"2017-04-30 18:06:32",
"2017-04-30 18:06:37",
"2017-04-30 18:06:46",
#"2017-04-30 18:07:04",
"2017-04-30 18:07:11",
"2017-04-30 18:07:14",
"2017-04-30 18:07:57",
"2017-04-30 18:08:00",
"2017-04-30 18:08:09",
"2017-04-30 18:08:13"]

list_of_annotation_times5 = [
"2017-04-30 20:41:00.596009",
"2017-04-30 20:41:23.815964",
"2017-04-30 20:44:48.476644",
"2017-04-30 20:44:58.438005",
"2017-04-30 20:45:29.599184",
"2017-04-30 20:45:41.650340",
"2017-04-30 20:45:57.672109",
"2017-04-30 20:55:43.163265",
"2017-04-30 20:55:47.842086",
"2017-04-30 21:02:10.541769",
"2017-04-30 21:02:12.260045",
"2017-04-30 21:02:19.040272",
"2017-04-30 21:02:22.314286",
"2017-04-30 21:02:52.268027",
"2017-04-30 21:02:56.354739",
"2017-04-30 21:03:03.622585",
"2017-04-30 21:03:07.314558",
"2017-04-30 21:04:15.836644",
"2017-04-30 21:04:30.256236",
"2017-04-30 21:04:47.752472",
"2017-04-30 21:04:51.641814",
"2017-04-30 21:04:59.478549",
"2017-04-30 21:05:03.449161",
"2017-04-30 21:05:46.754376",
"2017-04-30 21:05:47.985034",
"2017-04-30 21:07:36.213243",
"2017-04-30 21:07:37.420680"
]

list_of_prediction_times5 = [
"2017-04-30 20:41:06",
"2017-04-30 20:41:25",
"2017-04-30 20:44:48",
"2017-04-30 20:44:58",
"2017-04-30 20:45:31",
"2017-04-30 20:45:40",
"2017-04-30 20:45:59",
"2017-04-30 20:55:43",
"2017-04-30 20:55:48",
"2017-04-30 21:02:10",
"2017-04-30 21:02:13",
"2017-04-30 21:02:20",
"2017-04-30 21:02:25",
"2017-04-30 21:02:52",
"2017-04-30 21:02:55",
"2017-04-30 21:03:04",
"2017-04-30 21:03:07",
"2017-04-30 21:04:17",
"2017-04-30 21:04:33",
"2017-04-30 21:04:48",
"2017-04-30 21:04:52",
"2017-04-30 21:04:59",
"2017-04-30 21:05:04",
"2017-04-30 21:05:48",
"2017-04-30 21:05:48",
"2017-04-30 21:07:37",
"2017-04-30 21:07:38"
]

list_of_prediction_times6 = [
"2017-04-30 22:52:28",
"2017-04-30 22:52:34",
"2017-04-30 22:52:43",
"2017-04-30 22:52:49",
"2017-04-30 22:53:31",
"2017-04-30 22:53:37",
"2017-04-30 22:53:56",
"2017-04-30 22:54:22",
"2017-04-30 22:54:29",
"2017-04-30 22:54:35",
"2017-04-30 23:03:02",
"2017-04-30 23:03:12",
"2017-04-30 23:10:04",
"2017-04-30 23:10:08",
"2017-04-30 23:10:20",
"2017-04-30 23:10:22",
"2017-04-30 23:11:43",
"2017-04-30 23:11:43"]

list_of_annotation_times6 = ["2017-04-30 22:52:28.876676",
"2017-04-30 22:52:35.597868",
"2017-04-30 22:52:42.834423",
"2017-04-30 22:52:48.052473",
"2017-04-30 22:53:31.461068",
"2017-04-30 22:53:37.634687",
"2017-04-30 22:53:55.500604",
"2017-04-30 22:54:19.142881",
"2017-04-30 22:54:30.781495",
"2017-04-30 22:54:35.247974",
"2017-04-30 23:03:01.694107",
"2017-04-30 23:03:03.444194",
"2017-04-30 23:10:06.605521",
"2017-04-30 23:10:07.829508",
"2017-04-30 23:10:20.370007",
"2017-04-30 23:10:21.411470",
"2017-04-30 23:11:35.902895",
"2017-04-30 23:11:42.586508"]


list_of_annotation_times7 = [
"2017-05-01 08:18:24.307069",
"2017-05-01 08:18:25.912350",
"2017-05-01 08:19:46.910971",
"2017-05-01 08:19:48.407418",
"2017-05-01 08:24:08.789280",
"2017-05-01 08:24:12.435170",
"2017-05-01 08:24:22.284516",
"2017-05-01 08:24:24.842080",
"2017-05-01 08:27:28.741872",
"2017-05-01 08:27:31.027355",
"2017-05-01 08:27:35.135784",
"2017-05-01 08:27:38.523197",
"2017-05-01 08:27:43.978428",
"2017-05-01 08:27:46.549597",
"2017-05-01 08:27:51.637518",
"2017-05-01 08:27:56.072445",
"2017-05-01 08:28:07.261791",
"2017-05-01 08:28:08.717426",
"2017-05-01 08:28:12.771438",
"2017-05-01 08:28:17.233572",
"2017-05-01 08:31:41.042918",
"2017-05-01 08:31:45.069722",
"2017-05-01 08:32:41.036857",
"2017-05-01 08:32:44.709956",
"2017-05-01 08:32:52.518691",
"2017-05-01 08:32:54.749758",
"2017-05-01 08:33:10.285604",
"2017-05-01 08:33:27.617186",
"2017-05-01 08:38:51.933492",
"2017-05-01 08:39:05.308186",
"2017-05-01 08:46:13.762789",
"2017-05-01 08:46:17.106463",
"2017-05-01 08:47:44.181293",
"2017-05-01 08:47:48.871723",
"2017-05-01 08:56:43.952358",
"2017-05-01 08:56:47.621111",
"2017-05-01 09:00:54.960068",
"2017-05-01 09:00:57.746463",
"2017-05-01 09:01:17.924603",
"2017-05-01 09:01:23.729592",
"2017-05-01 09:08:22.826553",
"2017-05-01 09:08:30.721338",
"2017-05-01 09:18:09.501927",
"2017-05-01 09:18:14.749637"
]

list_of_prediction_times7 = [
"2017-05-01 08:18:24",
"2017-05-01 08:18:27",
"2017-05-01 08:19:47",
"2017-05-01 08:19:49",
"2017-05-01 08:24:10",
"2017-05-01 08:24:13",
"2017-05-01 08:24:22",
"2017-05-01 08:24:25",
"2017-05-01 08:27:28",
"2017-05-01 08:27:29",
"2017-05-01 08:27:36",
"2017-05-01 08:27:39",
"2017-05-01 08:27:44",
"2017-05-01 08:27:44",
"2017-05-01 08:27:53",
"2017-05-01 08:27:55",
"2017-05-01 08:28:06",
"2017-05-01 08:28:07",
"2017-05-01 08:28:14",
"2017-05-01 08:28:19",
"2017-05-01 08:31:41",
"2017-05-01 08:31:44",
"2017-05-01 08:32:42",
"2017-05-01 08:32:43",
"2017-05-01 08:32:52",
"2017-05-01 08:32:56",
"2017-05-01 08:33:10",
"2017-05-01 08:33:29",
"2017-05-01 08:38:51",
"2017-05-01 08:39:05",
"2017-05-01 08:46:13",
"2017-05-01 08:46:18",
"2017-05-01 08:47:44",
"2017-05-01 08:47:50",
"2017-05-01 08:56:43",
"2017-05-01 08:56:48",
"2017-05-01 09:00:54",
"2017-05-01 09:00:59",
"2017-05-01 09:01:17",
"2017-05-01 09:01:27",
"2017-05-01 09:08:26",
"2017-05-01 09:08:32",
"2017-05-01 09:18:09",
"2017-05-01 09:18:17"
]

list_of_annotation_times8 = [
"2017-05-01 11:03:49.256206",
"2017-05-01 11:03:53.034998",
"2017-05-01 11:04:06.209148",
"2017-05-01 11:04:09.905344",
"2017-05-01 11:04:16.079436",
"2017-05-01 11:04:22.232879",
"2017-05-01 11:09:52.474546",
"2017-05-01 11:10:03.046905",
"2017-05-01 11:10:12.339017",
"2017-05-01 11:10:17.955583",
"2017-05-01 11:10:20.846462",
"2017-05-01 11:12:30.946358",
"2017-05-01 11:12:33.764965",
"2017-05-01 11:12:38.689784",
"2017-05-01 11:12:41.002488",
"2017-05-01 11:20:30.078636",
"2017-05-01 11:20:32.928217",
"2017-05-01 11:20:42.819154",
"2017-05-01 11:20:49.571422",
"2017-05-01 11:26:49.300058",
"2017-05-01 11:26:55.598046"
]

list_of_prediction_times8 = [
"2017-05-01 11:03:49",
"2017-05-01 11:03:54",
"2017-05-01 11:04:07",
"2017-05-01 11:04:08",
"2017-05-01 11:04:15",
"2017-05-01 11:04:22",
"2017-05-01 11:09:52",
"2017-05-01 11:10:04",
"2017-05-01 11:10:12",
"2017-05-01 11:10:21",
"2017-05-01 11:10:22",
"2017-05-01 11:12:31",
"2017-05-01 11:12:32",
"2017-05-01 11:12:39",
"2017-05-01 11:12:42",
"2017-05-01 11:20:28",
"2017-05-01 11:20:34",
"2017-05-01 11:20:43",
"2017-05-01 11:20:51",
"2017-05-01 11:26:50",
"2017-05-01 11:26:56"
]

list_of_annotation_times9 = [
"2017-05-01 14:18:53.526819",
"2017-05-01 14:18:57.013639",
"2017-05-01 14:19:04.057631",
"2017-05-01 14:19:10.345340",
"2017-05-01 14:21:23.992128",
"2017-05-01 14:21:34.879097",
"2017-05-01 14:21:43.409276",
"2017-05-01 14:21:49.565074",
"2017-05-01 14:22:24.565187",
"2017-05-01 14:22:31.424506",
"2017-05-01 14:22:38.494880",
"2017-05-01 14:32:36.996810",
"2017-05-01 14:32:53.635054",
"2017-05-01 14:33:19.594937",
"2017-05-01 14:40:12.525916",
"2017-05-01 14:40:17.345027",
"2017-05-01 14:42:17.99868",
"2017-05-01 14:42:22.219801",
"2017-05-01 14:42:46.139477",
"2017-05-01 14:42:50.026424",
"2017-05-01 14:43:04.290289",
"2017-05-01 14:43:07.913416",
"2017-05-01 14:43:48.840684",
"2017-05-01 14:44:01.240221",
"2017-05-01 14:56:14.809169",
"2017-05-01 14:56:20.085567",
"2017-05-01 14:59:07.479323",
"2017-05-01 14:59:12.403962"
]

list_of_prediction_times9 = [
"2017-05-01 14:18:55",
"2017-05-01 14:18:57",
"2017-05-01 14:19:04",
"2017-05-01 14:19:12",
"2017-05-01 14:21:24",
"2017-05-01 14:21:35",
"2017-05-01 14:21:43",
"2017-05-01 14:21:49",
"2017-05-01 14:22:23",
"2017-05-01 14:22:32",
"2017-05-01 14:22:40",
"2017-05-01 14:32:37",
"2017-05-01 14:32:54",
"2017-05-01 14:33:19",
"2017-05-01 14:40:12",
"2017-05-01 14:40:18",
"2017-05-01 14:42:18",
"2017-05-01 14:42:23",
"2017-05-01 14:42:45",
"2017-05-01 14:42:51",
"2017-05-01 14:43:04",
"2017-05-01 14:43:08",
"2017-05-01 14:43:47",
"2017-05-01 14:44:00",
"2017-05-01 14:56:09",
"2017-05-01 14:56:21",
"2017-05-01 14:59:07",
"2017-05-01 14:59:21"
]

list_of_annotation_times10 = [
"2017-05-01 18:43:09.510230",	#hall
"2017-05-01 18:43:14.953721",	#stairs
"2017-05-01 18:43:26.644853",	#landing
"2017-05-01 18:43:36.140032",	#toilet
"2017-05-01 18:45:42.051672",	#landing
"2017-05-01 18:45:43.536260",	#bedroom
"2017-05-01 18:46:05.805083",	#landing
"2017-05-01 18:46:17.047746",	#stairs
"2017-05-01 18:46:27.733689",	#hall
"2017-05-01 18:46:30.888439",	#kitchen
"2017-05-01 18:54:12.688167",	#hall
"2017-05-01 18:54:18.951274",	#lounge
"2017-05-01 19:01:24.285803",	#hall
"2017-05-01 19:01:28.662246",	#kitchen
"2017-05-01 19:02:37.015162",	#hall
"2017-05-01 19:02:40.958600",	#lounge
"2017-05-01 19:11:23.487266",	#hall
"2017-05-01 19:11:27.910101",	#kitchen
"2017-05-01 19:15:21.871929",	#hall
"2017-05-01 19:15:31.815577",	#study
"2017-05-01 19:15:40.692178"	#hal
]

list_of_prediction_times10 = [
"2017-05-01 18:43:12",
"2017-05-01 18:43:18",
"2017-05-01 18:43:25",
"2017-05-01 18:43:36",
"2017-05-01 18:45:43",
"2017-05-01 18:45:44",
"2017-05-01 18:46:05",
"2017-05-01 18:46:18",
"2017-05-01 18:46:27",
"2017-05-01 18:46:31",
"2017-05-01 18:54:12",
"2017-05-01 18:54:20",
"2017-05-01 19:01:24",
"2017-05-01 19:01:29",
"2017-05-01 19:02:36",
"2017-05-01 19:02:42",
"2017-05-01 19:11:24",
"2017-05-01 19:11:29",
"2017-05-01 19:15:20",
"2017-05-01 19:15:32",
"2017-05-01 19:15:39"
]

list_of_annotation_times11 = [
"2017-05-01 19:44:45.395233",#	hall
"2017-05-01 19:44:49.586807",#	kitchen
"2017-05-01 19:48:54.043770",#	hall
"2017-05-01 19:48:58.367709",#	stairs
"2017-05-01 19:49:06.309637",#	landing
"2017-05-01 19:49:09.949687",#	bedroom
"2017-05-01 19:49:46.570801",#	landing
"2017-05-01 19:49:49.968181",#	stairs
	#hall puudu siit
"2017-05-01 19:50:01.263368",#	lounge
#"2017-05-01 19:51:28.183360",#	hall
"2017-05-01 19:51:35.761284",#	porch
"2017-05-01 19:51:51.578957",#	hall
"2017-05-01 19:52:00.932784",#	study
"2017-05-01 19:52:44.690602",#	hall
"2017-05-01 19:52:59.250804",#	stairs
"2017-05-01 19:53:09.619433", #landing
"2017-05-01 19:53:13.303605" #bedroom
]

list_of_prediction_times11 = [
"2017-05-01 19:44:43",
"2017-05-01 19:44:50",
"2017-05-01 19:48:54",
"2017-05-01 19:49:00",
"2017-05-01 19:49:07",
"2017-05-01 19:49:11",
"2017-05-01 19:49:47",
"2017-05-01 19:49:50",
"2017-05-01 19:50:03",
#"2017-05-01 19:51:18",
"2017-05-01 19:51:37",
"2017-05-01 19:51:53",
"2017-05-01 19:52:02",
"2017-05-01 19:52:41",
"2017-05-01 19:53:02",
"2017-05-01 19:53:09",
"2017-05-01 19:53:14"
]

def measure_diff(predictions, annotations):
	diff_sum = 0
	i = 0
	for i in range(len(predictions)):
		pred_time = datetime.strptime(predictions[i], "%Y-%m-%d %H:%M:%S")
		annot_time = datetime.strptime(annotations[i], "%Y-%m-%d %H:%M:%S.%f")
		time_diff = abs((pred_time - annot_time).total_seconds())
		diff_sum += time_diff
		print(time_diff)
	print("average is " + str(diff_sum / (i + 1)))
	print("võrdlemiseks on kasutatud " + str(i + 1) + " märgedust")


measure_diff(list_of_prediction_times11, list_of_annotation_times11)