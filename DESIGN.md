---
version: alpha
name: Geometric Math Lab & Blueprint Studio
description: Tactile, high-contrast Swiss geometric workshop design system for MEB TYMM 5th, 6th, and 7th Grade Mathematics Simulation Platform.
colors:
  surface-paper: "#F7F5F0"
  surface-card: "#FFFFFF"
  surface-grid: "#ECE8DF"
  ink-primary: "#141413"
  ink-secondary: "#4A4843"
  ink-muted: "#78756E"
  accent-signal: "#FF5500"
  accent-signal-hover: "#E04800"
  grade-5-emerald: "#00875A"
  grade-6-cobalt: "#0052CC"
  grade-7-amber: "#D97706"
  status-success: "#00875A"
  status-warning: "#D97706"
  status-error: "#DC2626"
  border-sharp: "#141413"
  border-subtle: "#D8D3C8"
  dark-surface: "#0D1520"
  dark-card: "#152232"
  dark-ink: "#F3F4F6"
typography:
  headline-display:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 44px
    fontWeight: 700
    lineHeight: 1.08
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: -0.02em
  headline-md:
    fontFamily: "Space Grotesk, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
  body-lg:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 500
    lineHeight: 1.6
  body-md:
    fontFamily: "Plus Jakarta Sans, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.6
  label-mono:
    fontFamily: "JetBrains Mono, monospace"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.04em
rounded:
  none: 0px
  sharp: 2px
  sm: 4px
spacing:
  xs: 6px
  sm: 12px
  md: 20px
  lg: 32px
  xl: 48px
components:
  button-primary:
    backgroundColor: "{colors.accent-signal}"
    textColor: "{colors.surface-card}"
    rounded: "{rounded.sharp}"
    padding: 12px
  card-atelier:
    backgroundColor: "{colors.surface-card}"
    rounded: "{rounded.sharp}"
    padding: 20px
---

# Geometric Math Lab & Blueprint Studio

## Overview
Türkiye Yüzyılı Maarif Modeli (TYMM) 5, 6 ve 7. sınıf matematik simülasyonları için tasarlanmış **İsviçre Geometrik Laboratuvarı (Swiss Geometric Lab)** ve **Teknik Blueprint (Koyu Mod)** tasarım dili. Sıradan yuvarlatılmış şablonlar veya yapay zeka klişesi mor gradyanlar yerine; cetvel, gönye, pergel ve teknik çizim kağıdının fiziksel dokusunu hissettiren net kenarlı (`2px` keskin köşe + fiziksel ofset gölge), yüksek kontrastlı bir pedagojik atölye arayüzü sunar.

## Colors
- **Surface Paper (`#F7F5F0`):** Göz yormayan sıcak teknik çizim kağıdı zemini (akıllı tahta parlamasını önler).
- **Ink Primary (`#141413`):** Keskin teknik çini mürekkebi siyahı; tüm ana metinler ve `2px` yapısal çerçeveler için.
- **Accent Signal (`#FF5500`):** Sinyal Turuncusu; birincil etkileşim noktaları, aktif simülasyon tutamaçları ve "Evet" aksiyonları için.
- **Sınıf Kodlaması:**
  - **5. Sınıf (`#00875A` - Zümrüt Yeşili):** Geometrik keşif ve doğallık.
  - **6. Sınıf (`#0052CC` - Teknik Kobalt):** Çarpanlar, katlar ve analitik yapı.
  - **7. Sınıf (`#D97706` - Koyu Kehribar):** Tam sayılar, rasyonel sayılar ve cebirsel muhakeme.
- **Blueprint Dark Mode (`#0D1520`):** Tek tıkla aktifleşen koyu mühendislik modu.

## Typography
- **Space Grotesk:** Başlıklar, kazanım kodları ve sayısal göstergeler için geometrik, teknik karakterli sans-serif.
- **Plus Jakarta Sans:** Öğrenci yönergeleri, yeni nesil soru kökleri ve ipuçları için yüksek okunabilirlikli gövde yazı tipi.
- **JetBrains Mono:** Açı ölçüleri (`180°`), koordinatlar, kesirler, kazanım kodları (`MAT.5.3.1`) ve formüller için.

## Layout
- Üst kısımda sabit teknik durum çubuğu (Sınıf, Hafta, TYMM Kazanım Kodu, Tema Değiştirici ve İlerleme).
- **3 Aşamalı Pedagojik Sekme & Akış Yapısı:**
  1. **Aşama 1 (Aktif Öğrenme & Keşif Simülasyonu):** Sol panelde adım adım rehberli görev kartları ve ipuçları, sağ/orta alanda interaktif çizim ve deney tuvali.
  2. **Aşama 2 (Öğrendim mi? - Anlık Değerlendirme):** Simülasyonun hemen ardından kazanımı doğrulayan etkileşimli mini kontrol görevi.
  3. **Aşama 3 ("Ek Soru Çözmek İster misiniz?" ve 10 Yeni Nesil Soru Havuzu):** Sayfa altında yer alan karar kartı. Başlangıçta ve "Hayır" seçildiğinde soru havuzu gizlidir (`display: none`); "Evet" tıklandığında 10 yeni nesil soru kartı (hem 1-10 numaralı gezgin hem de tam liste görünümüyle) açılır.

## Elevation & Depth
- Bulanık (blur) gölgeler yerine teknik çizim masası hissi veren `3px 3px 0px #141413` sert ofset gölgeler.
- Tıklanabilir tüm butonlarda `:active` durumunda `translate(2px, 2px)` fiziksel basılma tepkisi.

## Shapes
- **Sharp Atelier (`2px` border-radius):** Yuvarlak "balon" tasarım yerine cetvelle çizilmiş net geometrik sınırlar.

## Components
- **Simulation Canvas Workbench:** Noktalı/kareli/izometrik arka plan seçenekli, üst araç çubuklu, canlı ölçüm göstergeli etkileşim alanı.
- **MEB Context Ribbon (`.meb-context-ribbon`):** MEB TYMM Öğrenme-Öğretme Uygulamaları kılavuzundaki resmi bağlam ve yönerge bandı.
- **Hypothesis Box (`.hypothesis-box`):** Deneye başlamadan önce öğrencinin matematiksel varsayımını/hipotezini seçtiği alan.
- **Dual Control Bar (`.dual-control-bar`):** Çok değişkenli dinamik deney sürgüleri ve parametre kontrolleri (cevabı doğrudan dikte etmeyen keşif alanı).
- **Observation Drawer & Table (`.observation-drawer`, `.observation-table`):** "📋 Gözlemi Kaydet" butonu ile yapılan denemelerin anlık olarak kaydedildiği bilimsel veri tablosu.
- **Conjecture Box (`.conjecture-box`):** Toplanan verilerden ve denemelerden hareketle öğrencinin matematiksel kuralı/genellemeyi çıkardığı akıl yürütme kutusu.
- **Guided Stepper Card:** Öğrenciye o anki adımı gösteren, varsayım + deney + kural çıkarımını doğrulayan ("🔍 Çıkarımımı Doğrula") aktif yönlendirme bileşeni.
- **Conditional Extra Question Gate:** "Ek soru çözmek ister misiniz? (Evet / Hayır)" kontrol kutusu ve ona bağlı 10 soruluk yeni nesil soru motoru.

## Do's and Don'ts
- **Do:** Her etkileşimde öğrenciye anında görsel ve metinsel pedagojik geri bildirim ver.
- **Do (Aktif Öğrenme Döngüsü):** Pasif sürgü kaydırma yerine "Varsayım Belirleme -> Bağımsız Değişken Deneyi -> Veri/Gözlem Kaydetme -> Kural Çıkarımı" pedagojik döngüsünü uygula.
- **Do:** Simülasyon adımları arasında geçiş yapıldığında ("Sonraki Adım →", adım sekmeleri veya araç butonları tıklandığında) ya da sürgü hareket ettirildiğinde `#sim-feedback-box` alanını (`resetFeedbackForStep`) mutlaka yeni adımın durumuna sıfırla; önceki adımın "🎉 Tebrikler!" mesajını yeni adımda ekranda bırakma.
- **Do:** Etkinlik sayfalarında başka bir sınıf veya haftaya doğrudan geçiş linki bulundurma; yalnızca `../index.html` ("🏠 Ana Sayfa") dönüş butonu kullan.
- **Do:** "Ek soru çözmek ister misiniz?" alanında başlangıçta ve "Hayır" durumunda 10 ek soruyu tamamen gizli tut; yalnızca "Evet" butonuna basıldığında görünür yap.
- **Don't:** "Hedef Konuma Getir" gibi öğrencinin yerine deneyi çözen pasif/hile butonları kesinlikle ekleme.
- **Don't:** Mor, eflatun veya indigo (`#8b5cf6`, `#6366f1`) renklerini kesinlikle kullanma.
- **Don't:** Öğrenciyi metin yığınına boğma; her adımı interaktif tuval üzerindeki eylemlerle eşleştir.

