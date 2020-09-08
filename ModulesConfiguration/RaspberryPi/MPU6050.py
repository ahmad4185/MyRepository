import RPi.GPIO as GPIO
import time
import smbus
import math
GPIO.setmode(GPIO.BCM)
#-------------------------------------------
# Some MPU6050 Registers and their Address
#-------------------------------------------

PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

#-------------------------------------------
# Post-Processed MPU6050 Global Variables
#-------------------------------------------

Ax=0
Ay=0
Az=0
Gx=0
Gy=0
Gz=0
G_x=0
G_y=0
G_z=0
A_x=0
A_y=0
A_z=0
a = 0
factor = 1.0
Mul_acc = 16384.0/factor
Mul_gyro= 131.0/factor

SAMPLING_RATE = 60
SAMPLING_TIME = 1/SAMPLING_RATE
    
    
def MPU_values():
    global Ax
    global Ay
    global Az
    global Gx
    global Gy
    global Gz
    global A_x
    global A_y
    global A_z
    global Mul_acc
    global Mul_gyro
    
    
        #Read Accelerometer raw value
    acc_x = read_raw_data(ACCEL_XOUT_H)
    acc_y = read_raw_data(ACCEL_YOUT_H)
    acc_z = read_raw_data(ACCEL_ZOUT_H)
    
    #Read Gyroscope raw value
    gyro_x = read_raw_data(GYRO_XOUT_H)
    gyro_y = read_raw_data(GYRO_YOUT_H)
    gyro_z = read_raw_data(GYRO_ZOUT_H)
    Ax = acc_x/Mul_acc
    #Ax = acc_x
    Ay = acc_y/Mul_acc
    #Ay = acc_y
    Az = acc_z/Mul_acc
    #Az = acc_z
    Gx = gyro_x/Mul_gyro
    Gy = gyro_y/Mul_gyro
    Gz = gyro_z/Mul_gyro
    x2 = Ax*Ax
    y2 = Ay*Ay
    z2 = Az*Az
    sqr_x = math.sqrt(y2+z2)
    sqr_y = math.sqrt(x2+z2)
    sqr_z = math.sqrt(y2+x2)
    A_x = 57.298*math.atan2(Ax,sqr_x)
    A_y = 57.298*math.atan2(Ay,sqr_y)
    A_z = 57.298*math.atan2(Az,sqr_z)
    
def MPU_Init():
    #write to sample rate register
    bus.write_byte_data(Device_Address, SMPLRT_DIV, 0)
    
    #Write to power management register
    bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
    
    #Write to Configuration register
    bus.write_byte_data(Device_Address, CONFIG, 1)
    
    #Write to Gyro configuration register
    bus.write_byte_data(Device_Address, GYRO_CONFIG, 0)
    
    #Write to interrupt enable register
    bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
    #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)
        #concatenate higher and lower value
        value = ((high << 8) | low)
        
        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value
bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address
#plt.ion()
MPU_Init()    
    

#This is a test code. You can change it according to your application.     
while (1):
    MPU_values()
    print("Ax = ",round(A_x,0), "| Ay = ", round(A_y,0), "| Az = ", round(A_z,0))
    time.sleep(SAMPLING_TIME)
