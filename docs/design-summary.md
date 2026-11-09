# Design summary and evidence

## Context

METU Formula Racing, **Devrim 26**, sensor-interface electronics. A contributor reports that the board was ordered from China, manufactured, tested, used on the car, and met the relevant technical requirements. These deployment statements are not independently established by files in this repository.

## Directly supported by the EasyEDA JSON

Source: `source/SCH_sensorpcb_2026-11-09.json`.

| Sheet | What it covers | Representative items |
| --- | --- | --- |
| PLAN | Functional grouping | ESP32 logic, power conversion, USB |
| Vsupply | Input protection and regulated supplies | 12 V supply, 3.3 V and 5 V conversion, TPS562201 and protection parts |
| PMI Sensor | Four PMI interfaces | LM358 signal-conditioning circuits and connectors |
| OMRON | Four OMRON interfaces | Connectors and sensor-interface components |
| USB | USB-to-serial interface | FT230XS, status LEDs and protection parts |
| CANBUS | CAN PHY and signal connections | SN65HVD230, CANH/CANL |
| ESP32 | Main control circuitry | ESP32-WROOM-32E family, control pins, sensor nets |

The schematic contains collaborator notes and component choices from a work-in-progress engineering environment. The whole PCB should therefore be attributed to **METU Formula Racing hardware team** unless exact individual block ownership is separately established.

## Original vs interpreted

**Original source:** the seven-sheet EasyEDA schematic JSON with components and net wiring.

**Created portfolio graphic:** `assets/formula-sensor-architecture.svg`, a simplified block-level interpretation of that source.

**Contributor-reported lifecycle:** manufacturing, receipt of boards, physical testing, use in Devrim 26 and relevant Formula Racing checks.

**Not established:** correspondence of this exact export with final fabricated PCB revision; production test pass/fail records; measurable electrical performance; per-person schematic ownership; formal scrutineering certificates.

## What would most strengthen this repository later

A team-approved photograph of the fabricated PCB installed on Devrim 26, an appropriately redacted PCB layout or 3D render, a verified final revision number, and non-sensitive test results. Those should be published only with permission.
