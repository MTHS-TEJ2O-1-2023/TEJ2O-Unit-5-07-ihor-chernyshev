from microbit import *
from microbit import i2c
import time

_PCA9685_ADDRESS = 0x40
_MODE1 = 0x00
_PRESCALE = 0xFE
_LED0_ON_L = 0x06

_STP_CHA_L = 2047
_STP_CHA_H = 4095
_STP_CHB_L = 1
_STP_CHB_H = 2047
_STP_CHC_L = 1023
_STP_CHC_H = 3071
_STP_CHD_L = 3071
_STP_CHD_H = 1023


class PCA9685:
    def __init__(self):
        self.write(_PCA9685_ADDRESS, _MODE1, 0x00)
        self.setFreq(50)
        for i in range(0, 16):
            self.setPwm(i, 0, 0)

    def write(self, addr, reg, val):
        i2c.write(addr, bytes([reg, val]))

    def read(self, addr, reg):
        i2c.write(addr, bytes([reg]))
        return i2c.read(addr, 1)[0]

    def setFreq(self, freq):
        prescale = round(
            25000000.0 / 4096.0 / freq - 1
        )  # since python 3, round returns int.
        oldmode = self.read(_PCA9685_ADDRESS, _MODE1)
        newmode = (oldmode & 0x7F) | 0x10  # sleep
        self.write(_PCA9685_ADDRESS, _MODE1, newmode)  # go to sleep
        self.write(_PCA9685_ADDRESS, _PRESCALE, prescale)  # set the prescaler
        self.write(_PCA9685_ADDRESS, _MODE1, oldmode)
        time.sleep_us(5000)
        self.write(_PCA9685_ADDRESS, _MODE1, oldmode | 0xA1)

    def setPwm(self, channel, on, off):
        i2c.write(
            _PCA9685_ADDRESS,
            bytes(
                [
                    _LED0_ON_L + 4 * channel,
                    on & 0xFF,
                    (on >> 8) & 0xFF,
                    off & 0xFF,
                    (off >> 8) & 0xFF,
                ]
            ),
        )

    def setServoDegrees(self, servo, degree):  # servo: 1, etc.
        v_us = degree * 1800 / 180 + 600  # 0.6 ~ 2.4
        value = v_us * 4096 / 20000
        self.setPwm(servo + 7, 0, round(value))

    def releaseServo(self, servo):  # servo: 1, etc.
        self.setPwm(servo + 7, 0, 0)


pca = PCA9685()

while True:
    pca.setServoDegrees(1, 0)
    sleep(500)
    pca.setServoDegrees(1, 180)
    sleep(500)
