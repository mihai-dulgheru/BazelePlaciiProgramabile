#include <DHT.h>

#define DHTPIN 2       // DHT11 Data Pin
#define DHTTYPE DHT11  // Tipul senzorului
DHT dht(DHTPIN, DHTTYPE);

#define TRIG_PIN 3  // Trig pin al HC-SR04
#define ECHO_PIN 4  // Echo pin al HC-SR04

#define LED_RED 5   // LED roșu
#define LED_BLUE 6  // LED albastru

unsigned long lastTempHumidityRead = 0;      // Timpul ultimei citiri DHT11
unsigned long tempHumidityInterval = 10000;  // 10 secunde

void setup() {
  Serial.begin(9600);
  dht.begin();

  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);

  pinMode(LED_RED, OUTPUT);
  pinMode(LED_BLUE, OUTPUT);
}

void loop() {
  // Citește temperatura și umiditatea la fiecare 10 secunde
  unsigned long currentMillis = millis();
  if (currentMillis - lastTempHumidityRead >= tempHumidityInterval) {
    lastTempHumidityRead = currentMillis;

    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    if (isnan(temperature) || isnan(humidity)) {
      Serial.println("Eroare la citirea senzorului DHT11!");
    } else {
      Serial.print("Temperatura: ");
      Serial.print(temperature);
      Serial.print(" °C, Umiditate: ");
      Serial.print(humidity);
      Serial.println(" %");

      // Controlează LED-urile în funcție de temperatură
      if (temperature < 25) {
        digitalWrite(LED_BLUE, HIGH);  // Temperatură scăzută
        digitalWrite(LED_RED, LOW);
      } else {
        digitalWrite(LED_BLUE, LOW);
        digitalWrite(LED_RED, HIGH);  // Temperatură ridicată
      }
    }
  }

  // Măsoară distanța în mod constant
  float distance = measureDistance();

  Serial.print("Distanta: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Palpită LED-urile dacă distanța este mai mică de 10 cm
  if (distance > 0 && distance < 10) {  // Validează că distanța este măsurată corect
    pulseLEDs();
  }

  delay(100);  // Întârziere scurtă pentru măsurare constantă a distanței
}

float measureDistance() {
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  long duration = pulseIn(ECHO_PIN, HIGH);
  float distance = duration * 0.034 / 2;
  return distance;
}

void pulseLEDs() {
  // Palpită LED-urile pentru o perioadă scurtă
  for (int i = 0; i < 5; i++) {  // LED-urile vor palpita de 5 ori
    digitalWrite(LED_RED, HIGH);
    digitalWrite(LED_BLUE, HIGH);
    delay(200);  // LED-urile rămân aprinse 200 ms
    digitalWrite(LED_RED, LOW);
    digitalWrite(LED_BLUE, LOW);
    delay(200);  // LED-urile rămân stinse 200 ms
  }
}
