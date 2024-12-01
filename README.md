# Proiect Monitorizare Senzori cu Arduino

Acest proiect demonstrează utilizarea combinată a mai multor senzori și LED-uri cu o placă Arduino, oferind funcționalități precum monitorizarea temperaturii și umidității, măsurarea distanței și semnalizare vizuală prin LED-uri.

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
3. Conectează placa Arduino.
4. Mergi la **Tools > Port** și selectează: **COM3** (sau alt port disponibil în funcție de sistemul tău).

---

## Structura proiectului

Proiectul este împărțit în pași, fiecare având un folder dedicat:

- **1_LEDuri:** Controlul LED-urilor.
- **2_SenzorDHT11:** Citirea temperaturii și umidității.
- **3_SenzorHCSR04:** Măsurarea distanței.
- **4_LEDSiSenzori:** Integrarea tuturor funcționalităților.

---

## Cerințe hardware

- Placă Arduino (UNO, Nano etc.)
- Senzor DHT11
- Senzor HC-SR04
- LED-uri (roșu și albastru)
- Rezistențe
- Breadboard și cabluri de conexiune

---

## Testare

1. Testează fiecare pas individual urmând instrucțiunile din fișierele `.md`.
2. Integrează toate componentele folosind codul din folderul **4_LEDSiSenzori**.
3. Verifică valorile pe monitorul serial și funcționalitatea LED-urilor în raport cu temperaturile și distanța detectată.
