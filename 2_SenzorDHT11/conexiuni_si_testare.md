# Pasul 2: Utilizarea senzorului DHT11

## Conexiuni hardware

1. Modulul DHT11 (3 pini: `+`, `OUT`, `-`):
   - Pinul `+` → 5V pe Arduino.
   - Pinul `OUT` → Pin digital D2 pe Arduino.
   - Pinul `-` → GND pe Arduino.

---

## Biblioteca necesară

Codul folosește biblioteca **DHT sensor library** (Adafruit). Instaleaz-o înainte de compilare, urmând secțiunea „4. Instalează biblioteca DHT” din [README](../README.md).

---

## Modalitate de rulare și testare

1. Deschide fișierul `2_SenzorDHT11.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor**, setează viteza la **9600 baud** și observă valorile de temperatură și umiditate.
