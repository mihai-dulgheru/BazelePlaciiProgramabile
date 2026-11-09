# Pasul 3: Utilizarea senzorului HC-SR04

## Conexiuni hardware

1. Senzor HC-SR04:
   - Pinul **GND** → GND pe Arduino.
   - Pinul **Echo** → Pin digital D4 pe Arduino.
   - Pinul **Trig** → Pin digital D3 pe Arduino.
   - Pinul **VCC** → 5V pe Arduino.

**Dacă păstrezi montajul de la pasul 2:** placa are doi pini 5V și trei pini GND. DHT11 folosește deja un pin 5V și un pin GND, așa că leagă HC-SR04 la celălalt pin 5V și la un pin GND liber.

---

## Modalitate de rulare și testare

1. Deschide fișierul `3_SenzorHCSR04.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**.
5. Testează:
   - Apropie un obiect de senzor.
   - Observă valorile distanței afișate pe monitorul serial în centimetri.

Dacă apare mesajul „Eroare: Nu s-a primit semnal de la senzorul HC-SR04.”, verifică firele de la pinii **Trig** și **Echo** sau apropie un obiect (senzorul măsoară până la aproximativ 4 m).
