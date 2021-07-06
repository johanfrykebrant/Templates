import os
import glob
import time

device_files = []

def init():
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
     
    base_dir = '/sys/bus/w1/devices/'
    sensors = glob.glob(base_dir + '28*')
    nbrSensors = len(sensors)
    
    for i in range(nbrSensors):
        device_files.append(glob.glob(base_dir + '28*')[i] + '/w1_slave')
    
    return nbrSensors

def read_temp_raw(nbr):
    f = open(device_files[nbr], 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp(nbr):
    lines = read_temp_raw(nbr)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(nbr)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    return "reading failed"


init()

while True:
        print('Sensor 1: ' + str(read_temp(0)) + ' degC')
        time.sleep(2)

