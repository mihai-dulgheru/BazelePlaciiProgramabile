# Proiect Monitorizare Senzori cu Arduino

Acest proiect demonstrează utilizarea combinată a mai multor senzori și LED-uri cu placa NEXTLAB (compatibilă Arduino), oferind funcționalități precum monitorizarea temperaturii și umidității, măsurarea distanței și semnalizare vizuală prin LED-uri.

---

## Instalare și configurare mediul de dezvoltare Arduino IDE

### 1. Descarcă și instalează Arduino IDE

- Accesează [pagina oficială Arduino IDE](https://www.arduino.cc/en/software).
- Descarcă versiunea corespunzătoare sistemului tău de operare (Windows, macOS, Linux).
- Instalează Arduino IDE urmând pașii specifici pentru platforma ta.

---

### 2. Configurează MiniCore

MiniCore este o platformă pentru suport extins al microcontrollerelor ATmega328.

#### **Cum să instalezi MiniCore:**

1. Deschide Arduino IDE.
2. Accesează **File > Preferences**.
3. În câmpul **Additional Boards Manager URLs**, adaugă următorul URL: <https://mcudude.github.io/MiniCore/package_MCUdude_MiniCore_index.json>
4. Accesează **Tools > Board > Boards Manager...**.
5. Așteaptă să se descarce indexurile platformei.
6. Găsește MiniCore în listă și apasă pe **Install**.
7. Închide fereastra Boards Manager după instalare.

---

### 3. Selectează placa și configurările corecte

1. Mergi la **Tools > Board** și selectează: **MiniCore > ATmega328**
2. Mergi la **Tools > Variant** și selectează: **328PB**
3. Conectează placa la calculator cu cablul USB.
4. Mergi la **Tools > Port** și selectează: **COM3** (sau alt port disponibil în funcție de sistemul tău).

Dacă portul plăcii nu apare în listă, instalează driverul **CH340** (linkul este în lecția „Bazele plăcii programabile”, pasul 6, de pe labs.ase.ro), apoi reconectează placa.

---

### 4. Instalează biblioteca DHT

Codul din pașii 2 și 4 folosește biblioteca pentru senzorul DHT11. Fără ea, compilarea se oprește cu eroarea `DHT.h: No such file or directory`.

1. Mergi la **Tools > Manage Libraries...**.
2. Caută **DHT sensor library** (autor: Adafruit) și apasă pe **Install**.
3. Când Arduino IDE propune și dependențele (**Adafruit Unified Sensor**), alege **Install All**.

---

## Structura proiectului

Proiectul este împărțit în pași, fiecare având un folder dedicat:

- **1_LEDuri:** Controlul LED-urilor.
- **2_SenzorDHT11:** Citirea temperaturii și umidității.
- **3_SenzorHCSR04:** Măsurarea distanței.
- **4_LEDSiSenzori:** Integrarea tuturor funcționalităților.
- **5_SenzorLumina (opțional):** Măsurarea luminii cu fotodioda din kit și aprinderea LED-ului pe întuneric.

Fiecare componentă folosește alt pin, deci **nu demonta circuitul între pași**: la fiecare pas adaugi componente noi, iar la pasul 4 doar încarci codul.

| Componentă            | Pin pe placă |
| --------------------- | ------------ |
| LED roșu              | D5           |
| LED albastru          | D6           |
| DHT11 (`OUT`)         | D2           |
| HC-SR04 (Trig / Echo) | D3 / D4      |
| Fotodiodă             | A0           |

---

## Cerințe hardware

Toate componentele fac parte din kitul [NEXTLAB ENTRY I](https://shop.nextlab.tech/en/cumpara/kit-de-robotica-entry-i-657):

- Placa NEXTLAB.TECH A1 (ATmega328PB, compatibilă Arduino UNO) și cablul USB
- Senzor DHT11 (modul cu 3 pini: `+`, `OUT`, `-`)
- Senzor HC-SR04
- 2 LED-uri (în exemple: roșu și albastru)
- 2 dintre cele 5 rezistoare din kit, câte unul pentru fiecare LED
- Fotodiodă (pentru pasul 5)
- Breadboard și fire de legătură

---

## Testare

1. Testează fiecare pas individual urmând instrucțiunile din fișierele `.md`.
2. Integrează toate componentele folosind codul din folderul **4_LEDSiSenzori**.
3. Verifică valorile pe monitorul serial și funcționalitatea LED-urilor în raport cu temperaturile și distanța detectată.
