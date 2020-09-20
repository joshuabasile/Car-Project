import serial

SerialPort = serial.Serial("COM5", "9600", timeout=1)

while (1):
    IncomingData = SerialPort.readline()
    if (IncomingData):
        ard_data = str(IncomingData.decode('utf-8'))
        ard_data = ard_data.rstrip().split(',')
        print(ard_data)




