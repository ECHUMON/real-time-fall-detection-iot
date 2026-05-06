import serial
import time
from datetime import datetime
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

print("📡 Fall Detection Email System Started")

# ---------------- SERIAL CONFIG ----------------
SERIAL_PORT = "COM3"
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2)

# ---------------- SENDGRID CONFIG ----------------
SENDGRID_API_KEY = "ADD UR API KEY FROM SENDGRID "# use ur api key

EMAIL_SENDER = "use ur sender email"   # must match SendGrid verified sender
EMAIL_RECEIVER = "use ur reciever email"

# ---------------- COOLDOWN ----------------
last_alert = 0
cooldown = 30  # seconds

# ---------------- EMAIL FUNCTION ----------------
def send_email():
    message = Mail(
        from_email=EMAIL_SENDER,
        to_emails=EMAIL_RECEIVER,
        subject="⚠ FALL DETECTED ALERT",
        plain_text_content=f"""
⚠ FALL DETECTED ALERT

Time: {datetime.now()}
System: Arduino Fall Detection System

Please check immediately.
"""
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print("📧 Email sent! Status:", response.status_code)

    except Exception as e:
        print("❌ SendGrid error:", e)

# ---------------- MAIN LOOP ----------------
while True:
    try:
        line = ser.readline().decode("utf-8", errors="ignore").strip()

        if line:
            print("📥 Arduino:", line)

        if "FALL DETECTED" in line:
            now = time.time()

            if now - last_alert > cooldown:
                print("⚠ FALL DETECTED → Sending email...")
                send_email()
                last_alert = now
            else:
                print("⏳ Cooldown active. Email not sent.")

    except Exception as e:
        print("❌ Error:", e)
        time.sleep(1)