from machine import Pin, SPI, PWM
import time

# SPI Commands
# ToDo: Define the SPI commands
READ_DATA = 
READ_STATUS = 
READ_MANUFACTURER_ID = 
RELEASE_DEEP_POWER_DOWN = 

# SPI Pins
SPI_SCK = 2
SPI_MOSI = 3
SPI_MISO = 0
CS_PIN = 1

cs = Pin(CS_PIN, Pin.OUT)

# ToDo: polarity and phase values differ on some WiFi Routers
spi = SPI(0, baudrate=1000, polarity=1, phase=1, sck=Pin(SPI_SCK), mosi=Pin(SPI_MOSI), miso=Pin(SPI_MISO))


def select_chip():
    cs.value(0)
    time.sleep_us(5)

def deselect_chip():
    time.sleep_us(5)
    cs.value(1)


def read_data(address, length, cmd=READ_DATA):
    select_chip()
    # ToDo spi write_readinto
    deselect_chip()
    return data


address = # ToDo
data = read_data(address, 16)
print("Dumped data:", [hex(x) for x in data])