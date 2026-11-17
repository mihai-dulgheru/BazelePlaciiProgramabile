"""Generează schemele de montaj (schema_montaj.svg) pentru pașii 1-5.

Rulare din rădăcina proiectului:  python tools/genereaza_scheme.py
Pozițiile pinilor urmează placa NEXTLAB.TECH A1 (2 pini 5V, 3 pini GND).

Firele sunt trasate pe benzi separate, astfel încât să nu se suprapună și să nu se încrucișeze:
- firele spre rândul de sus al plăcii (D2-D6, GND de sus) trec pe deasupra;
- firele spre zona POWER / ANALOG IN trec pe dedesubt;
- prin breadboard, firele merg doar printre rânduri, nu peste găuri.
"""
import os
from itertools import combinations

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1070, 580

# --- Breadboard mini: 17 coloane; găurile a-e (și f-j) din aceeași coloană sunt legate ---
BBX, BBY = 110, 190


def COL(c):
    return BBX + 30 + (c - 1) * 20


ROW = {r: BBY + 30 + i * 20 for i, r in enumerate("abcde")}
ROW.update({r: BBY + 150 + i * 20 for i, r in enumerate("fghij")})
LANE = {"ef": 320, "fg": 350, "gh": 370, "hi": 390, "ij": 410}  # benzi printre rândurile din jumătatea de jos


def hole(c, r):
    return COL(c), ROW[r]


# --- Placa NEXTLAB A1 ---
BX, BY, BW, BH = 620, 190, 420, 280
TOP_Y, BOT_Y = BY + 20, BY + BH - 20
PINS = {}  # cheie -> (x, y, etichetă)
for i, n in enumerate(["AREF", "GND", "13", "12", "11", "10", "9", "8"]):
    PINS["GNDs" if n == "GND" else n] = (BX + 70 + i * 22, TOP_Y, n)
for i, n in enumerate(["7", "6", "5", "4", "3", "2", "TX", "RX"]):
    PINS[n] = (BX + 250 + i * 22, TOP_Y, n)
for i, (k, n) in enumerate([("5V1", "5V"), ("RES", "RES"), ("3V3", "3.3V"), ("5V2", "5V"),
                            ("GND1", "GND"), ("GND2", "GND"), ("VIN", "VIN")]):
    PINS[k] = (BX + 90 + i * 22, BOT_Y, n)
for i in range(6):
    PINS[f"A{i}"] = (BX + 270 + i * 22, BOT_Y, f"A{i}")

C5V, CGND = "#d32f2f", "#212121"
CD2, CD3, CD4, CD5, CD6, CA0 = "#f9a825", "#2e7d32", "#1565c0", "#ef6c00", "#6a1b9a", "#00838f"


def board(used):
    s = [f'<rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="12" fill="#5b2c86" stroke="#3d1d5c" stroke-width="2"/>',
         f'<rect x="{BX - 18}" y="{BY + 60}" width="60" height="50" rx="3" fill="#c9c9c9" stroke="#999"/>',
         f'<text x="{BX + 12}" y="{BY + 127}" class="sm" fill="#ddd" text-anchor="middle">USB</text>',
         f'<rect x="{BX - 8}" y="{BY + 190}" width="50" height="45" rx="3" fill="#222"/>',
         # butonul reset, în colțul din stânga sus (ca pe placă)
         f'<rect x="{BX + 16}" y="{BY + 10}" width="26" height="26" rx="3" fill="#888"/>',
         f'<circle cx="{BX + 29}" cy="{BY + 23}" r="7" fill="#333"/>',
         f'<text x="{BX + 29}" y="{BY + 50}" class="sm" fill="#ddd" text-anchor="middle">reset</text>',
         # microcontrolerul ATmega328PB
         *[f'<rect x="{BX + 247 + i * 8}" y="{BY + 92}" width="3" height="56" fill="#aaa"/>' for i in range(5)],
         *[f'<rect x="{BX + 237}" y="{BY + 102 + i * 8}" width="56" height="3" fill="#aaa"/>' for i in range(5)],
         f'<rect x="{BX + 243}" y="{BY + 98}" width="44" height="44" rx="2" fill="#1b1b1b"/>',
         f'<text x="{BX + 265}" y="{BY + 162}" class="sm" fill="#ddd" text-anchor="middle">ATmega328PB</text>',
         f'<text x="{BX + 210}" y="{BY + 190}" class="title" fill="#fff" text-anchor="middle">NEXTLAB.TECH A1</text>',
         f'<text x="{BX + 340}" y="{TOP_Y + 62}" class="sm" fill="#ddd" text-anchor="middle">DIGITAL (PWM~)</text>',
         f'<text x="{BX + 156}" y="{BOT_Y - 44}" class="sm" fill="#ddd" text-anchor="middle">POWER</text>',
         f'<text x="{BX + 325}" y="{BOT_Y - 44}" class="sm" fill="#ddd" text-anchor="middle">ANALOG IN</text>']
    for k, (x, y, n) in PINS.items():
        s.append(f'<rect x="{x - 8}" y="{y - 8}" width="16" height="16" fill="#111"/>'
                 f'<rect x="{x - 3}" y="{y - 3}" width="6" height="6" fill="#555"/>')
        ty = y + 14 if y == TOP_Y else y - 14
        anchor = "end" if y == TOP_Y else "start"
        s.append(f'<text x="{x + 3}" y="{ty}" transform="rotate(-90 {x + 3} {ty})" text-anchor="{anchor}" '
                 f'class="{"pin on" if k in used else "pin"}">{n}</text>')
    return s


def breadboard(hidden_top, hidden_bottom):
    """Numerele coloanelor sunt sus și jos, ca pe breadboard-ul real; unde trece un fir
    sau piciorul unui modul, numărul de pe acea margine nu se desenează."""
    assert not hidden_top & hidden_bottom, f"coloane fără număr: {hidden_top & hidden_bottom}"
    s = [f'<rect x="{BBX}" y="{BBY}" width="380" height="260" rx="8" fill="#f1f1ef" stroke="#c8c8c4" stroke-width="2"/>',
         f'<rect x="{BBX + 10}" y="{BBY + 122}" width="360" height="16" rx="3" fill="#dcdcd8"/>']
    for c in range(1, 18):
        for r in ROW:
            x, y = hole(c, r)
            s.append(f'<rect x="{x - 3}" y="{y - 3}" width="6" height="6" fill="#4a4a4a"/>')
        if c not in hidden_top:
            s.append(f'<text x="{COL(c)}" y="{BBY + 14}" class="xs" text-anchor="middle">{c}</text>')
        if c not in hidden_bottom:
            s.append(f'<text x="{COL(c)}" y="{BBY + 252}" class="xs" text-anchor="middle">{c}</text>')
    for r, y in ROW.items():
        s.append(f'<text x="{BBX + 12}" y="{y + 3}" class="xs" text-anchor="middle">{r}</text>')
    return s


def path(pts, radius=8):
    """Linie frântă cu colțuri rotunjite (segmente doar orizontale/verticale)."""
    d = f"M{pts[0][0]},{pts[0][1]}"
    for (ax, ay), (px, py), (bx, by) in zip(pts, pts[1:], pts[2:]):
        l1, l2 = abs(px - ax) + abs(py - ay), abs(bx - px) + abs(by - py)
        r = min(radius, l1 / 2, l2 / 2)
        ux, uy = (px - ax) / l1, (py - ay) / l1
        vx, vy = (bx - px) / l2, (by - py) / l2
        d += f" L{px - ux * r:g},{py - uy * r:g} Q{px},{py} {px + vx * r:g},{py + vy * r:g}"
    return d + f" L{pts[-1][0]},{pts[-1][1]}"


def wire(pts, color):
    d = path(pts)
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    return [f'<path d="{d}" fill="none" stroke="#fff" stroke-width="8" stroke-linejoin="round"/>',
            f'<path d="{d}" fill="none" stroke="{color}" stroke-width="5" stroke-linejoin="round" stroke-linecap="round"/>',
            f'<circle cx="{x1}" cy="{y1}" r="4" fill="{color}" stroke="#fff"/>',
            f'<circle cx="{x2}" cy="{y2}" r="4" fill="{color}" stroke="#fff"/>']


def over(c, pin, lane_y, color):
    """Din rândul a, drept în sus, apoi pe deasupra până la un pin din rândul de sus al plăcii."""
    x, y = hole(c, "a")
    px, py, _ = PINS[pin]
    return [(x, y), (x, lane_y), (px, lane_y), (px, py)], color


def around(c, r, lane, x_lane, y_lane, pin, color):
    """Din jumătatea de jos: pe banda `lane` spre stânga/dreapta până la x_lane,
    apoi pe deasupra (pin sus) sau pe dedesubt (pin jos) la înălțimea y_lane."""
    x, y = hole(c, r)
    ly = LANE[lane]
    px, py, _ = PINS[pin]
    return [(x, y), (x, ly), (x_lane, ly), (x_lane, y_lane), (px, y_lane), (px, py)], color


def resistor(c1, c2, r):
    (x1, y), (x2, _) = hole(c1, r), hole(c2, r)
    m = (x1 + x2) / 2
    bands = "".join(f'<rect x="{m - 9 + i * 6}" y="{y - 6}" width="3" height="12" fill="{c}"/>'
                    for i, c in enumerate(["#8b4513", "#111", "#8b4513", "#c9a227"]))
    return [f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#999" stroke-width="2"/>',
            f'<circle cx="{x1}" cy="{y}" r="2.5" fill="#999"/><circle cx="{x2}" cy="{y}" r="2.5" fill="#999"/>',
            f'<rect x="{m - 14}" y="{y - 6}" width="28" height="12" rx="5" fill="#d8b98e" stroke="#a68457"/>', bands]


def diode(anode, cathode, r, fill, stroke, plus_dx, plus_dy):
    """LED / fotodiodă văzută de sus, cu picioarele în două coloane alăturate; + = piciorul lung (anodul)."""
    (ax, y), (kx, _) = hole(anode, r), hole(cathode, r)
    return [f'<circle cx="{(ax + kx) / 2}" cy="{y}" r="9.5" fill="{fill}" stroke="{stroke}" stroke-width="2"/>',
            f'<circle cx="{(ax + kx) / 2 - 3}" cy="{y - 3}" r="3" fill="#fff" opacity="0.7"/>',
            f'<text x="{ax + plus_dx}" y="{y + plus_dy}" class="plus" text-anchor="middle">+</text>']


def module(cols, labels, body, name):
    """Modul (DHT11, HC-SR04) înfipt în rândul j; corpul stă sub breadboard."""
    y = ROW["j"]
    bx, by, bw, bh = body
    s = [f'<line x1="{COL(c)}" y1="{y}" x2="{COL(c)}" y2="{by}" stroke="#999" stroke-width="3"/>' for c in cols]
    s.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="5" fill="#1e5aa8" stroke="#0d3b75" stroke-width="2"/>')
    s += [f'<text x="{COL(c) + 4}" y="{by + 6}" transform="rotate(-90 {COL(c) + 4} {by + 6})" class="xs w" '
          f'text-anchor="end">{l}</text>' for c, l in zip(cols, labels)]
    s.append(f'<text x="{bx + bw / 2}" y="{by + bh + 18}" class="sm b" text-anchor="middle">{name}</text>')
    return s


MOD_Y = ROW["j"] + 40


def leds():
    """Pasul 1: D5 → R (coloanele 7-10) → LED roșu; D6 → R (9-12) → LED albastru; catozii în coloana 11 → GND."""
    parts = resistor(7, 10, "b") + resistor(9, 12, "c")
    parts += diode(10, 11, "d", "#ff5252", "#b71c1c", -11, -8)
    parts += diode(12, 11, "e", "#448aff", "#0d47a1", 11, -8)
    wires = [over(7, "5", 140, CD5), over(9, "6", 155, CD6), over(11, "GNDs", 170, CGND)]
    return parts, wires, ["5", "6", "GNDs"]


def dht():
    """DHT11 în coloanele 12-14 (+, OUT, -)."""
    x0 = COL(13) - 44
    parts = module([12, 13, 14], ["+", "OUT", "-"], (x0, MOD_Y, 88, 80), "DHT11")
    parts.append(f'<rect x="{x0 + 14}" y="{MOD_Y + 32}" width="60" height="42" rx="3" fill="#e8f1fb"/>')
    parts += [f'<line x1="{x0 + 18}" y1="{MOD_Y + 40 + i * 9}" x2="{x0 + 70}" y2="{MOD_Y + 40 + i * 9}" '
              f'stroke="#9bb8d8" stroke-width="2"/>' for i in range(4)]
    wires = [around(12, "f", "ef", 555, 490, "5V1", C5V),
             around(13, "i", "ij", 65, 90, "2", CD2),
             around(14, "h", "hi", 510, 535, "GND2", CGND)]
    return parts, wires, ["5V1", "2", "GND2", 12, 13, 14]  # numerele = coloanele picioarelor


def hc():
    """HC-SR04 în coloanele 2-5 (VCC, Trig, Echo, GND)."""
    x0 = (COL(3) + COL(4)) / 2 - 100
    parts = module([2, 3, 4, 5], ["VCC", "Trig", "Echo", "GND"], (x0, MOD_Y, 200, 80), "HC-SR04")
    for cx in (x0 + 35, x0 + 165):
        parts.append(f'<circle cx="{cx}" cy="{MOD_Y + 48}" r="24" fill="#cfd4da" stroke="#8a9199" stroke-width="3"/>'
                     f'<circle cx="{cx}" cy="{MOD_Y + 48}" r="14" fill="#5f6670"/>')
    wires = [around(2, "g", "fg", 540, 505, "5V2", C5V),
             around(3, "h", "gh", 80, 105, "3", CD3),
             around(4, "f", "ef", 95, 120, "4", CD4),
             around(5, "h", "gh", 525, 520, "GND1", CGND)]
    return parts, wires, ["5V2", "3", "4", "GND1", 2, 3, 4, 5]


def light():
    """Pasul 5: A0 → R (coloanele 5-8) → piciorul scurt al fotodiodei (8); piciorul lung (9) → GND.
    LED roșu ca la pasul 1: D5 → R → LED → GND."""
    parts = resistor(3, 6, "b") + diode(6, 7, "d", "#ff5252", "#b71c1c", -11, -8)
    parts += resistor(5, 8, "h") + diode(9, 8, "g", "#f4f8fb", "#6b7b8c", 11, 15)
    wires = [over(3, "5", 140, CD5), over(7, "GNDs", 170, CGND),
             around(9, "f", "fg", 555, 490, "GND1", CGND),
             around(5, "i", "ij", 540, 505, "A0", CA0)]
    return parts, wires, ["5", "GNDs", "GND1", "A0"]


def svg(title, note, parts, wires, used):
    top = {(pts[0][0] - COL(1)) // 20 + 1 for pts, _ in wires if pts[0][1] == ROW["a"] and pts[1][1] < ROW["a"]}
    bottom = {u for u in used if isinstance(u, int)}
    body = board(used) + breadboard(top, bottom) + parts + [x for pts, color in wires for x in wire(pts, color)]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Segoe UI, Helvetica, Arial, sans-serif">
<style>.title{{font-size:20px;font-weight:700}}.sm{{font-size:13px}}.xs{{font-size:9px;fill:#777}}.w{{fill:#fff;font-size:10px}}
.b{{font-weight:700;fill:#222}}.plus{{font-size:14px;font-weight:700;fill:#222}}
.pin{{font-size:10px;fill:#cdbfe0}}.on{{fill:#ffeb3b;font-weight:700;font-size:11px}}</style>
<rect width="{W}" height="{H}" fill="#ffffff"/>
<text x="20" y="34" class="title" fill="#222">{title}</text>
<text x="20" y="58" class="sm" fill="#555">{note}</text>
{chr(10).join(body)}
</svg>
'''


def check(wires, gap=9):
    """Oprește generarea dacă două fire diferite se ating sau se încrucișează."""
    segs = [(i, a, b) for i, (pts, _) in enumerate(wires) for a, b in zip(pts, pts[1:])]
    for (i, a, b), (j, c, d) in combinations(segs, 2):
        if i == j:
            continue
        x1, x2, y1, y2 = min(a[0], b[0]), max(a[0], b[0]), min(a[1], b[1]), max(a[1], b[1])
        x3, x4, y3, y4 = min(c[0], d[0]), max(c[0], d[0]), min(c[1], d[1]), max(c[1], d[1])
        assert x1 - gap >= x4 or x3 - gap >= x2 or y1 - gap >= y4 or y3 - gap >= y2,             f"firele {wires[i][1]} și {wires[j][1]} se ating: {a}-{b} / {c}-{d}"


def combine(*items):
    parts, wires, used = [], [], []
    for p, w, u in items:
        parts, wires, used = parts + p, wires + w, used + u
    return parts, wires, used


def main():
    note = "Firele roșii = 5V, negre = GND. + marchează piciorul lung (anodul)."
    note5 = "Firele negre = GND. + marchează piciorul lung; atenție, la fotodiodă piciorul lung merge la GND."
    steps = {
        "1_LEDuri": ("Pasul 1: LED-uri", "Firele negre = GND. + marchează piciorul lung (anodul).", combine(leds())),
        "2_SenzorDHT11": ("Pasul 2: se adaugă DHT11 (LED-urile de la pasul 1 rămân)", note, combine(leds(), dht())),
        "3_SenzorHCSR04": ("Pasul 3: se adaugă HC-SR04 (montajul de la pașii 1-2 rămâne)", note,
                           combine(leds(), dht(), hc())),
        "4_LEDSiSenzori": ("Pasul 4: montajul complet", note, combine(leds(), dht(), hc())),
        "5_SenzorLumina": ("Pasul 5: fotodiodă și LED roșu (montaj separat)", note5, combine(light())),
    }
    for folder, (title, n, (parts, wires, used)) in steps.items():
        check(wires)
        with open(os.path.join(ROOT, folder, "schema_montaj.svg"), "w", encoding="utf-8") as f:
            f.write(svg(title, n, parts, wires, used))


if __name__ == "__main__":
    main()
