/*

*/
const int trigPin = 3;
const int echoPin = 4;
long duration;

void setup()
{
  //setup code here, runs once
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() 
{
  // main code, runs repeatedly
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  //send a 10 second high pulse
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  //store the high pulse's duration
  duration = pulseIn(echoPin, HIGH);
  double distance = (double)duration * 345 / 2 / 1000000;
  Serial.println(distance); // in meters
}

// @param microseconds a number of microseconds
// @return the conversion of the provided microseconds into a distance

const double distance(const long microseconds) 
{
// Initialize m and b to their respective values in the formula, y = mx + b.
// y = distance, x = time (in microseconds).
const double m = 0.8799510004;
const double b = 0.004083299306;
return m * microseconds + b;
}

// blutooth setup

//#include <SoftwareSerial.h>
//char Incoming_value = 0;    

//SoftwareSerial mySerial(3,4);//Variabe for storing Incoming_value

//oid setup() 
//{
 // Serial.begin(9600);//Sets the baud rate for serial data transmission 
//}
//void loop()
//{
 // if(Serial.available() > 0) 
 // {
  //  float val = 30.00;
  //  char cmd = Serial.read(); 
  //  if (cmd == 's')
   // {
   //   Serial.println(val);
   //   delay(100);
  //  }
 // }
//}
