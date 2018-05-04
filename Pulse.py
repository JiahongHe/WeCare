import mraa
import time
import math

#Initialization
led_pin_number=6
led = mraa.Gpio(led_pin_number)
led.dir(mraa.DIR_OUT)
last_signal = [0]
current_signal = [0]
last_time = [0]
current_time = [0]
BPM = [0]
#Set heart rate test function
def test_pulse():
    #Read raw data from pulse sensor
    Pulse = float(PulSensor.read())
    current_signal[0] = Pulse
    #Calculate BPM (Beat per minute)
    if current_signal[0]>550 and last_signal[0] <550:
        current_time[0] = int(time.time()*1000)
        BPM[0] = 60000/(current_time[0]-last_time[0])
        last_time[0] = current_time[0]
    last_signal[0] = current_signal[0]
    if Pulse > 550:
        led.write(1)
    else:
        led.write(0)
    time.sleep(0.02)
    print(BPM[0])

#set Pulse senor
PulSensor = mraa.Aio(1)

try:
    while(1):
        test_pulse()
except KeyboardInterrupt:
    led.write(0)
    exit
