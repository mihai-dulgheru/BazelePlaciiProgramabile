#define LIGHT_PIN A0  // A0 → rezistor → piciorul scurt al fotodiodei; piciorul lung → GND
#define LED_RED 5     // LED-ul roșu (iluminat automat)

const unsigned long MAX_TIME_MS = 1000;  // Nu așteptăm mai mult de o secundă

// Pragul de întuneric se calculează la pornire, din lumina camerei:
// "întuneric" = timp de descărcare de cel puțin DARK_FACTOR ori mai mare decât în cameră.
// Pragul rămâne între 20 și 800 ms, ca să funcționeze și ziua, și seara.
const unsigned long DARK_FACTOR = 4;
unsigned long darkThresholdMs;

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

  // Calibrare: media a 5 măsurători la lumina camerei, cu fotodioda descoperită.
  // Butonul reset al plăcii refă calibrarea când se schimbă lumina din cameră.
  unsigned long roomMs = 0;
  for (int i = 0; i < 5; i++) {
    roomMs += measureDischargeMicros() / 1000;
  }
  roomMs /= 5;
  darkThresholdMs = constrain(roomMs * DARK_FACTOR, 20UL, 800UL);

  Serial.print("Lumina camerei: ");
  Serial.print(roomMs);
  Serial.print(" ms, prag de întuneric: ");
  Serial.print(darkThresholdMs);
  Serial.println(" ms");
}

void loop() {
  unsigned long timeMicros = measureDischargeMicros();

  // Descărcare aproape instantanee: fotodioda conduce (polarizare directă), deci e montată pe dos
  if (timeMicros < 100) {
    digitalWrite(LED_RED, LOW);
    Serial.println("Fotodioda e montată pe dos (picior lung spre A0): schimbă picioarele între ele.");
    delay(1000);
    return;
  }

  unsigned long timeMs = timeMicros / 1000;
  bool isDark = timeMs >= darkThresholdMs;

  digitalWrite(LED_RED, isDark ? HIGH : LOW);  // Aprinde LED-ul doar pe întuneric

  Serial.print("Timp de descărcare: ");
  Serial.print(timeMs);
  Serial.println(isDark ? " ms (întuneric, LED aprins)" : " ms (lumină, LED stins)");

  delay(300);
}
