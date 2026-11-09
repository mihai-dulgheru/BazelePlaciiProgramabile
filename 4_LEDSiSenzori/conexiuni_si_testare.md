# Pasul 4: Aplicație completă - monitorizare senzori și control LED-uri

Dacă ai parcurs pașii 1-3 fără să demontezi circuitul, montajul este deja complet: verifică legăturile de mai jos și încarcă direct codul.

## Conexiuni hardware

### 1. Alimentare

Placa are doi pini 5V și trei pini GND. Pinii 5V și doi dintre pinii GND sunt în zona **POWER** a plăcii, iar al treilea GND e în rândul de sus, lângă pinul 13.

- **5V:** ai nevoie de două legături și placa are doi pini: pinul `+` al DHT11 → primul pin 5V, pinul **VCC** al HC-SR04 → al doilea pin 5V.
- **GND:** ai nevoie de patru legături (două LED-uri, DHT11, HC-SR04), dar placa are doar trei pini. De aceea, catozii celor două LED-uri stau pe același rând de pe breadboard, legat cu un singur fir la primul pin GND. Pinul `-` al DHT11 → al doilea pin GND, pinul **GND** al HC-SR04 → al treilea.

### 2. LED-uri

- **LED roșu:**
  - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D5 pe Arduino.
  - Catodul (piciorul mai scurt) → rândul comun de GND al LED-urilor.
- **LED albastru:**
  - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D6 pe Arduino.
  - Catodul (piciorul mai scurt) → rândul comun de GND al LED-urilor.

### 3. Senzor DHT11

- Pinul `+` → 5V pe Arduino (primul pin 5V).
- Pinul `OUT` → Pin digital D2 pe Arduino.
- Pinul `-` → al doilea pin GND.

### 4. Senzor HC-SR04

- Pinul **GND** → al treilea pin GND.
- Pinul **Echo** → Pin digital D4 pe Arduino.
- Pinul **Trig** → Pin digital D3 pe Arduino.
- Pinul **VCC** → 5V pe Arduino (al doilea pin 5V).

---

## Modalitate de rulare și testare

Codul folosește biblioteca **DHT sensor library** (Adafruit); dacă nu ai instalat-o la pasul 2, urmează secțiunea „4. Instalează biblioteca DHT” din [README](../README.md).

1. Deschide fișierul `4_LEDSiSenzori.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**.
5. Testează funcționalitatea:
   - **LED-uri:** LED-ul roșu se aprinde la cel puțin 25 °C, iar cel albastru sub 25 °C. Temperatura se citește la 5 secunde; ca să schimbi culoarea, încălzește senzorul DHT11 ținându-l câteva secunde între degete.
   - **Senzor DHT11:** Citirile de temperatură și umiditate pe Serial Monitor.
   - **Senzor HC-SR04:** Detectarea distanței pe Serial Monitor și clipirea alternativă a LED-urilor când un obiect este la mai puțin de 10 cm.
