#include <Arduino_BMI270_BMM150.h>
#include <math.h>

float impactThreshold = 2.5;
float stillThreshold = 1.2;

bool impactDetected = false;
unsigned long impactTime = 0;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!IMU.begin()) {
    Serial.println("IMU FAILED");
    while (1);
  }

  Serial.println("ax,ay,az,accMag,status");
}

void loop() {
  float ax = 0, ay = 0, az = 0;

  if (IMU.accelerationAvailable()) {
    IMU.readAcceleration(ax, ay, az);
  }

  float accMag = sqrt(ax*ax + ay*ay + az*az);

  const char* status = "NORMAL";

  // Step 1: impact detection
  if (!impactDetected && accMag > impactThreshold) {
    impactDetected = true;
    impactTime = millis();
    status = "IMPACT";
  }

  // Step 2: fall confirmation
  if (impactDetected) {
    if (millis() - impactTime > 2000) {
      if (accMag < stillThreshold) {
        status = "FALL DETECTED";
      }
      impactDetected = false;
    }
  }

  Serial.print(ax); Serial.print(",");
  Serial.print(ay); Serial.print(",");
  Serial.print(az); Serial.print(",");
  Serial.print(accMag); Serial.print(",");
  Serial.println(status);

  delay(100);
}