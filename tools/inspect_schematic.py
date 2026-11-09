#!/usr/bin/env python3
"""Inspect an EasyEDA multi-sheet schematic archive without a CAD tool.

This verifies JSON structure and reports evidence, not electrical design rules,
fabrication correctness, safety, or a hardware test pass.
"""
import argparse
import json
from pathlib import Path


def inspect(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("schematics"), list):
        raise ValueError("Expected an EasyEDA object with a schematics array")
    sheet_info = []
    for sheet in data["schematics"]:
        title = sheet.get("title")
        shapes = sheet.get("dataStr", {}).get("shape", [])
        if not isinstance(title, str) or not isinstance(shapes, list):
            raise ValueError("Invalid sheet structure")
        sheet_info.append({"sheet": title, "drawing_elements": len(shapes)})
    return {
        "project_title": data.get("title"),
        "editor_version": data.get("editorVersion"),
        "sheet_count": len(sheet_info),
        "sheets": sheet_info,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("file", type=Path)
    p.add_argument("--verify-archive", action="store_true",
                   help="Check expected supplied sheet names; not circuit correctness")
    args = p.parse_args()
    info = inspect(args.file)
    print(json.dumps(info, ensure_ascii=False, indent=2))
    if args.verify_archive:
        expected = {
            "PLAN", "Vsupply", "PMI Sensor", "OMRON",
            "USB", "CANBUS", "ESP32",
        }
        names = {s["sheet"] for s in info["sheets"]}
        if names != expected or info["sheet_count"] != 7:
            raise SystemExit("Archive sheets differ from the supplied seven-sheet source")
        print("Archive structure check passed (no electrical validation implied).")


if __name__ == "__main__":
    main()
