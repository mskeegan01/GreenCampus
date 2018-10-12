#include <OneWire.h>
#include <DallasTemperature.h>
//Pin Output for light

int lightSensor = A5;
int tempSensor = 2;       
int moistureSensor = A0;
int greenLedPin = 5;
int yellowLedPin = 6;
int redLedPin = 7;

int lightIntensity = 0;
int lowerLimit = 15;      //define the lower threshold for the temperature
int upperLimit = 35;      //define the upper threshold for the temperature

OneWire oneWirePin(tempSensor);
DallasTemperature sensors(&oneWirePin);

void setup(void) {
  pinMode(lightSensor, INPUT);
  pinMode(greenLedPin, OUTPUT);
  pinMode(yellowLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);

  Serial.begin(9600);
  sensors.begin();

}

void loop() {
  lightIntensity = analogRead(lightSensor);
  if(lightIntensity < 800){            
    digitalWrite(redLedPin, HIGH);
    Serial.println("redHigh");
    Serial.println(analogRead(lightSensor));
    delay(1000);
  }
  else if(lightIntensity >= 800 && lightIntensity <= 840){
    digitalWrite(yellowLedPin, HIGH);
    Serial.println("yellowHigh");
    Serial.println(analogRead(lightSensor));
    delay(1000);
  }
  else{
    digitalWrite(greenLedPin, HIGH);
    Serial.println("greenHigh");
    Serial.println(analogRead(lightSensor));
    delay(1000);
  }
  delay(2000);
  digitalWrite(greenLedPin, LOW);
  digitalWrite(yellowLedPin, LOW);
  digitalWrite(redLedPin, LOW);
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println("°C");
  delay(2000);

  int output_value = analogRead(moistureSensor);  
  output_value = map(output_value,550,0,0,100);
  Serial.print("Mositure: ");
  Serial.print(output_value);
  Serial.println("%");
  delay(2000);
}
