int turn_counter = 0;

///////////////////////// SENSORS

//Sensor 1
const int trigPin1 = 31;
const int echoPin1 = 30;
long duration1;

//Sensor 2
const int trigPin2 = 27;
const int echoPin2 = 26;
long duration2;

//Sensor 3 
const int trigPin3 = 23;
const int echoPin3 = 22;
long duration3;

//Sensor 4
const int trigPin4 = 35;
const int echoPin4 = 34;
long duration4; 

///////////////////////// MOTORS

//enable for H Bridge 1 (front of car)
const int enableA_H1 = 2;
const int enableB_H1 = 3;

//Motor A_H1 (left)
const int motorPin1_H1  = 4;  
const int motorPin2_H1  = 5; 
//Motor B_H1 (right)
const int motorPin3_H1  = 7; 
const int motorPin4_H1  = 6; 

//enable for H bridge 2 (back of car)
const int enableA_H2 = 8;
const int enableB_H2 = 9;

//Motor A_H2 (left)
const int motorPin1_H2 = 11;
const int motorPin2_H2 = 10;
//Motor B_H2 (right)
const int motorPin3_H2 = 12;
const int motorPin4_H2 = 13;

void setup() 
{
  Serial.begin(9600);
  
  //Set pin modes for sensors
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin3, OUTPUT);
  pinMode(echoPin3, INPUT);
  pinMode(trigPin4, OUTPUT);
  pinMode(echoPin4, INPUT);
  
  //Set pin modes for motors
  pinMode(enableA_H1, OUTPUT);
  pinMode(enableB_H1, OUTPUT);
  pinMode(motorPin1_H1, OUTPUT);
  pinMode(motorPin2_H1, OUTPUT);
  pinMode(motorPin3_H1, OUTPUT);
  pinMode(motorPin4_H1, OUTPUT);
  pinMode(enableA_H2, OUTPUT);
  pinMode(enableB_H2, OUTPUT);
  pinMode(motorPin1_H2, OUTPUT);
  pinMode(motorPin2_H2, OUTPUT);
  pinMode(motorPin3_H2, OUTPUT);
  pinMode(motorPin4_H2, OUTPUT);
    
  //Set enable pins for H Bridges
  analogWrite(enableA_H1, 255);
  analogWrite(enableB_H1, 255);
  analogWrite(enableA_H2, 255);
  analogWrite(enableB_H2, 255);

  delay(2000);

  //Sensor 1
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);

  duration1 = pulseIn(echoPin1, HIGH);
  double distance1 = (double)duration1 * 345 / 2 / 1000000;

  //Read distance on sensor 2
  delayMicroseconds(2);
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  
  duration2 = pulseIn(echoPin2, HIGH);
  double distance2 = (double)duration2 * 345 / 2 / 1000000;

  //Read distance on sensor 3
  delayMicroseconds(2);
  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);
  
  duration3 = pulseIn(echoPin3, HIGH);
  double distance3 = (double)duration3 * 345 / 2 / 1000000;

  //Read distance on sensor 4
  delayMicroseconds(2);
  digitalWrite(trigPin4, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin4, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin4, LOW);
  
  duration4 = pulseIn(echoPin4, HIGH);
  double distance4 = (double)duration4 * 345 / 2 / 1000000;

  String data = String(String(distance1) + "," + String(distance2) + "," + String(distance3) + "," + String(distance4) + "," + String(turn_counter));
  Serial.println(data);
}

void loop() 
{
  //Read distance on sensor 1, put value into array
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin1, LOW);

  duration1 = pulseIn(echoPin1, HIGH);
  double distance1 = (double)duration1 * 345 / 2 / 1000000;

  //Read distance on sensor 2
  delayMicroseconds(2);
  digitalWrite(trigPin1, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin2, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);
  
  duration2 = pulseIn(echoPin2, HIGH);
  double distance2 = (double)duration2 * 345 / 2 / 1000000;
  
  //Read distance on sensor 3
  delayMicroseconds(2);
  digitalWrite(trigPin3, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin3, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin3, LOW);
  
  duration3 = pulseIn(echoPin3, HIGH);
  double distance3 = (double)duration3 * 345 / 2 / 1000000;

  //Read distance on sensor 4
  delayMicroseconds(2);
  digitalWrite(trigPin4, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin4, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin4, LOW);
  
  duration4 = pulseIn(echoPin4, HIGH);
  double distance4 = (double)duration4 * 345 / 2 / 1000000;

  //Have car move if front of car reaches wall
  if (distance2 > 0.07 && distance3 > 0.07) {
    forward();
  }
  else {
    turn_counter++;
    turn_right();
  }

  String data = String(String(distance1) + "," + String(distance2) + "," + String(distance3) + "," + String(distance4) + "," + String(turn_counter));
  Serial.println(data);

  if (turn_counter == 4)
  {
    while (1)
      stop_moving();
  }
}

void forward()
{
  //H Bridge 1
  digitalWrite(motorPin1_H1, LOW);
  digitalWrite(motorPin2_H1, HIGH);
  digitalWrite(motorPin3_H1, LOW);
  digitalWrite(motorPin4_H1, HIGH);
  //H Bridge 2
  digitalWrite(motorPin1_H2, LOW);
  digitalWrite(motorPin2_H2, HIGH);
  digitalWrite(motorPin3_H2, LOW);
  digitalWrite(motorPin4_H2, HIGH);
}

void turn_right()
{
  //Motor A_H1 goes forward, Motor B_H1 goes backward
  digitalWrite(motorPin1_H1, LOW);
  digitalWrite(motorPin2_H1, HIGH);
  digitalWrite(motorPin3_H1, HIGH);
  digitalWrite(motorPin4_H1, LOW);
  //Motor A_H2 goes forward, Motor B_H2 goes backward
  digitalWrite(motorPin1_H2, LOW);
  digitalWrite(motorPin2_H2, HIGH);
  digitalWrite(motorPin3_H2, HIGH);
  digitalWrite(motorPin4_H2, LOW);

  delay(2850);
}

void turn_left()
{
  //Motor A_H1 goes backward, Motor B_H1 goes forward
  digitalWrite(motorPin1_H1, HIGH);
  digitalWrite(motorPin2_H1, LOW);
  digitalWrite(motorPin3_H1, LOW);
  digitalWrite(motorPin4_H1, HIGH);
  //Motor A_H2 goes backward, Motor B_H2 goes forward
  digitalWrite(motorPin1_H2, HIGH);
  digitalWrite(motorPin2_H2, LOW);
  digitalWrite(motorPin3_H2, LOW);
  digitalWrite(motorPin4_H2, HIGH);

  delay(2900);
}

void stop_moving()
{
  //H Bridge 1
  digitalWrite(motorPin1_H1, LOW);
  digitalWrite(motorPin2_H1, LOW);
  digitalWrite(motorPin3_H1, LOW);
  digitalWrite(motorPin4_H1, LOW);
  //H Bridge 2
  digitalWrite(motorPin1_H2, LOW);
  digitalWrite(motorPin2_H2, LOW);
  digitalWrite(motorPin3_H2, LOW);
  digitalWrite(motorPin4_H2, LOW);
}
