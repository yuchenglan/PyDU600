import serial

port  = serial.Serial("/dev/ttyUSB0",
      baudrate = 9600,
      parity = serial.PARITY_NONE,
      stopbits = serial.STOPBITS_ONE,
      bytesize = serial.EIGHTBITS,
#      bytesize=serial.SEVENBITS,
      writeTimeout = 0,
      timeout = 10)

print(port.isOpen()) 

print("Port opened...")

while True:
     print("inside while")
     response = port.read(8)
     print(response)
     print ("Data Received") 
