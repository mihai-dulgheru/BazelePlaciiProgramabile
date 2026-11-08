# Pasul 5 (opțional): Senzor de lumină cu fotodioda din kit

Fotodioda lasă să treacă mai mult curent când primește mai multă lumină. Placa măsoară acest lucru pe un pin analogic și aprinde LED-ul roșu de la pasul 1 când se face întuneric, ca un iluminat automat.

## Conexiuni hardware

1. Fotodioda:
   - Un picior → Pin analogic A0 pe Arduino.
   - Celălalt picior → GND pe Arduino.

   Nu ai nevoie de rezistor: codul activează rezistorul intern al plăcii pe pinul A0 (`INPUT_PULLUP`).

2. LED roșu: rămâne montat de la pasul 1 (anodul → rezistor din kit → D5, catodul → GND).

---

## Modalitate de rulare și testare

1. Deschide fișierul `5_SenzorLumina.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă, cu fotodioda descoperită.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**. La pornire, placa măsoară lumina din cameră și afișează pragul de întuneric (jumătate din lumina măsurată).
5. Testează:
   - Acoperă fotodioda cu mâna: valoarea luminii scade, iar LED-ul roșu se aprinde.
   - Descoper-o: LED-ul se stinge.
   - Luminează fotodioda cu lanterna telefonului: valoarea crește.

Dacă valoarea aproape nu se schimbă când acoperi fotodioda, ai montat-o invers: schimbă picioarele între ele și apasă butonul **reset** al plăcii, ca să refacă măsurarea luminii din cameră.
