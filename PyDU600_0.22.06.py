import time
import serial
import csv

port = serial.Serial("//dev/ttyUSB0", 
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    writeTimeout = 1,
    timeout = 10)

while True:
    x = port.readline()
    data = open('PP-FOH-009P-0min.csv', 'a')
    writer = csv.writer(data, delimiter = ',')
    writer.writerow([x])
    while x[1] == ' ':
        port.close()
    data.close()

