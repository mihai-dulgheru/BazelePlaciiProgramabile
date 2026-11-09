# Pasul 1: Controlul LED-urilor

## Conexiuni hardware

1. LED roșu:
   - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D5 pe Arduino.
   - Catodul (piciorul mai scurt) → rândul comun de GND al LED-urilor (vezi mai jos).

2. LED albastru:
   - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D6 pe Arduino.
   - Catodul (piciorul mai scurt) → rândul comun de GND al LED-urilor (vezi mai jos).

Pune catozii ambelor LED-uri pe același rând de pe breadboard și leagă rândul cu un singur fir la un pin GND al plăcii. Placa are doar trei pini GND, iar la pasul 4 ceilalți doi vor fi folosiți de senzori.

---

## Modalitate de rulare și testare

1. Deschide fișierul `1_LEDuri.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Observă cum LED-urile roșu și albastru se aprind alternativ.
