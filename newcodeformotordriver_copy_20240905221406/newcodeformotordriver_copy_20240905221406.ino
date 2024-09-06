#include <Wire.h>
#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 

// Store motors in an array for quick access
Adafruit_DCMotor *motors[4] = {AFMS.getMotor(1), AFMS.getMotor(2), AFMS.getMotor(3), AFMS.getMotor(4)};

// Optimized motor control function
void setMotor(byte motor, byte direction, byte speed) {
  if (motor < 1 || motor > 4) return;  // Ensure motor index is valid

  Adafruit_DCMotor *MOTO = motors[motor - 1];
  
  MOTO->setSpeed(speed);
  
  switch (direction) {
    case 1:
      MOTO->run(FORWARD);
      break;
    case 0:
      MOTO->run(BACKWARD);
      break;
    default:
      MOTO->run(RELEASE);
      break;
  }
}

void setup() {
  Serial.begin(9600);  // Start serial communication at 9600 baud rate
  AFMS.begin();        // Start the Motor Shield
}

void loop() {
  if (Serial.available() >= 12) {  // Wait until 12 bytes are available
    byte byteArray[12];
    Serial.readBytes(byteArray, 12);  // Read 12 bytes

    for (int i = 0; i < 12; i += 3) {
      byte motor = byteArray[i];
      byte direction = byteArray[i + 1];
      byte speed = byteArray[i + 2];

      setMotor(motor, direction, speed);  // Set each motor
    }
  }
}
