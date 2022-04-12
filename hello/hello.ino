
#include <avr/io.h>

#define F_CPU 1000000UL
void setup() {
  // put your setup code here, to run once:
  Serial.begin(38400);
}

void loop() {
  // put your main code here, to run repeatedly:
if (Serial.available() > 0){
  Serial.println("Hallo");
}
}
