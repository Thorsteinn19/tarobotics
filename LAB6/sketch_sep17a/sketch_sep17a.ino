#include <EnableInterrupt.h>

int analogPin = A3;
int analogPinpon = A2;
int a1value = 0;
int a0value = 0;


volatile long encValue = 0;
long prevmillis = 0;
long currentmillis = 0;
long delta =0;
float pps;
int rpm = 0;
int state = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(3,INPUT);
  pinMode(2,INPUT);
  enableInterrupt(3, funcname,RISING);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    pps=(1/delta)*100;
    a0value= analogRead(analogPin);
    a1value = analogRead(analogPinpon);
    
    String sendstring = " "+ String(a0value)+" "+String(a1value)+" "+String(state);
    Serial.print(delta);
    Serial.println(sendstring);
  }


  delay(100); //One measurement per 1 sek

}
void funcname(){
  currentmillis = micros();
  delta = (currentmillis-prevmillis);
  prevmillis = currentmillis;
  state = digitalRead(2);
}
