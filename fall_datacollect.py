import time, math, mraa, socket, select  
import numpy as np
import csv
#Similar as norm datacollect, just save data in different csv 
switch_pin_number=8
buzz_pin_number=6
 
x = mraa.I2c(6)  
MPU = 0x68  
x.address(MPU)  
x.writeReg(0x6B, 0) 

def data_collect(args):
        buzz.write(1)
        time.sleep(0.2)
        buzz.write(0)
        X_Ac = []
        Y_Ac = []
        Z_Ac = []
        X_Gy = []
        Y_Gy = []
        Z_Gy = []
        x.address(MPU)
        for i in range (0,80):
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
        #print "X_Ac:",(X_Ac)
        with open("Fall_X_Accelerometer.csv","ab") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(X_Ac)
        with open("Fall_Y_Accelerometer.csv","ab") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(Y_Ac)
        with open("Fall_Z_Accelerometer.csv","ab") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(Z_Ac) 
        with open("Fall_X_Gyroscope.csv","ab") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(X_Gy)
        with open("Fall_Y_Gyroscope.csv","ab") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(Y_Gy)
        with open("Fall_Z_Gyroscope.csv","ab") as csvfile: 
            writer = csv.writer(csvfile)
            writer.writerow(Z_Gy) 
        buzz.write(1)
        time.sleep(0.2)
        buzz.write(0)
 
 
switch = mraa.Gpio(switch_pin_number)
buzz = mraa.Gpio(buzz_pin_number)

switch.dir(mraa.DIR_IN)
buzz.dir(mraa.DIR_OUT)

switch.isr(mraa.EDGE_RISING, data_collect, data_collect)
 
try:
        while(1):
                pass    
except KeyboardInterrupt:
        buzz.write(0)
        exit