#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5. Sınıf Matematik Aktif Öğrenme v2.0 Müfredat ve Simülasyon Verisi (Hafta 1-7)
"""

GRADE5_MODULES = [
    # 5. SINIF 1. HAFTA
    {
        "grade": 5,
        "week": 1,
        "title": "Temel Geometrik Çizimler ve İnşalar Atölyesi",
        "date": "14–18 Eylül",
        "hours": "5 Ders Saati",
        "theme": "3. TEMA: GEOMETRİK ŞEKİLLER",
        "outcome_code": "MAT.5.3.1",
        "outcome_text": "Temel geometrik çizimler için matematiksel araç ve teknolojiden yararlanabilme.",
        "process_items": [
            "Temel geometrik çizim araç ve teknolojilerini tanır.",
            "Uygun matematiksel araç ve teknolojiyi belirler.",
            "Belirlediği aracı kullanarak geometrik çizimi inşa eder."
        ],
        "meb_quote": "Ölçüsüz cetvel (çizgeç) ile doğru parçası, uç noktaları uzatarak ışın ve doğru; pergel ile çember; dış noktadan doğruya dikme inşa ederek en kısa mesafeyi keşfetme.",
        "sim_steps": [
            {
                "tag": "DİJİTAL CETVEL & IŞIN",
                "title": "Adım 1: Doğru Parçası [AB] ve Işın [AC Keşfi",
                "instruction": "Sürgüyle [AB] doğru parçasının uzunluğunu değiştirin. Birkaç farklı uzunluk deneyip '📋 Gözlemi Kaydet' butonuna basarak tabloya ekleyin. Cetvel ile ışın ve doğru parçası arasındaki farkı gözlemleyin.",
                "hint": "İki ucu sınırlı çizgiye doğru parçası [AB], tek ucu sınırlı diğer ucu sınırsız uzanan çizgiye ışın [AC denir.",
                "hypotheses": [
                    {"text": "Hem doğru parçasının hem de ışının uzunluğu cetvelle tam olarak ölçülebilir.", "correct": False},
                    {"text": "Yalnızca iki ucu sınırlı olan [AB] doğru parçasının uzunluğu ölçülebilir; ışın sonsuza uzandığı için ölçülemez.", "correct": True}
                ],
                "conjectures": [
                    {"text": "İki ucu sınırlı [AB] doğru parçasının uzunluğu cetvelle tam ölçülebilir; tek yönde sınırsız uzanan [AC ışınının uzunluğu ölçülemez.", "correct": True},
                    {"text": "Işın ve doğru parçası tamamen aynı geometrik kavramlardır.", "correct": False},
                    {"text": "Işının uzunluğu cetvelle ölçülür, doğru parçası ölçülemez.", "correct": False}
                ],
                "sliderLabel": "|AB| Doğru Parçası Uzunluğu:",
                "min": 2, "max": 10, "defaultVal": 4, "unit": "birim",
                "simType": "ruler_line",
                "hasSecondary": False
            },
            {
                "tag": "İLETKİ / AÇIÖLÇER",
                "title": "Adım 2: Işının Dönmesiyle Açının Keşfi",
                "instruction": "Açı sürgüsünü hareket ettirerek [BC kolunu döndürün. Farklı açı değerlerini gözlem tablosuna kaydedin ve 90° referansına göre açının türünü inceleyin.",
                "hint": "Başlangıç noktaları ortak iki ışının birleşimi açı oluşturur. 90° dik açı, 90°'den küçükler dar, büyükler geniş açıdır.",
                "hypotheses": [
                    {"text": "Açı ölçüsü büyüdükçe kolların uzunluğu da artmak zorundadır.", "correct": False},
                    {"text": "Açı, ışının köşe etrafında dönme miktarıdır; kolların uzunluğundan bağımsızdır.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Ölçüsü 0° ile 90° arasındakiler Dar Açı, tam 90° olan Dik Açı, 90° ile 180° arasındakiler Geniş Açıdır.", "correct": True},
                    {"text": "90°'den büyük tüm açılar dar açıdır.", "correct": False},
                    {"text": "Açının kolları uzatıldığında açının derece ölçüsü de büyür.", "correct": False}
                ],
                "sliderLabel": "Dönme Açısı m(ABC):",
                "min": 15, "max": 165, "defaultVal": 45, "unit": "derece",
                "simType": "angle_draw",
                "hasSecondary": False
            },
            {
                "tag": "PERGEL & ÇEMBER",
                "title": "Adım 3: Sabit Noktaya Eşit Uzaklık & Çember",
                "instruction": "Pergel açıklığını (yarıçap r) değiştirerek farklı çemberler çizin. Her denemeyi gözlem tablosuna kaydederek yarıçap ile çap arasındaki ilişkiyi inceleyin.",
                "hint": "Pergelin sivri ucu merkezdir; kalem ucunun izi ise merkeze eşit uzaklıktaki noktalardır (çember).",
                "hypotheses": [
                    {"text": "Merkezden çember çizgisine çizilen tüm doğru parçalarının uzunluğu birbirine eşittir.", "correct": True},
                    {"text": "Çember üzerindeki noktaların merkeze uzaklığı değişkendir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Sabit bir noktaya eşit uzaklıktaki noktaların kümesi çemberdir; çap yarıçapın 2 katıdır (R = 2r).", "correct": True},
                    {"text": "Yarıçap çaptan daima daha büyüktür.", "correct": False},
                    {"text": "Pergel sadece üçgen çizmek için kullanılır.", "correct": False}
                ],
                "sliderLabel": "Pergel Yarıçap Açıklığı (r):",
                "min": 2, "max": 7, "defaultVal": 4, "unit": "birim",
                "simType": "circle_radius",
                "hasSecondary": False
            },
            {
                "tag": "GÖNYE & EN KISA DİKME",
                "title": "Adım 4: Dış Noktadan Doğruya En Kısa Dikme [PH] ⊥ d",
                "instruction": "P noktasından d doğrusuna inen doğru parçasının açısını sürgüyle değiştirin. Farklı açılardaki uzunlukları tabloya kaydedin ve mesafenin en küçük olduğu anı keşfedin.",
                "hint": "Bir noktanın bir doğruya olan en kısa mesafesi, doğruya dik (90°) olarak indirilen doğru parçasıdır.",
                "hypotheses": [
                    {"text": "En kısa mesafe dar açılı (45°) veya geniş açılı bir çizgi ile elde edilir.", "correct": False},
                    {"text": "En kısa mesafe, noktadan doğruya 90° dik açıyla indirilen dikmedir.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Bir noktanın bir doğruya en kısa mesafesi daima dikmedir ([PH] ⊥ d).", "correct": True},
                    {"text": "Eğik çizgiler dikmeden daha kısadır.", "correct": False},
                    {"text": "Açı küçüldükçe mesafe daima azalır.", "correct": False}
                ],
                "sliderLabel": "İnme Açısı:",
                "min": 45, "max": 135, "defaultVal": 60, "unit": "derece",
                "simType": "perpendicular_drop",
                "hasSecondary": False
            }
        ]
    },

    # 5. SINIF 2. HAFTA
    {
        "grade": 5,
        "week": 2,
        "title": "Temel Geometrik Çizimler ve Deneyimler Atölyesi",
        "date": "21–25 Eylül",
        "hours": "5 Ders Saati",
        "theme": "3. TEMA: GEOMETRİK ŞEKİLLER",
        "outcome_code": "MAT.5.3.2",
        "outcome_text": "Temel geometrik çizimlere dayalı deneyimlerini yansıtabilme.",
        "process_items": [
            "Temel geometrik çizimlerle ilgili edindiği deneyimleri gözden geçirir.",
            "Doğru, doğru parçası, ışın, açı ve çember özelliklerine dair çıkarım yapar.",
            "Çıkarımlarını farklı örnekler üzerinden değerlendirir."
        ],
        "meb_quote": "İki noktadan yalnız bir doğru geçtiği, çember yarıçaplarının eşitliği ile doğru parçası taşıma, gönye ile doğruya eşit uzaklıktaki noktaları birleştirerek paralel doğruları keşfetme.",
        "sim_steps": [
            {
                "tag": "İKİ NOKTADAN TEK DOĞRU",
                "title": "Adım 1: İki Noktadan Geçen Doğru Sayısı",
                "instruction": "Tuvaldeki A ve B noktaları arasından doğru çizin. Doğrunun eğimini ve konumunu inceleyerek farklı iki noktadan kaç doğru geçebileceğini test edin.",
                "hint": "Bir noktadan sonsuz doğru geçerken, iki nokta sabitlendiğinde aralarından kaç doğru geçebilir?",
                "hypotheses": [
                    {"text": "Farklı iki noktadan sonsuz sayıda farklı doğru geçebilir.", "correct": False},
                    {"text": "Farklı iki noktadan yalnızca ve yalnızca BİR tek doğru geçer.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Düzlemde farklı iki noktadan yalnız ve yalnız tek bir doğru geçer.", "correct": True},
                    {"text": "İki noktadan hiç doğru geçemez.", "correct": False},
                    {"text": "İki noktadan geçen doğru sayısı noktalara göre değişir.", "correct": False}
                ],
                "sliderLabel": "Nokta B Konumu:",
                "min": 1, "max": 8, "defaultVal": 4, "unit": "birim",
                "simType": "ruler_line",
                "hasSecondary": False
            },
            {
                "tag": "PERGEL İLE EŞ PARÇA",
                "title": "Adım 2: Pergel ile Eş Doğru Parçası İnşası",
                "instruction": "Pergeli [AB] uzunluğunda açarak yeni bir ışın üzerine [CD] doğru parçası kopyalayın. Uzunlukları tabloya kaydedin.",
                "hint": "Pergel yalnızca çember çizmek için değil, 'uzunluk taşımak' için de kullanılan antik bir matematiksel araçtır.",
                "hypotheses": [
                    {"text": "Ölçüsüz cetvel ve pergel ile tam eş uzunlukta doğru parçası inşa edilebilir.", "correct": True},
                    {"text": "Eş doğru parçası çizmek için mutlaka milimetrik cetvel gerekir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Pergel açıklığı bozulmadan taşındığında, çizilen iki doğru parçasının uzunlukları birbirine eşit olur (|AB| = |CD|).", "correct": True},
                    {"text": "Pergel ile taşınan doğru parçaları daima küçülür.", "correct": False}
                ],
                "sliderLabel": "Taşınan Uzunluk:",
                "min": 2, "max": 8, "defaultVal": 5, "unit": "birim",
                "simType": "ruler_line",
                "hasSecondary": False
            },
            {
                "tag": "YARIÇAPLARIN EŞİTLİĞİ",
                "title": "Adım 3: Çember Yarıçaplarının Eşitliği",
                "instruction": "Bir çember üzerinde farklı yönlere yarıçap doğru parçaları çizin. Her birinin uzunluğunu tabloya kaydedip karşılaştırın.",
                "hint": "Bir çemberin merkezinden çember yayına çizilen tüm çizgiler yarıçaptır.",
                "hypotheses": [
                    {"text": "Aynı çemberdeki tüm yarıçapların uzunlukları birbirine eşittir.", "correct": True},
                    {"text": "Yarıçaplar yönlerine göre farklı uzunlukta olabilir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bir çember üzerindeki tüm noktaların merkeze olan uzaklıkları daima birbirine eşittir (|OA| = |OB| = r).", "correct": True},
                    {"text": "Yarıçaplar çemberin büyüklüğüne göre kendi içinde değişir.", "correct": False}
                ],
                "sliderLabel": "Çember Yarıçapı (r):",
                "min": 2, "max": 7, "defaultVal": 4, "unit": "birim",
                "simType": "circle_radius",
                "hasSecondary": False
            },
            {
                "tag": "GÖNYE & PARALEL DOĞRULAR",
                "title": "Adım 4: Paralel Doğruların Keşfi (Tren Rayları)",
                "instruction": "İki doğru arasındaki dik mesafeyi sürgüyle değiştirin. Rayların hiçbir noktada kesişmediğini ve aralarındaki mesafenin her yerde sabit kaldığını gözlemleyin.",
                "hint": "Aralarındaki uzaklık her yerde eşit olan ve sonsuza kadar uzatılsalar bile kesişmeyen doğrulara paralel doğrular denir.",
                "hypotheses": [
                    {"text": "Paralel doğrular çok uzatılırsa bir noktada kesişir.", "correct": False},
                    {"text": "Paralel doğrular hiçbir noktada kesişmez; aralarındaki dik uzaklık daima sabittir.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Aynı düzlemde kesişmeyen ve aralarındaki dik uzaklık her noktada aynı kalan doğrular paraleldir (d1 // d2).", "correct": True},
                    {"text": "Paralel doğrular birbirine diktir.", "correct": False}
                ],
                "sliderLabel": "Raylar Arası Dik Mesafe:",
                "min": 2, "max": 8, "defaultVal": 4, "unit": "birim",
                "simType": "perpendicular_drop",
                "hasSecondary": False
            }
        ]
    },

    # 5. SINIF 3. HAFTA
    {
        "grade": 5,
        "week": 3,
        "title": "Açı Ölçme ve Eş Açı İnşası Atölyesi",
        "date": "28 Eylül–02 Ekim",
        "hours": "5 Ders Saati",
        "theme": "3. TEMA: GEOMETRİK ŞEKİLLER",
        "outcome_code": "MAT.5.3.3",
        "outcome_text": "Açıları ölçmek için matematiksel araç ve teknolojiden yararlanabilme.",
        "process_items": [
            "Açı ölçmek için gerekli araç ve teknolojiyi tanır.",
            "Açı ölçmek için uygun araç ve teknolojiyi belirler.",
            "Açı ölçmek için uygun araç ve teknolojiyi kullanır."
        ],
        "meb_quote": "Tam dönme (360° tam açı) ve yarım dönme (180° doğru açı) üzerinden 1°'nin 360 eş dilimden biri olduğunu keşfetme; açıölçerle ölçüm ve verilen açıya eş açı inşa etme.",
        "sim_steps": [
            {
                "tag": "1 DERECE KEŞFİ",
                "title": "Adım 1: Tam Dönme (360°) ve 1° Tanımı",
                "instruction": "Çember dilim sürgüsünü hareket ettirerek yarım dönme (180°) ve tam dönme (360°) durumlarını inceleyin. Gözlemlerinizi tabloya kaydedin.",
                "hint": "Bir çemberin tamamı 360 eş dilime bölündüğünde her bir dilim 1 derecelik (1°) açıdır.",
                "hypotheses": [
                    {"text": "Tam bir tur dönme 360 dereceye karşılık gelir.", "correct": True},
                    {"text": "Tam dönme 100 derecedir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Tam dönme 360°, doğru açı 180°, dik açı 90°'dir ve 1° tam açının 360'ta biridir.", "correct": True},
                    {"text": "Doğru açı 360 derecedir.", "correct": False}
                ],
                "sliderLabel": "Dönme Açıklığı:",
                "min": 30, "max": 180, "defaultVal": 90, "unit": "derece",
                "simType": "angle_draw",
                "hasSecondary": False
            },
            {
                "tag": "İLETKİ İLE DAR AÇI",
                "title": "Adım 2: İletki ile Dar Açı Ölçümü",
                "instruction": "İletki merkezini açının köşesine yerleştirin ve 0°-90° arasındaki dar açıları ölçün. Farklı açıları tabloya kaydedin.",
                "hint": "Açının bir kolu iletkinin 0° çizgisine hizalanır, diğer kolun gösterdiği rakam açının ölçüsüdür.",
                "hypotheses": [
                    {"text": "Dar açının ölçüsü daima 90°'den küçüktür.", "correct": True},
                    {"text": "Dar açılar 90°'den büyüktür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Ölçüsü 0° ile 90° arasında olan tüm açılar Dar Açıdır.", "correct": True},
                    {"text": "Dar açıların kolları birbirine diktir.", "correct": False}
                ],
                "sliderLabel": "Dar Açı Ölçüsü:",
                "min": 15, "max": 85, "defaultVal": 45, "unit": "derece",
                "simType": "angle_draw",
                "hasSecondary": False
            },
            {
                "tag": "İLETKİ İLE GENİŞ AÇI",
                "title": "Adım 3: İletki ile Geniş Açı Ölçümü",
                "instruction": "90° ile 180° arasındaki geniş açıları iletki ile ölçün ve tabloya kaydedin.",
                "hint": "Dik açıdan (90°) büyük ve doğru açıdan (180°) küçük olan açılar geniş açıdır.",
                "hypotheses": [
                    {"text": "Geniş açının ölçüsü 90° ile 180° arasındadır.", "correct": True},
                    {"text": "Geniş açı 180°'den büyüktür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Ölçüsü 90°'den büyük ve 180°'den küçük açılar Geniş Açıdır.", "correct": True},
                    {"text": "90° tam olarak geniş açıdır.", "correct": False}
                ],
                "sliderLabel": "Geniş Açı Ölçüsü:",
                "min": 95, "max": 175, "defaultVal": 135, "unit": "derece",
                "simType": "angle_draw",
                "hasSecondary": False
            },
            {
                "tag": "EŞ AÇI İNŞASI",
                "title": "Adım 4: Verilen Bir Açıya Eş Açı İnşası",
                "instruction": "Açıölçer ve cetvel kullanarak verilen bir açının eşini yan tarafa inşa edin. Açı ölçülerini karşılaştırın.",
                "hint": "İki açının eş olması için kollarının arasındaki açıklık derecesinin eşit olması yeterlidir; kolların uzunluğu açıyı değiştirmez.",
                "hypotheses": [
                    {"text": "İki açının eş olması için kollarının boyunun da eşit olması gerekir.", "correct": False},
                    {"text": "Kolların uzunluğu ne olursa olsun, derece ölçüleri eşit olan açılar eş açılardır.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Ölçüleri birbirine eşit olan açılara Eş Açılar denir; kol uzunlukları açının ölçüsünü etkilemez.", "correct": True},
                    {"text": "Kolları daha uzun olan açı daima daha büyüktür.", "correct": False}
                ],
                "sliderLabel": "İnşa Edilen Eş Açı:",
                "min": 20, "max": 160, "defaultVal": 60, "unit": "derece",
                "simType": "angle_draw",
                "hasSecondary": False
            }
        ]
    },

    # 5. SINIF 4. HAFTA
    {
        "grade": 5,
        "week": 4,
        "title": "Kesişen Doğrularda Açılar Atölyesi",
        "date": "05–09 Ekim",
        "hours": "5 Ders Saati",
        "theme": "3. TEMA: GEOMETRİK ŞEKİLLER",
        "outcome_code": "MAT.5.3.4",
        "outcome_text": "Düzlemde iki veya üç doğrunun birbirine göre durumuna bağlı olarak oluşabilecek açılara dair çıkarım yapabilme.",
        "process_items": [
            "Varsayımlarda bulunur.",
            "Oluşan açıları belirleyerek listeler.",
            "Karşılaştırır.",
            "Önerme sunar ve gerekçe belirtir."
        ],
        "meb_quote": "Düzlemde 2 veya 3 doğrunun durumuna göre açılara dair varsayımda bulunma, ölçümleri tablo temsili üzerinde (eş olanlar, toplamı 180° olanlar) listeleme; kesişen, dik, paralel ve çakışık doğruları keşfetme.",
        "sim_steps": [
            {
                "tag": "KOMŞU BÜTÜNLER",
                "title": "Adım 1: Kesişen İki Doğruda Komşu Açılar",
                "instruction": "Kesişen iki doğrudan birinin açısını sürgüyle değiştirin. Yan yana duran iki açının (α ve β) toplamını gözlem tablosuna kaydedin.",
                "hint": "Bir doğru üzerinde yan yana duran iki komşu açının toplamı daima doğru açı (180°) yapar.",
                "hypotheses": [
                    {"text": "Bir doğru üzerindeki komşu iki açının toplamı daima 180°'dir.", "correct": True},
                    {"text": "Komşu açıların toplamı 90°'dir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Doğrusal bir hat üzerinde komşu olan iki açının ölçüleri toplamı daima 180°'dir (Komşu Bütünler Açılar).", "correct": True},
                    {"text": "Komşu açıların toplamı açı büyüdükçe artar.", "correct": False}
                ],
                "sliderLabel": "Açı α:",
                "min": 20, "max": 160, "defaultVal": 60, "unit": "derece",
                "simType": "angle_draw",
                "hasSecondary": False
            },
            {
                "tag": "TERS AÇILAR",
                "title": "Adım 2: Kesişen İki Doğruda Ters Açıların Eşitliği",
                "instruction": "Kesişen iki doğrudan karşılıklı duran zıt yönlü açıları inceleyin. Sürgüyü değiştirip ters açıların ölçülerini tabloya kaydedin.",
                "hint": "Kesişen iki doğrunun oluşturduğu zıt yönlü açılara ters açılar denir.",
                "hypotheses": [
                    {"text": "Ters açıların ölçüleri birbirine daima eşittir.", "correct": True},
                    {"text": "Ters açılardan biri daima diğerinden büyüktür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Kesişen iki doğrunun oluşturduğu karşılıklı ters açıların ölçüleri birbirine daima eşittir.", "correct": True},
                    {"text": "Ters açıların toplamı 90°'dir.", "correct": False}
                ],
                "sliderLabel": "Ters Açı Ölçüsü:",
                "min": 25, "max": 155, "defaultVal": 75, "unit": "derece",
                "simType": "angle_draw",
                "hasSecondary": False
            },
            {
                "tag": "DİK KESİŞEN DOĞRULAR",
                "title": "Adım 3: İki Doğrunun Dik Kesişmesi (90°)",
                "instruction": "Açıyı tam 90° konumuna getirin. Oluşan 4 açının her birini inceleyip gözlem tablosuna kaydedin.",
                "hint": "Birbirini 90° ile kesen doğrular dik kesişen doğrulardır ve aralarında 4 tane dik açı oluşur.",
                "hypotheses": [
                    {"text": "İki doğru dik kesiştiğinde oluşan 4 açının dördü de 90°'dir.", "correct": True},
                    {"text": "Dik kesişmede sadece bir açı 90° olur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Dik kesişen iki doğru arasında 4 adet 90°'lik dik açı oluşur ve d1 ⊥ d2 ile gösterilir.", "correct": True},
                    {"text": "Dik doğrular kesişmeyen doğrulardır.", "correct": False}
                ],
                "sliderLabel": "Kesişim Açısı:",
                "min": 45, "max": 135, "defaultVal": 90, "unit": "derece",
                "simType": "angle_draw",
                "hasSecondary": False
            },
            {
                "tag": "PARALEL DOĞRULAR VE AÇI",
                "title": "Adım 4: Paralel Doğruların Kesişmeme Durumu",
                "instruction": "İki doğruyu paralel konuma getirin. Kesişme olup olmadığını ve aralarında bir açı oluşup oluşmadığını inceleyin.",
                "hint": "Açı oluşabilmesi için kolların kesiştiği bir köşe noktası bulunmalıdır.",
                "hypotheses": [
                    {"text": "Paralel doğrular hiçbir noktada kesişmedikleri için aralarında açı oluşturmazlar.", "correct": True},
                    {"text": "Paralel doğrular 180 derecelik açı oluşturur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Düzlemde kesişmeyen paralel doğrular ortak bir köşe noktası oluşturmadıkları için aralarında açı oluşmaz.", "correct": True},
                    {"text": "Paralel doğrular daima dar açı oluşturur.", "correct": False}
                ],
                "sliderLabel": "Aralık Mesafesi:",
                "min": 2, "max": 8, "defaultVal": 4, "unit": "birim",
                "simType": "perpendicular_drop",
                "hasSecondary": False
            }
        ]
    },

    # 5. SINIF 5. HAFTA
    {
        "grade": 5,
        "week": 5,
        "title": "Ardışık Kesişen Doğrular ve Çokgenler Atölyesi",
        "date": "12–16 Ekim",
        "hours": "5 Ders Saati",
        "theme": "3. TEMA: GEOMETRİK ŞEKİLLER",
        "outcome_code": "MAT.5.3.5",
        "outcome_text": "Çokgenleri düzlemde ardışık olarak kesişen doğruların oluşturduğu kapalı şekiller olarak yorumlayabilme.",
        "process_items": [
            "Düzlemde en az üç doğrunun ardışık kesişerek oluşturdukları durumları inceler.",
            "Çeşitli çokgenler oluşturur.",
            "Çokgenleri ifade eder."
        ],
        "meb_quote": "En az 3 doğrunun (ilk doğru son doğruyla kesişecek koşuluyla) ardışık kesişimiyle oluşan kapalı şekilleri çizme; doğru sayısı ile kenar sayısı arasındaki birebir ilişkiyi gözlemleme.",
        "sim_steps": [
            {
                "tag": "KAPALILIK KOŞULU",
                "title": "Adım 1: En Az Kaç Doğru Kapalı Şekil Oluşturur?",
                "instruction": "Doğru sayısını 2 ve 3 yaparak tuvaldeki şekli inceleyin. 2 doğru ile kapalı bir bölge sınırlandırmanın mümkün olup olmadığını tabloya kaydedin.",
                "hint": "Bir şeklin çokgen olabilmesi için kapalı olması ve en az 3 doğru parçasından oluşması gerekir.",
                "hypotheses": [
                    {"text": "Düzlemde 2 doğru ile kapalı bir çokgen oluşturulabilir.", "correct": False},
                    {"text": "Kapalı bir geometrik bölge (çokgen) oluşturabilmek için en az 3 doğru gereklidir.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Düzlemde en az 3 doğrunun ardışık kesişmesiyle kapalı şekil oluşur; ilk çokgen Üçgendir.", "correct": True},
                    {"text": "2 doğru birleşerek kapalı çokgen oluşturur.", "correct": False}
                ],
                "sliderLabel": "Doğru Sayısı (n):",
                "min": 2, "max": 4, "defaultVal": 3, "unit": "doğru",
                "simType": "polygon_builder",
                "hasSecondary": False
            },
            {
                "tag": "DÖRTGEN İNŞASI",
                "title": "Adım 2: 4 Doğrunun Ardışık Kesişimi (Dörtgen)",
                "instruction": "Doğru sayısını 4 yapın. Ardışık kesişen 4 doğrunun oluşturduğu kenar ve köşe sayısını inceleyip tabloya kaydedin.",
                "hint": "4 doğrunun kapalı bir bölge oluşturacak biçimde ardışık kesişmesiyle dörtgen elde edilir.",
                "hypotheses": [
                    {"text": "4 doğrunun ardışık kesişmesiyle 4 kenarlı ve 4 köşeli bir dörtgen oluşur.", "correct": True},
                    {"text": "4 doğru 3 köşeli şekil oluşturur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "4 doğrunun sonuncusu ilkiyle kesiştiğinde 4 kenarlı ve 4 köşeli bir Dörtgen oluşur.", "correct": True},
                    {"text": "Dörtgenin kenar sayısı köşe sayısından fazladır.", "correct": False}
                ],
                "sliderLabel": "Doğru Sayısı:",
                "min": 3, "max": 6, "defaultVal": 4, "unit": "doğru",
                "simType": "polygon_builder",
                "hasSecondary": False
            },
            {
                "tag": "KENAR VE KÖŞE EŞİTLİĞİ",
                "title": "Adım 3: Beşgen ve Altıgen İnşası",
                "instruction": "Doğru sayısını 5 ve 6'ya çıkarın. Kenar sayısı ile köşe sayısı arasındaki ilişkiyi gözlem tablosuna kaydedin.",
                "hint": "Çokgenler kenar sayılarına göre üçgen, dörtgen, beşgen, altıgen olarak isimlendirilir.",
                "hypotheses": [
                    {"text": "Çokgenlerde kenar sayısı daima köşe sayısına eşittir.", "correct": True},
                    {"text": "Çokgenin köşe sayısı kenar sayısından 1 eksiktir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bir çokgende kenar sayısı, köşe sayısı ve iç açı sayısı daima birbirine eşittir (n kenar = n köşe).", "correct": True},
                    {"text": "Altıgenin 5 kenarı ve 6 köşesi vardır.", "correct": False}
                ],
                "sliderLabel": "Doğru / Kenar Sayısı:",
                "min": 3, "max": 8, "defaultVal": 6, "unit": "kenar",
                "simType": "polygon_builder",
                "hasSecondary": False
            },
            {
                "tag": "KAPALI ŞEKİL KURALI",
                "title": "Adım 4: Son Doğrunun İlk Doğruyla Kesişmesi",
                "instruction": "Son doğrunun ilk doğru ile kesişmediği (açık kalan) durumu inceleyin. Şeklin çokgen sayılabilmesi için kapalılık şartını test edin.",
                "hint": "Kenarları birleşmeyen, uçları açık kalan çizgiler çokgen oluşturmaz.",
                "hypotheses": [
                    {"text": "Uçları açık kalan çizgiler de çokgen sayılır.", "correct": False},
                    {"text": "Bir şeklin çokgen olması için son doğrunun ilk doğruyla kesişerek kapalı bir bölge oluşturması şarttır.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Çokgenler yalnızca ardışık kesişen ve son doğrusu ilk doğrusuyla birleşen KAPALI düzlemsel şekillerdir.", "correct": True},
                    {"text": "Açık eğriler çokgendir.", "correct": False}
                ],
                "sliderLabel": "Kapalılık Durumu (Kenar):",
                "min": 3, "max": 7, "defaultVal": 5, "unit": "kenar",
                "simType": "polygon_builder",
                "hasSecondary": False
            }
        ]
    },

    # 5. SINIF 6. HAFTA
    {
        "grade": 5,
        "week": 6,
        "title": "Çokgenlerin Özellikleri ve Üçgen İç Açıları Atölyesi",
        "date": "19–23 Ekim",
        "hours": "5 Ders Saati",
        "theme": "3. TEMA: GEOMETRİK ŞEKİLLER",
        "outcome_code": "MAT.5.3.6",
        "outcome_text": "Çokgenlerin özellikleri ile ilgili edindiği deneyimleri yansıtabilme.",
        "process_items": [
            "Çokgenlerin özellikleri ile ilgili edindiği deneyimleri gözden geçirir.",
            "Kenar ve açı özelliklerine dair çıkarım yapar.",
            "Çıkarımını farklı örnekler üzerinden değerlendirir."
        ],
        "meb_quote": "Çokgenlerde iç/dış açı, ardışık olmayan köşeleri birleştirerek köşegen çizme; kağıt kesme ve açı ölçme ile üçgenin iç açıları toplamının 180° olduğunu, bir üçgende iki dik açı olamayacağını keşfetme.",
        "sim_steps": [
            {
                "tag": "KÖŞEGEN KEŞFİ",
                "title": "Adım 1: Çokgende Köşegen Çizimi",
                "instruction": "Dörtgen, beşgen ve altıgende ardışık olmayan köşeleri birleştiren doğru parçalarını (köşegenleri) çizin. Üçgende köşegen olup olmadığını inceleyin.",
                "hint": "Bir çokgende komşu olmayan iki köşeyi birleştiren doğru parçasına köşegen denir. Üçgenin tüm köşeleri birbirine komşudur!",
                "hypotheses": [
                    {"text": "Üçgenin de diğer tüm çokgenler gibi köşegenleri vardır.", "correct": False},
                    {"text": "Üçgende komşu olmayan köşe bulunmadığı için üçgenin köşegeni yoktur.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Ardışık olmayan iki köşeyi birleştiren çizgi köşegendir; Üçgenin köşegeni yoktur, dörtgenin 2 köşegeni vardır.", "correct": True},
                    {"text": "Köşegen kenarla aynı şeydir.", "correct": False}
                ],
                "sliderLabel": "Çokgen Kenar Sayısı:",
                "min": 3, "max": 6, "defaultVal": 4, "unit": "kenar",
                "simType": "polygon_builder",
                "hasSecondary": False
            },
            {
                "tag": "ÜÇGENİN İÇ AÇILARI",
                "title": "Adım 2: Üçgenin İç Açıları Toplamı (180°)",
                "instruction": "Üçgenin köşelerindeki açıları sürgüyle değiştirin. Üç açının toplamını gözlem tablosuna kaydedin.",
                "hint": "Üçgenin üç köşesini yırtıp yan yana getirdiğinizde bir doğru açı (180°) oluştururlar.",
                "hypotheses": [
                    {"text": "Büyük üçgenlerin iç açıları toplamı küçük üçgenlerden daha büyüktür.", "correct": False},
                    {"text": "Bütün üçgenlerin iç açıları ölçüleri toplamı daima 180 derecedir.", "correct": True}
                ],
                "conjectures": [
                    {"text": "Üçgenin çeşidi ve boyutu ne olursa olsun iç açılarının ölçüleri toplamı daima 180°'dir.", "correct": True},
                    {"text": "Eşkenar üçgenin açıları toplamı 360°'dir.", "correct": False}
                ],
                "sliderLabel": "Açı 1:",
                "min": 20, "max": 120, "defaultVal": 60, "unit": "derece",
                "simType": "triangle_angle_sum",
                "hasSecondary": True,
                "sliderLabel2": "Açı 2:",
                "min2": 20, "max2": 120, "defaultVal2": 60, "unit2": "derece"
            },
            {
                "tag": "İKİ DİK AÇI KURALI",
                "title": "Adım 3: Bir Üçgende İki Dik Açı Olabilir mi?",
                "instruction": "Bir açıyı 90° yapın ve ikinci açıyı da 90° yapmayı deneyin. Üçgenin kapanıp kapanmadığını gözlemleyin.",
                "hint": "İki açı 90° + 90° = 180° olursa, üçüncü açıya 0° kalır ve kollar paralel uzanarak birleşemez!",
                "hypotheses": [
                    {"text": "Bir üçgende iki tane 90°'lik dik açı bulunabilir.", "correct": False},
                    {"text": "Bir üçgende en fazla bir tane dik açı veya geniş açı bulunabilir; iki dik açı üçgen oluşturamaz.", "correct": True}
                ],
                "conjectures": [
                    {"text": "İç açılar toplamı 180° olduğundan, bir üçgende en fazla BİR dik veya BİR geniş açı bulunabilir.", "correct": True},
                    {"text": "Üçgende üç tane dik açı olabilir.", "correct": False}
                ],
                "sliderLabel": "1. Açı Ölçüsü:",
                "min": 30, "max": 120, "defaultVal": 90, "unit": "derece",
                "simType": "triangle_angle_sum",
                "hasSecondary": True,
                "sliderLabel2": "2. Açı Ölçüsü:",
                "min2": 15, "max2": 85, "defaultVal2": 45, "unit2": "derece"
            },
            {
                "tag": "DÜZGÜN ÇOKGENLER",
                "title": "Adım 4: Eşkenar Üçgen ve Düzgün Çokgenler",
                "instruction": "Tüm kenarları ve tüm iç açıları eşit olan düzgün çokgenleri (eşkenar üçgen, kare, düzgün altıgen) inceleyin.",
                "hint": "Eşkenar üçgenin 3 açısı da eşittir: 180° ÷ 3 = 60°.",
                "hypotheses": [
                    {"text": "Eşkenar üçgenin her bir iç açısı tam olarak 60 derecedir.", "correct": True},
                    {"text": "Eşkenar üçgenin açıları 90 derecedir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Tüm kenar uzunlukları ve açı ölçüleri eşit olan çokgenler düzgündür; Eşkenar üçgenin her bir açısı 60°'dir.", "correct": True},
                    {"text": "Düzgün çokgenlerin açıları birbirinden farklıdır.", "correct": False}
                ],
                "sliderLabel": "Düzgün Çokgen Kenar Sayısı:",
                "min": 3, "max": 8, "defaultVal": 3, "unit": "kenar",
                "simType": "polygon_builder",
                "hasSecondary": False
            }
        ]
    },

    # 5. SINIF 7. HAFTA (YENİ MODÜL)
    {
        "grade": 5,
        "week": 7,
        "title": "İki Çember Kesişimi ile Üçgen İnşası ve Yaşam Çiçeği Atölyesi",
        "date": "26–30 Ekim",
        "hours": "5 Ders Saati",
        "theme": "3. TEMA: GEOMETRİK ŞEKİLLER",
        "outcome_code": "MAT.5.3.7",
        "outcome_text": "Matematiksel araç ve teknoloji yardımıyla düzlemde iki noktada kesişen çember çiftinin merkezleri ve kesişim noktalarından biri ile inşa edilen üçgenlerin kenar özelliklerine yönelik çıkarım yapabilme.",
        "process_items": [
            "İki noktada kesişen çember çiftinin merkezleri ve kesişim noktasıyla üçgen inşasına yönelik varsayımda bulunur.",
            "İnşa edilen üçgenleri kenar özelliklerine göre belirleyerek listeler.",
            "Karşılaştırır.",
            "Önerme sunar ve gerekçelendirir."
        ],
        "meb_quote": "Yaşam çiçeği ve logo bağlamı; kesişen iki çemberin merkezleri ve kesişim noktasından üçgen inşası için varsayımda bulunma, çember yarıçaplarını dinamik manipüle ederek çeşitkenar, ikizkenar ve eşkenar üçgenleri listeleme; Öklid'in 1. Önermesi.",
        "sim_steps": [
            {
                "tag": "ÇEMBER KESİŞİMİ & ÜÇGEN",
                "title": "Adım 1: Merkezler ve Kesişim Noktasından Üçgen İnşası",
                "instruction": "A ve B merkezli iki çemberin kesişim noktası olan C noktasını inceleyin. Merkezleri ve C noktasını birleştiren [AB], [AC] ve [BC] doğru parçalarını oluşturup tabloya kaydedin.",
                "hint": "C noktası her iki çember üzerinde de yer aldığı için, [AC] 1. çemberin yarıçapı, [BC] ise 2. çemberin yarıçapıdır.",
                "hypotheses": [
                    {"text": "Kesişen iki çemberin merkezleri ve kesişim noktası birleştirildiğinde daima bir üçgen oluşur.", "correct": True},
                    {"text": "Bu üç nokta daima doğrusaldır ve üçgen oluşturmaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Düzlemde kesişen iki çemberin merkezleri (A, B) ve kesişim noktası (C) birleştirildiğinde bir ABC üçgeni inşa edilir.", "correct": True},
                    {"text": "Çember kesişimlerinden yalnızca kare elde edilir.", "correct": False}
                ],
                "sliderLabel": "1. Çember Yarıçapı (r1):",
                "min": 80, "max": 180, "defaultVal": 140, "unit": "px",
                "simType": "euclid_flower",
                "hasSecondary": True,
                "sliderLabel2": "2. Çember Yarıçapı (r2):",
                "min2": 80, "max2": 180, "defaultVal2": 140, "unit2": "px"
            },
            {
                "tag": "ÖKLİD 1. ÖNERMESİ",
                "title": "Adım 2: Öklid'in 1. Önermesi (Eşkenar Üçgen)",
                "instruction": "Her iki çemberin yarıçapını da merkezler arası mesafeye eşit (r1 = r2 = |AB| = 140 px) yapın. Oluşan üçgenin kenar uzunluklarını gözlem tablosuna kaydedin.",
                "hint": "Öklid M.Ö. 300 yılında cetvel ve pergel ile eşkenar üçgen çizimini bu yöntemle ispatlamıştır: |AB| = |AC| = |BC| = r.",
                "hypotheses": [
                    {"text": "Yarıçaplar merkezler arası mesafeye eşitlendiğinde ölçüm yapmadan eşkenar üçgen inşa edilmiş olur.", "correct": True},
                    {"text": "Yarıçaplar eşit olsa da oluşan üçgen çeşitkenardır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "r1 = r2 = |AB| olduğunda Öklid'in 1. Önermesi gereğince üç kenarı eşit EŞKENAR ÜÇGEN inşa edilir (|AB| = |AC| = |BC|).", "correct": True},
                    {"text": "Eşkenar üçgen çizmek için açıölçer şarttır.", "correct": False}
                ],
                "sliderLabel": "Yarıçap r1 (|AB| = 140 px):",
                "min": 80, "max": 180, "defaultVal": 140, "unit": "px",
                "simType": "euclid_flower",
                "hasSecondary": True,
                "sliderLabel2": "Yarıçap r2:",
                "min2": 80, "max2": 180, "defaultVal2": 140, "unit2": "px"
            },
            {
                "tag": "İKİZKENAR ÜÇGEN",
                "title": "Adım 3: Eşit Yarıçaplı Çemberlerle İkizkenar Üçgen",
                "instruction": "İki çemberin yarıçapını birbirine eşit (r1 = r2 = 110 px) ancak merkezler arası mesafeden (|AB| = 140 px) farklı yapın. Kenarları tabloya kaydedin.",
                "hint": "C noktası her iki çembere de eşit uzaklıktadır: |AC| = |BC| = r, ancak taban |AB| farklıdır.",
                "hypotheses": [
                    {"text": "r1 = r2 ≠ |AB| olduğunda iki kenarı eşit olan İkizkenar Üçgen elde edilir.", "correct": True},
                    {"text": "Bu durumda üçgen oluşmaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "İki çemberin yarıçapı eşit fakat merkezler arası mesafeden farklı olduğunda İKİZKENAR ÜÇGEN oluşur (|AC| = |BC| ≠ |AB|).", "correct": True},
                    {"text": "Yarıçaplar eşitse üçgen daima çeşitkenardır.", "correct": False}
                ],
                "sliderLabel": "Eşit Yarıçap r1:",
                "min": 80, "max": 180, "defaultVal": 110, "unit": "px",
                "simType": "euclid_flower",
                "hasSecondary": True,
                "sliderLabel2": "Eşit Yarıçap r2:",
                "min2": 80, "max2": 180, "defaultVal2": 110, "unit2": "px"
            },
            {
                "tag": "ÇEŞİTKENAR ÜÇGEN",
                "title": "Adım 4: Farklı Yarıçaplarla Çeşitkenar Üçgen",
                "instruction": "Birinci çemberin yarıçapını 160 px, ikincisini 100 px yapın (r1 ≠ r2 ≠ |AB|). Kenar uzunluklarını inceleyip tabloya kaydedin.",
                "hint": "Üç kenar uzunluğu da birbirinden farklı olduğunda çeşitkenar üçgen elde edilir.",
                "hypotheses": [
                    {"text": "r1 ve r2 birbirinden ve |AB|'den farklı seçildiğinde tüm kenarları farklı bir Çeşitkenar Üçgen oluşur.", "correct": True},
                    {"text": "Çember kesişimlerinden çeşitkenar üçgen üretilemez.", "correct": False}
                ],
                "conjectures": [
                    {"text": "İki çemberin yarıçapları birbirinden ve merkezler arası mesafeden farklı olduğunda ÇEŞİTKENAR ÜÇGEN inşa edilir (|AC| ≠ |BC| ≠ |AB|).", "correct": True},
                    {"text": "Farklı yarıçaplı çemberler daima eşkenar üçgen verir.", "correct": False}
                ],
                "sliderLabel": "Yarıçap r1:",
                "min": 90, "max": 180, "defaultVal": 160, "unit": "px",
                "simType": "euclid_flower",
                "hasSecondary": True,
                "sliderLabel2": "Yarıçap r2:",
                "min2": 80, "max2": 150, "defaultVal2": 100, "unit2": "px"
            }
        ],
        "mini_tasks": [
            {
                "id": 1,
                "tag": "ÖKLİD ÖNERMESİ VE EŞKENAR ÜÇGEN",
                "question": "A ve B merkezli iki çemberin yarıçapları merkezler arası uzaklığa eşit (|AB| = r1 = r2 = 6 cm) ve C kesişim noktasıdır. ABC üçgeninin kenar türü nedir?",
                "options": [
                    {"label": "A) İkizkenar Üçgen (6 cm, 6 cm, 12 cm)", "correct": False},
                    {"label": "B) Eşkenar Üçgen (|AB| = |AC| = |BC| = 6 cm)", "correct": True},
                    {"label": "C) Çeşitkenar Üçgen", "correct": False}
                ]
            },
            {
                "id": 2,
                "tag": "İKİZKENAR ÜÇGEN KOŞULU",
                "question": "A ve B merkezli çemberlerin yarıçapları birbirine eşit (r1 = r2 = 8 cm), ancak merkezler arasındaki uzaklık |AB| = 10 cm'dir. Kesişim noktası C ile kurulan ABC üçgeni nasıldır?",
                "options": [
                    {"label": "A) |AC| = |BC| = 8 cm ve |AB| = 10 cm olan bir İkizkenar Üçgendir.", "correct": True},
                    {"label": "B) Eşkenar üçgendir.", "correct": False},
                    {"label": "C) Dik üçgendir.", "correct": False}
                ]
            },
            {
                "id": 3,
                "tag": "ÇEŞİTKENAR ÜÇGEN ÇIKARIMI",
                "question": "r1 = 7 cm, r2 = 9 cm ve merkezler arası uzaklık |AB| = 11 cm olan iki çemberin kesişim noktası C ile oluşan üçgenin kenar özelliği nedir?",
                "options": [
                    {"label": "A) İki kenarı eşittir.", "correct": False},
                    {"label": "B) Üç kenar uzunluğu da birbirinden farklı bir Çeşitkenar Üçgendir.", "correct": True},
                    {"label": "C) Eşkenar üçgendir.", "correct": False}
                ]
            }
        ],
        "extra_questions": [
            {
                "id": 1,
                "tag": "YENİ NESİL • ÖKLİD'İN 1. ÖNERMESİ VE PERGEL",
                "scenario": "Bir mimarlık ofisinde logo tasarlayan Kerem, pergel açıklığını 10 cm'ye ayarlayarak A merkezli bir çember çiziyor. Pergel açıklığını hiç bozmadan pergelin iğneli ucunu çember üzerindeki B noktasına batırıp ikinci bir çember çiziyor. İki çember C ve D noktalarında kesişiyor.",
                "stem": "Kerem düz cetvel ile A, B ve C noktalarını birleştirdiğinde oluşan ABC üçgeninin kenar özellikleri hakkında hangisi kesinlikle doğrudur?",
                "choices": [
                    "|AB| = |AC| = |BC| = 10 cm olup üçgen kesinlikle Eşkenar Üçgendir.",
                    "|AC| = 10 cm, |BC| = 10 cm fakat |AB| = 20 cm olan ikizkenar üçgendir.",
                    "Açıları 90°, 45°, 45° olan ikizkenar dik üçgendir.",
                    "Çeşitkenar bir üçgendir."
                ],
                "correctIndex": 0,
                "explanation": "B noktası A merkezli çember üzerinde olduğundan |AB| = 10 cm'dir. C noktası hem A merkezli hem de B merkezli çember üzerinde olduğundan |AC| = 10 cm ve |BC| = 10 cm'dir. Üç kenar eşit olduğundan eşkenar üçgendir (Öklid'in 1. Önermesi)."
            },
            {
                "id": 2,
                "tag": "YENİ NESİL • YAŞAM ÇİÇEĞİ MOTİFİ",
                "scenario": "Geleneksel Selçuklu ve Osmanlı taş süslemelerinde kullanılan 'Yaşam Çiçeği' motifinde, eş yarıçaplı çemberler birbirlerinin merkezlerinden geçecek şekilde ardışık olarak çizilir.",
                "stem": "Bu motifte bir çemberin merkezinden geçen diğer iki eş çemberin kesişim noktaları birleştirildiğinde oluşan temel geometrik çokgen hangisidir?",
                "choices": [
                    "Kare",
                    "Eşkenar Üçgen ve Düzgün Altıgen örüntüsü",
                    "Dikdörtgen",
                    "Yalnızca Çeşitkenar Üçgen"
                ],
                "correctIndex": 1,
                "explanation": "Eş yarıçaplı çemberlerin merkezleri ve kesişim noktaları birleştirildiğinde kenarları çember yarıçapına (r) eşit olan eşkenar üçgenler ve bunların birleşimiyle düzgün altıgenler oluşur."
            },
            {
                "id": 3,
                "tag": "YENİ NESİL • ÇEMBER KESİŞİMİNDE İKİZKENARLIK",
                "scenario": "Düzlemde merkezleri arasındaki uzaklık 12 cm olan K ve L merkezli iki çember çiziliyor. Çemberlerin yarıçapları birbirine eşit ve r = 9 cm'dir. İki çember M noktasında kesişmektedir.",
                "stem": "Buna göre KLM üçgeninin çevresi kaç santimetredir ve kenarlarına göre çeşidi nedir?",
                "choices": [
                    "Çevre = 30 cm, İkizkenar Üçgen (|KM| = |LM| = 9 cm, |KL| = 12 cm)",
                    "Çevre = 27 cm, Eşkenar Üçgen",
                    "Çevre = 36 cm, Çeşitkenar Üçgen",
                    "Çevre = 24 cm, Dik Üçgen"
                ],
                "correctIndex": 0,
                "explanation": "M noktası her iki çember üzerinde olduğundan |KM| = 9 cm ve |LM| = 9 cm'dir. Taban |KL| = 12 cm'dir. Çevre = 9 + 9 + 12 = 30 cm olup iki kenarı eşit olduğundan İkizkenar Üçgendir."
            },
            {
                "id": 4,
                "tag": "YENİ NESİL • ÇEŞİTKENAR ÜÇGEN İNŞASI",
                "scenario": "Bir robotik kol, P merkezli 15 cm yarıçaplı bir daire ve R merkezli 11 cm yarıçaplı bir daire çiziyor. P ve R merkezleri arasındaki uzaklık 18 cm olarak ayarlanıyor. İki dairenin kesişim noktalarından biri S olarak işaretleniyor.",
                "stem": "PRS üçgeninin kenar uzunlukları sırasıyla |PR|, |PS| ve |RS| hangisinde doğru verilmiştir?",
                "choices": [
                    "18 cm, 15 cm, 11 cm (Çeşitkenar Üçgen)",
                    "15 cm, 15 cm, 11 cm (İkizkenar Üçgen)",
                    "18 cm, 18 cm, 18 cm (Eşkenar Üçgen)",
                    "11 cm, 11 cm, 11 cm"
                ],
                "correctIndex": 0,
                "explanation": "|PR| merkezler arası mesafe olup 18 cm'dir. S noktası P merkezli çemberde olduğundan |PS| = 15 cm, R merkezli çemberde olduğundan |RS| = 11 cm'dir. Kenarları 18, 15, 11 cm olan çeşitkenar üçgendir."
            },
            {
                "id": 5,
                "tag": "YENİ NESİL • ÇEMBERLERİN KESİŞMEME DURUMU",
                "scenario": "Zeynep, defterine aralarında 16 cm uzaklık bulunan A ve B noktalarını işaretliyor. A merkezli 6 cm yarıçaplı bir çember, B merkezli ise 7 cm yarıçaplı bir çember çiziyor.",
                "stem": "Zeynep bu iki çemberin kesişim noktasını kullanarak bir üçgen inşa edebilir mi? Neden?",
                "choices": [
                    "İnşa edebilir; çemberler daima kesişir.",
                    "İnşa edemez; çünkü yarıçaplar toplamı (6 + 7 = 13 cm), merkezler arası uzaklıktan (16 cm) küçük olduğu için çemberler hiç kesişmez.",
                    "İnşa edebilir; eşkenar üçgen oluşur.",
                    "İnşa edebilir; dik üçgen oluşur."
                ],
                "correctIndex": 1,
                "explanation": "İki çemberin kesişebilmesi için yarıçaplar toplamının merkezler arası uzaklıktan büyük veya eşit olması gerekir. 6 + 7 = 13 < 16 olduğundan çemberler ayrık kalır, kesişim noktası oluşmaz."
            },
            {
                "id": 6,
                "tag": "YENİ NESİL • TEĞET ÇEMBERLER VE DOĞRUSALLIK",
                "scenario": "Merkezleri arasındaki uzaklık 14 cm olan iki çemberin yarıçapları 8 cm ve 6 cm'dir. Bu iki çember dıştan birbirine tek bir noktada değmektedir (teğettir).",
                "stem": "Bu iki çemberin merkezleri ve ortak değme noktası birleştirildiğinde bir üçgen oluşur mu?",
                "choices": [
                    "Evet, dar açılı üçgen oluşur.",
                    "Hayır; merkezler ve değme noktası aynı doğru üzerinde (doğrusal) yer aldığından üçgen oluşmaz (8 + 6 = 14 cm).",
                    "Evet, ikizkenar üçgen oluşur.",
                    "Evet, dik üçgen oluşur."
                ],
                "correctIndex": 1,
                "explanation": "Yarıçaplar toplamı merkezler arası mesafeye eşit olduğunda (8 + 6 = 14 cm) çemberler tek noktada teğettir ve üç nokta doğrusaldır; üçgen oluşabilmesi için noktaların doğrusal olmaması gerekir."
            },
            {
                "id": 7,
                "tag": "YENİ NESİL • ÇİFT KESİŞİM VE DÖRTGEN İLİŞKİSİ",
                "scenario": "A ve B merkezli eş iki çember (r = 10 cm, |AB| = 10 cm) iki farklı noktada (C ve D) kesişiyor. A, C, B ve D noktaları sırasıyla birleştirilerek ACBD dörtgeni oluşturuluyor.",
                "stem": "Oluşan ACBD dörtgeni hakkında hangisi doğrudur?",
                "choices": [
                    "Dört kenarı da 10 cm olan bir Eşkenar Dörtgendir (iki eşkenar üçgenin taban tabana birleşimi).",
                    "Bir karedir; tüm açıları 90 derecedir.",
                    "Kenarları farklı olan bir yamuktur.",
                    "Yalnızca bir dikdörtgendir."
                ],
                "correctIndex": 0,
                "explanation": "|AC| = |BC| = |AD| = |BD| = 10 cm olduğundan dört kenarı da eşittir. ABC ve ABD eşkenar üçgenlerinin birleşimidir; yani eşkenar dörtgendir."
            },
            {
                "id": 8,
                "tag": "YENİ NESİL • ÖLÇÜSÜZ CETVEL VE PERGEL MUHAKEMESİ",
                "scenario": "Eski Yunan matematikçileri açıölçer (iletki) kullanmadan, yalnızca ölçüsüz düz tahta (çizgeç) ve pergel yardımıyla 60°'lik açı inşa edebiliyorlardı.",
                "stem": "Ölçüsüz araçlarla 60°'lik açının inşa edilebilmesinin temel matematiksel gerekçesi nedir?",
                "choices": [
                    "Çember kesişimi ile inşa edilen eşkenar üçgenin tüm iç açılarının 60° olması.",
                    "Pergelin üzerinde derece çizgileri bulunması.",
                    "Düz tahtanın 60 cm uzunluğunda olması.",
                    "Gönye ile ölçüm yapılması."
                ],
                "correctIndex": 0,
                "explanation": "Öklid'in 1. Önermesi ile çizilen eşkenar üçgenin her bir iç açısı tam 60°'dir. Böylece açıölçer olmadan tam 60°'lik açı elde edilir."
            },
            {
                "id": 9,
                "tag": "YENİ NESİL • MERKEZLER ARASI MESAFEYİ DEĞİŞTİRME",
                "scenario": "Bir bilgisayar yazılımında iki eş çemberin yarıçapları 10 birim olarak sabit tutuluyor. Merkezler arası uzaklık (|AB|) 1 birimden başlayıp 19 birime kadar artırılıyor.",
                "stem": "Bu süreçte merkezler ve kesişim noktasıyla oluşan ABC üçgeninin tepe açısı ve kenarları nasıl değişir?",
                "choices": [
                    "|AB| arttıkça üçgen önce ikizkenar, |AB|=10 olduğunda eşkenar, sonra tekrar ikizkenar olur; |AB|>=20 olduğunda üçgen oluşmaz.",
                    "Üçgen daima eşkenar kalır.",
                    "Üçgen daima çeşitkenardır.",
                    "Merkezler arası mesafe değiştikçe yarıçaplar da küçülür."
                ],
                "correctIndex": 0,
                "explanation": "Yarıçaplar sabit (10 br) olduğundan |AC| = |BC| = 10 br daima eşittir (ikizkenar). Yalnızca |AB| = 10 olduğunda eşkenar olur. |AB| >= 20 olduğunda çemberler kesişmez."
            },
            {
                "id": 10,
                "tag": "YENİ NESİL • LOGO VE AMBLEM TASARIMI",
                "scenario": "Bir spor kulübü, birbiriyle kesişen 3 adet eş çember kullanarak bir logo tasarlıyor. Çemberlerin merkezleri bir eşkenar üçgenin köşeleridir.",
                "stem": "Bu logonun simetrik ve dengeli olmasını sağlayan temel geometrik kural hangisidir?",
                "choices": [
                    "Her bir çemberin diğer iki çemberin merkezinden geçmesi ve merkezlerin birbirine eşit uzaklıkta olması.",
                    "Çemberlerin farklı yarıçaplarda çizilmesi.",
                    "Merkezlerin doğrusal bir hat üzerinde sıralanması.",
                    "Çemberlerin birbirine hiç değmemesi."
                ],
                "correctIndex": 0,
                "explanation": "Eşkenar üçgen simetrisi, merkezlerin birbirine eşit uzaklıkta olması ve çemberlerin birbirlerinin merkezlerinden geçmesiyle kusursuz geometrik dengeyi sağlar."
            }
        ]
    }
]
