#define LIGHT_PIN A0  // Fotodioda: între A0 și GND
#define LED_RED 5     // LED-ul roșu de la pasul 1 (iluminat automat)

int darkThreshold;  // Sub această valoare a luminii considerăm că e întuneric

// Citește lumina: aproape 0 = întuneric, valori mai mari = mai multă lumină
int readLight() {
  return 1023 - analogRead(LIGHT_PIN);
}

void setup() {
  Serial.begin(9600);
  pinMode(LIGHT_PIN, INPUT_PULLUP);  // Rezistorul intern al plăcii ține locul unui rezistor din kit
  pinMode(LED_RED, OUTPUT);
  delay(100);  // Așteaptă stabilizarea tensiunii pe A0

  // Calibrare: măsoară lumina din cameră la pornire; "întuneric" = sub jumătate din ea.
  // Pornește placa cu fotodioda descoperită; butonul reset al plăcii refă calibrarea.
  // Dacă vrei un prag fix, înlocuiește linia de mai jos, de exemplu: darkThreshold = 20;
  darkThreshold = readLight() / 2;
  Serial.print("Prag de întuneric: ");
  Serial.println(darkThreshold);
}

void loop() {
  int light = readLight();
  bool isDark = light < darkThreshold;

  digitalWrite(LED_RED, isDark ? HIGH : LOW);  // Aprinde LED-ul doar pe întuneric

  Serial.print("Lumină: ");
  Serial.print(light);
  Serial.println(isDark ? " (întuneric, LED aprins)" : " (lumină, LED stins)");

  delay(500);
}
