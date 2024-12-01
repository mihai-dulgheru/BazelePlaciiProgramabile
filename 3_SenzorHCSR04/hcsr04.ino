#define TRIG_PIN 3  // Pinul Trig al HC-SR04
#define ECHO_PIN 4  // Pinul Echo al HC-SR04

void setup() {
  Serial.begin(9600);  // Inițializează comunicarea serială
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}

void loop() {
  // Trimite impulsul de măsurare
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Măsoară durata semnalului de răspuns
  long duration = pulseIn(ECHO_PIN, HIGH);

  // Calculează distanța în cm
  float distance = duration * 0.034 / 2;

  // Afișează distanța pe monitorul serial
  Serial.print("Distanta: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(1000);  // Așteaptă 1 secundă
}
