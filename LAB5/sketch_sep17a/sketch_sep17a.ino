#include <Servo.h>

Servo lightservo;
int analogPin = A3;
int analogPinpon = A2;
int a1value = 0;
int a0value = 0;
String DC = "a";
String STEP = "b";

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  //lightservo.attach(6);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    a0value= analogRead(analogPin);
    a1value = analogRead(analogPinpon);
    String sendstring = String(a0value)+" "+String(a1value);
    Serial.println(sendstring);
  }
  // If the motor is connected to the arduino uncomment this and line 14
  //if (a0value > 880) lightservo.write(180);
  //if (a0value <= 880) lightservo.write(0);

  delay(100); //One measurement per 1 sek

}
