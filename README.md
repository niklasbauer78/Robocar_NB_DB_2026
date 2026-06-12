# Robocar des FAFO-Team Ostalb
  
Ein linienfolgender Roboter auf Basis eines Modellbausets mit 3 Liniensensoren, 4 Antriebsmotoren und Python Steuerung, um den großen Preis von Heidenheim zu gewinnen.

---

## Inhaltsverzeichnis

- [Projektbeschreibung](#projektbeschreibung)
- [Teamvorstellung](#teamvorstellung)
- [Hardware](#hardware)
- [Projektstruktur](#projektstruktur)
- [Sensorlogik](#sensorlogik)
- [Motorlogik](#motorlogik)
- [Programm starten](#programm-starten)
- [Programm stoppen](#programm-stoppen)
- [Wichtige Einstellungen](#wichtige-einstellungen)

---

## Projektbeschreibung

Dieses Projekt soll eine vorgegebene Rennstrecke möglichst schnell absolvieren. Die Strecke besteht aus einer schwarzen Linie, mit einer Breite von 20mm, auf einem weißen Untergrund.

Das Programm ist bewusst einfach gehalten und kennt nur 3 Zustände:

| Sensorzustand | Aktion |
|---|---|
| Links aktiv | linke Motoren rückwärts, rechte Motoren vorwärts |
| Mitte aktiv | alle Motoren vorwärts |
| Rechts aktiv | linke Motoren vorwärts, rechte Motoren rückwärts |



---

## Teamvorstellung

Da keines der Teammitglieder perfekt programmieren konnte setzte sich schnell das Motto "Fuck around and find out" durch. Dessen Akronym "FAFO" findet sich im Teamnamen wieder.

| Teammitglieder: |
|---|
| Niklas Bauer |
| Dominik Borggreven |

---

## Hardware

- Raspberry Pi 3 Model B
- Lafvin Smart Car Kit for Raspberry Pi mit:
  - 4x DC-Motoren für die Räder
  - 3x Liniensensor TRCT5000
  - 1x PWM-Modul PCA9685
  - 3x Akkumulator 18650

---

## Projektstruktur

```text
.
├── main.py
├── motor.py
├── sensor.py
├── control.py
└── config.json
```

### main.py

Startet das Programm und wartet auf einen "Enter" Tastenbefehl. Danach wird das Programm in Dauerschleife ausgeführt. Durch "Strg+C" stoppt dieses Programm die Schleife kontrolliert und schaltet die Motoren ab.

### motor.py

Initialisiert die Motoren und steuert diese auf Befehl zwischen 0% und 100% an. Desweiteren müssen hier die Motoren den richtigen Kanälen zugeordnet werden.

### sensor.py

Empfängt die Signale der 3 Liniensensoren und stellt diese global zur Verfügung.

### control.py

Das Herzstück des Algorithmus. Es steuert die Motoren je nach Signal der Liniensensoren.

### config.json

Hier können die Geschwindigkeiten Räder angepasst werden.
Außerdem lässt sich die Taktzeit der control Schleife anpassen.

---

## Sensorlogik

Auf folgenden Eingängen des Raspberry Pi können die Sensorwerte ausgelesen werden:

| Sensor | Eingang |
|---|---|
| Links | GPIO 14 |
| Mitte | GPIO 15 |
| Rechts | GPIO 23 |

Bei "Linie erkannt" liefert GPIO eine 1. Bei "keine Linie erkannt" entsprechend eine 0.  
(Sollten die Sensoren invertiert reagieren, kann dies in der config.json angepasst werden)

## Motorlogik

Die Steuerung der Motoren erfolgt via PWM-Signal durch das PCA9685-Modul:

In unserem Fall sind die Kanäle wie folgt zugeordnet:

| Motor | Kanal + | Kanal - |
|---|---|---|
| Vorne links | 0 | 1 |
| Hinten links | 2 | 3 |
| Vorne rechts | 6 | 7 |
| Hinten rechts | 4 | 5 |

Um den Kurvenradius zu verringern macht es Sinn die kurveninneren Räder rückwärts anzusteuern und die kurvenäußeren vorwärts.
...wie bei einem Raupenbagger

---

## Programm starten

Virtuelle Umgebung aktivieren:

```bash
source .robocar/bin/activate
```

Programm starten:

```bash
python3 src/main.py
```

Das Programm gibt nun die Anweisung "Enter" zum Start. Nach klicken der "Enter"-Taste sollte das Robocar losfahren.

---

## Programm stoppen

Durch "Strg+C" kann das Programm jederzeit gestoppt werden. Das Programm sorgt selbstständig dafür, dass die Motoren abgeschalten werden.

---

## Wichtige Einstellungen:

### config.json

| Einstellung | Hinweis | Empfohlene Werte |
|---|---|---|
| Geschwindigkeit Geradeausfahrt | Wert muss eine gewisse Schwelle überschreiten, damit sich die Räder überhaupt bewegen | zwischen 25 und 30 |
| Geschwindigkeit der kurveninneren Räder | Wert muss eine gewisse Schwelle überschreiten, damit sich die Räder überhaupt bewegen | zwischen -35 und -25 |
| Geschwindigkeit der kurvenäußeren Räder | Wert muss eine gewisse Schwelle überschreiten, damit sich die Räder überhaupt bewegen | zwischen 25 und 35 |
| Sensor über schwarz | kann zwischen 0 und 1 verändert werden, falls die Liniensensoren invertierte Werte liefern | 1 |
| Taktgeschwindigkeit | passt die Taktgeschwindigkeit der control Schleife an | 0.05 |

### motor.py

Zuordnung der Räder zu den richtigen PCA9685-Kanälen vornehmen.

