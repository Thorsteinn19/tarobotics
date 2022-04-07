#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);


  

int weathertemp = 0;
int humid = 0;
String a;

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  pinMode(3,OUTPUT);

  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { 
    Serial.println(F("SSD1306 allocation failed"));  
  }
  delay(200);
  display.clearDisplay();
  display.setTextSize(1);
  display.setCursor(0,0);
  
  display.setTextColor(WHITE);
  display.println("Hello");
  display.display();
  delay(250);
  display.clearDisplay();
  delay(250);
   
  
  
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  
  if (Serial.available() > 0) {
    a = "";
    weathertemp = 0;
    for (int i = 0; i<=Serial.available(); i++){
    a = Serial.readString();
    }
    
    weathertemp = a.substring(0,3).toInt();
    humid = a.substring(3,5).toInt();
    Serial.print("Temprature is ");
    Serial.println(weathertemp);
    Serial.print("Humidity is ");
    Serial.println(humid);
    delay(100);
    

  }

  int sensorValue = analogRead(A1);
  // print out the value you read:
  //Serial.println(sensorValue);
  if (sensorValue<weathertemp) {
    digitalWrite(3,HIGH);
  }
  else {
    digitalWrite(3,LOW);
  }
  display.setCursor(0,0);
  display.print("Temp:");
  display.println(weathertemp);
  display.print("Humidity:");
  display.println(humid);
  display.print("Potent:");
  display.println(sensorValue);
  display.display();
  delay(250);
  display.clearDisplay();// delay in between reads for stability
}
