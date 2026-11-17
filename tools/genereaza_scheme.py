"""Generează schemele de montaj (schema_montaj.svg) pentru pașii 1-5.

Rulare din rădăcina proiectului:  python tools/genereaza_scheme.py
Pozițiile pinilor urmează placa NEXTLAB.TECH A1 (2 pini 5V, 3 pini GND).
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1060, 590

# --- Breadboard mini (17 coloane, rânduri a-e sus, f-j jos, fără șine) ---
BBX, BBY = 40, 190
COL = lambda c: BBX + 30 + (c - 1) * 20
ROW = {r: BBY + 30 + i * 20 for i, r in enumerate("abcde")}
ROW.update({r: BBY + 150 + i * 20 for i, r in enumerate("fghij")})
hole = lambda c, r: (COL(c), ROW[r])

# --- Placa NEXTLAB A1 ---
BX, BY, BW, BH = 600, 190, 420, 280
TOP_Y, BOT_Y = BY + 20, BY + BH - 20
PINS = {}  # cheie -> (x, y, eticheta)
for i, n in enumerate(["AREF", "GND", "13", "12", "11", "10", "9", "8"]):
    PINS["GNDs" if n == "GND" else n] = (BX + 70 + i * 22, TOP_Y, n)
for i, n in enumerate(["7", "6", "5", "4", "3", "2", "TX", "RX"]):
    PINS[n] = (BX + 250 + i * 22, TOP_Y, n)
for i, (k, n) in enumerate([("5V1", "5V"), ("RES", "RES"), ("3V3", "3.3V"), ("5V2", "5V"),
                            ("GND1", "GND"), ("GND2", "GND"), ("VIN", "VIN")]):
    PINS[k] = (BX + 90 + i * 22, BOT_Y, n)
for i in range(6):
    PINS[f"A{i}"] = (BX + 270 + i * 22, BOT_Y, f"A{i}")

COLORS = {"5V": "#d32f2f", "GND": "#212121", "D2": "#f9a825", "D3": "#2e7d32",
          "D4": "#1565c0", "D5": "#ef6c00", "D6": "#6a1b9a", "A0": "#00838f"}


def board(used):
    s = [f'<rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="12" fill="#5b2c86" stroke="#3d1d5c" stroke-width="2"/>',
         f'<rect x="{BX - 18}" y="{BY + 40}" width="60" height="50" rx="3" fill="#c9c9c9" stroke="#999"/>',
         f'<text x="{BX + 12}" y="{BY + 105}" class="sm" fill="#ddd" text-anchor="middle">USB</text>',
         f'<rect x="{BX - 8}" y="{BY + 200}" width="50" height="45" rx="3" fill="#222"/>',
         f'<rect x="{BX + 60}" y="{BY + 80}" width="28" height="28" rx="3" fill="#888"/>',
         f'<circle cx="{BX + 74}" cy="{BY + 94}" r="8" fill="#333"/>',
         f'<text x="{BX + 74}" y="{BY + 124}" class="sm" fill="#ddd" text-anchor="middle">reset</text>',
         f'<rect x="{BX + 230}" y="{BY + 95}" width="50" height="50" fill="#1b1b1b" transform="rotate(45 {BX + 255} {BY + 120})"/>',
         f'<text x="{BX + 210}" y="{BY + 185}" class="title" fill="#fff" text-anchor="middle">NEXTLAB.TECH A1</text>',
         f'<text x="{BX + 330}" y="{TOP_Y + 62}" class="sm" fill="#ddd" text-anchor="middle">DIGITAL (PWM~)</text>',
         f'<text x="{BX + 156}" y="{BOT_Y - 44}" class="sm" fill="#ddd" text-anchor="middle">POWER</text>',
         f'<text x="{BX + 325}" y="{BOT_Y - 44}" class="sm" fill="#ddd" text-anchor="middle">ANALOG IN</text>']
    for k, (x, y, n) in PINS.items():
        on = k in used
        s.append(f'<rect x="{x - 8}" y="{y - 8}" width="16" height="16" fill="#111"/>'
                 f'<rect x="{x - 3}" y="{y - 3}" width="6" height="6" fill="#555"/>')
        ty = y + 14 if y == TOP_Y else y - 14
        anchor = "end" if y == TOP_Y else "start"
        s.append(f'<text x="{x + 3}" y="{ty}" transform="rotate(-90 {x + 3} {ty})" text-anchor="{anchor}" '
                 f'class="{"pin on" if on else "pin"}">{n}</text>')
    return s


def breadboard():
    s = [f'<rect x="{BBX}" y="{BBY}" width="380" height="260" rx="8" fill="#f1f1ef" stroke="#c8c8c4" stroke-width="2"/>',
         f'<rect x="{BBX + 10}" y="{BBY + 122}" width="360" height="16" rx="3" fill="#dcdcd8"/>']
    for c in range(1, 18):
        for r in ROW:
            x, y = hole(c, r)
            s.append(f'<rect x="{x - 3}" y="{y - 3}" width="6" height="6" fill="#4a4a4a"/>')
        if c % 5 == 1:
            s.append(f'<text x="{COL(c)}" y="{BBY + 15}" class="xs" text-anchor="middle">{c}</text>')
    for r, y in ROW.items():
        s.append(f'<text x="{BBX + 12}" y="{y + 4}" class="xs" text-anchor="middle">{r}</text>')
    return s


def wire(a, pin_key, color, out=(0, -1), via=None):
    """Fir de la gaura `a` la pinul plăcii; `out` = direcția în care pleacă firul din gaură.
    `via` = punct prin care trece firul (folosit ca să ocolească placa pe deasupra)."""
    (x1, y1), (x2, y2, _) = a, PINS[pin_key]
    k = 50 + abs(x2 - x1) * 0.08  # arcele mai lungi urcă mai sus, ca să nu se încrucișeze
    c1 = (x1 + out[0] * k, y1 + out[1] * k)
    c_end = (x2, y2 - k if y2 == TOP_Y else y2 + k)
    if via:
        vx, vy = via
        d = f"M{x1},{y1} C{c1[0]},{c1[1]} {vx},{vy + k} {vx},{vy} S{c_end[0]},{c_end[1]} {x2},{y2}"
    else:
        d = f"M{x1},{y1} C{c1[0]},{c1[1]} {c_end[0]},{c_end[1]} {x2},{y2}"
    return [f'<path d="{d}" fill="none" stroke="#fff" stroke-width="8" stroke-linecap="round"/>',
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round"/>',
            f'<circle cx="{x1}" cy="{y1}" r="4" fill="{color}" stroke="#fff"/>',
            f'<circle cx="{x2}" cy="{y2}" r="4" fill="{color}" stroke="#fff"/>']


def resistor(a, b):
    (x1, y), (x2, _) = a, b
    m = (x1 + x2) / 2
    bands = "".join(f'<rect x="{m - 9 + i * 6}" y="{y - 6}" width="3" height="12" fill="{c}"/>'
                    for i, c in enumerate(["#8b4513", "#111", "#8b4513", "#c9a227"]))
    return [f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#999" stroke-width="2"/>',
            f'<rect x="{m - 14}" y="{y - 6}" width="28" height="12" rx="5" fill="#d8b98e" stroke="#a68457"/>', bands]


def diode(anode, cathode, fill, stroke, label, label_xy):
    """LED / fotodiodă văzută de sus: corpul deasupra picioarelor, piciorul lung (anodul) marcat cu +."""
    (ax, ay), (kx, ky) = anode, cathode
    mx, my = (ax + kx) / 2, min(ay, ky) - 16
    return [f'<line x1="{ax}" y1="{ay}" x2="{mx - 4}" y2="{my}" stroke="#999" stroke-width="2"/>',
            f'<line x1="{kx}" y1="{ky}" x2="{mx + 4}" y2="{my}" stroke="#999" stroke-width="2"/>',
            f'<circle cx="{mx}" cy="{my}" r="11" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
            f'<text x="{ax + (-8 if ax < kx else 8)}" y="{ay - 5}" class="sm b" text-anchor="middle">+</text>',
            f'<text x="{label_xy[0]}" y="{label_xy[1]}" class="sm b" text-anchor="middle">{label}</text>']


def module(cols, row, labels, body, name, color="#1e5aa8"):
    """Modul (DHT11, HC-SR04) înfipt în breadboard; corpul stă sub breadboard."""
    xs = [COL(c) for c in cols]
    y = ROW[row]
    bx, by, bw, bh = body
    s = [f'<line x1="{x}" y1="{y}" x2="{x}" y2="{by}" stroke="#999" stroke-width="3"/>' for x in xs]
    s.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="5" fill="{color}" stroke="#0d3b75" stroke-width="2"/>')
    s += [f'<text x="{x + 4}" y="{by + 6}" transform="rotate(-90 {x + 4} {by + 6})" class="xs w" text-anchor="end">{l}</text>'
          for x, l in zip(xs, labels)]
    s.append(f'<text x="{bx + bw / 2}" y="{by + bh + 18}" class="sm b" text-anchor="middle">{name}</text>')
    return s


def dht11():
    s = module([2, 3, 4], "j", ["+", "OUT", "-"], (COL(1) - 4, ROW["j"] + 40, 88, 80), "DHT11")
    s.append(f'<rect x="{COL(1) + 10}" y="{ROW["j"] + 62}" width="60" height="50" rx="3" fill="#e8f1fb"/>')
    s += [f'<line x1="{COL(1) + 14}" y1="{ROW["j"] + 70 + i * 10}" x2="{COL(1) + 66}" y2="{ROW["j"] + 70 + i * 10}" '
          f'stroke="#9bb8d8" stroke-width="2"/>' for i in range(4)]
    return s


def hcsr04():
    s = module([10, 11, 12, 13], "j", ["VCC", "Trig", "Echo", "GND"], (COL(7), ROW["j"] + 40, 180, 80), "HC-SR04")
    for cx in (COL(7) + 40, COL(7) + 140):
        s.append(f'<circle cx="{cx}" cy="{ROW["j"] + 88}" r="26" fill="#cfd4da" stroke="#8a9199" stroke-width="3"/>'
                 f'<circle cx="{cx}" cy="{ROW["j"] + 88}" r="14" fill="#5f6670"/>')
    return s


def leds():
    """Pasul 1: LED-uri în jumătatea de sus; catozii în coloana 6 (rândul comun de GND)."""
    s = resistor(hole(2, "b"), hole(4, "b")) + resistor(hole(8, "b"), hole(10, "b"))
    s += diode(hole(4, "d"), hole(6, "d"), "#ff5252", "#b71c1c", "LED roșu", (COL(3), ROW["e"] + 4))
    s += diode(hole(8, "e"), hole(6, "e"), "#448aff", "#0d47a1", "LED albastru", (COL(11) + 6, ROW["d"] + 4))
    wires = [wire(hole(2, "a"), "5", COLORS["D5"]), wire(hole(10, "a"), "6", COLORS["D6"]),
             wire(hole(6, "a"), "GNDs", COLORS["GND"])]
    return s, wires, ["5", "6", "GNDs"]


def dht_wires():
    return [wire(hole(2, "f"), "5V1", COLORS["5V"], (1, 0)), wire(hole(3, "g"), "2", COLORS["D2"], (1, 0), (470, 150)),
            wire(hole(4, "h"), "GND1", COLORS["GND"], (1, 0))], ["5V1", "2", "GND1"]


def hc_wires():
    return [wire(hole(10, "f"), "5V2", COLORS["5V"], (1, 0)), wire(hole(11, "g"), "3", COLORS["D3"], (1, 0), (500, 140)),
            wire(hole(12, "h"), "4", COLORS["D4"], (1, 0), (530, 130)), wire(hole(13, "i"), "GND2", COLORS["GND"], (1, 0))], \
        ["5V2", "3", "4", "GND2"]


def light():
    """Pasul 5: A0 → rezistor → piciorul scurt al fotodiodei; piciorul lung → GND. LED roșu pe D5."""
    s = resistor(hole(2, "h"), hole(4, "h")) + resistor(hole(10, "b"), hole(12, "b"))
    s += diode(hole(6, "g"), hole(4, "g"), "#f4f8fb", "#6b7b8c", "fotodiodă", (COL(5), ROW["i"] + 4))
    s += diode(hole(12, "d"), hole(14, "d"), "#ff5252", "#b71c1c", "LED roșu", (COL(13), ROW["e"] + 4))
    wires = [wire(hole(2, "j"), "A0", COLORS["A0"], (0, 1)), wire(hole(6, "j"), "GND1", COLORS["GND"], (0, 1)),
             wire(hole(10, "a"), "5", COLORS["D5"]), wire(hole(14, "a"), "GNDs", COLORS["GND"])]
    return s, wires, ["A0", "GND1", "5", "GNDs"]


def svg(title, parts, wires, used, note):
    body = board(used) + breadboard() + parts + [x for w in wires for x in w]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Segoe UI, Helvetica, Arial, sans-serif">
<style>.title{{font-size:20px;font-weight:700}}.sm{{font-size:13px}}.xs{{font-size:10px;fill:#666}}.b{{font-weight:700;fill:#222;paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}}.w{{fill:#fff}}
.pin{{font-size:10px;fill:#cdbfe0}}.on{{fill:#ffeb3b;font-weight:700;font-size:11px}}</style>
<rect width="{W}" height="{H}" fill="#ffffff"/>
<text x="20" y="34" class="title" fill="#222">{title}</text>
<text x="20" y="58" class="sm" fill="#555">{note}</text>
{chr(10).join(body)}
</svg>
'''


def main():
    led_parts, led_w, led_used = leds()
    dw, du = dht_wires()
    hw, hu = hc_wires()
    note = "Firele roșii = 5V, negre = GND. + marchează piciorul lung (anodul)."
    note5 = "Firele negre = GND. + marchează piciorul lung; atenție, la fotodiodă piciorul lung merge la GND."
    steps = {
        "1_LEDuri": ("Pasul 1: LED-uri", led_parts, led_w, led_used),
        "2_SenzorDHT11": ("Pasul 2: se adaugă DHT11 (LED-urile de la pasul 1 rămân)",
                          led_parts + dht11(), led_w + dw, led_used + du),
        "3_SenzorHCSR04": ("Pasul 3: se adaugă HC-SR04 (montajul de la pașii 1-2 rămâne)",
                           led_parts + dht11() + hcsr04(), led_w + dw + hw, led_used + du + hu),
        "4_LEDSiSenzori": ("Pasul 4: montajul complet", led_parts + dht11() + hcsr04(),
                           led_w + dw + hw, led_used + du + hu),
        "5_SenzorLumina": ("Pasul 5: fotodiodă și LED roșu (montaj separat)", *light()),
    }
    for folder, (title, parts, wires, used) in steps.items():
        with open(os.path.join(ROOT, folder, "schema_montaj.svg"), "w", encoding="utf-8") as f:
            f.write(svg(title, parts, wires, used, note5 if folder.startswith("5") else note))


if __name__ == "__main__":
    main()
