#include <DHT.h>

// Configurarea pinului pentru DHT11 și tipul senzorului
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// Configurarea pinilor pentru HC-SR04
#define TRIG_PIN 3  // Pin pentru semnalul Trig
#define ECHO_PIN 4  // Pin pentru semnalul Echo

// Configurarea pinilor pentru LED-uri
#define LED_RED 5   // Pin pentru LED roșu
#define LED_BLUE 6  // Pin pentru LED albastru

// Temporizări și intervale
unsigned long lastTempHumidityRead = 0;     // Timpul ultimei citiri de temperatură și umiditate
unsigned long tempHumidityInterval = 5000;  // Interval pentru citirea temperaturii și umidității
unsigned long lastDistanceMeasure = 0;      // Timpul ultimei măsurători de distanță
unsigned long distanceInterval = 1000;      // Interval pentru măsurarea distanței
unsigned long lastLEDChange = 0;            // Timpul ultimei alternări a LED-urilor
unsigned long ledInterval = 500;            // Interval pentru alternarea LED-urilor

// Variabile de stare
bool toggleLEDState = false;      // Starea curentă a alternării LED-urilor
bool hasAlternated = false;       // Indică dacă LED-urile au alternat
bool isDistancePriority = false;  // Indică dacă măsurarea distanței are prioritate

// Controlează starea LED-urilor (aprins/stins)
void setLEDs(bool red, bool blue) {
  digitalWrite(LED_RED, red ? HIGH : LOW);
  digitalWrite(LED_BLUE, blue ? HIGH : LOW);
}

void setup() {
  Serial.begin(9600);  // Inițializează comunicarea serială
  dht.begin();         // Inițializează senzorul DHT11

  // Configurare pini
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);

  setLEDs(false, false);  // Stinge LED-urile la pornire
}

void loop() {
  unsigned long currentMillis = millis();

  // Măsoară și afișează distanța la fiecare interval specificat
  if (currentMillis - lastDistanceMeasure >= distanceInterval) {
    lastDistanceMeasure = currentMillis;
    measureAndDisplayDistance();
  }

  // Controlează alternarea LED-urilor dacă măsurarea distanței este prioritară
  if (isDistancePriority) {
    controlAlternateLEDs();
  }

  // Citește și afișează temperatura și umiditatea dacă distanța nu are prioritate
  if (!isDistancePriority && currentMillis - lastTempHumidityRead >= tempHumidityInterval) {
    lastTempHumidityRead = currentMillis;
    readAndDisplayTemperatureHumidity();
  }
}

// Măsoară și afișează distanța
void measureAndDisplayDistance() {
  float distance = measureDistance();

  if (distance == -1) {
    Serial.println("Eroare: Nu s-a primit semnal de la senzorul HC-SR04.");
    return;
  }

  Serial.print("Distanța: ");
  Serial.print(distance);
  Serial.println(" cm");

  if (distance < 10) {
    isDistancePriority = true;  // Prioritizează măsurarea distanței
    controlAlternateLEDs();
  } else {
    isDistancePriority = false;  // Elimină prioritatea pentru distanță
    stopAlternateLEDs();
  }
}

// Măsoară distanța folosind HC-SR04
float measureDistance() {
  digitalWrite(TRIG_PIN, LOW);  // Asigură un semnal LOW înainte de impuls
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);  // Trimite un impuls de 10 microsecunde
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  // Măsoară timpul de răspuns cu un timeout de 30 ms
  long duration = pulseIn(ECHO_PIN, HIGH, 30000);

  if (duration == 0) {
    return -1;  // Semnal invalid
  }

  // Calculează și returnează distanța în cm
  return duration * 0.034 / 2;
}

// Controlează alternarea LED-urilor la fiecare interval
void controlAlternateLEDs() {
  unsigned long currentMillis = millis();

  if (currentMillis - lastLEDChange >= ledInterval) {
    lastLEDChange = currentMillis;
    toggleLEDState = !toggleLEDState;          // Inversează starea alternării
    hasAlternated = true;                      // Marchează că LED-urile au alternat
    setLEDs(toggleLEDState, !toggleLEDState);  // Alternăm starea LED-urilor
  }
}

// Oprește alternarea LED-urilor dacă acestea au alternat înainte
void stopAlternateLEDs() {
  if (hasAlternated) {
    setLEDs(false, false);  // Stinge LED-urile
    hasAlternated = false;  // Resetează starea alternării
  }
}

// Citește și afișează temperatura și umiditatea
void readAndDisplayTemperatureHumidity() {
  float temperature = dht.readTemperature();  // Citește temperatura
  float humidity = dht.readHumidity();        // Citește umiditatea

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Eroare la citirea senzorului DHT11!");
  } else {
    Serial.print("Temperatura: ");
    Serial.print(temperature);
    Serial.print(" °C, Umiditate: ");
    Serial.print(humidity);
    Serial.println(" %");

    // Controlează LED-urile pe baza temperaturii
    setLEDs(temperature >= 25, temperature < 25);
  }
}
