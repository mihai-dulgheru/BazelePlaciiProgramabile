#define LED_RED 5
#define LED_BLUE 6

void setup() {
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
}

void loop() {
  digitalWrite(LED_RED, HIGH);
  digitalWrite(LED_BLUE, LOW);
  delay(1000);

  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_BLUE, HIGH);
  delay(1000);
}
