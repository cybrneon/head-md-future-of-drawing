#define BUTTON_PIN 8

void setup()
{
  // initialize serial communication at 9600 bits per second:
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  Serial.begin(9600);
  Serial.println("Hello World!");
}

void loop()
{
  boolean btn = digitalRead(BUTTON_PIN);
  //Serial.print("Button is ");
  Serial.println("btn");
}
