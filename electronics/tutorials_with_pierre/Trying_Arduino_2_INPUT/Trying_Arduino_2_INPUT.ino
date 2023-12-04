#define BUTTON_PIN 8
#define LED_PIN 13



void setup()
{
  pinMode(BUTTON_PIN, INPUT_PULLUP); // Connects internal pull-up resistor to button pin
  pinMode(LED_PIN, OUTPUT);

  //turns the led OFF when we start
  digitalWrite(LED_PIN, LOW);

    // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Serial.println("Hello World");
}

// the loop function runs over and over again forever
void loop()
{
  boolean buttonState = digitalRead(BUTTON_PIN); // reading the variable and storing it in buttonState

  digitalWrite(LED_PIN, buttonState);

  int freq = 1; //Hz
  Serial.print(sin(TWO_PI * freq * millis() / 1000.0));
  Serial.print("\t");
  Serial.print(buttonState);

  Serial.println();


  delay(100);
}