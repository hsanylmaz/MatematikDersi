#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tüm 21 modülün pedagojik ve teknik kurallara uygunluğunu denetler.
"""

import re
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

PURPLE_HEXES = ["#8b5cf6", "#6366f1", "#7c3aed", "#a855f7", "#9333ea", "#c084fc", "#4f46e5", "#4338ca"]

def verify():
    errors = []
    total_checked = 0

    for grade in [5, 6, 7]:
        for week in range(1, 8):
            file_path = ROOT_DIR / f"sinif-{grade}" / f"{grade}hafta-{week}.html"
            total_checked += 1

            if not file_path.exists():
                errors.append(f"{file_path.name} MEVCUT DEĞİL!")
                continue

            content = file_path.read_text(encoding="utf-8")

            # 1. Aşama 1 kontrolleri
            if 'id="stage-1"' not in content:
                errors.append(f"{file_path.name}: #stage-1 bulunamadı.")
            if 'class="meb-context-ribbon"' not in content:
                errors.append(f"{file_path.name}: meb-context-ribbon bulunamadı.")
            if 'id="hypothesis-container"' not in content:
                errors.append(f"{file_path.name}: hypothesis-container bulunamadı.")
            if 'id="sim-record-btn"' not in content:
                errors.append(f"{file_path.name}: sim-record-btn bulunamadı.")
            if 'class="observation-drawer"' not in content:
                errors.append(f"{file_path.name}: observation-drawer bulunamadı.")
            if 'id="conjecture-container"' not in content or 'id="conjecture-select"' not in content:
                errors.append(f"{file_path.name}: conjecture-container / select bulunamadı.")
            if 'id="verify-step-btn"' not in content:
                errors.append(f"{file_path.name}: verify-step-btn bulunamadı.")

            # Hile butonu kontrolü (Kaldırılmış olmalı!)
            if 'id="sim-auto-target-btn"' in content or 'Hedef Konuma Getir' in content:
                errors.append(f"{file_path.name}: 'Hedef Konuma Getir' butonu tespit edildi (Yasaklı!).")

            # 2. Aşama 2 kontrolleri
            if 'id="stage-2"' not in content:
                errors.append(f"{file_path.name}: #stage-2 bulunamadı.")
            mini_cards = re.findall(r'<article class="mini-check-card"', content)
            if len(mini_cards) != 3:
                errors.append(f"{file_path.name}: Beklenen 3 mini görev yerine {len(mini_cards)} bulundu.")

            # 3. Aşama 3 kontrolleri
            if 'id="stage-3"' not in content:
                errors.append(f"{file_path.name}: #stage-3 bulunamadı.")
            if 'id="btn-extra-yes"' not in content or 'id="btn-extra-no"' not in content:
                errors.append(f"{file_path.name}: Ek soru Evet/Hayır butonları eksik.")
            if 'id="extra-questions-panel" class="extra-questions-container is-hidden" hidden' not in content:
                errors.append(f"{file_path.name}: extra-questions-panel gizli olarak başlamıyor.")

            # 4. Navigasyon izolasyonu (Sadece ../index.html olmalı)
            hrefs = re.findall(r'href=["\'](.*?)["\']', content)
            for h in hrefs:
                if h.endswith('.html') and h != '../index.html':
                    errors.append(f"{file_path.name}: İzole olmayan link tespit edildi -> {h}")

            # 5. Mor renk yasağı
            for ph in PURPLE_HEXES:
                if ph in content.lower():
                    errors.append(f"{file_path.name}: Yasaklı mor renk ({ph}) tespit edildi.")

    print(f"Toplam {total_checked} modül denetlendi.")
    if errors:
        print(f"❌ {len(errors)} HATA BULUNDU:")
        for e in errors:
            print("  • " + e)
        return False
    else:
        print("✅ TÜM 21 MODÜL (5, 6, 7. SINIF 1-7. HAFTA) %100 KUSURSUZ DOĞRULANDI!")
        return True

if __name__ == "__main__":
    success = verify()
    sys.exit(0 if success else 1)
