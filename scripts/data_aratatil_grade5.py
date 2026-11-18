# 5. Sınıf 1. Ara Tatil Özel Pekiştirme Modülü Verisi
GRADE5_ARATATIL_1 = {
    "grade": 5,
    "week": 9.5,
    "file_id": "5hafta-aratatil-1",
    "week_label": "1. ARA TATİL",
    "footer_label": "1. Ara Tatil (Pekiştirme)",
    "title": "1. Ara Tatil Geometri ve Sayılar Keşif Kampı",
    "date": "16–20 Kasım",
    "hours": "Ara Tatil Özel",
    "theme": "ARA TATİL ÖZEL: PEKİŞTİRME & KEŞİF KAMPI",
    "outcome_code": "MAT.5.ARA-1",
    "outcome_text": "1-9. Haftalar arası temel geometrik çizimler, açılar, çember inşası, üçgen çeşitleri ve çok basamaklı sayılar konularını pekiştirebilme.",
    "process_items": [
        "Temel geometrik çizim araçlarını (cetvel, pergel, gönye, iletki) kullanarak çizimler yapar.",
        "Açı ölçülerini ve çeşitlerini (dar, dik, geniş) belirler.",
        "Kesişen çemberlerle inşa edilen üçgenlerin kenar özelliklerini karşılaştırır.",
        "Çok basamaklı sayıların bölüklerini ve basamak değerlerini çözümler."
    ],
    "meb_quote": "Ara tatil döneminde öğrencilerin 1. temada edindikleri geometri ve sayılar kazanımlarını pekiştirmeleri; pergel ve cetvel ile üçgen inşası, açı sınıflandırması ve çok basamaklı sayı çözümlemelerini içeren bütüncül aktif öğrenme laboratuvarı.",
    "sim_steps": [
        {
            "tag": "GEOMETRİK İNŞA PEKİŞTİRME",
            "title": "Görev 1: Pergel ve Cetvel ile Doğru Parçası / Işın Ölçümü",
            "instruction": "Sürgüyle [AB] doğru parçasının uzunluğunu değiştirin. Farklı uzunlukları '📋 Gözlemi Kaydet' ile tabloya kaydedin. Cetvel ile ölçülebilir doğru parçası ile sınırsız ışın arasındaki farkı gözlemleyin.",
            "hint": "[AB] doğru parçasının iki ucu sınırlıdır ve uzunluğu ölçülebilir; [AC ışını ise sonsuza uzanır.",
            "hypotheses": [
                {"text": "İki ucu sınırlı olan doğru parçasının uzunluğu cetvelle tam ölçülebilir; ışın sonsuza uzandığı için boyu ölçülemez.", "correct": True},
                {"text": "Hem ışın hem de doğru parçası cetvelle baştan sona ölçülebilir.", "correct": False}
            ],
            "conjectures": [
                {"text": "Doğru parçası [AB] sınırlı uzunluğa sahiptir; ışın [AC tek yönde sınırsızdır. Yalnızca doğru parçası cetvelle ölçülebilir.", "correct": True},
                {"text": "Işın ve doğru parçası tamamen aynı kavramdır.", "correct": False}
            ],
            "sliderLabel": "|AB| Doğru Parçası Uzunluğu:",
            "min": 2, "max": 10, "defaultVal": 5, "unit": "birim",
            "simType": "ruler_line",
            "hasSecondary": False
        },
        {
            "tag": "AÇI TÜRLERİ PEKİŞTİRME",
            "title": "Görev 2: İletki ile Dar, Dik ve Geniş Açı Keşfi",
            "instruction": "Dönme açısını sürgüyle değiştirin (15° - 165°). 90° referansına göre açının dar, dik veya geniş olma durumlarını tabloya kaydedin.",
            "hint": "0° < Dar Açı < 90°, Dik Açı = 90°, 90° < Geniş Açı < 180°.",
            "hypotheses": [
                {"text": "90°'den küçük açılar dar, tam 90° dik, 90°'den büyük açılar geniş açıdır.", "correct": True},
                {"text": "Açının kolları uzatıldığında açı derecesi de büyür.", "correct": False}
            ],
            "conjectures": [
                {"text": "Açı ışının dönme miktarıdır; kol uzunluğundan bağımsızdır. 90° dik, küçükler dar, büyükler geniş açıdır.", "correct": True},
                {"text": "Tüm üçgenlerde en az 2 tane geniş açı bulunabilir.", "correct": False}
            ],
            "sliderLabel": "Dönme Açısı m(ABC):",
            "min": 15, "max": 165, "defaultVal": 90, "unit": "derece",
            "simType": "angle_draw",
            "hasSecondary": False
        },
        {
            "tag": "ÇEMBER VE ÜÇGEN PEKİŞTİRME",
            "title": "Görev 3: Kesişen Çemberlerle Eşkenar ve İkizkenar İnşası",
            "instruction": "r1 ve r2 yarıçaplarını 140 px (|AB| mesafesi) yaparak eşkenar üçgen, 110 px yaparak ikizkenar üçgen oluşturun ve kaydedin.",
            "hint": "r1 = r2 = |AB| ➔ Eşkenar Üçgen (Öklid 1. Önermesi). r1 = r2 ≠ |AB| ➔ İkizkenar Üçgen.",
            "hypotheses": [
                {"text": "Yarıçaplar merkezler arası mesafeye eşit olduğunda eşkenar, mesafeden farklı ama birbirine eşit olduğunda ikizkenar üçgen oluşur.", "correct": True},
                {"text": "Çember kesişimlerinden yalnızca çeşitkenar üçgen elde edilir.", "correct": False}
            ],
            "conjectures": [
                {"text": "Kesişen eş çemberler yarıçap özellikleri sayesinde cetvelde sayı olmadan kusursuz eşkenar veya ikizkenar üçgen inşa etmeyi sağlar.", "correct": True},
                {"text": "Yarıçaplar eşitse üçgenin tüm açıları daima 90 derecedir.", "correct": False}
            ],
            "sliderLabel": "Yarıçap r1 (|AB| = 140 px):",
            "min": 80, "max": 180, "defaultVal": 140, "unit": "px",
            "simType": "euclid_flower",
            "hasSecondary": True,
            "sliderLabel2": "Yarıçap r2:",
            "min2": 80, "max2": 180, "defaultVal2": 140, "unit2": "px"
        },
        {
            "tag": "ÇOK BASAMAKLI SAYILAR",
            "title": "Görev 4: Milyonlar Bölüğü ve Basamak Çözümleme",
            "instruction": "Sürgüyle 7 basamaklı bir sayı belirleyin. Milyonlar, binler ve birler bölüklerini inceleyip tabloya kaydedin.",
            "hint": "Sayılar sağdan sola üçerli bölüklere ayrılır: Birler, Binler, Milyonlar. Her bölük kendi içinde okunur ve bölük adıyla tamamlanır.",
            "hypotheses": [
                {"text": "Çok basamaklı sayılar sağdan sola üçerli bölük gruplarına ayrılarak okunur; birler bölüğünün adı söylenmez.", "correct": True},
                {"text": "Sayılar soldan sağa dörderli basamak grupları halinde okunur.", "correct": False}
            ],
            "conjectures": [
                {"text": "Bölük sistemi sayesinde milyonlarca basamaklı sayılar üçerli bloklar halinde kolayca okunur ve basamak değerleri çözümlenir.", "correct": True},
                {"text": "Bir sayıda rakamın sayı değeri ile basamak değeri daima aynıdır.", "correct": False}
            ],
            "sliderLabel": "Sayı Değeri (Milyonlar):",
            "min": 1000000, "max": 9000000, "defaultVal": 5420100, "unit": "",
            "simType": "place_value_blocks",
            "hasSecondary": False
        }
    ],
    "mini_tasks": [
        {
            "id": 1,
            "tag": "TEMEL GEOMETRİ",
            "question": "Aşağıdaki ifadelerden hangisi daima doğrudur?",
            "options": [
                {"label": "A) İki ucu sınırlı [AB] doğru parçasının uzunluğu cetvelle tam ölçülebilir.", "correct": True},
                {"label": "B) Işının iki ucu da sınırlıdır.", "correct": False},
                {"label": "C) Doğrunun bir ucu sınırlıdır.", "correct": False}
            ]
        },
        {
            "id": 2,
            "tag": "ÜÇGEN İNŞASI",
            "question": "A ve B merkezli iki çemberin yarıçapları r1 = r2 = |AB| = 8 cm'dir. Kesişim noktası C ile oluşan ABC üçgeninin çeşidi nedir?",
            "options": [
                {"label": "A) Eşkenar Üçgen (Tüm kenarları 8 cm)", "correct": True},
                {"label": "B) İkizkenar Dik Üçgen", "correct": False},
                {"label": "C) Çeşitkenar Üçgen", "correct": False}
            ]
        },
        {
            "id": 3,
            "tag": "BÖLÜK OKUMA",
            "question": "45.008.203 sayısının binler bölüğündeki sayı kaçtır?",
            "options": [
                {"label": "A) 8 (veya 008)", "correct": True},
                {"label": "B) 45", "correct": False},
                {"label": "C) 203", "correct": False}
            ]
        }
    ],
    "extra_questions": [
        {
            "id": 1,
            "tag": "ARA TATİL • PERGEL VE ÇEMBER",
            "scenario": "Kerem ara tatil projesinde pergel açıklığını 6 cm yaparak bir çember çiziyor. Çemberin merkezini O olarak işaretliyor.",
            "stem": "Kerem'in çizdiği çemberin çapı (R) kaç santimetredir?",
            "choices": ["12 cm (Çap = 2 x Yarıçap)", "6 cm", "18 cm", "3 cm"],
            "correctIndex": 0,
            "explanation": "Çap, yarıçapın 2 katıdır: R = 2 x 6 = 12 cm'dir."
        },
        {
            "id": 2,
            "tag": "ARA TATİL • İLETKİ VE AÇI ÇEŞİDİ",
            "scenario": "Bir açının ölçüsü iletki ile 89° olarak ölçülmüştür.",
            "stem": "Bu açı hangi açı türüne girer?",
            "choices": ["Dar Açı (0° ile 90° arasında)", "Dik Açı", "Geniş Açı", "Doğru Açı"],
            "correctIndex": 0,
            "explanation": "Ölçüsü 90°'den küçük olan tüm pozitif açılar Dar Açıdır. 89° dar açıdır."
        },
        {
            "id": 3,
            "tag": "ARA TATİL • DİKME VE EN KISA UZAKLIK",
            "scenario": "Bir P noktasından d doğrusuna çizilen doğru parçalarından en kısa olanı doğruyla 90° açı yapmaktadır.",
            "stem": "Bu doğru parçasına ne ad verilir ve hangi sembolle gösterilir?",
            "choices": ["Dikme ([PH] ⊥ d)", "Paralel doğru", "Işın", "Geniş açı"],
            "correctIndex": 0,
            "explanation": "Bir noktanın bir doğruya en kısa mesafesi doğruya dik olarak indirilen dikmedir ve ⊥ sembolüyle gösterilir."
        },
        {
            "id": 4,
            "tag": "ARA TATİL • ÇOK BASAMAKLI SAYI OKUMA",
            "scenario": "Türkiye'nin yüz ölçümü göller dahil yaklaşık 783.562 km²'dir.",
            "stem": "Bu sayının binler bölüğündeki sayı kaçtır?",
            "choices": ["783", "562", "78", "356"],
            "correctIndex": 0,
            "explanation": "783.562 sayısında binler bölüğü 783, birler bölüğü 562'dir."
        },
        {
            "id": 5,
            "tag": "ARA TATİL • BASAMAK DEĞERİ",
            "scenario": "84.392.105 sayısında 4 rakamının bulunduğu basamak 'Milyonlar' basamağıdır.",
            "stem": "4 rakamının basamak değeri kaçtır?",
            "choices": ["4.000.000 (Dört Milyon)", "40.000.000", "400.000", "40.000"],
            "correctIndex": 0,
            "explanation": "Milyonlar basamağındaki 4 rakamının basamak değeri 4 x 1.000.000 = 4.000.000'dur."
        },
        {
            "id": 6,
            "tag": "ARA TATİL • ÖKLİD 1. ÖNERMESİ",
            "scenario": "Öklid'in Elements kitabının 1. Önermesi, cetvelde sayı bölmeleri olmadan sadece pergel ve düz çizgeçle bir geometrik şekil inşa etmeyi anlatır.",
            "stem": "Bu inşada elde edilen geometrik şekil hangisidir?",
            "choices": ["Eşkenar Üçgen", "Kare", "Dik Üçgen", "Yamuk"],
            "correctIndex": 0,
            "explanation": "Birbirinin merkezinden geçen eş yarıçaplı iki çemberin kesişimiyle kenarları yarıçapa eşit bir Eşkenar Üçgen inşa edilir."
        },
        {
            "id": 7,
            "tag": "ARA TATİL • ÜÇGENİN İÇ AÇILARI",
            "scenario": "Bir üçgenin iki iç açısının ölçüleri 45° ve 65° olarak ölçülmüştür.",
            "stem": "Üçüncü açının ölçüsü kaç derecedir ve açılarına göre üçgen türü nedir?",
            "choices": ["70° — Dar Açılı Üçgen (180 - [45+65] = 70)", "80° — Dik Üçgen", "90° — Dik Üçgen", "60° — Geniş Açılı Üçgen"],
            "correctIndex": 0,
            "explanation": "Üçgenin iç açıları toplamı 180°'dir. 45 + 65 = 110°. 180 - 110 = 70°. Üç açı da 90°'den küçük olduğu için dar açılı üçgendir."
        },
        {
            "id": 8,
            "tag": "ARA TATİL • PARALEL DOĞRULAR",
            "scenario": "Bir tren rayının iki çelik hattı boyunca uzanan doğrular hiçbir noktada kesişmez ve aralarındaki mesafe daima sabittir.",
            "stem": "Bu iki doğrunun geometrik konumu nedir ve hangi sembolle gösterilir?",
            "choices": ["Paralel Doğrular (d1 // d2)", "Kesişen Doğrular", "Dik Kesişen Doğrular (⊥)", "Çakışık Doğrular"],
            "correctIndex": 0,
            "explanation": "Düzlemde kesişmeyen ve aralarındaki uzaklık daima sabit olan doğrulara paralel doğrular denir ve // sembolüyle gösterilir."
        },
        {
            "id": 9,
            "tag": "ARA TATİL • BASAMAK DEĞERLERİ TOPLAMI",
            "scenario": "Bir sayının çözümlenmiş hali: (6 x 1.000.000) + (5 x 10.000) + (3 x 100) + (7 x 1) olarak verilmiştir.",
            "stem": "Bu sayı aşağıdakilerden hangisidir?",
            "choices": ["6.050.307", "6.500.370", "6.053.007", "6.503.070"],
            "correctIndex": 0,
            "explanation": "Milyonlar: 6, Yüz binler: 0, On binler: 5, Binler: 0, Yüzler: 3, Onlar: 0, Birler: 7 ➔ 6.050.307."
        },
        {
            "id": 10,
            "tag": "ARA TATİL • DÜZGÜN ÇOKGENLER",
            "scenario": "Tüm kenar uzunlukları ve tüm iç açı ölçüleri birbirine eşit olan çokgenlere düzgün çokgen denir.",
            "stem": "Buna göre düzgün üçgen ve düzgün dörtgenin özel adları sırasıyla hangisidir?",
            "choices": ["Eşkenar Üçgen — Kare", "İkizkenar Üçgen — Dikdörtgen", "Çeşitkenar Üçgen — Eşkenar Dörtgen", "Dik Üçgen — Kare"],
            "correctIndex": 0,
            "explanation": "Düzgün 3-gen Eşkenar Üçgen (tüm açıları 60°), düzgün 4-gen ise Kare'dir (tüm açıları 90°)."
        }
    ]
}
