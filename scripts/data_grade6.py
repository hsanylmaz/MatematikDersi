#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
6. Sınıf Matematik Aktif Öğrenme v2.0 Müfredat ve Simülasyon Verisi (Hafta 1-7)
"""

GRADE6_MODULES = [
    # 6. SINIF 1. HAFTA
    {
        "grade": 6,
        "week": 1,
        "title": "Doğal Sayıların Çarpanları ve Katları Atölyesi",
        "date": "14–18 Eylül",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.6.1.1",
        "outcome_text": "Karşılaştığı problem durumlarında bir doğal sayının çarpan ve katlarına yönelik muhakeme yapabilme.",
        "process_items": [
            "Bir doğal sayının çarpan ve katlarına yönelik varsayımlarda bulunur.",
            "Varsayımlarını alan modeli ve çarpan ağacı ile sınar.",
            "Çarpanların sonlu, katların sınırsız olduğuna dair önerme sunar.",
            "Önermesini gerekçelendirir."
        ],
        "meb_quote": "Okul bahçesi alanı/çevresi problemi; çarpan ve katlara yönelik varsayım üretme (çarpanlar sonludur, katlar sınırsızdır), dikdörtgen alan modeli ve çarpan ağacı ile sınama, önerme sunma.",
        "sim_steps": [
            {
                "tag": "DİKDÖRTGEN ALAN MODELİ",
                "title": "Adım 1: Alanı 24 br² Olan Dikdörtgenin Kenarları",
                "instruction": "En sürgüsünü 1'den 12'ye kadar değiştirin. Alanı 24 birimkare yapan tam sayı kenar ikililerini deneyerek gözlem tablosuna kaydedin.",
                "hint": "Alanı 24 br² olan bir dikdörtgenin kenar uzunlukları (En × Boy = 24), 24'ün doğal sayı çarpanlarıdır.",
                "hypotheses": [
                    {"text": "Bir sayının çarpanları sınırsızdır, sonsuz sayıda çarpanı vardır.", "correct": False},
                    {"text": "Bir sayının çarpanları sonlu sayıdadır; 1'den başlar ve en fazla sayının kendisine kadar gider.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Bir doğal sayının çarpanları (bölenleri) sonlu sayıdadır; en küçük çarpan 1, en büyük çarpan sayının kendisidir.", "correct": True},
                    {"text": "Çarpanlar sonsuzdur.", "correct": False}
                ],
                "sliderLabel": "En Uzunluğu (En × Boy = 24):",
                "min": 1, "max": 12, "defaultVal": 3, "unit": "birim",
                "simType": "factor_rect",
                "hasSecondary": False
            },
            {
                "tag": "ÇARPAN AĞACI",
                "title": "Adım 2: Çarpan Ağacı ile Asal Bileşenler",
                "instruction": "Sayının bölenlerini dallara ayırarak çarpan ağacını oluşturun. Uçlardaki asal çarpanları tabloya kaydedin.",
                "hint": "Bir sayıyı çarpan ağacında dallarına ayırdığınızda en uçta kalan sayılar sayının asal çarpanlarıdır.",
                "hypotheses": [
                    {"text": "Her bileşik sayı asal sayıların çarpımı olarak tek bir biçimde yazılabilir.", "correct": True},
                    {"text": "Asal çarpanlar sayıdan bağımsızdır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Her doğal sayı çarpan ağacı ile asal çarpanlarına ayrılabilir (Aritmetiğin Temel Teoremi).", "correct": True},
                    {"text": "Asal çarpanlar her zaman çifttir.", "correct": False}
                ],
                "sliderLabel": "Bölünen Değeri:",
                "min": 1, "max": 12, "defaultVal": 4, "unit": "birim",
                "simType": "factor_rect",
                "hasSecondary": False
            },
            {
                "tag": "SAYININ KATLARI",
                "title": "Adım 3: Sayının Katları ve Sonsuzluk",
                "instruction": "Sayının 1, 2, 3... katlarını sırayla inceleyin. Çarpanlar ile katlar arasındaki sınır durumunu karşılaştırıp tabloya kaydedin.",
                "hint": "Bir sayının katları sayının kendisiyle başlayıp ritmik olarak sonsuza kadar devam eder.",
                "hypotheses": [
                    {"text": "Bir sayının katları da çarpanları gibi belirli bir sayıda durur.", "correct": False},
                    {"text": "Bir doğal sayının katları sınırsızdır (sonsuza kadar gider).", "correct": True}
                ],
                "conjectures": [
                    {"text": "Bir doğal sayının çarpanları SONLU iken, katları SINIRSIZDIR (sonsuzdur).", "correct": True},
                    {"text": "Katlar sonlu, çarpanlar sonsuzdur.", "correct": False}
                ],
                "sliderLabel": "Kat Çarpanı:",
                "min": 1, "max": 10, "defaultVal": 3, "unit": "kat",
                "simType": "factor_rect",
                "hasSecondary": False
            },
            {
                "tag": "GENELLEME VE ÖNERME",
                "title": "Adım 4: Çarpan ve Kat Karşılaştırması",
                "instruction": "Farklı sayılar için çarpan ve kat tablosunu inceleyerek genellemeye ulaşın.",
                "hint": "a sayısı b sayısına kalansız bölünüyorsa, b sayısı a'nın bir çarpanı, a sayısı ise b'nin bir katıdır.",
                "hypotheses": [
                    {"text": "Çarpan ve bölen tamamen aynı anlama gelir.", "correct": True},
                    {"text": "Çarpan ile bölen farklı matematiksel kavramlardır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bir doğal sayının çarpanı aynı zamanda o sayının kalansız bölenidir; a, b'nin çarpanı ise b, a'nın katıdır.", "correct": True},
                    {"text": "Bölenler katlardan büyüktür.", "correct": False}
                ],
                "sliderLabel": "Sayı Seçimi:",
                "min": 1, "max": 8, "defaultVal": 6, "unit": "sayı",
                "simType": "factor_rect",
                "hasSecondary": False
            }
        ]
    },

    # 6. SINIF 2. HAFTA
    {
        "grade": 6,
        "week": 2,
        "title": "Bölünebilme Kriterleri ve Çıkarım Atölyesi",
        "date": "21–25 Eylül",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.6.1.2",
        "outcome_text": "Bir doğal sayının 2, 3, 4, 5, 6, 9 ve 10 ile tam bölünebilme kriterlerine ilişkin çıkarım yapabilme.",
        "process_items": [
            "Bölünebilme kriterlerine yönelik varsayımlarda bulunur.",
            "Yüzlük tablo ve basamak değeri analiziyle sınar.",
            "Bölünebilme kurallarına dair önermeler sunar.",
            "Tanılayıcı dallanmış ağaç üzerinden değerlendirir."
        ],
        "meb_quote": "Hızlı bölünebilme oyunu; yüzlük tablo ve basamak değeri analiziyle 2, 3, 4, 5, 6, 9, 10 bölünebilme varsayımlarını kurma, örneklerle sınama, tanılayıcı dallanmış ağaç ile doğrulama.",
        "sim_steps": [
            {
                "tag": "SON BASAMAK KURALLARI",
                "title": "Adım 1: 2, 5 ve 10 ile Bölünebilme (Son Basamak)",
                "instruction": "Sürgüyle sayıyı değiştirin. Sayının son basamağını inceleyip 2, 5 ve 10 ile bölünüp bölünmediğini gözlem tablosuna kaydedin.",
                "hint": "Son basamağı çift olanlar 2'ye; 0 veya 5 olanlar 5'e; son basamağı 0 olanlar 10'a tam bölünür.",
                "hypotheses": [
                    {"text": "2, 5 ve 10 ile bölünebilmede sadece sayının son basamağına bakmak yeterlidir.", "correct": True},
                    {"text": "Tüm basamakları toplamak gerekir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Son basamağı çift (0,2,4,6,8) olanlar 2'ye; 0 veya 5 olanlar 5'e; 0 olanlar 10'a tam bölünür.", "correct": True},
                    {"text": "Son basamağı tek sayılar 2'ye tam bölünür.", "correct": False}
                ],
                "sliderLabel": "İncelenen Sayı:",
                "min": 10, "max": 90, "defaultVal": 30, "unit": "sayı",
                "simType": "divisibility_test",
                "hasSecondary": False
            },
            {
                "tag": "RAKAMLAR TOPLAMI",
                "title": "Adım 2: 3 ve 9 ile Bölünebilme (Rakamlar Toplamı)",
                "instruction": "Farklı sayıların rakamları toplamını sürgüyle inceleyin. Rakamlar toplamının 3'ün ve 9'un katı olma durumlarını tabloya kaydedin.",
                "hint": "Bir sayının rakamları toplamı 3'ün katıysa 3'e; 9'un katıysa 9'a tam bölünür. (9'a bölünen her sayı 3'e de bölünür!)",
                "hypotheses": [
                    {"text": "9'a bölünen her doğal sayı aynı zamanda 3'e de kalansız bölünür.", "correct": True},
                    {"text": "3'e bölünen her sayı mutlaka 9'a da bölünür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Rakamları toplamı 3'ün katı olanlar 3'e, 9'un katı olanlar 9'a tam bölünür; 9'a bölünen her sayı 3'e de bölünür.", "correct": True},
                    {"text": "3'e bölünebilmek için son basamağın 3 olması şarttır.", "correct": False}
                ],
                "sliderLabel": "İncelenen Sayı:",
                "min": 12, "max": 99, "defaultVal": 45, "unit": "sayı",
                "simType": "divisibility_test",
                "hasSecondary": False
            },
            {
                "tag": "SON İKİ BASAMAK",
                "title": "Adım 3: 4 ile Bölünebilme (Son İki Basamak)",
                "instruction": "Sayının son iki basamağını inceleyerek 4 ile bölünebilmeyi test edin.",
                "hint": "Yüzler basamağı daima 100'ün (yani 4'ün) katı olduğundan, sadece son iki basamağın 4'e bölünmesi yeterlidir.",
                "hypotheses": [
                    {"text": "Bir sayının son iki basamağı 00 veya 4'ün katı ise sayı 4 ile tam bölünür.", "correct": True},
                    {"text": "Son basamağı 4 olan her sayı 4'e bölünür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bir sayının son iki basamağının oluşturduğu sayı 00 veya 4'ün katı ise o sayı 4 ile kalansız bölünür.", "correct": True},
                    {"text": "Son basamağı çift olan her sayı 4'e bölünür.", "correct": False}
                ],
                "sliderLabel": "İncelenen Sayı:",
                "min": 100, "max": 200, "defaultVal": 124, "unit": "sayı",
                "simType": "divisibility_test",
                "hasSecondary": False
            },
            {
                "tag": "BİLEŞİK BÖLÜNEBİLME",
                "title": "Adım 4: 6 ile Bölünebilme (Hem 2 Hem 3)",
                "instruction": "Bir sayının hem 2'ye (çift) hem de 3'e (rakamlar toplamı) bölündüğü durumları inceleyin.",
                "hint": "6 = 2 × 3 olduğundan, bir sayı hem 2'ye hem 3'e aynı anda bölünüyorsa 6'ya da tam bölünür.",
                "hypotheses": [
                    {"text": "Bir sayı hem 2'ye hem de 3'e kalansız bölünüyorsa 6 ile de tam bölünür.", "correct": True},
                    {"text": "6 ile bölünmek için son basamağın 6 olması gerekir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bir doğal sayı hem 2 ile (çift) hem de 3 ile (rakamlar toplamı) tam bölünüyorsa 6 ile de tam bölünür.", "correct": True},
                    {"text": "Tek sayılar da 6'ya bölünebilir.", "correct": False}
                ],
                "sliderLabel": "İncelenen Sayı:",
                "min": 12, "max": 96, "defaultVal": 36, "unit": "sayı",
                "simType": "divisibility_test",
                "hasSecondary": False
            }
        ]
    },

    # 6. SINIF 3. HAFTA
    {
        "grade": 6,
        "week": 3,
        "title": "Asal Sayılar, Ortak Kat ve Ortak Bölen Atölyesi",
        "date": "28 Eylül–02 Ekim",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.6.1.3 & MAT.6.1.4",
        "outcome_text": "MAT.6.1.3. Bir doğal sayının asal olma durumunu ve asal çarpanlarını çözümleyebilme • MAT.6.1.4. Günlük hayat problemleri ya da matematiksel durumlar üzerinden ortak kat ve ortak böleni yorumlayabilme.",
        "process_items": [
            "Asal sayıların yalnız 1'e ve kendisine bölündüğünü çözümler.",
            "Asal çarpan ağacı ve algoritmasını uygular.",
            "Günlük yaşam problemlerinde ortak bölen ve ortak kat durumlarını belirler."
        ],
        "meb_quote": "Yüzlük tabloda Eratosthenes Kalburu ile asal sayıları keşfetme, çarpan ağacı ve asal çarpan algoritması; tarım arazisine fidan dikme ve mama paketi hazırlama bağlamında ortak bölen, ortak kat ve aralarında asal sayıları keşfetme.",
        "sim_steps": [
            {
                "tag": "ERATOSTHENES KALBURU",
                "title": "Adım 1: Asal Sayı Keşfi ve 1 Dışındaki Bölenler",
                "instruction": "Yalnızca 1'e ve kendisine bölünebilen sayıları sürgüyle inceleyin. 1'in neden asal olmadığını ve tek çift asal sayıyı (2) tabloya kaydedin.",
                "hint": "1'den büyük olup yalnız 1'e ve kendisine bölünen sayılara asal sayı denir. 2, en küçük ve tek çift asal sayıdır.",
                "hypotheses": [
                    {"text": "1 sayısı da asal bir sayıdır.", "correct": False},
                    {"text": "En küçük asal sayı 2'dir ve 2 dışındaki tüm asal sayılar tektir; 1 asal sayı değildir.", "correct": True}
                ],
                "conjectures": [
                    {"text": "1'den büyük, sadece 1'e ve kendisine bölünen sayılar ASALDIR; 2 en küçük ve yegane çift asal sayıdır.", "correct": True},
                    {"text": "Tüm tek sayılar asaldır.", "correct": False}
                ],
                "sliderLabel": "İncelenen Sayı:",
                "min": 2, "max": 30, "defaultVal": 17, "unit": "sayı",
                "simType": "divisibility_test",
                "hasSecondary": False
            },
            {
                "tag": "ASAL ÇARPAN ALGORİTMASI",
                "title": "Adım 2: Asal Çarpan Bölen Listesi",
                "instruction": "Sayının bölen listesini (asal çarpan algoritmasını) çalıştırın. Sayıyı asal çarpanların üslü çarpımı olarak tabloya kaydedin.",
                "hint": "Sayı sırasıyla en küçük asal sayıdan (2, 3, 5, 7...) başlanarak 1 kalana kadar bölünür.",
                "hypotheses": [
                    {"text": "Her doğal sayı asal sayıların çarpımı olarak yazılabilir.", "correct": True},
                    {"text": "Asal çarpanlar sadece tek sayılardan oluşur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bölen listesi yöntemiyle her doğal sayı asal çarpanlarının çarpımı biçiminde ifade edilir (Örn: 60 = 2² × 3 × 5).", "correct": True},
                    {"text": "Bileşik sayıların asal çarpanı yoktur.", "correct": False}
                ],
                "sliderLabel": "Sayı:",
                "min": 12, "max": 72, "defaultVal": 60, "unit": "sayı",
                "simType": "divisibility_test",
                "hasSecondary": False
            },
            {
                "tag": "ORTAK BÖLEN (EŞİT ARALIKLAR)",
                "title": "Adım 3: Fidan Dikme Problemi & Ortak Bölenler",
                "instruction": "Kenarları 24 m ve 36 m olan bir bahçenin etrafına eşit aralıklarla fidan dikilecektir. Her iki sayıyı da tam bölen ortak aralıkları tabloya kaydedin.",
                "hint": "Her iki sayıyı da kalansız bölen sayılara 'ortak bölen' denir.",
                "hypotheses": [
                    {"text": "İki sayının ortak bölenlerinin en büyüğü iki kenara da eşit aralık koyabileceğimiz en büyük adımdır.", "correct": True},
                    {"text": "Ortak bölen sayıların toplamına eşittir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "İki sayının ortak bölenleri, her iki sayıyı da aynı anda kalansız bölen sayılardır (24 ve 36 için: 1, 2, 3, 4, 6, 12).", "correct": True},
                    {"text": "Ortak bölenler her zaman asal sayıdır.", "correct": False}
                ],
                "sliderLabel": "Aralık Adımı:",
                "min": 1, "max": 12, "defaultVal": 6, "unit": "metre",
                "simType": "factor_rect",
                "hasSecondary": False
            },
            {
                "tag": "ORTAK KAT (ZAMAN BİRLİKTELİĞİ)",
                "title": "Adım 4: Sefer Süreleri Problemi & Ortak Katlar",
                "instruction": "Biri 6 dakikada, diğeri 8 dakikada bir kalkan iki otobüsün birlikte kalktığı ortak dakikaları inceleyin.",
                "hint": "Her iki sayının da katı olan sayılara 'ortak kat' denir (6, 12, 18, 24... ve 8, 16, 24...).",
                "hypotheses": [
                    {"text": "İki otobüs ilk kez 6 ve 8'in en küçük ortak katında (24. dakikada) birlikte hareket eder.", "correct": True},
                    {"text": "İlk kez 6 + 8 = 14. dakikada karşılaşırlar.", "correct": False}
                ],
                "conjectures": [
                    {"text": "İki sayının ortak katları periyodik olarak devam eder; en küçük ortak kat iki sürecin ilk kez buluştuğu andır.", "correct": True},
                    {"text": "Ortak katlar sonludur.", "correct": False}
                ],
                "sliderLabel": "Dakika Kontrolü:",
                "min": 6, "max": 48, "defaultVal": 24, "unit": "dk",
                "simType": "factor_rect",
                "hasSecondary": False
            }
        ]
    },

    # 6. SINIF 4. HAFTA
    {
        "grade": 6,
        "week": 4,
        "title": "Deneysel Olasılık ve Göreli Sıklık Atölyesi",
        "date": "05–09 Ekim",
        "hours": "5 Ders Saati",
        "theme": "6. TEMA: VERİDEN OLASILIĞA",
        "outcome_code": "MAT.6.6.1",
        "outcome_text": "Bir olayın olasılığını gözleme dayalı tahmin edebilme.",
        "process_items": [
            "Bir olayın olasılığı ile deneylerden elde ettiği veriyi ilişkilendirir.",
            "Deneye ait tekrar sayısı ile deneyin çıktılarının göreli sıklıklarının ilişkisine yönelik çıkarım yapar."
        ],
        "meb_quote": "Olasılık spektrumu üzerinde ön tahmin (% beklenti), madeni para/zar/çark deneylerini 20-30+ kez tekrarlama, çetele tablosu ile kaydetme, beklenen vs gözlenen sıklığı karşılaştırıp göreli sıklık = olayın olma sayısı / toplam tekrar sayısı yargısına ulaşma.",
        "sim_steps": [
            {
                "tag": "GÖRELİ SIKLIK HESABI",
                "title": "Adım 1: Deney Verisi ve Göreli Sıklık",
                "instruction": "20 atışta gerçekleşen başarılı sonuç sayısını sürgüyle değiştirin. Göreli sıklık oranını (başarılı / 20) gözlem tablosuna kaydedin.",
                "hint": "Göreli sıklık = Olayın Gerçekleşme Sayısı ÷ Toplam Deneme Sayısıdır.",
                "hypotheses": [
                    {"text": "Göreli sıklık daima 0 ile 1 (veya %0 ile %100) arasında bir değer alır.", "correct": True},
                    {"text": "Göreli sıklık 1'den büyük çıkabilir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bir olayın göreli sıklığı (olay sayısı / toplam deneme), o olayın deneysel olasılık tahminidir ve 0 ile 1 arasındadır.", "correct": True},
                    {"text": "Göreli sıklık sadece tam sayı olabilir.", "correct": False}
                ],
                "sliderLabel": "Gerçekleşen Başarılı Çıktı:",
                "min": 1, "max": 20, "defaultVal": 8, "unit": "kez",
                "simType": "probability_fraction",
                "hasSecondary": False
            },
            {
                "tag": "TEKRAR SAYISININ ETKİSİ",
                "title": "Adım 2: Deney Tekrar Sayısını Artırma",
                "instruction": "Deneme sayısını 10, 50, 100 olarak artırın. Deney sayısı arttıkça oranın nasıl kararlı hale geldiğini tabloya kaydedin.",
                "hint": "Deneme sayısı arttıkça göreli sıklık teorik olasılığa giderek daha çok yaklaşır (Büyük Sayılar Yasası).",
                "hypotheses": [
                    {"text": "Deney sayısı arttıkça dalgalanma azalır ve olasılık tahmini daha güvenilir hale gelir.", "correct": True},
                    {"text": "Deney sayısını artırmak olasılık sonucunu değiştirmez, 5 atış yeterlidir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Deneyin tekrar sayısı arttıkça göreli sıklık kararlı hale gelir ve gözleme dayalı tahminin güvenilirliği artar.", "correct": True},
                    {"text": "Az deneme yapmak daha doğru sonuç verir.", "correct": False}
                ],
                "sliderLabel": "Başarı Sayısı (N=50 için):",
                "min": 5, "max": 50, "defaultVal": 25, "unit": "kez",
                "simType": "probability_fraction",
                "hasSecondary": False
            },
            {
                "tag": "RENKLİ ÇARK DENEYİ",
                "title": "Adım 3: Renkli Çark Çevirme Simülasyonu",
                "instruction": "4 eşit dilimli bir çarkta bir rengin gelme sıklığını inceleyin.",
                "hint": "Eşit 4 bölmeli bir çarkta her rengin teorik beklentisi 1/4 = 0,25 (%25)'tir.",
                "hypotheses": [
                    {"text": "Eşit dilimli çarkta çok sayıda çevirmede her dilimin gelme oranı yaklaşık %25 olur.", "correct": True},
                    {"text": "Bazı renkler şanslı olduğu için her zaman %80 çıkar.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Eşit alanlı dilimlere sahip çarklarda deney sayısı büyüdükçe göreli sıklıklar birbirine yaklaşır.", "correct": True},
                    {"text": "Çarkta olasılık her zaman 1'e eşittir.", "correct": False}
                ],
                "sliderLabel": "Renk Çıktı Sayısı:",
                "min": 1, "max": 25, "defaultVal": 10, "unit": "kez",
                "simType": "probability_fraction",
                "hasSecondary": False
            },
            {
                "tag": "GÖZLEME DAYALI TAHMİN",
                "title": "Adım 4: Gelecek Olayı Tahmin Etme",
                "instruction": "Göreli sıklığı 3/5 olan bir basketbol atıcısının 40 atışta beklenen isabet sayısını hesaplayıp tabloya kaydedin.",
                "hint": "Beklenen başarı = Toplam atış × Göreli sıklık = 40 × (3/5) = 24.",
                "hypotheses": [
                    {"text": "Geçmiş deneylerin göreli sıklığı gelecekteki benzer durumları tahmin etmede kullanılır.", "correct": True},
                    {"text": "Geçmiş veriler geleceğe dair hiçbir fikir vermez.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Gözleme dayalı olasılık, geçmiş deneme verilerinin oranını gelecekteki durumlara modelleyerek tahmin üretir.", "correct": True},
                    {"text": "Olasılık tahmini hiçbir zaman yapılamaz.", "correct": False}
                ],
                "sliderLabel": "Beklenen İsabet Sayısı:",
                "min": 10, "max": 35, "defaultVal": 24, "unit": "isabet",
                "simType": "probability_fraction",
                "hasSecondary": False
            }
        ]
    },

    # 6. SINIF 5. HAFTA
    {
        "grade": 6,
        "week": 5,
        "title": "Deneysel Olasılık ve Ondalık Basamaklar Atölyesi",
        "date": "12–16 Ekim",
        "hours": "5 Ders Saati",
        "theme": "6. TEMA: VERİDEN OLASILIĞA • 1. TEMA: SAYILAR VE NİCELİKLER (2)",
        "outcome_code": "MAT.6.6.1 & MAT.6.1.5",
        "outcome_text": "MAT.6.6.1. Bir olayın olasılığını gözleme dayalı tahmin edebilme • MAT.6.1.5. Gerçek yaşam durumlarında ondalık gösterimlerin basamak değerlerini kesirlerden yararlanarak yorumlayabilme.",
        "process_items": [
            "Olasılık oranını ondalık gösterimle ifade eder.",
            "10x10 kareli ızgara ve onluk bloklarla ondalık basamakları kesir toplamı olarak yazar.",
            "Onda birler, yüzde birler ve binde birler basamaklarını çözümler."
        ],
        "meb_quote": "Olasılık değerini ondalık olarak yorumlama (0 ile 1 arası); 10x10 kareli kağıt ve onluk bloklarla ondalık basamak değerlerini 1/10, 1/100, 1/1000 kesir toplamı olarak yazma.",
        "sim_steps": [
            {
                "tag": "OLASILIK VE ONDALIK DEĞER",
                "title": "Adım 1: 100 Denemede Olasılığın Ondalık Gösterimi",
                "instruction": "100 atışta gerçekleşen olay sayısını sürgüyle değiştirin. Ondalık karşılığını (ör. 47/100 = 0,47) tabloya kaydedin.",
                "hint": "Yüzde olarak ifade edilen olasılıklar paydası 100 olan kesirler ve ondalık sayılardır.",
                "hypotheses": [
                    {"text": "Yüzde 45 olasılık, ondalık olarak 0,45 değerine eşittir.", "correct": True},
                    {"text": "Yüzde 45 olasılık, 4,5 değerine eşittir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Olasılık değerleri kesir ve ondalık gösterimlerle ifade edilir; 100 denemede k kez gerçekleşen olay k/100 ondalığıdır.", "correct": True},
                    {"text": "Ondalık olasılık 1'den büyüktür.", "correct": False}
                ],
                "sliderLabel": "100 Denemedeki Başarı:",
                "min": 10, "max": 90, "defaultVal": 47, "unit": "kez",
                "simType": "decimal_grid",
                "hasSecondary": False
            },
            {
                "tag": "YÜZLÜK IZGARA MODELİ",
                "title": "Adım 2: 10x10 Izgarada Ondalık Çözümleme",
                "instruction": "100 birimkarelik ızgarada boyalı kare sayısını sürgüyle değiştirin. Kaç tam sütun (onda birler) ve kaç tekil kare (yüzde birler) olduğunu tabloya kaydedin.",
                "hint": "Her bir sütun 10 kareden oluşur ve bütünün onda biridir (1/10 = 0,1). Her küçük kare yüzde birdir (1/100 = 0,01).",
                "hypotheses": [
                    {"text": "0,46 sayısı; 4 adet onda bir (4/10) ile 6 adet yüzde birin (6/100) toplamıdır.", "correct": True},
                    {"text": "0,46 sayısı 46 tane tam sayıdır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Ondalık gösterimlerde virgülden sonraki ilk basamak onda birler (1/10), ikinci basamak yüzde birler (1/100) basamağıdır.", "correct": True},
                    {"text": "Virgülden sonra ilk basamak yüzde birlerdir.", "correct": False}
                ],
                "sliderLabel": "Boyalı Kare Sayısı:",
                "min": 5, "max": 95, "defaultVal": 46, "unit": "kare",
                "simType": "decimal_grid",
                "hasSecondary": False
            },
            {
                "tag": "KESİR TOPLAMIYLA ÇÖZÜMLEME",
                "title": "Adım 3: Ondalık Sayıyı Kesir Toplamı Olarak Yazma",
                "instruction": "Sayının basamaklarını kesir toplamına dönüştürün: ör. 3,27 = 3 + 2/10 + 7/100.",
                "hint": "Basamak değeri, rakamın bulunduğu basamağın değeriyle (1, 1/10, 1/100...) çarpılmasıyla bulunur.",
                "hypotheses": [
                    {"text": "Bir ondalık gösterim basamak değerlerinin toplamı olarak parçalanabilir.", "correct": True},
                    {"text": "Ondalık sayılar kesir olarak yazılamaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Ondalık sayılar tam kısım ve kesir basamaklarının (1/10, 1/100, 1/1000) toplamı biçiminde çözümlenir.", "correct": True},
                    {"text": "Virgülden sonraki basamaklar tam sayı gibi toplanır.", "correct": False}
                ],
                "sliderLabel": "Ondalık Değer:",
                "min": 10, "max": 90, "defaultVal": 35, "unit": "%",
                "simType": "decimal_grid",
                "hasSecondary": False
            },
            {
                "tag": "BİNDE BİRLER BASAMAĞI",
                "title": "Adım 4: 1/1000 Basamağının Eklenmesi",
                "instruction": "Virgülden sonraki 3. basamağı (binde birler, 1/1000) inceleyin.",
                "hint": "Virgülden sonraki 3. basamağın basamak değeri 1/1000 = 0,001'dir.",
                "hypotheses": [
                    {"text": "Virgülden sonraki 3. basamak binde birler basamağıdır.", "correct": True},
                    {"text": "Virgülden sonra 3. basamak yüzler basamağıdır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Virgülden sonra sırasıyla: onda birler (0,1), yüzde birler (0,01) ve binde birler (0,001) basamakları yer alır.", "correct": True},
                    {"text": "Binde birler en büyük basamaktır.", "correct": False}
                ],
                "sliderLabel": "Seçilen Değer:",
                "min": 1, "max": 9, "defaultVal": 5, "unit": "bindelik",
                "simType": "decimal_grid",
                "hasSecondary": False
            }
        ]
    },

    # 6. SINIF 6. HAFTA
    {
        "grade": 6,
        "week": 6,
        "title": "Ondalık Çözümleme ve Kesir-Bölme İlişkisi Atölyesi",
        "date": "19–23 Ekim",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (2)",
        "outcome_code": "MAT.6.1.5 & MAT.6.1.6",
        "outcome_text": "MAT.6.1.5. Gerçek yaşam durumlarında ondalık gösterimlerin basamak değerlerini kesirlerden yararlanarak yorumlayabilme • MAT.6.1.6. Kesir ve bölme işlemi arasındaki ilişkiye yönelik tümevarımsal akıl yürütebilme.",
        "process_items": [
            "Ondalık gösterimleri kesir toplamlarıyla çözümler.",
            "Kesir çizgisinin bölme işlemi anlamına geldiğini fark eder.",
            "Payı paydaya bölerek sonlu ve devirli ondalık örüntülerini keşfeder."
        ],
        "meb_quote": "Ondalık gösterimleri kesir toplamlarıyla çözümleme ve yuvarlama; paydası 10'un kuvveti olmayan kesirleri uzun bölme ile inceleme, kalanların tekrarından sonlu ve devirli ondalık örüntüleri keşfetme.",
        "sim_steps": [
            {
                "tag": "KESİR ÇÖZÜMLEME",
                "title": "Adım 1: Ondalık Gösterimi Kesirlerle Çözümleme",
                "instruction": "Sürgüyle ondalık sayıyı ayarlayın. Tam kısım ve kesir basamaklarının değerlerini tabloya kaydedin.",
                "hint": "5,408 = 5 + 4/10 + 0/100 + 8/1000.",
                "hypotheses": [
                    {"text": "0 olan basamaklar çözümlemede yazılmayabilir.", "correct": True},
                    {"text": "0 olan basamak sayıyı tanımsız yapar.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Ondalık sayılar tam kısım ve kesir basamaklarının (1/10, 1/100, 1/1000) toplamı olarak ifade edilir.", "correct": True},
                    {"text": "Çözümlemede paydalar daima 100 olmak zorundadır.", "correct": False}
                ],
                "sliderLabel": "Onda Birler Değeri:",
                "min": 1, "max": 9, "defaultVal": 4, "unit": "onda bir",
                "simType": "decimal_grid",
                "hasSecondary": False
            },
            {
                "tag": "KESİR-BÖLME İLİŞKİSİ",
                "title": "Adım 2: Kesir Çizgisi = Bölme İşlemi",
                "instruction": "3 ÷ 4 işlemini kesir çizgisiyle 3/4 olarak yazın ve ondalık karşılığını (0,75) tabloya kaydedin.",
                "hint": "a/b kesri, 'a doğal sayısının b doğal sayısına bölünmesi' anlamına gelir.",
                "hypotheses": [
                    {"text": "Her kesir payın paydaya bölünmesiyle bir ondalık sayıya dönüştürülebilir.", "correct": True},
                    {"text": "Küçük sayı büyük sayıya bölünemez.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Kesir çizgisi bölme işlemi anlamına gelir: a/b = a ÷ b.", "correct": True},
                    {"text": "Bölme işlemi ile kesir tamamen alakasızdır.", "correct": False}
                ],
                "sliderLabel": "Pay Değeri (Pay ÷ 4):",
                "min": 1, "max": 8, "defaultVal": 3, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": False
            },
            {
                "tag": "SONLU ONDALIK ÖRÜNTÜSÜ",
                "title": "Adım 3: Kalanın Sıfır Olduğu Sonlu Ondalıklar",
                "instruction": "5 ÷ 8 işlemini uzun bölmeyle yapın. Kalanın bir noktada sıfır olduğunu ve bölmenin bittiğini (0,625) gözlemleyin.",
                "hint": "Bölme işleminde kalan 0 olduğunda bölme sonlanır ve elde edilen sayıya 'sonlu ondalık gösterim' denir.",
                "hypotheses": [
                    {"text": "Kalan 0 olduğunda ondalık gösterim sonludur (virgülden sonraki basamaklar biter).", "correct": True},
                    {"text": "Her bölme işlemi sonsuza kadar sürer.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Pay paydaya bölündüğünde kalan 0 oluyorsa ondalık gösterim SONLUDUR (Örn: 5/8 = 0,625).", "correct": True},
                    {"text": "Sonlu ondalıkların paydası daima tektir.", "correct": False}
                ],
                "sliderLabel": "Pay:",
                "min": 1, "max": 7, "defaultVal": 5, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": False
            },
            {
                "tag": "DEVİRLİ ONDALIK ÖRÜNTÜSÜ",
                "title": "Adım 4: Kalanların Tekrarı ve Devirli Ondalık",
                "instruction": "2 ÷ 3 işlemini yapın. Kalanların sürekli 2 olarak tekrar ettiğini ve virgülden sonra 6 rakamının sonsuza kadar gittiğini (0,666... = 0,6̄) inceleyin.",
                "hint": "Kalan hiçbir zaman 0 olmuyor ve periyodik olarak tekrar ediyorsa sayı 'devirli ondalık gösterim'dir.",
                "hypotheses": [
                    {"text": "Kalanlar periyodik tekrar ediyorsa virgülden sonraki rakamlar devir çizgisiyle gösterilir.", "correct": True},
                    {"text": "Devirli sayılar hesaplanamaz, tanımsızdır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bölme işleminde kalan 0 olmuyor ve aynı rakamlar periyodik tekrarlıyorsa DEVİRLİ ONDALIK GÖSTERİM oluşur (2/3 = 0,6̄).", "correct": True},
                    {"text": "Devirli sayılarda virgülden sonra yalnız tek basamak vardır.", "correct": False}
                ],
                "sliderLabel": "Pay (Pay ÷ 3):",
                "min": 1, "max": 5, "defaultVal": 2, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": False
            }
        ]
    },

    # 6. SINIF 7. HAFTA (YENİ MODÜL)
    {
        "grade": 6,
        "week": 7,
        "title": "Kesir-Bölme İlişkisi ve Devirli Ondalık Kart Eşleştirme Atölyesi",
        "date": "26–30 Ekim",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (2)",
        "outcome_code": "MAT.6.1.6",
        "outcome_text": "Kesir ve bölme işlemi arasındaki ilişkiye yönelik tümevarımsal akıl yürütebilme.",
        "process_items": [
            "Kesir ve bölme işlemi arasındaki ilişkiye yönelik varsayımda bulunur.",
            "Uzun bölme ve hesap makinesiyle örüntüleri inceler.",
            "Sonlu ve devirli ondalık kartlarını eşleştirir.",
            "Paydaya göre tümevarımsal genelleme yapar."
        ],
        "meb_quote": "Paydası 10'un kuvveti olmayan kesirleri uzun bölme ve hesap makinesi ile inceleme, kalanların tekrarından sonlu ve devirli ondalık örüntüleri keşfetme, 'Kartların yerinden nasıl emin oluruz?' sayı/görsel kart eşleştirmesi.",
        "sim_steps": [
            {
                "tag": "BÖLME İLE KESİR DÖNÜŞÜMÜ",
                "title": "Adım 1: Payı Paydaya Bölme Laboratuvarı",
                "instruction": "Farklı kesirleri (pay ve payda) sürgülerle ayarlayın. Uzun bölme sonucundaki ondalık açılımı ve kalanı gözlem tablosuna kaydedin.",
                "hint": "Bir kesrin değerini bulmak için payı paydaya böleriz. Bölünmeyen yerde bölüme virgül konur ve kalanın yanına 0 eklenir.",
                "hypotheses": [
                    {"text": "Her kesir bölme işlemi yapılarak mutlaka ya sonlu ya da devirli bir ondalık sayıya dönüşür.", "correct": True},
                    {"text": "Bazı kesirler hiçbir ondalık sayıya dönüştürülemez.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Her kesir payın paydaya bölünmesiyle bir ondalık gösterim verir; bu gösterim ya SONLU ya da DEVİRLİDİR.", "correct": True},
                    {"text": "Tüm kesirler tam sayı çıkar.", "correct": False}
                ],
                "sliderLabel": "Pay (a):",
                "min": 1, "max": 9, "defaultVal": 3, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": True,
                "sliderLabel2": "Payda (b):",
                "min2": 2, "max2": 11, "defaultVal2": 4, "unit2": "payda"
            },
            {
                "tag": "PAYDA ASAL ÇARPANLARI",
                "title": "Adım 2: Sonlu vs Devirli Payda Kuralı",
                "instruction": "Paydaları 2, 4, 5, 8, 10 olan kesirler ile paydaları 3, 6, 7, 9, 11 olan kesirleri karşılaştırıp tabloya kaydedin.",
                "hint": "En sade haldeki bir kesrin paydasının asal çarpanlarında YALNIZCA 2 ve/veya 5 varsa sonlu; 2 ve 5 dışında başka bir asal (3, 7, 11...) varsa devirli olur!",
                "hypotheses": [
                    {"text": "Paydada 2 ve 5 dışında bir asal çarpan varsa ondalık açılım mutlaka devirli olur.", "correct": True},
                    {"text": "Sayının sonlu veya devirli olması tamamen payın büyüklüğüne bağlıdır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Sadeleşmiş kesrin paydasının asal çarpanları sadece 2 ve 5 ise SONLU; 2 ve 5 dışında asal çarpan varsa DEVİRLİ ondalık açılım oluşur.", "correct": True},
                    {"text": "Tüm tek paydalı kesirler sonludur.", "correct": False}
                ],
                "sliderLabel": "Pay:",
                "min": 1, "max": 8, "defaultVal": 5, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": True,
                "sliderLabel2": "Payda:",
                "min2": 2, "max2": 12, "defaultVal2": 6, "unit2": "payda"
            },
            {
                "tag": "DEVİR ÇİZGİSİ GÖSTERİMİ",
                "title": "Adım 3: Devir Çizgisinin Anlamı ve Yazılışı",
                "instruction": "Devreden rakamların üzerine konulan devir çizgisini inceleyin: 5/9 = 0,555... = 0,5̄ ; 7/6 = 1,1666... = 1,16̄.",
                "hint": "Devir çizgisi sadece tekrar eden (devreden) rakam veya rakam grubunun üzerine çekilir.",
                "hypotheses": [
                    {"text": "Devir çizgisi yalnız periyodik olarak tekrar eden rakamların üzerine konulur.", "correct": True},
                    {"text": "Devir çizgisi sayının tamamının üzerine konur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Ondalık açılımda periyodik olarak tekrar eden basamağın üzerine devir çizgisi (-) çekilerek gösterilir.", "correct": True},
                    {"text": "Devir çizgisi sayının negatif olduğunu gösterir.", "correct": False}
                ],
                "sliderLabel": "Pay:",
                "min": 1, "max": 8, "defaultVal": 7, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": True,
                "sliderLabel2": "Payda:",
                "min2": 3, "max2": 11, "defaultVal2": 9, "unit2": "payda"
            },
            {
                "tag": "KART EŞLEŞTİRME",
                "title": "Adım 4: 'Kartların Yerinden Nasıl Emin Oluruz?'",
                "instruction": "Kesir kartları ile ondalık gösterim kartlarını eşleştirin: 1/2 = 0,5 ; 1/3 = 0,3̄ ; 1/4 = 0,25 ; 1/5 = 0,2 ; 1/6 = 0,16̄.",
                "hint": "Eşleştirme yaparken paydanın 10, 100, 1000 yapılıp yapılamadığına veya bölme işlemine dikkat edin.",
                "hypotheses": [
                    {"text": "Paydası genişletilerek 10, 100 veya 1000 yapılabilen kesirler doğrudan sonlu ondalık gösterim verir.", "correct": True},
                    {"text": "Hiçbir kesir ondalık kartıyla tam eşleşmez.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Genişletilerek paydası 10'un kuvveti yapılanlar sonlu; yapılamayanlar ise bölme ile devirli olarak eşleştirilir.", "correct": True},
                    {"text": "Bütün kesirler virgülsüz tam sayıdır.", "correct": False}
                ],
                "sliderLabel": "Kart No:",
                "min": 1, "max": 6, "defaultVal": 3, "unit": "kart",
                "simType": "fraction_division",
                "hasSecondary": False
            }
        ],
        "mini_tasks": [
            {
                "id": 1,
                "tag": "KESİR-BÖLME İLİŞKİSİ",
                "question": "Bir sürahideki 3 litre limonata 4 bardağa eşit paylaştırıldığında her bardağa kaç litre limonata düşer?",
                "options": [
                    {"label": "A) 3 ÷ 4 = 3/4 = 0,75 litre", "correct": True},
                    {"label": "B) 4 ÷ 3 = 1,33 litre", "correct": False},
                    {"label": "C) 0,5 litre", "correct": False}
                ]
            },
            {
                "id": 2,
                "tag": "DEVİRLİ ONDALIK GÖSTERİM",
                "question": "5/9 kesrinin bölme işlemi yapılarak bulunan ondalık gösterimi hangisidir?",
                "options": [
                    {"label": "A) 0,5 (Sonlu)", "correct": False},
                    {"label": "B) 0,555... = 0,5̄ (Devirli)", "correct": True},
                    {"label": "C) 1,8", "correct": False}
                ]
            },
            {
                "id": 3,
                "tag": "PAYDA ANALİZİ VE SONLU ONDALIK",
                "question": "Aşağıdaki kesirlerden hangisinin ondalık gösterimi devirli DEĞİL, SONLUDUR?",
                "options": [
                    {"label": "A) 7/20 (Payda 20 = 2² × 5)", "correct": True},
                    {"label": "B) 5/6 (Paydada 3 asal çarpanı var)", "correct": False},
                    {"label": "C) 4/11", "correct": False}
                ]
            }
        ],
        "extra_questions": [
            {
                "id": 1,
                "tag": "YENİ NESİL • GERÇEK YAŞAM PAYLAŞIM VE BÖLME",
                "scenario": "Bir pastanedeki 7 kg fıstıklı baklava, 8 eşit pakete bölünerek satışa hazırlanacaktır.",
                "stem": "Her bir pakette kaç kilogram baklava bulunduğunu gösteren kesir ve ondalık gösterim ikilisi hangisidir?",
                "choices": [
                    "7/8 kg = 0,875 kg",
                    "8/7 kg = 1,14 kg",
                    "7/8 kg = 0,78 kg",
                    "7/8 kg = 0,85 kg"
                ],
                "correctIndex": 0,
                "explanation": "7 kg 8 pakete bölündüğünde paket başına 7 ÷ 8 = 7/8 kg düşer. 7'yi 8'e böldüğümüzde 7 ÷ 8 = 0,875 kg bulunur."
            },
            {
                "id": 2,
                "tag": "YENİ NESİL • DEVİRLİ SAYI VE DEVİR ÇİZGİSİ",
                "scenario": "Ece hesap makinesinde 8 ÷ 6 işlemini yaptığında ekranda 1.333333333 sayısı çıkmıştır.",
                "stem": "Ece'nin bulduğu sonucun matematiksel sembollerle devir çizgisi kullanılarak gösterimi hangisidir?",
                "choices": [
                    "1,3̄",
                    "1,33",
                    "1̄,3",
                    "1,33̄"
                ],
                "correctIndex": 0,
                "explanation": "8 ÷ 6 = 4/3 = 1,333... olduğundan tam kısım 1, virgülden sonra tekrar eden rakam 3'tür. Dolayısıyla 3'ün üzerine devir çizgisi konur: 1,3̄."
            },
            {
                "id": 3,
                "tag": "YENİ NESİL • PAYDANIN ASAL ÇARPANLARI KURALI",
                "scenario": "Matematik öğretmeni tahtaya şu kuralı yazıyor: 'En sade haldeki bir kesrin paydası asal çarpanlarına ayrıldığında, çarpanlar arasında YALNIZCA 2 ve/veya 5 varsa bu kesir sonlu ondalık gösterimdir; başka bir asal çarpan varsa devirlidir.'",
                "stem": "Buna göre aşağıdaki kesirlerden hangisi DEVİRLİ bir ondalık gösterime sahiptir?",
                "choices": [
                    "7/12 (12 = 2² × 3 ➔ 3 çarpanı var)",
                    "9/25 (25 = 5²)",
                    "13/40 (40 = 2³ × 5)",
                    "11/16 (16 = 2⁴)"
                ],
                "correctIndex": 0,
                "explanation": "7/12 kesrinin paydası 12 = 2² × 3 olup 2 ve 5 dışında '3' asal çarpanı içerdiğinden devirlidir (7 ÷ 12 = 0,583̄). Diğerlerinin paydaları sadece 2 ve 5 içerir."
            },
            {
                "id": 4,
                "tag": "YENİ NESİL • KART EŞLEŞTİRME OYUNU",
                "scenario": "Bir sınıfta öğrenciler ellerindeki kesir kartlarını uygun ondalık kartlarıyla eşleştirmektedir: K: 1/8, L: 2/3, M: 3/5, N: 5/6.",
                "stem": "Hangi kartların eşleştiği ondalık gösterimler sırasıyla SONLU ve DEVİRLİ olarak doğru gruplandırılmıştır?",
                "choices": [
                    "Sonlu: K (0,125) ve M (0,6) | Devirli: L (0,6̄) ve N (0,83̄)",
                    "Sonlu: L ve N | Devirli: K ve M",
                    "Hepsi sonludur.",
                    "Hepsi devirlidir."
                ],
                "correctIndex": 0,
                "explanation": "1/8 = 0,125 ve 3/5 = 0,6 sonludur. 2/3 = 0,6̄ ve 5/6 = 0,83̄ devirlidir."
            },
            {
                "id": 5,
                "tag": "YENİ NESİL • SAYI DOĞRUSUNDA DEVİRLİ SAYI KONUMU",
                "scenario": "Sayı doğrusunda 0 ile 1 arası 9 eş parçaya bölünmüştür. 0'dan sağa doğru 4. bölme noktasına K harfi yerleştirilmiştir.",
                "stem": "K noktasına karşılık gelen 4/9 kesrinin devirli ondalık gösterimi hangisidir?",
                "choices": [
                    "0,4̄",
                    "0,44",
                    "0,04̄",
                    "0,49"
                ],
                "correctIndex": 0,
                "explanation": "Paydası 9 olan tek basamaklı paylarda k/9 = 0,k̄ kuralı geçerlidir. 4/9 = 0,444... = 0,4̄."
            },
            {
                "id": 6,
                "tag": "YENİ NESİL • KALANLARIN PERİYODİK TEKRARI",
                "scenario": "Ali 5'i 11'e uzun bölme ile bölmektedir. Sırasıyla kalanları 5, 6, 5, 6, 5... olarak bulmaktadır.",
                "stem": "Kalanların bu şekilde periyodik olarak tekrar etmesi bölüm hakkında neyi kesinlikle kanıtlar?",
                "choices": [
                    "Bölümün virgülden sonraki kısmının '45' rakam grubu olarak sonsuza dek devredeceğini (0,45̄).",
                    "İşlemde hata yapıldığını.",
                    "Bölümün sonlu bir sayı olduğunu.",
                    "Sonucun 0'a eşit olduğunu."
                ],
                "correctIndex": 0,
                "explanation": "5 ÷ 11 = 0,454545... = 0,45̄. Kalanlar (5 ve 6) periyodik tekrar ettiği için virgülden sonra 45 periyodik olarak devreder."
            },
            {
                "id": 7,
                "tag": "YENİ NESİL • SADELEŞTİRME TUZAĞI",
                "scenario": "Burak, 9/15 kesrinin paydası 15 olduğu için (15 = 3 × 5) bu kesrin kesinlikle devirli olduğunu iddia ediyor. Öğretmeni ise kesri önce sadeleştirmesini söylüyor.",
                "stem": "9/15 kesri 3 ile sadeleştirildiğinde Burak'ın iddiası hakkında ne söylenebilir?",
                "choices": [
                    "9/15 = 3/5 olur; paydada sadece 5 kaldığı için kesir devirli değil, 0,6 olan SONLU bir sayıdır.",
                    "Burak haklıdır, kesir devirlidir.",
                    "Sadeleştirme sonucu değiştirmez, tanımsızdır.",
                    "Kesir 1'den büyüktür."
                ],
                "correctIndex": 0,
                "explanation": "Kural en sade hal için geçerlidir! 9/15 sadeleştirildiğinde 3/5 olur. Payda 5 olduğundan 3/5 = 6/10 = 0,6 (Sonlu ondalık) çıkar."
            },
            {
                "id": 8,
                "tag": "YENİ NESİL • TARTIDA DİJİTAL GÖSTERGE",
                "scenario": "Bir manavda tartılan 1/3 kg elma dijital ekranda 0.333 kg olarak gösterilmektedir. Müşteri 'Tam 1/3 kg tartmadınız' demektedir.",
                "stem": "Müşterinin bu ifadesinin matematiksel açıklaması nedir?",
                "choices": [
                    "1/3 devirli (0,3̄) bir sayı olduğundan dijital terazi ekrana sığacak kadar yuvarlama yapmıştır; tam değeri 0,333 değildir.",
                    "Terazi bozuktur.",
                    "1/3 kg aslında 0,5 kg'dır.",
                    "Elma ağırlığı kesirle gösterilemez."
                ],
                "correctIndex": 0,
                "explanation": "1/3 = 0,333333... sonsuza gider. Dijital cihazlar sınırlı basamak gösterdiği için devirli sayıları virgülden sonra belirli bir basamakta yuvarlar."
            },
            {
                "id": 9,
                "tag": "YENİ NESİL • YARIŞMA PROBLEMİ",
                "scenario": "Bir bilgi yarışmasında 4 arkadaşa şu kesirler verilmiştir: Ayşe: 3/8, Berk: 7/14, Can: 2/7, Deniz: 11/20. Hangisinin sayısı devirlidir sorusu sorulmuştur.",
                "stem": "Yarışmayı doğru cevaplayan kişi hangisidir?",
                "choices": [
                    "Can (2/7 kesrinin paydası 7 olduğundan devirlidir)",
                    "Ayşe (3/8 = 0,375 sonlu)",
                    "Berk (7/14 = 1/2 = 0,5 sonlu)",
                    "Deniz (11/20 = 0,55 sonlu)"
                ],
                "correctIndex": 0,
                "explanation": "3/8 = 0,375 (sonlu), 7/14 = 1/2 = 0,5 (sonlu), 11/20 = 0,55 (sonlu). 2/7 kesri ise devirlidir (0,285714̄)."
            },
            {
                "id": 10,
                "tag": "YENİ NESİL • DEVİRLİ VE DEVİRSİZ SIRALAMA",
                "scenario": "Tahtaya iki sayı yazılmıştır: A = 0,7 ve B = 0,7̄ (yani 0,777...).",
                "stem": "A ve B sayılarının büyüklük karşılaştırması ve aralarındaki fark hangisinde doğru açıklanmıştır?",
                "choices": [
                    "B > A'dır; çünkü B = 0,777... olup yüzde birler basamağı (7), A'nın yüzde birler basamağından (0) büyüktür.",
                    "A = B'dir.",
                    "A > B'dir.",
                    "Karşılaştırılamaz."
                ],
                "correctIndex": 0,
                "explanation": "A = 0,7000... ve B = 0,7777... Basamak basamak karşılaştırıldığında onda birler eşit (7=7), yüzde birlerde 7 > 0 olduğundan B > A'dır."
            }
        ]
    },
# 6. SINIF 8. HAFTA (YENİ MODÜL)
    {
        "grade": 6,
        "week": 8,
        "title": "Kesir, Ondalık ve Yüzde ile Dört İşlem Problemleri Atölyesi",
        "date": "02–06 Kasım",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (2)",
        "outcome_code": "MAT.6.1.7",
        "outcome_text": "Gerçek yaşam durumlarında karşılaşılan kesir, ondalık ve yüzde gösterimleri ile ilgili dört işlem gerektiren problemleri çözebilme.",
        "process_items": [
            "Kesir, ondalık ve yüzde gösterimleri ile ilgili problemlerde sayı ve işlem bileşenlerini belirler.",
            "Verilenler ile istenenlerin gerektirdiği işlemler arasındaki ilişkiyi belirler.",
            "Probleme uygun strateji oluşturur.",
            "Sonuca ilişkin tahminde bulunur ve işlemi gerçekleştirir."
        ],
        "meb_quote": "Kutup buzullarının erimesi (%5 popülasyon kaybı), karbon salınımı ve aile bütçesi tasarruf bağlamı; alışveriş indirimleri (%25 indirim = 1/4 oran), kesir-ondalık-yüzde dönüşümleriyle dört işlem gerektiren gerçek yaşam problemleri.",
        "sim_steps": [
            {
                "tag": "YÜZDE & KESİR DÖNÜŞÜMÜ",
                "title": "Adım 1: Etiket Fiyatı ve %25 İndirim (1/4 Oran)",
                "instruction": "Etiket fiyatını sürgüyle değiştirin (ör. 200 ₺). %25 (yani 1/4) indirimi hesaplayıp gözlem tablosuna kaydedin.",
                "hint": "%25 indirim = 25/100 = 1/4'tür. 200 ₺'nin 1/4'ü 50 ₺ tasarruftur; ödenen tutar 150 ₺ olur.",
                "hypotheses": [
                    {"text": "Bir sayının %25'ini bulmak o sayıyı 4'e bölmek (1/4 ile çarpmak) ile tamamen aynıdır.", "correct": True},
                    {"text": "%25 indirim fiyattan 25 TL düşmek anlamına gelir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "%25 indirim 1/4 kesrine denktir; etiket fiyatı 4'e bölünerek indirim miktarı, fiyattan çıkarılarak indirimli tutar bulunur.", "correct": True},
                    {"text": "Yüzdelerle işlem yapılırken kesre dönüştürülemez.", "correct": False}
                ],
                "sliderLabel": "Etiket Fiyatı (₺):",
                "min": 100, "max": 800, "defaultVal": 200, "unit": "₺",
                "simType": "fraction_discount_problem",
                "hasSecondary": True,
                "sliderLabel2": "İndirim Oranı (%):",
                "min2": 10, "max2": 50, "defaultVal2": 25, "unit2": "%"
            },
            {
                "tag": "ONDALIK & KESİR İŞLEMİ",
                "title": "Adım 2: Ondalık Çarpma ile İndirim Hesaplama (0,20 Çarpanı)",
                "instruction": "Fiyatı sürgüyle değiştirin ve %20 (0,2) indirim uygulayın. Ondalık gösterimle çarpmanın kesir karşılığını tabloya kaydedin.",
                "hint": "Bir sayının %20'si: Sayı x 0,20 veya Sayı x (20/100) = Sayı / 5.",
                "hypotheses": [
                    {"text": "0,20 ile çarpmak, 2/10 veya 1/5 ile çarpmakla aynı matematiksel sonucu verir.", "correct": True},
                    {"text": "0,20 ile çarpmak sayıyı 20 katına çıkarır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Ondalık çarpan (0,20) ile kesir (1/5) aynı miktarı ifade eder; ikisi de problemi doğru çözüme ulaştırır.", "correct": True},
                    {"text": "Ondalık işlemler kesir problemlerinde kullanılamaz.", "correct": False}
                ],
                "sliderLabel": "Ürün Fiyatı (₺):",
                "min": 100, "max": 1000, "defaultVal": 500, "unit": "₺",
                "simType": "fraction_discount_problem",
                "hasSecondary": True,
                "sliderLabel2": "İndirim Yüzdesi (%):",
                "min2": 10, "max2": 50, "defaultVal2": 20, "unit2": "%"
            },
            {
                "tag": "ÇOK ADIMLI TASARRUF",
                "title": "Adım 3: İki Aşamalı Kampanya ve Net Ödeme",
                "instruction": "İndirim oranını %30 ve %40 yaparak aile bütçesine sağlanan net katkıyı (tasarrufu) gözlem tablosuna kaydedin.",
                "hint": "Tasarruf = Etiket Fiyatı x (Yüzde / 100).",
                "hypotheses": [
                    {"text": "İndirim yüzdesi arttıkça ödenen tutar doğrusal olarak azalır, tasarruf miktarı artar.", "correct": True},
                    {"text": "İndirim oranı fiyattan bağımsız sabit bir değerdir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Ödenen Tutar = Etiket Fiyatı × (1 - Oran/100) bağıntısıyla tek işlemde hesaplanabilir.", "correct": True},
                    {"text": "Yüzdeler toplanıp fiyattan doğrudan sayı olarak çıkarılır.", "correct": False}
                ],
                "sliderLabel": "Alışveriş Sepeti (₺):",
                "min": 200, "max": 1200, "defaultVal": 600, "unit": "₺",
                "simType": "fraction_discount_problem",
                "hasSecondary": True,
                "sliderLabel2": "Kampanya Oranı (%):",
                "min2": 10, "max2": 50, "defaultVal2": 30, "unit2": "%"
            },
            {
                "tag": "GERÇEK YAŞAM VE BÜTÇE",
                "title": "Adım 4: %50 Sezon Sonu İndirimi (Yarı Fiyat 1/2)",
                "instruction": "%50 indirim oranını test edin. 1/2 kesri, 0,50 ondalığı ve %50 yüzdesinin denkliklerini kaydedin.",
                "hint": "1/2 = 0,50 = %50. Ürünün fiyatı tam yarıya iner.",
                "hypotheses": [
                    {"text": "%50 indirim doğrudan sayıyı 2'ye bölmek (yarıya indirmek) demektir.", "correct": True},
                    {"text": "%50 indirimde ürün bedava olur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "%50 = 0,50 = 1/2 denklikleri sayesinde hesaplamalar zihinden yarıya bölme stratejisiyle hızla yapılabilir.", "correct": True},
                    {"text": "%50 indirimi hesaplamak için mutlaka 100'e bölüp 50 ile çarpmak gerekir.", "correct": False}
                ],
                "sliderLabel": "Mont Fiyatı (₺):",
                "min": 300, "max": 1500, "defaultVal": 800, "unit": "₺",
                "simType": "fraction_discount_problem",
                "hasSecondary": True,
                "sliderLabel2": "İndirim Oranı (%):",
                "min2": 10, "max2": 50, "defaultVal2": 50, "unit2": "%"
            }
        ],
        "mini_tasks": [
            {
                "id": 1,
                "tag": "YÜZDE-KESİR DÖNÜŞÜMÜ",
                "question": "400 TL olan bir ayakkabı %25 indirimle satılmaktadır. Bu indirim kaç TL'ye karşılık gelir?",
                "options": [
                    {"label": "A) 400 ÷ 4 = 100 TL", "correct": True},
                    {"label": "B) 25 TL", "correct": False},
                    {"label": "C) 75 TL", "correct": False}
                ]
            },
            {
                "id": 2,
                "tag": "ONDALIKLA İNDİRİM HESABI",
                "question": "600 TL'lik elektrik faturasında %10 enerji tasarrufu sağlayan bir aile kaç TL öder?",
                "options": [
                    {"label": "A) 600 - 60 = 540 TL", "correct": True},
                    {"label": "B) 500 TL", "correct": False},
                    {"label": "C) 590 TL", "correct": False}
                ]
            },
            {
                "id": 3,
                "tag": "ÇOKLU TEMSİL DENKLİĞİ",
                "question": "'3/5' kesrinin yüzde ve ondalık gösterimi sırasıyla hangisidir?",
                "options": [
                    {"label": "A) 0,60 ve %60", "correct": True},
                    {"label": "B) 0,35 ve %35", "correct": False},
                    {"label": "C) 0,30 ve %50", "correct": False}
                ]
            }
        ],
        "extra_questions": [
            {
                "id": 1,
                "tag": "YENİ NESİL • ÇEVRESEL SÜRDÜRÜLEBİLİRLİK VE BUZULLAR",
                "scenario": "MEB TYMM sürdürülebilirlik araştırmasına göre, kutup bölgesindeki her 1000 kilometrekarelik buzul erimesi kutup foklarının popülasyonunda %5 azalmaya neden olmaktadır.",
                "stem": "Başlangıçta 4000 birey olan bir fok popülasyonu, 1000 km² buzul eridiğinde kaç bireye düşer?",
                "choices": [
                    "3800 birey (4000'in %5'i = 200 azalma)",
                    "3950 birey",
                    "3600 birey",
                    "3500 birey"
                ],
                "correctIndex": 0,
                "explanation": "4000 x (5/100) = 200 birey azalır. Kalan popülasyon: 4000 - 200 = 3800 bireydir."
            },
            {
                "id": 2,
                "tag": "YENİ NESİL • AİLE BÜTÇESİ VE TASARRUF",
                "scenario": "Bir ailenin aylık geliri 32.000 TL'dir. Aile bütçesinin 1/4'ünü ev kirasına, %30'unu gıda harcamalarına, 0,15'ini ise faturalara ayırmaktadır.",
                "stem": "Bu ailenin kira, gıda ve fatura dışındaki diğer harcamaları ve tasarrufu için geriye kaç TL kalır?",
                "choices": [
                    "9.600 TL (%30'u kalır)",
                    "8.000 TL",
                    "10.200 TL",
                    "11.400 TL"
                ],
                "correctIndex": 0,
                "explanation": "Kira = 1/4 = %25, Gıda = %30, Fatura = 0,15 = %15. Toplam harcama = %25 + %30 + %15 = %70. Kalan oran = %100 - %70 = %30. 32.000 x 0,30 = 9.600 TL kalır."
            },
            {
                "id": 3,
                "tag": "YENİ NESİL • KİTAP FUARI KAMPANYASI",
                "scenario": "Bir kitap fuarında etiket fiyatı 120 TL olan romanlarda %20 indirim, 80 TL olan bilim kitaplarında ise 1/4 oranında indirim uygulanmaktadır.",
                "stem": "1 roman ve 1 bilim kitabı alan bir öğrenci kasada toplam kaç TL öder?",
                "choices": [
                    "156 TL (Roman: 96 TL, Bilim: 60 TL)",
                    "160 TL",
                    "150 TL",
                    "144 TL"
                ],
                "correctIndex": 0,
                "explanation": "Roman indirimi = 120 x 0,20 = 24 TL ➔ 120 - 24 = 96 TL. Bilim kitabı indirimi = 80 x (1/4) = 20 TL ➔ 80 - 20 = 60 TL. Toplam ödeme = 96 + 60 = 156 TL."
            },
            {
                "id": 4,
                "tag": "YENİ NESİL • SU TÜKETİMİ VE DAMLA TASARRUFU",
                "scenario": "Günde ortalama 250 litre su tüketen bir evde, musluklara takılan perlatörler sayesinde su tüketiminde 0,12 oranında (yüzde 12) tasarruf sağlanmıştır.",
                "stem": "Bu evde 30 günde (bir ayda) toplam kaç litre su tasarrufu edilmiş olur?",
                "choices": [
                    "900 litre (Günde 30 L x 30 gün)",
                    "750 litre",
                    "600 litre",
                    "1200 litre"
                ],
                "correctIndex": 0,
                "explanation": "Günlük tasarruf: 250 x 0,12 = 30 litre. 30 günde tasarruf: 30 x 30 = 900 litredir."
            },
            {
                "id": 5,
                "tag": "YENİ NESİL • ELEKTRONİK MAĞAZASI ÇİFT İNDİRİM",
                "scenario": "Etiket fiyatı 2400 TL olan bir tablette önce %10 sezon indirimi yapılıyor, ardından indirimli fiyat üzerinden nakit ödemede 1/10 oranında ek indirim uygulanıyor.",
                "stem": "Bu tableti nakit alan bir müşteri kaç TL öder?",
                "choices": [
                    "1944 TL",
                    "1920 TL",
                    "2000 TL",
                    "1880 TL"
                ],
                "correctIndex": 0,
                "explanation": "1. indirim: 2400 x 0,10 = 240 TL ➔ 2400 - 240 = 2160 TL. 2. indirim: 2160 x (1/10) = 216 TL ➔ 2160 - 216 = 1944 TL."
            },
            {
                "id": 6,
                "tag": "YENİ NESİL • GÖRECELİ ORAN KARŞILAŞTIRMA",
                "scenario": "A mağazası 500 TL'lik cekette 150 TL indirim; B mağazası ise 400 TL'lik aynı cekette %30 indirim yapmaktadır.",
                "stem": "Hangi mağazada indirim oranı yüzde olarak daha fazladır?",
                "choices": [
                    "İkisi de eşittir (%30)",
                    "A mağazası daha fazladır",
                    "B mağazası daha fazladır",
                    "Karşılaştırılamaz"
                ],
                "correctIndex": 0,
                "explanation": "A mağazası oranı: 150 / 500 = 3/10 = %30. B mağazası oranı da %30'dur. Her iki mağazada da indirim oranı eşittir."
            },
            {
                "id": 7,
                "tag": "YENİ NESİL • SIVI VE KARIŞIM ORANI",
                "scenario": "600 gramlık bir meyve suyunun 2/5'i portakal, %35'i elma suyu ve geri kalanı sudur.",
                "stem": "Bu karışımda kaç gram su bulunmaktadır?",
                "choices": [
                    "150 gram (%25 su)",
                    "120 gram",
                    "180 gram",
                    "200 gram"
                ],
                "correctIndex": 0,
                "explanation": "Portakal = 2/5 = %40. Elma = %35. Toplam meyve = %40 + %35 = %75. Su oranı = %100 - %75 = %25. Su miktarı = 600 x 0,25 = 150 gramdır."
            },
            {
                "id": 8,
                "tag": "YENİ NESİL • GERİ DÖNÜŞÜM VE KAĞIT",
                "scenario": "1 ton atık kağıdın geri dönüştürülmesi ile 17 ağacın kesilmesi önlenmektedir. Bir okul kampanyasında 2500 kg (2,5 ton) atık kağıt toplanmıştır.",
                "stem": "Bu okul kaç ağacın kesilmesini önlemiştir?",
                "choices": [
                    "42,5 ağaç (yaklaşık 42-43 ağaç)",
                    "34 ağaç",
                    "51 ağaç",
                    "68 ağaç"
                ],
                "correctIndex": 0,
                "explanation": "2,5 ton x 17 ağaç/ton = 42,5 ağaç kurtarılmıştır."
            },
            {
                "id": 9,
                "tag": "YENİ NESİL • YOL VE HIZ PROBLEMİNDE KESİR",
                "scenario": "450 km'lik bir yolun 1/3'ünü saatte 75 km hızla giden bir araç, kalan yolun %60'ını saatte 90 km hızla gitmiştir.",
                "stem": "Aracın bu iki bölümde toplam harcadığı sürüş süresi kaç saattir?",
                "choices": [
                    "4 saat (150/75 = 2 sa, 180/90 = 2 sa)",
                    "3,5 saat",
                    "4,5 saat",
                    "5 saat"
                ],
                "correctIndex": 0,
                "explanation": "1. bölüm: 450 x (1/3) = 150 km ➔ Süre: 150 ÷ 75 = 2 saat. Kalan yol = 300 km. 2. bölüm: 300 x 0,60 = 180 km ➔ Süre: 180 ÷ 90 = 2 saat. Toplam süre = 2 + 2 = 4 saat."
            },
            {
                "id": 10,
                "tag": "YENİ NESİL • MARKET SEPETİ VE KDV ORANI",
                "scenario": "Bir market alışverişinde temel gıda maddelerine %1 KDV, temizlik ürünlerine ise %20 KDV uygulanmaktadır. 300 TL'lik gıda ve 200 TL'lik temizlik ürünü alınmıştır.",
                "stem": "Alışverişte ödenen toplam KDV tutarı kaç TL'dir?",
                "choices": [
                    "43 TL (Gıda KDV: 3 TL, Temizlik KDV: 40 TL)",
                    "35 TL",
                    "50 TL",
                    "60 TL"
                ],
                "correctIndex": 0,
                "explanation": "Gıda KDV = 300 x 0,01 = 3 TL. Temizlik KDV = 200 x 0,20 = 40 TL. Toplam KDV = 3 + 40 = 43 TL'dir."
            }
        ]
    },

    # 6. SINIF 9. HAFTA (YENİ MODÜL)
    {
        "grade": 6,
        "week": 9,
        "title": "Çoklu Temsillerle Problem Çözme ve Modelleme Atölyesi",
        "date": "09–13 Kasım",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (2)",
        "outcome_code": "MAT.6.1.7",
        "outcome_text": "Gerçek yaşam durumlarında karşılaşılan kesir, ondalık ve yüzde gösterimleri ile ilgili dört işlem gerektiren problemleri çözebilme.",
        "process_items": [
            "Problem bağlamına uygun temsilleri (şekil, tablo, diyagram) kullanır.",
            "Kullanılan temsil üzerinden problemi kendi ifadeleri ile açıklar.",
            "Alternatif stratejileri inceler ve çözüm yolunu kontrol eder.",
            "Çözüme ulaştıran stratejileri geneller."
        ],
        "meb_quote": "Parça-bütün şeritleri, 10x10 kareli alan modelleri ve sayı doğrusu diyagramları kullanarak kesir, ondalık ve yüzde dönüşümlü problem çözme; karbon ayak izi, su tasarrufu ve akıllı tüketici modelleri.",
        "sim_steps": [
            {
                "tag": "ŞERİT VE DİYAGRAM MODELİ",
                "title": "Adım 1: Parça-Bütün Şeridiyle Modelleme",
                "instruction": "Toplam bütçeyi sürgüyle belirleyin (ör. 600 ₺). Şerit üzerinde farklı harcama oranlarını (%15, %25, %40) deneyerek tabloya kaydedin.",
                "hint": "Bir bütünün farklı kesirlerini tek bir şerit üzerinde renkli bloklarla temsil edebilirsiniz.",
                "hypotheses": [
                    {"text": "Bütünün parçalarını gösteren şerit modellerinde tüm yüzdelerin toplamı daima %100 (1 tam) eder.", "correct": True},
                    {"text": "Şerit modelinde yüzdelerin toplamı fiyata göre değişir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Parça-bütün şerit modeli problemin görselleştirilmesini sağlar; harcamaların toplamı 1 tamdan (veya %100'den) çıkarılarak kalan bulunur.", "correct": True},
                    {"text": "Şerit modeli yalnızca çıkarma işlemlerinde çalışır.", "correct": False}
                ],
                "sliderLabel": "Toplam Bütçe (₺):",
                "min": 200, "max": 1000, "defaultVal": 600, "unit": "₺",
                "simType": "fraction_discount_problem",
                "hasSecondary": True,
                "sliderLabel2": "Tasarruf Oranı (%):",
                "min2": 10, "max2": 50, "defaultVal2": 30, "unit2": "%"
            },
            {
                "tag": "TABLO TEMSİLİ",
                "title": "Adım 2: Tablo Temsili ile Karşılaştırmalı Problem Çözme",
                "instruction": "Farklı marketlerdeki indirim oranlarını (%10, %20, %35) tabloya kaydedip en avantajlı seçeneği belirleyin.",
                "hint": "Tablo temsili, birden çok veriyi organize etmeyi ve karşılaştırmayı kolaylaştırır.",
                "hypotheses": [
                    {"text": "Tablo kullanımı, işlem adımlarının kontrol edilmesini ve en ekonomik seçeneğin doğrudan görülmesini sağlar.", "correct": True},
                    {"text": "Tablo çizmek hesaplama sonucunu değiştirir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Tablo temsili veriler arasındaki ilişkileri somutlaştırır; birim fiyat ve indirim miktarı karşılaştırmasında en verimli stratejidir.", "correct": True},
                    {"text": "Tablolar problem çözmeyi zorlaştırır.", "correct": False}
                ],
                "sliderLabel": "Ürün Fiyatı (₺):",
                "min": 150, "max": 900, "defaultVal": 450, "unit": "₺",
                "simType": "fraction_discount_problem",
                "hasSecondary": True,
                "sliderLabel2": "Seçilen İndirim (%):",
                "min2": 10, "max2": 50, "defaultVal2": 20, "unit2": "%"
            },
            {
                "tag": "ALAN MODELİ (10x10)",
                "title": "Adım 3: 100'lük Izgarada Yüzde ve Kesir Birleşimi",
                "instruction": "100 birimkarelik ızgara üzerinde %45'lik alanı modelleyin. Ondalık (0,45) ve kesir (9/20) karşılıklarını tabloya kaydedin.",
                "hint": "100 küçük karenin 45 tanesini boyamak %45 = 0,45 = 45/100 = 9/20 anlamına gelir.",
                "hypotheses": [
                    {"text": "10x10 kareli alan modeli, yüzde ile ondalık ve kesir arasındaki geçişi doğrudan somutlaştırır.", "correct": True},
                    {"text": "100'lük ızgarada sadece tam sayılar gösterilebilir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "10x10 alan modeli, bir problemdeki payda eşitleme ve yüzde hesaplamalarını zihinsel olarak hızlandıran temel bir geometrik temsildir.", "correct": True},
                    {"text": "Alan modeli kesirlerde kullanılmaz.", "correct": False}
                ],
                "sliderLabel": "Boya Miktarı (Kare Sayısı):",
                "min": 10, "max": 90, "defaultVal": 45, "unit": "kare",
                "simType": "decimal_grid",
                "hasSecondary": False
            },
            {
                "tag": "GENELLEME & STRATEJİ",
                "title": "Adım 4: Geriye Doğru Çalışma Stratejisi",
                "instruction": "İndirimden sonraki fiyatı bilinen bir ürünün orijinal etiket fiyatını bulma sürecini inceleyin ve tabloya kaydedin.",
                "hint": "%20 indirimli hali 240 TL olan ürünün %80'i 240 TL'dir. Tamamı (240 ÷ 80) x 100 = 300 TL'dir.",
                "hypotheses": [
                    {"text": "Parçadan bütüne giderken (geriye doğru çalışma), verilen tutar kalan yüzde oranına bölünerek 1 birim (%1) bulunur.", "correct": True},
                    {"text": "Geriye doğru çalışırken indirimli fiyata doğrudan %20 eklenir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "İndirimli fiyattan orijinal fiyata ulaşırken doğrudan yüzde eklenemez; kalan yüzdeye bölünüp 100 ile çarpılmalıdır.", "correct": True},
                    {"text": "240 TL'ye %20 eklenirse tam 300 TL eder.", "correct": False}
                ],
                "sliderLabel": "İndirimli Son Fiyat (₺):",
                "min": 80, "max": 720, "defaultVal": 240, "unit": "₺",
                "simType": "fraction_discount_problem",
                "hasSecondary": True,
                "sliderLabel2": "Uygulanmış İndirim (%):",
                "min2": 10, "max2": 50, "defaultVal2": 20, "unit2": "%"
            }
        ],
        "mini_tasks": [
            {
                "id": 1,
                "tag": "GERİYE DOĞRU ÇALIŞMA",
                "question": "%20 indirimli fiyatı 160 TL olan bir pantolonun indirimden önceki fiyatı kaç TL'dir?",
                "options": [
                    {"label": "A) %80'i 160 TL ise tamamı 200 TL'dir.", "correct": True},
                    {"label": "B) 160 + 20 = 180 TL", "correct": False},
                    {"label": "C) 192 TL", "correct": False}
                ]
            },
            {
                "id": 2,
                "tag": "TEMSİL DÖNÜŞÜMÜ",
                "question": "Bir çiftçi tarlasının 3/8'ine buğday, %25'ine mısır ekmiştir. Geriye kalan alan tarlanın kaçta kaçıdır?",
                "options": [
                    {"label": "A) 3/8 (Çünkü %25 = 2/8, 3/8 + 2/8 = 5/8, kalan 3/8)", "correct": True},
                    {"label": "B) 1/8", "correct": False},
                    {"label": "C) 1/2", "correct": False}
                ]
            },
            {
                "id": 3,
                "tag": "BÜTÇE DİYAGRAMI",
                "question": "Maaşının 0,35'ini birikime ayıran bir mühendis, maaşı 40.000 TL ise kaç TL biriktirir?",
                "options": [
                    {"label": "A) 40.000 x 0,35 = 14.000 TL", "correct": True},
                    {"label": "B) 12.000 TL", "correct": False},
                    {"label": "C) 16.000 TL", "correct": False}
                ]
            }
        ],
        "extra_questions": [
            {
                "id": 1,
                "tag": "YENİ NESİL • GERİYE DOĞRU ÇALIŞMA MUHAKEMESİ",
                "scenario": "Bir kırtasiyede tüm sırt çantalarına %30 sezon sonu indirimi uygulanıyor. Bir çantayı indirimli olarak 280 TL'ye satın alan Kerem, arkadaşına bu çantayı indirimden önce alsaydı kaç TL ödeyeceğini anlatıyor.",
                "stem": "Çantanın indirimden önceki etiket fiyatı kaç TL'dir?",
                "choices": [
                    "400 TL (%70'i 280 TL ise tamamı 400 TL)",
                    "350 TL",
                    "364 TL",
                    "420 TL"
                ],
                "correctIndex": 0,
                "explanation": "Ürünün %30 indirimli fiyatı, etiket fiyatının %70'ine eşittir. %70'i 280 TL ise %1'i 280 / 70 = 4 TL'dir. Tamamı (%100) 4 x 100 = 400 TL'dir."
            },
            {
                "id": 2,
                "tag": "YENİ NESİL • ÇOKLU TEMSİLLİ ÇİFTLİK PROBLEMİ",
                "scenario": "Bir organik çiftlikte 1200 dönümlük arazinin 0,30'una zeytinlik kurulmuş, 1/4'üne lavanta dikilmiş, geri kalan alanın ise %50'sine güneş enerjisi panelleri yerleştirilmiştir.",
                "stem": "Güneş enerjisi panelleri kurulan alan kaç dönümdür?",
                "choices": [
                    "270 dönüm (Kalan 540 dönümün %50'si)",
                    "300 dönüm",
                    "240 dönüm",
                    "360 dönüm"
                ],
                "correctIndex": 0,
                "explanation": "Zeytinlik = 1200 x 0,30 = 360 dönüm. Lavanta = 1200 x 1/4 = 300 dönüm. Toplam = 660 dönüm. Kalan = 1200 - 660 = 540 dönüm. Güneş paneli = 540 x %50 = 270 dönümdür."
            },
            {
                "id": 3,
                "tag": "YENİ NESİL • ENERJİ VERİMLİLİĞİ VE FATURA",
                "scenario": "A sınıfı bir buzdolabı kullanan bir aile, eski buzdolabına göre ayda 45 kilovatsaat (kWh) daha az elektrik tüketmektedir. Elektriğin 1 kWh birim fiyatı 2,40 TL'dir.",
                "stem": "Bu aile yeni buzdolabı sayesinde 1 yılda (12 ayda) elektrik faturasından toplam kaç TL tasarruf eder?",
                "choices": [
                    "1296 TL (Ayda 108 TL x 12 ay)",
                    "1200 TL",
                    "1180 TL",
                    "1350 TL"
                ],
                "correctIndex": 0,
                "explanation": "Aylık tasarruf = 45 x 2,40 = 108 TL. Yıllık tasarruf = 108 x 12 = 1296 TL'dir."
            },
            {
                "id": 4,
                "tag": "YENİ NESİL • AKILLI ALIŞVERİŞ VE 3 AL 2 ÖDE",
                "scenario": "Bir markette tanesi 60 TL olan şampuanlarda '3 Al 2 Öde' kampanyası vardır. Yan markette ise aynı şampuan tekli alımlarda %30 indirimle satılmaktadır.",
                "stem": "3 adet şampuan almak isteyen bir tüketici hangi seçenekte kaç TL daha az öder?",
                "choices": [
                    "3 Al 2 Öde kampanyasında 6 TL daha az öder (120 TL vs 126 TL)",
                    "İki seçenek de aynı tutardadır",
                    "%30 indirimli markette 10 TL daha az öder",
                    "3 Al 2 Öde kampanyasında 15 TL daha az öder"
                ],
                "correctIndex": 0,
                "explanation": "1. market (3 al 2 öde): 2 x 60 = 120 TL. 2. market (%30 indirim): 60 x 0,70 = 42 TL ➔ 3 x 42 = 126 TL. 1. market 126 - 120 = 6 TL daha ucuzdur."
            },
            {
                "id": 5,
                "tag": "YENİ NESİL • SU DEPOSU VE KADEMELİ BOŞALMA",
                "scenario": "Tamamı 800 litre su alan bir deponun önce 3/10'u bahçe sulamada kullanılıyor. Daha sonra kalan suyun %40'ı temizlik için harcanıyor.",
                "stem": "Son durumda depoda kaç litre su kalmıştır?",
                "choices": [
                    "336 litre",
                    "320 litre",
                    "350 litre",
                    "280 litre"
                ],
                "correctIndex": 0,
                "explanation": "1. kullanım: 800 x (3/10) = 240 L ➔ Kalan = 800 - 240 = 560 L. 2. kullanım: 560 x 0,40 = 224 L ➔ Kalan = 560 - 224 = 336 litredir."
            },
            {
                "id": 6,
                "tag": "YENİ NESİL • DİYAGRAMDAN YÜZDE ÇIKARIMI",
                "scenario": "Bir okul kütüphanesindeki kitapların türlerine göre dağılımı şöyledir: Roman %45, Şiir 1/5, Tarih 0,15, geri kalanı ise Bilim kitaplarıdır.",
                "stem": "Kütüphanede toplam 1500 kitap olduğuna göre bilim kitabı sayısı kaçtır?",
                "choices": [
                    "300 kitap (%20'si)",
                    "250 kitap",
                    "350 kitap",
                    "280 kitap"
                ],
                "correctIndex": 0,
                "explanation": "Roman = %45, Şiir = 1/5 = %20, Tarih = 0,15 = %15. Toplam = 45 + 20 + 15 = %80. Bilim = %100 - %80 = %20. 1500 x 0,20 = 300 kitap."
            },
            {
                "id": 7,
                "tag": "YENİ NESİL • KARŞILAŞTIRMALI YAKIT TASARRUFU",
                "scenario": "Bir hibrit otomobil, 100 kilometrede benzinli araca göre 2,5 litre daha az yakıt tüketmektedir. Yakıtın litresi 42 TL'dir.",
                "stem": "Yılda 20.000 kilometre yol yapan bu hibrit aracın sahibi yıllık kaç TL yakıt tasarrufu sağlar?",
                "choices": [
                    "21.000 TL (500 L tasarruf x 42 TL)",
                    "18.500 TL",
                    "24.000 TL",
                    "19.200 TL"
                ],
                "correctIndex": 0,
                "explanation": "20.000 km'de 200 adet 100 km vardır. Toplam yakıt tasarrufu = 200 x 2,5 = 500 litre. Parasal tasarruf = 500 x 42 = 21.000 TL."
            },
            {
                "id": 8,
                "tag": "YENİ NESİL • KADEMELİ VERGİ HESABI",
                "scenario": "Bir e-ticaret satıcısı 10.000 TL'ye kadar olan satışlardan %5 komisyon, 10.000 TL'yi aşan kısım için ise %3 komisyon ödemektedir.",
                "stem": "18.000 TL'lik satış yapan bir satıcının ödeyeceği toplam komisyon kaç TL'dir?",
                "choices": [
                    "740 TL (10.000'in %5'i = 500 TL + 8.000'in %3'ü = 240 TL)",
                    "800 TL",
                    "700 TL",
                    "680 TL"
                ],
                "correctIndex": 0,
                "explanation": "İlk 10.000 TL için: 10.000 x 0,05 = 500 TL. Kalan 8.000 TL için: 8.000 x 0,03 = 240 TL. Toplam = 500 + 240 = 740 TL."
            },
            {
                "id": 9,
                "tag": "YENİ NESİL • TEKSTİL FİRESİ VE VERİMLİLİK",
                "scenario": "Bir tekstil atölyesinde üretilen kumaşların %4'ü üretim hatası sebebiyle fireye ayrılmaktadır. Bir ayda 7500 metre kumaş üretilmiştir.",
                "stem": "Kusursuz olarak piyasaya sürülen kaliteli kumaş miktarı kaç metredir?",
                "choices": [
                    "7200 metre (%96'sı)",
                    "7100 metre",
                    "7300 metre",
                    "7050 metre"
                ],
                "correctIndex": 0,
                "explanation": "Fire oranı %4 ise sağlam oran %96'dır. 7500 x 0,96 = 7200 metre sağlam kumaş üretilmiştir."
            },
            {
                "id": 10,
                "tag": "YENİ NESİL • ÇOKLU SEÇENEK MALİYET ANALİZİ",
                "scenario": "Bir yazıcı kiralama şirketi iki tarife sunuyor: A Tarifesi: Ayda 300 TL sabit ücret + sayfa başı 0,20 TL. B Tarifesi: Sabit ücret yok, sayfa başı 0,35 TL.",
                "stem": "Ayda 3000 sayfa çıktı alan bir ofis için hangi tarife kaç TL daha ekonomiktir?",
                "choices": [
                    "A Tarifesi 150 TL daha ekonomiktir (900 TL vs 1050 TL)",
                    "B Tarifesi 100 TL daha ekonomiktir",
                    "İkisi de aynı maliyettedir",
                    "A Tarifesi 200 TL daha ekonomiktir"
                ],
                "correctIndex": 0,
                "explanation": "A Tarifesi: 300 + (3000 x 0,20) = 300 + 600 = 900 TL. B Tarifesi: 3000 x 0,35 = 1050 TL. A Tarifesi 1050 - 900 = 150 TL daha ekonomiktir."
            }
        ]
    }
]
