const int trigPin = 23;
const int echoPin = 22;
long duration;

void setup() 
{
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

void loop() 
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  double distance = (double)duration * 345 / 2 / 1000000;
    
  Serial.println(distance); // in meters
  delay(100);
}
