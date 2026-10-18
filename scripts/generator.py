#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MEB TYMM 2026-2027 Matematik Atölyesi — Haftalık Modül & Müfredat Üretici (generator.py)

Kullanım Amacı:
Tüm 36 haftayı topluca boş şablon olarak üretmek YERİNE, her hafta sonu yalnızca
bir sonraki haftanın etkinliğini hazırlamak ve `data/*.docx` yıllık planlarından
ilgili haftanın kazanımlarını çekmek için tasarlanmıştır.

Örnek Kullanımlar:
1) Yıllık planları (.docx) okuyup index.html için müfredat verisini güncellemek:
   python scripts/generator.py --sync

2) Belirli bir haftanın (ör. 2. Hafta) kazanım özetini görmek:
   python scripts/generator.py --info --hafta 2

3) Belirli bir sınıf ve hafta için başlangıç şablonu oluşturmak (ör. 5. sınıf 2. hafta -> sinif-5/5hafta-2.html):
   python scripts/generator.py --sinif 5 --hafta 2
"""

import argparse
import json
import os
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
ASSETS_JS_DIR = ROOT_DIR / "assets" / "js"

DOCX_FILES = {
    5: DATA_DIR / "5-sinif-matematik.docx",
    6: DATA_DIR / "6-sinif-matematik.docx",
    7: DATA_DIR / "7-sinif-matematik.docx",
}

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def parse_grade_docx(grade: int, docx_path: Path) -> list[dict]:
    """data/{grade}-sinif-matematik.docx dosyasındaki haftalık plan tablolarını okur."""
    if not docx_path.exists():
        return []

    weeks_data = []
    seen_weeks = set()

    with zipfile.ZipFile(docx_path, "r") as zf:
        root = ET.fromstring(zf.read("word/document.xml"))

    for tbl in root.findall(".//w:tbl", NS):
        rows = tbl.findall(".//w:tr", NS)
        if not rows:
            continue

        header_cells = [
            clean_text("".join(t.text for t in c.findall(".//w:t", NS) if t.text))
            for c in rows[0].findall(".//w:tc", NS)
        ]
        if not header_cells or "HAFTA" not in header_cells[1:3] and "TARİH" not in header_cells[0]:
            continue

        for row in rows[1:]:
            cells = [
                clean_text("".join(t.text for t in c.findall(".//w:t", NS) if t.text))
                for c in row.findall(".//w:tc", NS)
            ]
            if len(cells) < 7:
                continue

            date_str = cells[0]
            week_str = cells[1]
            hours_str = cells[2]
            theme_str = cells[3]
            content_str = cells[4]
            outcome_str = cells[5]
            process_str = cells[6]

            m = re.search(r"(\d+)\.\s*Hafta", week_str, re.IGNORECASE)
            if not m:
                continue

            week_num = int(m.group(1))
            if week_num in seen_weeks:
                continue
            seen_weeks.add(week_num)

            file_name = f"{grade}hafta-{week_num}.html"
            rel_path = f"sinif-{grade}/{file_name}"
            abs_path = ROOT_DIR / f"sinif-{grade}" / file_name

            weeks_data.append({
                "grade": grade,
                "week": week_num,
                "weekLabel": f"{week_num}. Hafta",
                "fileId": f"{grade}hafta-{week_num}",
                "fileName": file_name,
                "path": rel_path,
                "isReady": abs_path.exists(),
                "date": date_str,
                "hours": hours_str,
                "theme": theme_str,
                "content": content_str,
                "outcomes": outcome_str,
                "process": process_str,
            })

    weeks_data.sort(key=lambda x: x["week"])
    return weeks_data


def sync_curriculum_js() -> dict:
    """Tüm sınıfların yıllık plan verisini ve hangi haftaların hazır olduğunu assets/js/curriculum-data.js dosyasına yazar."""
    ASSETS_JS_DIR.mkdir(parents=True, exist_ok=True)
    all_data = {}
    for grade, path in DOCX_FILES.items():
        all_data[str(grade)] = parse_grade_docx(grade, path)

    js_path = ASSETS_JS_DIR / "curriculum-data.js"
    js_content = (
        "// Otomatik üretildi: scripts/generator.py --sync\n"
        "// MEB TYMM 2026-2027 5, 6 ve 7. Sınıf Yıllık Plan Verisi ve Aktif Hafta Durumu\n"
        f"window.TYMM_CURRICULUM = {json.dumps(all_data, ensure_ascii=False, indent=2)};\n"
    )
    js_path.write_text(js_content, encoding="utf-8")
    return all_data


def print_week_info(week_num: int, grade_filter: int | None = None) -> None:
    all_data = sync_curriculum_js()
    grades = [grade_filter] if grade_filter else [5, 6, 7]
    for g in grades:
        items = [w for w in all_data.get(str(g), []) if w["week"] == week_num]
        if not items:
            print(f"[{g}. Sınıf - {week_num}. Hafta] Plan kaydı bulunamadı.")
            continue
        w = items[0]
        status = "HAZIR (YAYINDA)" if w["isReady"] else "HENÜZ OLUŞTURULMADI (Hafta Sonu Hazırlanacak)"
        print(f"=== {g}. SINIF • {w['weekLabel']} ({w['date']}) [{status}] ===")
        print(f"  Hedef Dosya      : {w['path']}")
        print(f"  Tema             : {w['theme']}")
        print(f"  İçerik Çerçevesi : {w['content']}")
        print(f"  Öğrenme Çıktısı  : {w['outcomes']}")
        print(f"  Süreç Bileşenleri: {w['process'][:250]}...")
        print()


def main():
    parser = argparse.ArgumentParser(
        description="MEB TYMM Haftalık Simülasyon & Müfredat Senkronizasyon Aracı"
    )
    parser.add_argument("--sync", action="store_true", help="data/*.docx dosyalarını okuyup curriculum-data.js dosyasını günceller")
    parser.add_argument("--info", action="store_true", help="Belirtilen haftanın MEB TYMM kazanımlarını listeler")
    parser.add_argument("--sinif", type=int, choices=[5, 6, 7], help="Sınıf düzeyi (5, 6 veya 7)")
    parser.add_argument("--hafta", type=int, help="Hafta numarası (1-36)")

    args = parser.parse_args()

    if args.info and args.hafta:
        print_week_info(args.hafta, args.sinif)
        return

    # Varsayılan olarak sadece müfredat indeksini senkronize et (toplu hafta dosyası üretme!)
    data = sync_curriculum_js()
    ready_Summary = []
    for g in ["5", "6", "7"]:
        ready_files = [w["fileName"] for w in data[g] if w["isReady"]]
        ready_Summary.append(f"{g}. Sınıf ({len(data[g])} hafta okundu, Yayında: {', '.join(ready_files) or 'Yok'})")

    print("✓ TYMM Yıllık Plan verileri `assets/js/curriculum-data.js` dosyasına aktarıldı.")
    for line in ready_Summary:
        print("  • " + line)


if __name__ == "__main__":
    main()
