# Matematik Atölyesi & Simülasyon Platformu (MEB TYMM 2026-2027)

## Overview
Türkiye MEB Türkiye Yüzyılı Maarif Modeli (TYMM) 2026-2027 yıllık planlarına (`data/5-sinif-matematik.docx`, `data/6-sinif-matematik.docx`, `data/7-sinif-matematik.docx`) dayalı; 5., 6. ve 7. sınıfları kapsayan, GitHub Pages uyumlu, mobil ve akıllı tahta dostu **Matematik Atölyesi & Simülasyon Platformu**.

Her haftalık modül (`sinif-5/5hafta-X.html`, `sinif-6/6hafta-X.html`, `sinif-7/7hafta-X.html`) zorunlu **3 Aşamalı Pedagojik Akış** içerir:
1. **Aktif Öğrenme ve Keşif Aşaması:** Adım adım görev kartları, ipuçları ve interaktif simülasyon tuvali.
2. **Anlık Değerlendirme (Öğrendim mi?) Sekmesi:** Kazanımın özümsenip özümsenmediğini ölçen etkileşimli mini kontrol görevi.
3. **Dinamik Soru Havuzu ve "Ek Soru İster misiniz? (Evet / Hayır)" Mekanizması:** Başlangıçta ve "Hayır" seçildiğinde gizli kalan; yalnızca **"Evet"** butonuna tıklandığında açılan **10 adet yeni nesil ek soru** (anında geri bildirim ve detaylı çözümlü).

## Project Type
**WEB** (Static HTML5 + Custom Modular CSS + Vanilla ES6 JavaScript + Python Docx Generator Script for GitHub Pages)

## Success Criteria
- [x] `index.html` üzerinde 5, 6 ve 7. sınıf sekmeleri, tema filtreleri, hafta kartları ve `localStorage` ilerleme rozetlerinin çalışması.
- [x] Haftalık dosya isimlendirme standardının `sinif-5/5hafta-1.html`, `sinif-6/6hafta-1.html`, `sinif-7/7hafta-1.html` olarak uygulanması.
- [x] Her hafta sayfasında 3 aşamalı pedagojik yapının (Yönlendirmeli Simülasyon ➔ Öğrendim mi? Değerlendirme Sekmesi ➔ Koşullu Görünümlü 10 Yeni Nesil Ek Soru Havuzu) eksiksiz çalışması.
- [x] Sayfa ilk açıldığında ve "Hayır" seçildiğinde 10 ek sorunun gizli (`hidden`) olması, "Evet" butonuna basıldığında anında görünür olması.
- [x] `scripts/generator.py` betiğinin `data/*.docx` dosyalarını okuyup yıllık plan verilerini ayrıştırması ve haftalık şablonları (`5hafta-X.html`, `6hafta-X.html`, `7hafta-X.html`) üretebilmesi.

## Tech Stack
- **Frontend:** Semantic HTML5, Custom CSS Grid/Flexbox (`assets/css/style.css`), Vanilla JavaScript (ES6+), SVG/Canvas 2D İnteraktif Simülasyon Motoru.
- **Data & Automation:** Python 3 (`scripts/generator.py`) — standart kütüphane (`zipfile`, `xml.etree.ElementTree`, `json`) ile harici paket bağımlılığı olmadan `.docx` okuma ve statik HTML üretimi.
- **Hosting:** GitHub Pages (Zero-build, doğrudan statik yayın).

## File Structure
```text
MatematikDersi/
├── DESIGN.md                         # Tasarım sistemi ve token spesifikasyonu
├── matematik-atolyesi-platform.md    # Proje görev ve doğrulama planı
├── index.html                        # 5, 6 ve 7. sınıf ana karşılama ve modül menüsü
├── assets/
│   ├── css/
│   │   └── style.css                 # Geometric Math Lab + Blueprint Dark tasarım sistemi
│   └── js/
│       └── curriculum-data.js        # generator.py tarafından docx'lerden üretilen müfredat verisi
├── data/
│   ├── 5-sinif-matematik.docx        # 5. Sınıf TYMM Yıllık Planı
│   ├── 6-sinif-matematik.docx        # 6. Sınıf TYMM Yıllık Planı
│   └── 7-sinif-matematik.docx        # 7. Sınıf TYMM Yıllık Planı
├── sinif-5/
│   └── 5hafta-1.html                 # 5. Sınıf 1. Hafta: Temel Geometrik Çizimler ve İnşalar
├── sinif-6/
│   └── 6hafta-1.html                 # 6. Sınıf 1. Hafta: Doğal Sayının Çarpanları ve Katları
├── sinif-7/
│   └── 7hafta-1.html                 # 7. Sınıf 1. Hafta: Tam Sayılar ve Rasyonel Sayılar
└── scripts/
    └── generator.py                  # Yıllık planları okuyup 5/6/7hafta-X.html üreten betik
```

## Task Breakdown

| Task ID | Name | Agent | Skills | Priority | Dependencies | INPUT → OUTPUT → VERIFY |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **T1** | Tasarım Spesifikasyonu (`DESIGN.md`) | `frontend-specialist` | `design-spec`, `frontend-design` | P0 | None | Tasarım kararları → `DESIGN.md` → Token ve renk kuralları kontrolü (No Purple) |
| **T2** | Ana Stil Sistemi (`assets/css/style.css`) | `frontend-specialist` | `frontend-design`, `clean-code` | P0 | T1 | `DESIGN.md` → `assets/css/style.css` → Mobil, masaüstü ve akıllı tahta görünüm doğrulaması |
| **T3** | Yıllık Plan Okuyucu ve Üretici (`scripts/generator.py`) | `backend-specialist` | `python-patterns`, `clean-code` | P1 | None | `data/*.docx` → `scripts/generator.py` & `assets/js/curriculum-data.js` → Python çalıştırma testi |
| **T4** | 5. Sınıf 1. Hafta Simülasyonu (`sinif-5/5hafta-1.html`) | `frontend-specialist` | `frontend-design`, `clean-code` | P1 | T2 | MAT.5.3.1 kazanımı → `sinif-5/5hafta-1.html` → 3 aşamalı akış + 10 ek soru koşul testi |
| **T5** | 6. ve 7. Sınıf 1. Hafta Simülasyonları (`6hafta-1.html`, `7hafta-1.html`) | `frontend-specialist` | `frontend-design`, `clean-code` | P1 | T2, T4 | MAT.6.1.1 & MAT.7.1.1 → `sinif-6/6hafta-1.html`, `sinif-7/7hafta-1.html` → 3 aşamalı akış testi |
| **T6** | Ana Karşılama Portalı (`index.html`) | `frontend-specialist` | `frontend-design`, `clean-code` | P1 | T2, T3, T4, T5 | Müfredat verisi → `index.html` → Sınıf filtreleri ve `5hafta-1`, `6hafta-1`, `7hafta-1` bağlantıları |

## Phase X: Final Verification
- [x] No purple/violet hex codes (`#8b5cf6`, `#6366f1`, vb. kesinlikle yok)
- [x] Socratic Gate tamamlandı ve kullanıcı onayı alındı
- [x] `scripts/generator.py` betiği `data/*.docx` dosyalarını başarıyla işliyor ve toplu dosya üretmeden haftalık çalışma akışını destekliyor
- [x] "Ek soru çözmek ister misiniz?" mekanizması başlangıçta ve "Hayır" durumunda gizli, "Evet" durumunda 10 yeni nesil soruyu açıyor

## ✅ PHASE X COMPLETE
- Lint & Structure: ✅ Pass
- Security: ✅ No critical issues (Zero external untrusted runtime dependencies)
- Build & Curriculum Sync: ✅ Success (`assets/js/curriculum-data.js` generated from `data/*.docx`)
- Date: 2026-10-16

