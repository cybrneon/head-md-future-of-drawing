#define PIEZO 9

void setup()
{
  pinMode(PIEZO, OUTPUT);
}

void loop()
{
  
  // digitalWrite(PIEZO, HIGH); //5V sent to the PIEZO
  // delay(4);
  // digitalWrite(PIEZO, LOW); //0V
  // delay(4);

  //plays 1 sec
  tone(PIEZO, 40, 50);

    //plays 1 sec
  tone(PIEZO, 40, 50);  
  tone(PIEZO, 60, 20);
  delay(20);
  noTone(PIEZO);

  delay(2000);
}
