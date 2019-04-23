library(plotly)


# Creates plot from elecricity sensors
electricity_plotter <- function(data) {
  d <- data %>% dplyr::filter(device_id == "02052")
  d$value = as.numeric(as.character(d$value))
  elec_1 <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"02052")
  
  d <- data %>% dplyr::filter(device_id == "03727")
  d$value = as.numeric(as.character(d$value))
  elec_2 <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"03727")
  
  d <- data %>% dplyr::filter(device_id == "03454")
  d$value = as.numeric(as.character(d$value))
  elec_3 <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"03454")
  
  d <- data %>% dplyr::filter(device_id == "03182")
  d$value = as.numeric(as.character(d$value))
  elec_4 <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"03182")
  
  d <- data %>% dplyr::filter(device_id == "02813")
  d$value = as.numeric(as.character(d$value))
  elec_5 <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"02813")
  
  elec_plot <- subplot(elec_1, elec_2, elec_3, elec_4, elec_5, nrows = 2)
  return (elec_plot)
}


# Creates plots from 4 existing access points
access_points_plotter <- function (data, access_point) {
  d_data <- data %>% dplyr::filter(device_id == access_point & sensor != "PIR_TRIGS")
  d_data$value <- as.numeric(as.character(d_data$value))
  
  d <- d_data %>% dplyr::filter(sensor == "BMP_PRES")
  bmp_pres <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"BMP_PRES")
  
  d <- d_data %>% dplyr::filter(sensor == "HDC_HUM")
  hdc_hum <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"HDC_HUM")
  
  d <- d_data %>% dplyr::filter(sensor == "BMP_TEMP")
  bmp_temp <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"BMP_TEMP")
  
  d <- d_data %>% dplyr::filter(sensor == "HDC_TEMP")
  hdc_temp <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"HDC_TEMP")
  
  plot <- subplot(bmp_pres, hdc_hum, bmp_temp, hdc_temp, nrows = 2)
  return (plot)
}


# Creates plots from 7 environment sensors
env_sensors_plotter <- function(data, sensor_id) {
  d_data <- data %>% dplyr::filter(device_id == sensor_id)
  
  d <- d_data %>% dplyr::filter(sensor == "BMP_PRES")
  d$value <- as.numeric(as.character(d$value))
  bmp_pres <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"BMP_PRES")
  
  d <- d_data %>% dplyr::filter(sensor == "HDC_HUM")
  d$value <- as.numeric(as.character(d$value))
  hdc_hum <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"HDC_HUM")
  
  d <- d_data %>% dplyr::filter(sensor == "BMP_TEMP")
  d$value <- as.numeric(as.character(d$value))
  bmp_temp <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"BMP_TEMP")
  
  d <- d_data %>% dplyr::filter(sensor == "HDC_TEMP")
  d$value <- as.numeric(as.character(d$value))
  hdc_temp <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~"HDC_TEMP")
  
  d <- d_data %>% dplyr::filter(sensor == "LT")
  d$value <- as.numeric(as.character(d$value))
  lt <- plot_ly(d, x = ~datetime, y = ~value, mode ='lines') %>%
    add_lines(name = ~"LT")
  
  d <- d_data %>% dplyr::filter(sensor == "PIR_TRIGS")
  d$value <- as.numeric(as.character(d$value))
  pir <- plot_ly(d, x = ~datetime, y = ~value, mode ='lines') %>%
    add_lines(name = ~"PIR")
  
  if (sensor_id == "fd00::212:4b00:0:85") {     #I have also water data to plot
    d <- d_data %>% dplyr::filter(sensor == "PIEZO_WATER_C")
    d$value <- as.numeric(as.character(d$value))
    water_c <- plot_ly(d, x = ~datetime, y = ~value, mode ='lines') %>%
      add_lines(name = ~"PIEZO_WATER_C")
    
    d <- d_data %>% dplyr::filter(sensor == "PIEZO_WATER_H")
    d$value <- as.numeric(as.character(d$value))
    water_h <- plot_ly(d, x = ~datetime, y = ~value, mode ='lines') %>%
      add_lines(name = ~"PIEZO_WATER_H")
    
    plot <- subplot(bmp_pres, hdc_hum, bmp_temp, hdc_temp, lt, pir, water_c, water_h, nrows = 3)
  }
  else 
    plot <- subplot(bmp_pres, hdc_hum, bmp_temp, hdc_temp, lt, pir, nrows = 2) 
  
  return (plot)
}


# creates pir plot from data and consideres device_id
single_pir_plotter <- function(data, device) {
  d <- data %>% dplyr::filter(device_id == device)
  return(plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
    add_lines(name = ~device))
}


# plots every pir sensor
pir_plotter <- function(env_data, video_data, start_date, start_time, end_date, end_time) {
  data <- env_data %>% dplyr::filter(sensor == "PIR_TRIGS")
  data <- data_between(data, start_date, start_time, end_date, end_time)
  video_data <- data_between(video_data, start_date, start_time, end_date, end_time)
  
  pir1 <- single_pir_plotter(data, "fd00::212:4b00:0:83")
  pir2 <- single_pir_plotter(data, "fd00::212:4b00:0:85")
  pir3 <- single_pir_plotter(data, "fd00::212:4b00:0:80")
  pir4 <- single_pir_plotter(data, "fd00::212:4b00:0:81")
  pir5 <- single_pir_plotter(data, "fd00::212:4b00:0:82")
  pir6 <- single_pir_plotter(data, "fd00::212:4b00:0:84")
  pir7 <- single_pir_plotter(data, "fd00::212:4b00:0:86")
  
  lounge_video_data <- video_data %>% dplyr::filter(device_id == "b8aeed756145" & key =="Activity")
  hall_video_data <- video_data %>% dplyr::filter(device_id == "b8aeed75e024" & key =="Activity")
  kitchen_video_data <- video_data %>% dplyr::filter(device_id == "b8aeed78cffe" & key =="Activity")
  
  l <- lounge_video_data
  l$value <-  "lounge"
  k <- kitchen_video_data
  k$value <-  "kitchen"
  h <- hall_video_data
  h$value <- "hall"
  joined <- rbind(l,k,h)
  vid_plot <- plot_ly(joined, x=~datetime, y=~value, type='scatter', mode='markers', name='video_data')
  pir_all <- subplot(pir1, pir2, pir3, pir4, pir5, pir6, pir7, vid_plot, nrows=3)
  return (pir_all)
}


# Data must have been read in
d_data <- data_between(env_data, "2017-04-30", "09:00", "2017-04-30", "11:00")

elec_plot <- electricity_plotter(env_filtered)
bedroom2_plot <- access_points_plotter(env_data, "fd00::212:4b00:0:6")
bedroom1_plot <- access_points_plotter(env_data, "fd00::212:4b00:0:5")
kitchen_plot <- access_points_plotter(env_data, "fd00::212:4b00:0:3")
lounge_plot <- access_points_plotter(env_data, "fd00::212:4b00:0:4")
room1_plot <- env_sensors_plotter(env_data, "fd00::212:4b00:0:83")
room2_plot <- env_sensors_plotter(env_data, "fd00::212:4b00:0:85")  
room3_plot <- env_sensors_plotter(d_data, "fd00::212:4b00:0:80")
room4_plot <- env_sensors_plotter(env_data, "fd00::212:4b00:0:81")
room5_plot <- env_sensors_plotter(env_data, "fd00::212:4b00:0:82")
room6_plot <- env_sensors_plotter(env_data, "fd00::212:4b00:0:84")
room7_plot <- env_sensors_plotter(env_data, "fd00::212:4b00:0:86")

pir_plots <- pir_plotter(env_data, video_data, "2017-04-30", "09:00", "2017-04-30", "11:00")

# you probably won't see anyting special here (too many graphs)
big_plot <- subplot(elec_plot, bedroom2_plot, bedroom1_plot, kitchen_plot, lounge_plot,
                    room1_plot, room2_plot, room3_plot, room4_plot,
                    room5_plot, room6_plot, room7_plot, nrows = 3)



d_data <- data_between(env_all, "2017-05-01", "1:30", "2017-05-01", "3:30")
d_data <- data_between(data, "2017-04-30", "10:01", "2017-04-30", "10:19")     
d_data <- d_data %>% dplyr::filter(sensor == "PIR_TRIGS")
pir1 <- single_pir_plotter(d_data, "fd00::212:4b00:0:84")



b <- single_pir_plotter(a, "fd00::212:4b00:0:82")

elec_plot <- electricity_plotter(d_data)

d_data <- data_between(data, "2017-04-30", "9:30", "2017-05-01", "4:30")


d_data <- data_between(data, "2017-05-07", "1:30", "2017-05-11", "4:30")
d <- d_data %>% dplyr::filter(device_id == "02052")
d$value = as.numeric(as.character(d$value))
elec_1 <- plot_ly(d, x = ~datetime, y = ~value, mode = 'lines') %>%
  add_lines(name = ~"02052")
elec_1



# water plots
d <- env_data %>% dplyr::filter(sensor == "PIEZO_WATER_C")
d$value <- as.numeric(as.character(d$value))
water_c <- plot_ly(d, x = ~datetime, y = ~value, mode ='lines') %>%
  add_lines(name = ~"PIEZO_WATER_C")

d <- env_data %>% dplyr::filter(sensor == "PIEZO_WATER_H")
d$value <- as.numeric(as.character(d$value))
water_h <- plot_ly(d, x = ~datetime, y = ~value, mode ='lines') %>%
  add_lines(name = ~"PIEZO_WATER_H")

plot <- subplot(water_c, water_h, nrows = 1)




#study plots
d <- data_between(env_data, "2017-04-30", "10:01", "2017-04-30", "10:02")
study1_plot <- env_sensors_plotter(d, "fd00::212:4b00:0:80")
study2_plot <- access_points_plotter(d, "fd00::212:4b00:0:4")


#bedroom plots
d <- data_between(env_data, "2017-04-30", "00:02", "2017-04-30", "23:59")
bed1_plot <- env_sensors_plotter(d, "fd00::212:4b00:0:84")
bed2_plot <- access_points_plotter(d, "fd00::212:4b00:0:5")


#kitchen plots
d <- data_between(env_data, "2017-04-30", "00:00", "2017-04-30", "22:06")
kitchen1 <- env_sensors_plotter(d, "fd00::212:4b00:0:82")
kitchen2 <- access_points_plotter(d, "fd00::212:4b00:0:3")
kitchen3 <- env_sensors_plotter(d, "fd00::212:4b00:0:85")
kitchen4 <- electricity_plotter(d)
