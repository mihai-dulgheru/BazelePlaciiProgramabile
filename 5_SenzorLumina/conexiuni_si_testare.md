# Pasul 5 (opțional): Senzor de lumină cu fotodioda din kit

Fotodioda din kit arată ca un LED transparent. Lumina o face să lase să treacă un curent foarte mic, prea mic pentru `analogRead`. De aceea, placa o încarcă precum un mic condensator și cronometrează cât durează până când lumina o descarcă: **cu cât e mai întuneric, cu atât timpul e mai mare**. Când timpul trece de prag, LED-ul roșu se aprinde, ca un iluminat automat. Pragul îl alege placa la pornire, din lumina camerei: întuneric înseamnă un timp de cel puțin 4 ori mai mare decât în cameră.

Pasul 5 este un montaj separat de pașii 1-4: ai nevoie doar de fotodiodă, de LED-ul roșu și de două rezistoare.

## Conexiuni hardware

1. Fotodioda (contează sensul):
   - Pin analogic A0 pe Arduino → Rezistor din kit → Piciorul scurt al fotodiodei.
   - Piciorul lung al fotodiodei → GND pe Arduino.

   Spre deosebire de LED, fotodioda se montează cu piciorul scurt (catodul) spre pin și piciorul lung (anodul) la GND. Așa lucrează în **polarizare inversă**: nu lasă curentul să treacă, iar doar lumina o descarcă.

   Rezistorul protejează placa dacă fotodioda este montată pe dos.

2. LED roșu:
   - Anodul (piciorul mai lung) → Rezistor din kit → Pin digital D5 pe Arduino.
   - Catodul (piciorul mai scurt) → GND pe Arduino.

---

## Modalitate de rulare și testare

1. Deschide fișierul `5_SenzorLumina.ino` în Arduino IDE.
2. Conectează placa Arduino la computer.
3. Încarcă codul pe placă, cu fotodioda descoperită, la lumina camerei.
4. Deschide **Serial Monitor** și setează viteza la **9600 baud**. La pornire, placa afișează lumina camerei și pragul de întuneric, de exemplu „Lumina camerei: 17 ms, prag de întuneric: 68 ms”. Deschiderea Serial Monitor repornește placa, așa că ține fotodioda descoperită și atunci.
5. Testează:
   - Fotodioda descoperită: timpul rămâne sub prag, iar LED-ul roșu e stins.
   - Acoperă bine fotodioda, de exemplu cu degetul apăsat peste ea sau cu un capac de pix: timpul crește de câteva ori peste prag, iar LED-ul roșu se aprinde. Ziua, lumina trece puțin prin deget, deci timpul crește mai puțin decât seara.
   - Luminează fotodioda cu lanterna telefonului: timpul scade la câteva milisecunde.

Dacă Serial Monitor afișează „Fotodioda e montată pe dos”, piciorul lung este spre A0 (polarizare directă): schimbă picioarele fotodiodei între ele.

Dacă lumina din cameră se schimbă mult (se aprinde lumina sau se lasă seara), apasă butonul **reset** al plăcii, cu fotodioda descoperită, ca să refacă măsurarea. Dacă LED-ul se aprinde prea ușor sau prea greu, schimbă valoarea `DARK_FACTOR` din cod (implicit 4).
