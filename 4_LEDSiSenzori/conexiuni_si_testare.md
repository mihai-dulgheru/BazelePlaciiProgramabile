# Aplicație Completă: Monitorizare senzori și control LED-uri

Dacă ai parcurs pașii 1-3 fără să demontezi circuitul, montajul este deja complet: verifică legăturile de mai jos și încarcă direct codul.

## Conexiuni hardware

### 1. Alimentare

Placa are un singur pin 5V, iar ambii senzori au nevoie de el:

- Pinul **5V** al plăcii → un rând liber de pe breadboard (rândul de 5V).
- Pinul `+` al DHT11 și pinul **VCC** al HC-SR04 → rândul de 5V.
- Toate legăturile la GND (LED-uri, DHT11, HC-SR04) → pinii GND ai plăcii (placa are mai mulți) sau un rând de pe breadboard legat la GND.

### 2. LED-uri

- **LED roșu:**
  - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D5 pe Arduino.
  - Catodul (piciorul mai scurt) → GND.
- **LED albastru:**
  - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D6 pe Arduino.
  - Catodul (piciorul mai scurt) → GND.

### 3. Senzor DHT11

- Pinul `+` → rândul de 5V.
- Pinul `OUT` → Pin digital D2 pe Arduino.
- Pinul `-` → GND.

### 4. Senzor HC-SR04

- Pinul **GND** → GND.
- Pinul **Echo** → Pin digital D4 pe Arduino.
- Pinul **Trig** → Pin digital D3 pe Arduino.
- Pinul **VCC** → rândul de 5V.

---

## Modalitate de rulare și testare

Codul folosește biblioteca **DHT sensor library** (Adafruit); dacă nu ai instalat-o la pasul 2, urmează secțiunea „4. Instalează biblioteca DHT” din [README](../README.md).

1. Deschide fișierul `4_LEDSiSenzori.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**.
5. Testează funcționalitatea:
   - **LED-uri:** Aprinderea în funcție de temperatura citită.
   - **Senzor DHT11:** Citirile de temperatură și umiditate pe Serial Monitor.
   - **Senzor HC-SR04:** Detectarea distanței pe Serial Monitor și clipirea alternativă a LED-urilor când un obiect este la mai puțin de 10 cm.
