#import serial, string, time

#print("Start")

#output = ""
#ser = serial.Serial('/dev/ttyACM0', 9600, 8, 'N', 1, timeout=1)

#for i in range(0,256):
#    print unichr(i)
#    ser.write(chr(i))
#    time.sleep(1)


#use PIN 13 GPIO on Pi
import serial, time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.output(13,0)
ser = serial.Serial('/dev/ttyACM0', 2000000)
data = []
sendOn = True
counter = 0
unoSW = 13
#digitalwrite high from gpio pin to arduin digital in
GPIO.output(unoSW,1)
print("sent high")
time.sleep(3) # allow collection of data for 1 second
#digitalwrite low from gpio pins to uno
GPIO.output(unoSW,0)
print("Sent LOW")

while counter==0:
    #print("READING")
    read_serial=ser.readline()
    element = read_serial[:-2]
    print("LINE READ - "),
    print(element)
    if(element=='done'):
        counter=1
    else:
    #print("Length is: "),
    #print(len(read_serial))
    #print(read_serial[1])
    #print(read_serial[2])
    #readString = str(read_serial)
    #newString = readString.replace("a", "")
        
    #print read_serial
    #print element
        data.append(element)
    #print newString

print("Collected this data")
print(data)
print("LENGHT IS : ")
print(len(data))

f = open("scanTestD.txt", "a+")
for i in data:
    print i
    f.write(str(i) + " ")
f.write("\n")
f.close()

GPIO.cleanup()
