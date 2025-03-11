import os
import serial

ser = serial.Serial('/dev/ttyS0', 9600)  # 根据实际串口设备修改

while True:
    data = ser.readline().decode().strip()
    if data == "poweroff":
        os.system("sudo shutdown -h now")  # 执行关机命令