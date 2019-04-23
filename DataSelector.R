library(dplyr)
library(stringr)
library(plotly)


# converts the datetime into comparable R datetime
convert_datetime <- function(dt) {      
  splt <- strsplit(as.character(dt), "T")[[1]]
  date <- splt[1]
  clock <- splt[2]
  clock <- clock %>% str_replace("Z", "")
  result <- paste(date, clock)
  return(result)
}


#Gives data between given datetimes
data_between <- function(data, date1, time1,date2, time2) {
  dt1 <- as.POSIXct(paste(as.character(date1), as.character(time1)))
  dt2 <- as.POSIXct(paste(as.character(date2), as.character(time2)))
  result <- data %>% dplyr::filter(datetime > dt1 & datetime < dt2)
  return (result)
}


#rows for reading in data
video_data <- read.csv("C:/kool/thesis/sphere_1m_env/video_labeled_dates.csv")

#datatime converting done here
video_data$datetime <- as.POSIXct(sapply(video_data$datetime, convert_datetime))

# Here I get wished data
video_data <- data_between(video_data, "2017-04-30", "09:00", "2017-04-30", "11:00")
video_data <- video_data %>% dplyr::select(-X, -X.1)
video_data <- video_data %>% dplyr::filter(key == "2DCen")

lounge_video_data <- video_data %>% dplyr::filter(device_id == "b8aeed756145" & key =="Activity")
hall_video_data <- video_data %>% dplyr::filter(device_id == "b8aeed75e024" & key =="Activity")
kitchen_video_data <- video_data %>% dplyr::filter(device_id == "b8aeed78cffe" & key =="Activity")



env_data <- read.csv("C:/kool/thesis/sphere_1m_env/ENV_labeled_dates_edited.csv")
env_data <- env_data %>% dplyr::select(-X)
env_data$datetime <- as.POSIXct(env_data$datetime)

env_filtered <- data_between(env_data, "2017-04-30", "10:00", "2017-04-30", "11:00")
env_filtered <- env_filtered %>% dplyr::filter(sensor=="PIR_TRIGS")
env_filtered <- env_filtered %>% dplyr::filter(value==1)


env_all <- read.csv("C:/kool/thesis/sphere_1m_env/ENV_all.csv")
env_all <- env_all %>% dplyr::select(-X)
env_all <- env_all %>% dplyr::filter(device_id == "02052")
env_all2 <- env_all %>% dplyr::filter(value != "00000")
env_all$datetime <- as.POSIXct(env_all$datetime)
env_all_filtered <- data_between(env_all, "2017-04-30", "15:00", "2017-05-02", "10:00")


#env_all <- env_all %>% dplyr::filter(sensor)




