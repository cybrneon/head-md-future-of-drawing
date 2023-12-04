#define LED 13 //Define the constant
boolean val = HIGH; //Variable (needs a semicolon)

//Turns on the on-board LED
void setup()
{
  pinMode(LED, OUTPUT);
}

// the loop function runs over and over again forever
void loop()
{
  digitalWrite(LED, val);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  val = !val;
}