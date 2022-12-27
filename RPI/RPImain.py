#! /usr/bin python3
import Adafruit_DHT
import RPi.GPIO as GPIO
import serial

ser = serial.Serial("/dev/ttyS0", 9600)  # Open port with baud rate

GPIO.setmode(GPIO.BCM)

sensor = Adafruit_DHT.DHT11
dht11_pin = 4
moisture_pin = 17

GPIO.setup(moisture_pin, GPIO.IN)


def get_dht11_data():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, dht11_pin)
    return temperature, humidity


def get_moisture_data():
    return GPIO.input(moisture_pin)


while True:
    temperature, humidity = get_dht11_data()
    moisture = get_moisture_data()
    ser.write(f"{temperature},{humidity},{moisture}\n")  # transmit data serially
