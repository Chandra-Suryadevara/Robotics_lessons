#include <Wire.h>
#include <Adafruit_MotorShield.h>

int M_Y[4] = {22, 24, 28, 32};  // Yellow pin numbers for motors 1 to 4
int M_G[4] = {23, 25, 29, 33};  // Green pin numbers for motors 1 to 4

byte byteArray[8];


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

  for (int i = 0; i < 4; i++) {
    pinMode(M_Y[i], INPUT);
    pinMode(M_G[i], INPUT);
  }
}

void loop() {



  if (Serial.available() >= 12) {
   byte byteArray[12];
   Serial.readBytes(byteArray, 12);  

   for (int i = 0; i < 12; i += 3) {
      byte motor = byteArray[i];
      byte direction = byteArray[i + 1];
      byte speed = byteArray[i + 2];

      setMotor(motor, direction, speed);
   }
  }
  
  for (int i = 0; i < 8; i+=2) {
    int index = i /2;
    byteArray[i] = digitalRead(M_Y[index]);     // Store Yellow pin values
    byteArray[i + 1] = digitalRead(M_G[index]); // Store Green pin values
  }

  Serial.write(byteArray, sizeof(byteArray));

}
