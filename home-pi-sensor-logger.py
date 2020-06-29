#!/usr/bin/python3
import sys
import gspread
import Adafruit_DHT
import time
from datetime import datetime
# hard coding sensor model 2302 because I know what I have
# pin = 4
# humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)

#howlong = int(sys.argv[1])
gc = gspread.service_account(filename='/home/pi/home-pi-sensor/home-gus-io-29e43cbe0731.json')
sheet = gc.open("home_temp_humidity_log").sheet1

while True:
    humidity, temp = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 4)
    #now = datetime.now()
    #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #print(dt_string)
    if humidity is not None and temp is not None:
        sheet.append_row((datetime.now().isoformat(), temp, humidity))
    else:
        print('failed at something, lets try again')
        sys.exit()
    time.sleep(60)

