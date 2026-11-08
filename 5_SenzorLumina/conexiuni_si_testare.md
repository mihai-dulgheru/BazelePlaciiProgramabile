# Pasul 5 (opțional): Senzor de lumină cu fotodioda din kit

Fotodioda din kit arată ca un LED transparent. Lumina o face să lase să treacă un curent foarte mic, prea mic pentru `analogRead`. De aceea, placa o încarcă precum un mic condensator și cronometrează cât durează până când lumina o descarcă: **cu cât e mai întuneric, cu atât timpul e mai mare**. Când timpul trece de prag, LED-ul roșu de la pasul 1 se aprinde, ca un iluminat automat.

## Conexiuni hardware

1. Fotodioda (contează sensul):
   - Pin analogic A0 pe Arduino → Rezistor din kit → Piciorul scurt al fotodiodei.
   - Piciorul lung al fotodiodei → GND pe Arduino.

   Spre deosebire de LED, fotodioda se montează cu piciorul scurt (catodul) spre pin și piciorul lung (anodul) la GND. Așa lucrează în **polarizare inversă**: nu lasă curentul să treacă, iar doar lumina o descarcă.

   Rezistorul protejează placa dacă fotodioda este montată pe dos.

2. LED roșu: rămâne montat de la pasul 1 (anodul → rezistor din kit → D5, catodul → GND).

---

## Modalitate de rulare și testare

1. Deschide fișierul `5_SenzorLumina.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**.
5. Testează:
   - Fotodioda descoperită, la lumina camerei: timpul este de zeci sau sute de milisecunde, iar LED-ul roșu e stins.
   - Acoperă fotodioda cu degetul: timpul urcă la 1000 ms, iar LED-ul roșu se aprinde.
   - Luminează fotodioda cu lanterna telefonului: timpul scade la câteva milisecunde.

Dacă Serial Monitor afișează „Fotodioda e montată pe dos”, piciorul lung este spre A0 (polarizare directă): schimbă picioarele fotodiodei între ele.

Dacă LED-ul se aprinde și când fotodioda e descoperită (de exemplu, într-o cameră slab luminată), mărește valoarea `DARK_THRESHOLD_MS` din cod.
