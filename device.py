import serial
import time

def getDevice():
	try:
		ser = serial.Serial('/dev/ttyACM0') 
	except:
		ser = serial.Serial('/dev/ttyACM1')
	return ser

def write(str_):
	try:
		print str_
		ser.write(b''+str_+'')  
		time.sleep(2)
	except Exception as e:
		print e
		pass