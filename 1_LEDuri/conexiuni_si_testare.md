# Pasul 1: Controlul LED-urilor

## Conexiuni hardware

![Schema de montaj pentru pasul 1](schema_montaj.svg)

Pe breadboard, cele 5 găuri a-e din aceeași coloană numerotată sunt legate între ele (la fel f-j).

1. LED roșu:
   - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D5 pe Arduino.
   - Catodul (piciorul mai scurt) → coloana comună de GND a LED-urilor (vezi mai jos).

2. LED albastru:
   - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D6 pe Arduino.
   - Catodul (piciorul mai scurt) → coloana comună de GND a LED-urilor (vezi mai jos).

Pune catozii ambelor LED-uri în aceeași coloană a breadboard-ului (coloana 7 din schemă) și leag-o cu un singur fir la pinul GND din rândul de pini de sus al plăcii, lângă pinul 13. Placa are doar trei pini GND, iar la pasul 4 ceilalți doi vor fi folosiți de senzori.

---

## Modalitate de rulare și testare

1. Deschide fișierul `1_LEDuri.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Observă cum LED-urile roșu și albastru se aprind alternativ.
