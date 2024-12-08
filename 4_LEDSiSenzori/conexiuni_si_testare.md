# Aplicație Completă: Monitorizare senzori și control LED-uri

## Conexiuni hardware

### 1. LED-uri

- **LED roșu:**
  - Anodul (pata mai lungă) → Rezistor → Pin digital D5 pe Arduino.
  - Catodul (pata mai scurtă) → GND pe breadboard.
- **LED albastru:**
  - Anodul (pata mai lungă) → Rezistor → Pin digital D6 pe Arduino.
  - Catodul (pata mai scurtă) → GND pe breadboard.

### 2. Senzor DHT11

- Pinul `+` → 5V pe Arduino.
- Pinul `OUT` → Pin digital D2 pe Arduino.
- Pinul `-` → GND pe Arduino.

### 3. Senzor HC-SR04

- Pinul **GND** → GND pe Arduino.
- Pinul **Echo** → Pin digital D4 pe Arduino.
- Pinul **Trig** → Pin digital D3 pe Arduino.
- Pinul **VCC** → 5V pe Arduino.

---

## Modalitate de rulare și testare

1. Deschide fișierul `led_si_senzori.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**.
5. Testează funcționalitatea:
   - **LED-uri:** Aprinderea în funcție de temperatura citită.
   - **Senzor DHT11:** Citirile de temperatură și umiditate pe Serial Monitor.
   - **Senzor HC-SR04:** Detectarea distanței pe Serial Monitor și palpitarea LED-urilor când un obiect este la <10 cm.
