#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)

Adafruit_BME280 bme; // I2C
//Adafruit_BME280 bme(BME_CS); // hardware SPI
//Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO, BME_SCK); // software SPI



//-------------Constantes----------------
//--Sistema
int id = 0;

//--Higrometro
const int AirValue = 620;   //valor señal analogica al aire
const int WaterValue = 310;  //valor señal analogica en agua

//-- Pines direccion can
const int pin0 = 1;
const int pin1 = 2;
const int pin2 = 3;
const int pin3 = 4;
int AdressPins[] = {pin0, pin1, pin2, pin3};



void setup(){
    Serial.begin(9600);
    pinMode(pin0, INPUT);
    pinMode(pin1, INPUT);
    pinMode(pin2, INPUT);
    pinMode(pin3, INPUT);

    while(!Serial);    // time to get serial running
    
    Serial.println(F("BME280 test"));

    unsigned status;
    
    // default settings
    // (you can also pass in a Wire library object like &Wire2)
    status = bme.begin();  
    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!");
        Serial.print("SensorID was: 0x");
        Serial.println(bme.sensorID(),16);
        Serial.print("        ID of 0xFF probably means a bad address, a BMP 180 or BMP 085\n");
        Serial.print("   ID of 0x56-0x58 represents a BMP 280,\n");
        Serial.print("        ID of 0x60 represents a BME 280.\n");
        Serial.print("        ID of 0x61 represents a BME 680.\n");
        while (1);
    }
    
    long delayTime = 1000;

    Serial.println();
}

void readSoilHumidity(int AnalogInputPin){
  int AnalogRead = analogRead(AnalogInputPin);
  int soilMoisturePercent = map(AnalogRead, AirValue, WaterValue, 0, 100);
  if(soilMoisturePercent >= 100)
  {
    return(100);
  }
  else if(soilMoisturePercent <=0)
  {
    return(0);
  }
  else if(soilMoisturePercent >0 && soilMoisturePercent < 100)
  {
    return(soilMoisturePercent);    
  }
}


void resolveId(){ //Convierte los interruptores de 4 pines en un numero natural que se emplea como id
  id = 0;
  char *cadenaBinaria = "";
  for(int i = 0; i < 3; i++){  
    if(digitalRead(AdressPins[i])== HIGH ){
      char *cadenaBinaria = *cadenaBinaria + "1";
    }
    else{
      char *cadenaBinaria = *cadenaBinaria + "0";
    }
  int multiplicador = 1;
  char caracterActual;
  for (int i = 4 - 1; i >= 0; i--) {
    caracterActual = cadenaBinaria[i];
    if (caracterActual == '1') {
      id += multiplicador;
    }
    multiplicador = multiplicador * 2;
  }
  return id;
}

}
