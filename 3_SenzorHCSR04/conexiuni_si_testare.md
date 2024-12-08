# Pasul 3: Utilizarea senzorului HC-SR04

## Conexiuni hardware

1. Senzor HC-SR04:
   - Pinul **GND** → GND pe Arduino.
   - Pinul **Echo** → Pin digital D4 pe Arduino.
   - Pinul **Trig** → Pin digital D3 pe Arduino.
   - Pinul **VCC** → 5V pe Arduino.

---

## Modalitate de rulare și testare

1. Deschide fișierul `hcsr04.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**.
5. Testează:
   - Apropiindu-te de senzor cu un obiect.
   - Observă valorile distanței afișate pe monitorul serial în centimetri.
