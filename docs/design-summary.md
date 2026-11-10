# Circuit overview

This repository contains a seven-sheet EasyEDA schematic for the sensor-interface electronics of METU Formula Racing's **Devrim 26**.

## Design organization

| Sheet | Main function | Main components or nets |
| --- | --- | --- |
| `PLAN` | Top-level system organization | Controller, supply, USB and sensor blocks |
| `Vsupply` | Regulation and input protection | 12 V input, 5 V/3.3 V rails, TPS562201 circuitry |
| `PMI Sensor` | Four sensor channels | Analog interface circuits, LM358 and connectors |
| `OMRON` | Four sensor channels | OMRON sensor connections and interface parts |
| `USB` | PC-to-board serial connection | FT230XS and associated components |
| `CANBUS` | Connection to the vehicle CAN network | SN65HVD230, CANH, CANL |
| `ESP32` | Microcontroller connections | ESP32-WROOM-32E and peripheral signals |

## Board-level design

The ESP32 acts as the board controller. PMI and OMRON channels provide sensor inputs, while the CAN transceiver connects the board to the vehicle's CAN network. The FT230XS handles USB-to-UART communication. The supply section generates the regulated rails used by the digital and analog blocks.

The input protection, regulator choices, analog front-end circuitry and communication interfaces can be inspected in the [source schematic](../source/SCH_sensorpcb_2026-11-09.json).

## From design to car

The hardware was ordered from a manufacturer in China, delivered to the team, tested and installed on Devrim 26. It was used on the vehicle and passed the relevant Formula Racing technical checks, as reported by the project team.

The included JSON is a **schematic export**, not a PCB layout or manufacturing package. The final production revision, Gerbers, test logs and photographs would be useful additions if they are available later.

## Attribution

This was a team project. The schematic retains contributor comments; the repository does not assign all circuit blocks to one person.
