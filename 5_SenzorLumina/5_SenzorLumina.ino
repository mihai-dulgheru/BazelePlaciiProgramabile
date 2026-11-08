#define LIGHT_PIN A0  // A0 → rezistor → piciorul scurt al fotodiodei; piciorul lung → GND
#define LED_RED 5     // LED-ul roșu de la pasul 1 (iluminat automat)

// Prag de întuneric: peste acest timp de descărcare considerăm că e întuneric.
// Ajustează-l după valorile din Serial Monitor (cameră luminată vs. fotodiodă acoperită).
const unsigned long DARK_THRESHOLD_MS = 800;
const unsigned long MAX_TIME_MS = 1000;  // Nu așteptăm mai mult de o secundă

// Fotodioda produce un curent prea mic pentru analogRead. De aceea o încărcăm
// ca pe un mic condensator și cronometrăm cât durează până o descarcă lumina:
// mai multă lumină = timp mai scurt, întuneric = timp mai lung.
unsigned long measureDischargeMicros() {
  pinMode(LIGHT_PIN, OUTPUT);
  digitalWrite(LIGHT_PIN, HIGH);  // Încarcă fotodioda
  delayMicroseconds(100);
  pinMode(LIGHT_PIN, INPUT);  // Fără pull-up: doar lumina o mai descarcă

  unsigned long start = micros();
  while (digitalRead(LIGHT_PIN) == HIGH && micros() - start < MAX_TIME_MS * 1000UL) {
  }
  return micros() - start;
}

void setup() {
  Serial.begin(9600);
  pinMode(LED_RED, OUTPUT);
}

void loop() {
  unsigned long timeMicros = measureDischargeMicros();

  // Descărcare aproape instantanee: fotodioda conduce, deci e montată invers
  if (timeMicros < 100) {
    digitalWrite(LED_RED, LOW);
    Serial.println("Fotodioda pare montată invers: schimbă picioarele între ele.");
    delay(1000);
    return;
  }

  unsigned long timeMs = timeMicros / 1000;
  bool isDark = timeMs >= DARK_THRESHOLD_MS;

  digitalWrite(LED_RED, isDark ? HIGH : LOW);  // Aprinde LED-ul doar pe întuneric

  Serial.print("Timp de descărcare: ");
  Serial.print(timeMs);
  Serial.println(isDark ? " ms (întuneric, LED aprins)" : " ms (lumină, LED stins)");

  delay(300);
}
