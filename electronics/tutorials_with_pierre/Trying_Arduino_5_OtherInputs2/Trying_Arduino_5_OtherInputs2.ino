#define LED 13

int lum = 15; //brightness between 0 and 20

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop() {
  // Will get a value between 0 and 1023
  int value = analogRead(A1);
  Serial.println(value);

  // Map the value from 0-1023 range to 0-180 range
  lum = map (value, 0, 1023, 320, 0);

  digitalWrite(LED, HIGH);
  delay(lum);
  digitalWrite(LED, LOW);
  delay(lum);
}