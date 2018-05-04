import time, math, mraa, socket, select  
import numpy as np
import csv
import requests
import sys,json
import boto3
import aws
#Iniatialization
led_pin_number=4
led = mraa.Gpio(led_pin_number)
led.dir(mraa.DIR_OUT)
last_signal = [0]
current_signal = [0]
last_time = [0]
current_time = [0]
BPM = [0]

switch_pin_number=8
buzz_pin_number=6
PulSensor = mraa.Aio(1)

x = mraa.I2c(6)  
MPU = 0x68  
x.address(MPU)  
x.writeReg(0x6B, 0)
#Heart rate calculation function
def test_pulse():
    Pulse = float(PulSensor.read())
    current_signal[0] = Pulse
    if current_signal[0]>550 and last_signal[0] <550:
        current_time[0] = int(time.time()*1000)
        BPM[0] = 60000/(current_time[0]-last_time[0])
        last_time[0] = current_time[0]
    last_signal[0] = current_signal[0]
    if Pulse > 550:
        led.write(1)
    else:
        led.write(0)
#get location function using google API
def GPS():
    GOOGLE_MAPS_API_URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBUj_H7Bp6sel10RKaSJm8DQop5NoH1-WE'
    params = {'wifiAccessPoints':[{'macAddress':'fc:c2:de:3c:4f:8f'}]}
    req = requests.post(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()
    lat = res['location']['lat']
    lng = res['location']['lng']
    return (lat,lng)
# Data collect function
def data_collect(args):
        buzz.write(1)
        time.sleep(0.2)
        buzz.write(0)
        phone_parent=9293106827
        phone_children=9293106827
        X_Ac = []
        Y_Ac = []
        Z_Ac = []
        X_Gy = []
        Y_Gy = []
        Z_Gy = []
        x.address(MPU)
        #Read raw data
        for i in range (0,80):
            test_pulse()
            AcX = np.int16(x.readReg(0x3C) | x.readReg(0x3B)<<8)  
            AcY = np.int16(x.readReg(0x3E) | x.readReg(0x3D)<<8)  
            AcZ = np.int16(x.readReg(0x40) | x.readReg(0x3F)<<8)  
            GyX = np.int16(x.readReg(0x44) | x.readReg(0x43)<<8)  
            GyY = np.int16(x.readReg(0x46) | x.readReg(0x45)<<8)  
            GyZ = np.int16(x.readReg(0x48) | x.readReg(0x47)<<8)
            X_Ac.append(AcX)
            Y_Ac.append(AcY)
            Z_Ac.append(AcZ)
            X_Gy.append(GyX)
            Y_Gy.append(GyY)
            Z_Gy.append(GyZ)
            time.sleep(0.02)
        ##########################################################
        #data preprocessing
        data = np.zeros(53)
        data[0] = np.max(X_Gy)
        data[1] = np.min(X_Gy)
        data[2] = np.mean(X_Gy)
        data[3] = np.var(X_Gy)
        data[4] = data[0] - data[1]
        data[5] = np.mean(X_Gy[0:40])
        data[6] = np.mean(X_Gy[40:80])
        data[7] = data[5]-data[6]
        data[8] = np.max(Y_Gy)
        data[9] = np.min(Y_Gy)
        data[10] = np.mean(Y_Gy)
        data[11] = np.var(Y_Gy)
        data[12] = data[8] - data[9]
        data[13] = np.mean(Y_Gy[0:40])
        data[14] = np.mean(Y_Gy[40:80])
        data[15] = data[13]-data[14]
        data[16] = np.max(Z_Gy)
        data[17] = np.min(Z_Gy)
        data[18] = np.mean(Z_Gy)
        data[19] = np.var(Z_Gy)
        data[20] = data[16] - data[17]
        data[21] = np.mean(Z_Gy[0:40])
        data[22] = np.mean(Z_Gy[40:80])
        data[23] = data[21]-data[22]
        data[24] = np.max(X_Ac)
        data[25] = np.min(X_Ac)
        data[26] = np.mean(X_Ac)
        data[27] = np.var(X_Ac)
        data[28] = data[24] - data[25]
        data[29] = np.mean(X_Ac[0:40])
        data[30] = np.mean(X_Ac[40:80])
        data[31] = data[29]-data[30]
        data[32] = np.max(Y_Ac)
        data[33] = np.min(Y_Ac)
        data[34] = np.mean(Y_Ac)
        data[35] = np.var(Y_Ac)
        data[36] = data[32] - data[33]
        data[37] = np.mean(Y_Ac[0:40])
        data[38] = np.mean(Y_Ac[40:80])
        data[39] = data[37]-data[38]
        data[40] = np.max(Z_Ac)
        data[41] = np.min(Z_Ac)
        data[42] = np.mean(Z_Ac)
        data[43] = np.var(Z_Ac)
        data[44] = data[40] - data[41]
        data[45] = np.mean(Z_Ac[0:40])
        data[46] = np.mean(Z_Ac[40:80])
        data[47] = data[45]-data[46]
        (lat,lng) = GPS()
        data[48]=phone_parent
        data[49]=phone_children
        data[50]=int(BPM[0])
        data[51]=float(lat)
	data[52]=float(lng)
        #save the data in an csv
        with open("data.csv","wb") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = ["XG_max","XG_min","XG_mean","XG_var","XG_max-min","XG_fmean","XG_lmean",
            "XG_f-lmean","YG_max","YG_min","YG_mean","YG_var","YG_max-min","XG_fmean","YG_lmean","YG_f-lmean",
            "ZG_max","ZG_min","ZG_mean","ZG_var","ZG_max-min","ZG_fmean","ZG_lmean","ZG_f-lmean","XA_max","XA_min",
            "XA_mean","XA_var","XA_max-min","XA_fmean","XA_lmean","XA_f-lmean","YA_max","YA_min","YA_mean","YA_var",
            "YA_max-min","XA_fmean","YA_lmean","YA_f-lmean","ZA_max","ZA_min","ZA_mean","ZA_var","ZA_max-min","ZA_fmean","ZA_lmean",
            "ZA_f-lmean","phone_parent","phone_children", "BPM","lat","lng"
            ], delimiter = ',')
            writer.writeheader()
            writer = csv.writer(csvfile)
            writer.writerow(data)
	    csvfile.close()
        #Push the data to kinesis
        KINESIS_STREAM_NAME = "finalproject"
        kinesis = boto3.client('kinesis', region_name='us-east-1')
        with open("data.csv",'rb') as f:
    	    dataReader = csv.DictReader(f)
            for row in dataReader:
                kinesis.put_record(StreamName=KINESIS_STREAM_NAME, Data=json.dumps(row), PartitionKey='0')
                break
            f.close()
        buzz.write(1)
        time.sleep(0.2)
        buzz.write(0)
        print "data",(data)
        print "BPM",(BPM[0])




 
switch = mraa.Gpio(switch_pin_number)
buzz = mraa.Gpio(buzz_pin_number)

switch.dir(mraa.DIR_IN)
buzz.dir(mraa.DIR_OUT)

switch.isr(mraa.EDGE_RISING, data_collect, data_collect)
 
try:
        while(1):
                test_pulse()
                time.sleep(0.02)
except KeyboardInterrupt:
        buzz.write(0)
	led.write(0)
        exit
