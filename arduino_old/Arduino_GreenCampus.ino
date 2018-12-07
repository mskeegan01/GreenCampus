#include <OneWire.h>
#include <DallasTemperature.h>

const int moistureSensor = A0;
const int lightSensor = A1;
const int BLUE = 6;
const int tempSensor = 8;

OneWire oneWirePin(tempSensor);
DallasTemperature sensors(&oneWirePin);

void setup(void) {
  pinMode(lightSensor, INPUT);
  Serial.begin(9600);
  sensors.begin();
}

//Configures the light according to its perfect value.
int lightRegulation(int lightIntensity){
  int idealLightValue = 950;
  if (lightIntensity != idealLightValue) {
     int lightDifference = idealLightValue - lightIntensity;
  return lightDifference;
  }
}

int trackLightValue(){
  int lightIntensity = analogRead(lightSensor);
  return lightIntensity;
}


int trackTempValue(){
  sensors.requestTemperatures();
  float temperature = sensors.getTempCByIndex(0);
  return temperature;
}

int trackMoistValue(){
  int moistValue = analogRead(moistureSensor);
  moistValue = map(moistValue, 550, 0, 0, 100);
  return moistValue;
}

void printData(){
  Serial.print("Lightintensity: ");
  Serial.println(trackLightValue());
  Serial.print("Temperature: ");
  Serial.print(trackTempValue());
  Serial.println("°C");
  Serial.print("Moisture: ");
  Serial.print(trackMoistValue());
  Serial.println("%");
}
void loop() {
analogWrite(BLUE, lightRegulation(trackLightValue));
printData();
delay(5000);
}
//TODO
//Connect WifiAdapter and let it send data to the database
//Build the watertank
//Find out which temperature is the best for the plant.
//Find the values for really completly dry and completly wet and set the values according to that.
