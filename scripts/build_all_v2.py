#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MEB TYMM 2026-2027 Aktif Öğrenme v2.0 Tüm Modülleri İnşa Eden Ana Betik (build_all_v2.py)
5, 6 ve 7. Sınıf 1-7. Hafta Modüllerini (21 Adet) üretir, müfredatı senkronize eder.
"""

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR / "scripts"))

from builder_engine import build_module_html
from extract_helpers import extract_existing_raw_sections
from data_grade5 import GRADE5_MODULES
from data_grade6 import GRADE6_MODULES
from data_grade7 import GRADE7_MODULES
from generator import sync_curriculum_js

ALL_GRADES = {
    5: GRADE5_MODULES,
    6: GRADE6_MODULES,
    7: GRADE7_MODULES,
}

def main():
    print("=" * 60)
    print("MATEMATİK ATÖLYESİ — AKTİF ÖĞRENME v2.0 TOPLU İNŞA MOTORU")
    print("=" * 60)

    total_created = 0

    for grade, modules in ALL_GRADES.items():
        grade_dir = ROOT_DIR / f"sinif-{grade}"
        grade_dir.mkdir(parents=True, exist_ok=True)

        for mod_cfg in modules:
            week = mod_cfg["week"]
            file_name = f"{grade}hafta-{week}.html"
            target_path = grade_dir / file_name

            # Mevcut 1-6. haftalardan önceki 10 soruyu ve 3 mini görevi koru
            eq_raw, mt_existing = extract_existing_raw_sections(target_path)

            final_extra_questions = eq_raw if eq_raw else mod_cfg.get("extra_questions", [])
            final_mini_tasks = mt_existing if mt_existing else mod_cfg.get("mini_tasks", [])

            mod_payload = {
                "grade": grade,
                "week": week,
                "title": mod_cfg["title"],
                "date": mod_cfg["date"],
                "hours": mod_cfg["hours"],
                "theme": mod_cfg["theme"],
                "outcome_code": mod_cfg["outcome_code"],
                "outcome_text": mod_cfg["outcome_text"],
                "process_items": mod_cfg["process_items"],
                "meb_quote": mod_cfg["meb_quote"],
                "sim_steps": mod_cfg["sim_steps"],
                "mini_tasks": final_mini_tasks,
                "extra_questions": final_extra_questions
            }

            html_output = build_module_html(mod_payload)
            target_path.write_text(html_output, encoding="utf-8")
            total_created += 1
            print(f"✓ [{grade}. Sınıf {week}. Hafta] -> {target_path.relative_to(ROOT_DIR)} ({len(html_output)} bayt)")

    print("-" * 60)
    print(f"Toplam {total_created} haftalık modül Aktif Öğrenme v2.0 ile üretildi.")
    print("Müfredat verisi senkronize ediliyor...")
    sync_curriculum_js()
    print("✓ curriculum-data.js güncellendi!")
    print("=" * 60)

if __name__ == "__main__":
    main()
