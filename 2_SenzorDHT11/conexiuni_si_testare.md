# Pasul 2: Utilizarea senzorului DHT11

## Conexiuni hardware

![Schema de montaj pentru pasul 2](schema_montaj.svg)

Schema păstrează LED-urile de la pasul 1. Modulul DHT11 este înfipt în breadboard, iar firele pleacă din aceeași coloană cu pinul lui.

1. Modulul DHT11 (3 pini: `+`, `OUT`, `-`):
   - Pinul `+` → primul pin 5V din zona **POWER** (de la stânga la dreapta).
   - Pinul `OUT` → Pin digital D2 pe Arduino.
   - Pinul `-` → al doilea pin GND din zona **POWER**. GND-ul din rândul de sus e folosit deja de LED-uri.

---

## Biblioteca necesară

Codul folosește biblioteca **DHT sensor library** (Adafruit). Instaleaz-o înainte de compilare, urmând secțiunea „4. Instalează biblioteca DHT” din [README](../README.md).

---

## Modalitate de rulare și testare

1. Deschide fișierul `2_SenzorDHT11.ino` în Arduino IDE.
2. Conectează placa la calculator cu cablul USB.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor**, setează viteza la **9600 baud** și observă valorile de temperatură și umiditate.
