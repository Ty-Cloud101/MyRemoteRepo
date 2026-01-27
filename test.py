from machine import Pin
import time

# Create LED object on GPIO 2
led = Pin(4, Pin.OUT)

while True:
    led.on()          # Turn LED ON
    print("LED ON")
    time.sleep(2)     # Wait 2 seconds

    led.off()         # Turn LED OFF
    print("LED OFF")
    time.sleep(2)     # Wait 2 seconds
