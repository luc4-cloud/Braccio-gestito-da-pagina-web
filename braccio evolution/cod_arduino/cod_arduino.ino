#include <Servo.h>

Servo servo1;
Servo servo2;

void setup() {
  servo1.attach(9);
  servo2.attach(10);
  Serial.begin(9600);
  Serial.print("pronto");
}

void loop() {
  //if(Serial.available()){
  Serial.println("funziona nel loop");
  String data = Serial.readStringUntil('\n');
  Serial.println(data);
  delay(10000);
  int sep = data.indexOf(',');
  if(sep>0){
    int angolo1 = data.substring(0, sep).toInt();
    int angolo2 = data.substring(sep + 1).toInt();
    servo1.write(angolo1);
    servo2.write(angolo2);
    Serial.print(angolo1);
    Serial.print(angolo2);
  }
}