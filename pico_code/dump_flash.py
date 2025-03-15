from machine import Pin, SPI, PWM
import time

# SPI Commands
READ_DATA = 0x03
READ_STATUS = 0x05
READ_MANUFACTURER_ID = 0x90
RELEASE_DEEP_POWER_DOWN = 0xAB

# SPI Pins
SPI_SCK = 2
SPI_MOSI = 3
SPI_MISO = 0
CS_PIN = 1

cs = Pin(CS_PIN, Pin.OUT)

# ToDo: polarity and phase values differ on some WiFi Routers
spi = SPI(0, baudrate=1000, polarity=0, phase=1, sck=Pin(SPI_SCK), mosi=Pin(SPI_MOSI), miso=Pin(SPI_MISO))


def select_chip():
    cs.value(0)
    time.sleep_us(5)

def deselect_chip():
    time.sleep_us(5)
    cs.value(1)


def read_data(address, length, cmd=READ_DATA):
    select_chip()
    data = bytearray(length)
    spi.write_readinto(bytes([READ_DATA]) + address.to_bytes(3, 'big') + bytes(length-4), data)
    deselect_chip()
    return data


address = 0x00d120
data = read_data(address, 16)
print("Dumped data:", [hex(x) for x in data])
print(data)
