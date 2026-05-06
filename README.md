# real-time-fall-detection-iot
IoT-based fall detection system using Arduino with real-time sensor data, CSV logging, visualization, and automated email alerts via SendGrid.

# 🛡️ IoT Fall Detection System (Arduino + Python)

## 📌 Project Overview
This project is an **IoT-based Fall Detection System** designed to detect fall events using motion sensor readings collected from an **Arduino board**. The Arduino continuously sends real-time sensor data to a Python program through **Serial Communication**.

The Python backend processes this live sensor stream, detects fall-like motion patterns using **threshold-based logic**, and instantly triggers an **email alert** using the **SendGrid API**. The system also supports **CSV logging** for storing sensor readings and includes a visualization module to plot recorded data for analysis.

This project can be useful for **elderly monitoring, healthcare safety systems, and wearable/assistive IoT devices**.

---

## ⚙️ System Architecture
Arduino Sensor Module
↓ (Serial Data)
Python Fall Detection Logic
↓
Fall Detected? → YES → SendGrid Email Alert
↓
Optional CSV Logging
↓
Visualization Module (Matplotlib Graphs)
------------


---

## 🧠 Key Features
✅ Real-time sensor data collection using Arduino  
✅ Live Serial communication between Arduino and Python  
✅ Fall detection using threshold-based logic  
✅ Automatic email alert system using SendGrid API  
✅ CSV logging for storing sensor readings  
✅ Offline visualization of recorded sensor values using Matplotlib  

---

## 🛠️ Tech Stack
- **Arduino IDE** (Sensor data collection + transmission)
- **Python** (Data processing + fall detection logic)
- **SendGrid API** (Email alerts)
- **CSV** (Data storage)
- **Matplotlib** (Visualization)

---

## 📂 Repository Structure
| File Name | Description |
|----------|-------------|
| `fall_detection_arduino.ino` | Arduino program for sensor reading + serial transmission |
| `sendgrid_fall_alert_service.py` | Python script for fall detection + email alert system |
| `csv_logger_only.py` | Logs serial sensor readings into a CSV file |
| `visualization.py` | Generates graphs from stored CSV data |
| `README.md` | Documentation |

---

## 🔌 Hardware Requirements
To run this project, you need:
- Arduino Board (Uno / Nano / Mega)
- Motion Sensor / Accelerometer Module (example: MPU6050 or similar)
- USB cable for connecting Arduino to PC
- Laptop/PC with Python installed

---

## 💻 Software Requirements
- Arduino IDE installed
- Python 3.x installed
- Required Python libraries:
  - `sendgrid`
  - `matplotlib`
  - `csv` (built-in)
  - `serial` (pyserial)

---

## 📦 Installation & Setup
2️⃣ Install Required Python Packages
pip install pyserial matplotlib sendgrid
3️⃣ Upload Arduino Code
Open Arduino IDE

Open the file:

fall_detection_arduino.ino

Select your Arduino board from:
Tools → Board
Select the correct COM port from:
Tools → Port
Click Upload

🔑 SendGrid Email Setup
Step 1: Create a SendGrid Account

Go to SendGrid and create an account.

Step 2: Generate an API Key
Go to Settings → API Keys
Create a new API key
Copy and save it

Step 3: Add API Keyto Code

In sendgrid_fall_alert_service.py, locate the API key section and paste your key:

SENDGRID_API_KEY = "YOUR_SENDGRID_API_KEY"

Also update sender and receiver emails:

FROM_EMAIL = "your_verified_email@example.com"
TO_EMAIL = "receiver_email@example.com"

⚠️ Note: SendGrid requires sender email verification.

🚨 How the System Works
Step-by-step Workflow
Arduino reads motion/accelerometer sensor values continuously.
Arduino sends sensor readings to Python via Serial port.
Python reads the data stream live.
Python applies fall detection logic based on threshold conditions.
If fall detected:
Python triggers SendGrid API
Email alert is sent instantly
Sensor values can optionally be stored in CSV format.
Visualization script plots recorded sensor values for analysis.

🧪 Fall Detection Logic (Threshold Based)

The current implementation uses a simple threshold-based approach such as:

Sudden spike in acceleration values
Sudden change in orientation
Motion instability within a short time window

This method is fast and works well for prototypes but can be improved using ML models later.
-----------------------
▶️ Running the Project
-----------------------
1️⃣ Run the Fall Detection + Email Alert Script
python sendgrid_fall_alert_service.py

Make sure Arduino is connected and sending data.

2️⃣ Run CSV Logger (Optional)

To store sensor readings in a CSV file:

python csv_logger_only.py

This will generate a .csv file containing sensor readings.

3️⃣ Run Visualization Script

After CSV is generated, run:

python visualization.py

This will plot sensor values in graph form for offline analysis.

📊 Output Example
Live serial monitor shows sensor readings continuously.
When fall is detected:
Terminal prints: "Fall Detected!"
Email alert is sent immediately.
CSV file stores readings for later analysis.
Visualization script generates acceleration graphs.
🧩 Possible Applications

🏥 Elderly healthcare monitoring systems
🏠 Smart home safety solutions
⌚ Wearable fall detection devices
🚑 Emergency alert systems
🧑‍⚕️ Patient monitoring in hospitals

🚀 Future Improvements

🔹 Machine Learning-based fall detection for better accuracy
🔹 Mobile app integration (SMS / push notifications)
🔹 Cloud database storage (Firebase / AWS / MongoDB)
🔹 Real-time dashboard UI (Flask / Streamlit / Web app)
🔹 Add buzzer or alarm module for local alerting

⚠️ Limitations
Threshold-based detection may produce false positives.
Sensor calibration may be required depending on hardware.
Email alert depends on internet connectivity and SendGrid service.
=============================================================================
👨‍💻 Author
Nayan
=============================================================================

📜 License

This project is open-source and available for educational and research purposes.

