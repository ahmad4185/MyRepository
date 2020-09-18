
# Plug & Play Modules Configuration Files!
Hello people! I am glad to announce my brand new series of Plug & Play Module Configuration series. In this repository you will find number of Python codes developed for Raspberry Pi projects. 

## Why We Need this Repository?
Many IoT and Embedded engineers spent a lot of time in configurations of the sensors and modules. The purpose is to save their time and to get them focused on the real solutions. 

## Files Explanation
The explanation of files are given below: 

### 1. MP06050.py
This is Python written library for MPU6050 module to be used with Raspberry Pi. To use this library, make sure that you have installed **smbus** and **Rpi.GPIO** in your Raspberry Pi module:

#### Hardware Pins 
MPU6050 sends data through **I2C** protocol. The information of required pins is given below:

- Connect MPU6050's **VCC** to Raspberry Pi's **5V**
- Connect MPU6050's **GND** to Raspberry Pi's **GND**
- Connect MPU6050's **SDA** to Raspberry Pi's Pin No. **3**
- Connect MPU6050's **SCL** to Raspberry Pi's Pin No. **5**

#### Packages Required
Follow the steps below for installing the packages if you are using **pip** for **Python3**. Otherwise, just replace **pip** with **pip3**.  

```sh
$ pip install smbus
$ pip install RPi.GPIO
```

#### Let's Get the Output
After successfully installing all the packages. Please write following command given below to run the MPU6050.py: 

```sh
$ python3 MPU6050.py
```

*Yahooo!! We got our output now and we saved the precious 2 days our life. Let's utilize it in completing our projects!*


### 2. Ultrasonic.py
This is Python written library for Ultrasonic sensor module. The distance programming has been done in centimeters. To use this library, make sure that you have installed **Rpi.GPIO** in your Raspberry Pi module:

#### Hardware Pins 
Ultrasonic sensor module calculates distance by initiating the **trigger** and capturing by **echo**. After this we simply use _S = v t_ formula along with _Speed of Sound in Air_ to get the distance in **centimeters**:

- Connect Ultrasonic sensor module's **VCC** to Raspberry Pi's **5V**
- Connect Ultrasonic sensor module's **GND** to Raspberry Pi's **GND**
- Connect Ultrasonic sensor module's **TRIG** to Raspberry Pi's Pin No. **23**
- Connect Ultrasonic sensor module's **ECHO** to Raspberry Pi's Pin No. **24**

#### Packages Required
Follow the steps below for installing the packages if you are using **pip** for **Python3**. Otherwise, just replace **pip** with **pip3**.  

```sh
$ pip install RPi.GPIO
```

#### Let's Get the Output
After successfully installing all the packages. Please write following command given below to run the Ultrasonic.py: 

```sh
$ python3 Ultrasonic.py
```

*Yahooo!! We are getting distance now!!!! Now let's make obstacle avoidance robot*

### 3. GPIO_Clean.py
Imagine, you are working on RC car project and after breaking your code, the motors are still running. Why?? 
It is because you did not clear the GPIO pins. They are still working even after your breaking the code!!!
How to stop the motors? **GPIO_Clean.py** helps you to make you calm. No hard instructions. Just run this file 
everytime you feel that I do not want to work on my project more. Let's work on anoter. The instructions are 
super easy. Please write following command given below to run the GPIO_Clean.py

```sh
$ python3 GPIO_Clean.py
```
*Seems like our GPIO pins are now in peace. Hail Peace and Inner Satisfaction!! Pheewww...*
