# Pasul 3: Utilizarea senzorului HC-SR04

## Conexiuni hardware

1. Senzor HC-SR04:
   - Pinul **GND** → GND pe Arduino.
   - Pinul **Echo** → Pin digital D4 pe Arduino.
   - Pinul **Trig** → Pin digital D3 pe Arduino.
   - Pinul **VCC** → 5V pe Arduino.

**Dacă păstrezi montajul de la pasul 2:** placa are un singur pin 5V, pe care îl folosește deja DHT11. Leagă pinul 5V cu un fir la un rând liber de pe breadboard și alimentează din acel rând atât pinul `+` al DHT11, cât și pinul **VCC** al HC-SR04. Pentru GND poți folosi oricare dintre pinii GND ai plăcii.

---

## Modalitate de rulare și testare

1. Deschide fișierul `3_SenzorHCSR04.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**.
5. Testează:
   - Apropiindu-te de senzor cu un obiect.
   - Observă valorile distanței afișate pe monitorul serial în centimetri.
