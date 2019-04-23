library(stringr)
library(dplyr)

# for limiting sata
data <- read.csv("C:/kool/thesis/sphere_1m_env/ENV_all.csv")
decreased <- data %>% filter(str_detect(datetime, "2017-04-30T") | str_detect(datetime, "2017-05-01T"))

write.csv(decreased, "C:/kool/thesis/sphere_1m_env/scripts/ENV_labeled_dates.csv")

data$datetime <- as.POSIXct(data$datetime)
env_filtered <- data_between(data, "2017-04-30", "14:00", "2017-04-30", "15:00")
env_filtered = env_filtered %>% filter(sensor=="PIR_TRIGS")


# for converting datetime

convert_datetime <- function(dt) {
  splt <- strsplit(as.character(dt), "T")[[1]]
  date <- splt[1]
  clock <- splt[2]
  clock <- clock %>% str_replace("Z", "")
  result <- paste(date, clock)
  return (result)
}

data <- read.csv("C:/kool/thesis/sphere_1m_env/ENV_labeled_dates.csv")
data$datetime <- as.POSIXlt(sapply(data$datetime, convert_datetime))



#datetime has to be the first column
#python value array has to be the 4th columnt
pir_trigs_edited <- function(env_data) {
  pir <- env_data %>% dplyr::filter(sensor == "PIR_TRIGS")
  without_pir <- env_data %>% dplyr::filter(sensor != "PIR_TRIGS")
  datetime <- c()
  device_id <- c()
  value <- c()
  result <- data.frame()
  
  for (d_id in c("fd00::212:4b00:0:80", "fd00::212:4b00:0:81", "fd00::212:4b00:0:82",
                 "fd00::212:4b00:0:83", "fd00::212:4b00:0:84", "fd00::212:4b00:0:85",
                 "fd00::212:4b00:0:86", "fd00::212:4b00:0:87")) {
    print(d_id)                                            # for keeping track, how far I am
    sensor_data <- pir%>% dplyr::filter(device_id == d_id)
    start <- Sys.time()
    for (row_nr in c(1:nrow(sensor_data))) {
      current_datetime <- round(sensor_data$datetime[row_nr] - 30, "secs")
      next_datetime <- round(sensor_data$datetime[row_nr + 1] - 30, "secs")
      current_second <- as.POSIXlt(current_datetime)$s
      next_second <- as.POSIXlt(next_datetime)$s

      str_value <- as.character(sensor_data$value[row_nr])
      numbers_str <- str_replace_all(str_value, "[[:punct:]]", "")
      values <- as.numeric(unlist(strsplit(numbers_str, " ")))

      if (is.na(next_second)) {
        if (length(grep("\\d+-\\d+-\\d+ \\d+:\\d+:\\d+", c(as.character(current_datetime)),         #removes midnight but saves other data
                        value=TRUE)) == 1) {
          for (i in c(1:30)) {
            value <- c(value, values[i])
            datetime <- c(datetime, as.character(current_datetime))
            device_id <- c(device_id, d_id)
            current_datetime <- current_datetime + 1
          }
        }
      } else {
        index = 1
        while (current_second != next_second) {
          if (length(grep("\\d+-\\d+-\\d+ \\d+:\\d+:\\d+", c(as.character(current_datetime)),           #removes midnight but saves other data
                          value=TRUE)) == 1) {
            value <- c(value, values[index])
            datetime <- c(datetime, as.character(current_datetime))
            device_id <- c(device_id, d_id)
          }
          index <- index + 1
          current_datetime <- current_datetime + 1
          current_second <- as.POSIXlt(current_datetime)$s
        }
      }
      if (row_nr %% 50 == 0) {                    #inceases the speed with large data drastically
        new_pir <- data.frame(device_id, value)
        new_pir$sensor <-  "PIR_TRIGS"
        new_pir$datetime <- as.POSIXct(datetime)
        result <- rbind(result, new_pir)

        datetime <- c()
        device_id <- c()
        value <- c()
      }
    }
    end = Sys.time()
    print(end-start)
    new_pir <- data.frame(device_id, value)
    new_pir$sensor <-  "PIR_TRIGS"
    new_pir$datetime <- as.POSIXct(datetime)
    result <- rbind(new_pir, result)
  }
  return (rbind(result, without_pir))
}



env_edited <- pir_trigs_edited(env_all)
env_edited$datetime <- as.POSIXct(a$datetime)
write.csv(env_edited, "C:/kool/thesis/sphere_1m_env/ENV_labeled_dates_edited.csv")


write.csv(data, "C:/kool/thesis/sphere_1m_env/ENV_all_with_datetimes.csv")


