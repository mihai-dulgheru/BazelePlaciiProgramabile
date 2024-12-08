#define TRIG_PIN 3  // Pinul Trig al HC-SR04
#define ECHO_PIN 4  // Pinul Echo al HC-SR04

void setup() {
  Serial.begin(9600);         // Inițializează comunicarea serială
  pinMode(TRIG_PIN, OUTPUT);  // Configurează pinul Trig ca OUTPUT
  pinMode(ECHO_PIN, INPUT);   // Configurează pinul Echo ca INPUT
}

void loop() {
  // Trimite impulsul de măsurare
  digitalWrite(TRIG_PIN, LOW);   // Asigură-te că Trig este inițial LOW
  delayMicroseconds(2);          // Așteaptă 2 microsecunde
  digitalWrite(TRIG_PIN, HIGH);  // Trimite un impuls HIGH de 10 microsecunde
  delayMicroseconds(10);         // Durata impulsului
  digitalWrite(TRIG_PIN, LOW);   // Revine la LOW

  // Măsoară durata semnalului de răspuns
  long duration = pulseIn(ECHO_PIN, HIGH);  // Durata semnalului Echo în μs (microsecunde)

  // Calculează distanța în cm
  // Formula: distance = (duration * 0.034) / 2
  // Explicație:
  //  - `duration`: Timpul total (în μs) pentru ca unda ultrasonică să parcurgă distanța dus-întors.
  //  - `0.034`: Viteza sunetului în aer este aproximativ 343 m/s sau 0.034 cm/μs.
  //  - Împărțim la 2 deoarece `duration` reprezintă timpul pentru dus-întors, dar avem nevoie doar de distanța dus.
  float distance = duration * 0.034 / 2;

  // Afișează distanța pe monitorul serial
  Serial.print("Distanta: ");
  Serial.print(distance);
  Serial.println(" cm");

  delay(1000);  // Așteaptă 1 secundă
}
