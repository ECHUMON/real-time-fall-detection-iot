import serial
import csv
import time
from datetime import datetime

print("📊 CSV Logger Started (Final Stable Version)")

# -------------------------------
# SERIAL CONNECTION
# -------------------------------
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
    time.sleep(2)
    print("✅ Connected to Arduino on COM3")
except Exception as e:
    print("❌ Serial connection failed:", e)
    exit()

# -------------------------------
# CSV FILE SETUP
# -------------------------------
file_name = "fall_data.csv"

try:
    file = open(file_name, "a", newline="")
    writer = csv.writer(file)

    # Clean header
    writer.writerow([])
    writer.writerow(["--- NEW SESSION ---"])
    writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    writer.writerow(["time", "ax", "ay", "az", "extra", "status"])
    file.flush()

except Exception as e:
    print("❌ CSV setup failed:", e)
    exit()

print("📁 Logging started...\n")

# -------------------------------
# MAIN LOOP
# -------------------------------
while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()

        if not line:
            continue

        print("DATA:", line)

        parts = [p.strip() for p in line.split(",")]

        # ❗ Skip completely broken data
        if len(parts) < 4:
            print("⚠ Skipped bad line:", line)
            continue

        # Extract values safely
        ax = parts[0]
        ay = parts[1]
        az = parts[2]

        # Handle both formats (4 or 5 values)
        if len(parts) >= 5:
            extra = parts[3]
            status = parts[4]
        else:
            extra = "N/A"
            status = parts[3]

        # Write to CSV
        writer.writerow([
            datetime.now().strftime("%H:%M:%S"),
            ax,
            ay,
            az,
            extra,
            status
        ])

        file.flush()  # 🔥 ensures real-time saving

        print("✔ CSV SAVED")

    except Exception as e:
        print("❌ Error:", e)