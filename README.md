# Devrim 26 · Sensor Interface PCB

**METU Formula Racing | Embedded hardware · analog sensor interfaces · CAN communication**

This repository documents a **collaborative sensor-interface PCB** developed for METU Formula Racing's **Devrim 26** car. The design combines an ESP32 microcontroller with multiple sensor channels, CAN communications, USB–UART connectivity and regulated power supplies.

> **Hardware outcome (team-reported):** the PCB was manufactured, received from the fabricator in China, bench-tested, and installed and used in the Devrim 26 vehicle. The contributor reports that the board met applicable Formula Racing technical requirements. This repository does not contain an independent inspection certificate or complete test record.

![Functional block diagram (not a photograph or routed board)](assets/formula-sensor-architecture.svg)

## What is in the design

| Functional area | Components / structure present in the supplied schematic |
| --- | --- |
| Control | ESP32-WROOM-32E |
| Vehicle CAN interface | SN65HVD230 CAN transceiver |
| USB to serial | FT230XS USB–UART bridge |
| Analog signal conditioning | LM358 operational amplifier circuitry |
| Sensor connections | Four PMI channels and four OMRON channels |
| Power | 12 V input, 5 V and 3.3 V regulation and protection |

The component list describes the **supplied EasyEDA schematic**, not an independently verified final assembly BOM.

## Design files and navigation

- [Original EasyEDA schematic export](source/SCH_sensorpcb_2026-11-09.json) — seven design sheets, retained as supplied.
- [Design summary and evidence boundaries](docs/design-summary.md) — what the schematic actually documents and what comes from the project contributor.
- [Architecture illustration](assets/formula-sensor-architecture.svg) — derived overview; **not** a CAD view, PCB routing screenshot or measured result.
- [Standard-library source check](tools/inspect_schematic.py) — summarizes project structure and checks the JSON archive without external EDA software.

```bash
python3 tools/inspect_schematic.py source/SCH_sensorpcb_2026-11-09.json
```

The source has seven sheets: `PLAN`, `Vsupply`, `PMI Sensor`, `OMRON`, `USB`, `CANBUS`, and `ESP32`. This export preserves original collaborator annotations.

## Project contribution and provenance

This is **team engineering work**, not a claim of individual authorship of every circuit and sheet. It combines electronics design work with a practical design-to-fabrication-to-vehicle lifecycle. The original schematic dates and comments reflect the historical design workflow; the export has **not** been identified as the exact manufactured board revision.

**Repository status:** Private, pending team approval before release of source schematic, photos, Gerbers, layout and collaborator annotations. See [publication checklist](docs/publication-checklist.md).

## Important limitations

- No PCB copper routing, Gerbers, drill files, manufacturer outputs, assembly photographs, test logs or technical inspection record were included with this upload.
- JSON parsing and source inspection are **not** DRC, ERC, ESD validation, hardware testing or official Formula Student scrutineering.
- The architecture image is an interpretation of sheet labels and parts, not a verified net-by-net functional simulation.
