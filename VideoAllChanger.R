library(stringr)
data <- read.csv("C:/kool/thesis/sphere_1m_env/video_all.csv")

decreased <- data %>% filter(str_detect(datetime, "2017-04-30T") | str_detect(datetime, "2017-05-01T"))
decreased <- decreased %>% dplyr::select(-X)
decreased$datetime <- as.POSIXct(sapply(decreased2$datetime, convert_datetime))
decreased <- decreased %>% dplyr::filter(key == "2DCen")


write.csv(decreased, "C:/kool/thesis/sphere_1m_env/video_labeled_dates.csv")


#data <- read.csv("C:/kool/thesis/sphere_1m_env/ENV_labeled_dates.csv")

#sorted <- data %>% filter (device_id == "fd00::212:4b00:0:86")


flt <- function(date, time) {
  dt <- as.POSIXlt(paste(as.character(date), as.character(time)))
  result <- data %>% filter(as.POSIXlt(datetime) < dt)
  return (result)
}


r <- flt("2017-04-30", "00:00:10")
