from mpu6050 import mpu6050
import time, csv, sys

sensor = mpu6050(0x68)
filename = sys.argv[1] if len(sys.argv) > 1 else "data.csv"

with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "x", "y", "z"])
    start = time.time()
    while time.time() - start < 120:  # 2 minutes
        a = sensor.get_accel_data()
        writer.writerow([time.time(), a['x'], a['y'], a['z']])
        time.sleep(0.02)  # 50Hz