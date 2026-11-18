# 7. Sınıf 1. Ara Tatil Özel Pekiştirme Modülü Verisi
GRADE7_ARATATIL_1 = {
    "grade": 7,
    "week": 9.5,
    "file_id": "7hafta-aratatil-1",
    "week_label": "1. ARA TATİL",
    "footer_label": "1. Ara Tatil (Pekiştirme)",
    "title": "1. Ara Tatil Rasyonel Sayılar, 3B Yapılar ve Prizmalar Kampı",
    "date": "16–20 Kasım",
    "hours": "Ara Tatil Özel",
    "theme": "ARA TATİL ÖZEL: PEKİŞTİRME & KEŞİF KAMPI",
    "outcome_code": "MAT.7.ARA-1",
    "outcome_text": "1-9. Haftalar arası tam sayılar, rasyonel sayılarda dört işlem ve modelleme, eş küplerle 3B yapılar ve dikdörtgenler prizmasının yüzey alanı / hacim bağıntısını pekiştirebilme.",
    "process_items": [
        "Tam sayılar ve rasyonel sayıları sayı doğrusunda modeller.",
        "Rasyonel sayılarla çarpma işlemini alan modeliyle çözümler.",
        "Eş küplerle oluşturulan yapıların farklı yönlerden görünümlerini ilişkilendirir.",
        "Dikdörtgenler prizmasının açınımından yüzey alanını ve birim küplerle hacmini hesaplar."
    ],
    "meb_quote": "Ara tatil döneminde öğrencilerin 1. ve 4. temalarda edindikleri rasyonel sayılar, alan modeliyle çarpma, eş küplerle 3B görünümler ve prizmaların yüzey alanı / hacim bağıntısını pekiştirmeleri; dinamik sayı doğrusu, izometrik izdüşüm ve prizma açınımı laboratuvarı.",
    "sim_steps": [
        {
            "tag": "SAYI DOĞRUSUNDA RASYONEL SAYILAR",
            "title": "Görev 1: Rasyonel Sayıların Sayı Doğrusundaki Yeri",
            "instruction": "Pay ve payda sürgülerini değiştirerek pozitif ve negatif rasyonel sayıların sayı doğrusundaki yerini inceleyin ve tabloya kaydedin.",
            "hint": "Sayı doğrusunda 0'ın sağı pozitif, solu negatif rasyonel sayılardır. Sağdaki sayı daima soldakinden büyüktür.",
            "hypotheses": [
                {"text": "Negatif rasyonel sayılarda 0'a daha yakın olan sayı diğerinden daha büyüktür (ör. -1/4 > -3/4).", "correct": True},
                {"text": "Negatif sayılarda sayı değeri büyük olan daima daha büyüktür.", "correct": False}
            ],
            "conjectures": [
                {"text": "Sayı doğrusu üzerinde sağa gidildikçe sayılar büyür; negatif rasyonel sayılarda mutlak değeri küçük olan sayı daha büyüktür.", "correct": True},
                {"text": "Pozitif ve negatif rasyonel sayılar aynı sıralama kuralına uyar.", "correct": False}
            ],
            "sliderLabel": "Pay Değeri (a):",
            "min": -8, "max": 8, "defaultVal": -3, "unit": "",
            "simType": "rational_line",
            "hasSecondary": True,
            "sliderLabel2": "Payda Değeri (b):",
            "min2": 2, "max2": 8, "defaultVal2": 4, "unit2": ""
        },
        {
            "tag": "ALAN MODELİYLE ÇARPMA",
            "title": "Görev 2: Rasyonel Sayılarla Çarpmanın Alan Modeli",
            "instruction": "En (n1/4) ve boy (n2/3) kesirlerini sürgülerle belirleyin. Ortak kesişen taralı alanın çarpım sonucuna eşitliğini gözlem tablosuna kaydedin.",
            "hint": "(a/b) x (c/d) = (a x c) / (b x d). Kesişen alan modelinde payların çarpımı boyalı kutu, paydaların çarpımı toplam kutu sayısıdır.",
            "hypotheses": [
                {"text": "İki basit kesrin çarpımı her iki çarpandan da daha küçük bir sonuç verir (0 ile 1 arasında küçülür).", "correct": True},
                {"text": "Çarpma işlemi sayıları daima büyütür.", "correct": False}
            ],
            "conjectures": [
                {"text": "Alan modeli kesirlerle çarpmanın mantığını somutlaştırır; iki basit kesir çarpıldığında sonuç çarpanlardan daha küçük bir bütünü ifade eder.", "correct": True},
                {"text": "Kesirlerle çarpma yaparken paydalar eşitlenmelidir.", "correct": False}
            ],
            "sliderLabel": "En Kesri Payı (n1/4):",
            "min": 1, "max": 4, "defaultVal": 3, "unit": "",
            "simType": "rational_mult",
            "hasSecondary": True,
            "sliderLabel2": "Boy Kesri Payı (n2/3):",
            "min2": 1, "max2": 3, "defaultVal2": 2, "unit2": ""
        },
        {
            "tag": "3B YAPILAR VE İZDÜŞÜMLER",
            "title": "Görev 3: Eş Küplerle Yapı ve 2B İzdüşüm Görünümleri",
            "instruction": "Küp sayısını değiştirin. Önden, üstten ve sağdan bakıldığında kaç kare görüldüğünü tabloya kaydedin.",
            "hint": "3 boyutlu yapılar tek bir yönden görünümle tam anlaşılamaz; en az 3 farklı yönün (ön, üst, sağ) ortak kesişimi gereklidir.",
            "hypotheses": [
                {"text": "Önden görünüm ile sağdan görünüm yapının derinliğini ve yüksekliğini farklı açılardan gösterir.", "correct": True},
                {"text": "Tüm yönlerden bakıldığında görülen kare sayısı daima eşittir.", "correct": False}
            ],
            "conjectures": [
                {"text": "Sağ-sol ve ön-arka görünümleri karşılıklı simetriktir; üstten görünüm zemin tabanını verir.", "correct": True},
                {"text": "Tek bir görünüm yapının kaç küpten oluştuğunu kesin olarak belirler.", "correct": False}
            ],
            "sliderLabel": "Eş Küp Sayısı:",
            "min": 1, "max": 6, "defaultVal": 4, "unit": "küp",
            "simType": "isometric_cubes",
            "hasSecondary": False
        },
        {
            "tag": "PRİZMA ALAN VE HACİM",
            "title": "Görev 4: Dikdörtgenler Prizması Açınımı ve Hacim Bağıntısı",
            "instruction": "Ayrıtları sürgülerle değiştirin (a x b x 2). 6 yüzeyin alanını ve birim küplerle hacmi (V = a x b x c) hesaplayıp tabloya kaydedin.",
            "hint": "Yüzey Alanı = 2(ab + ac + bc). Hacim = Taban Alanı x Yükseklik = a x b x c.",
            "hypotheses": [
                {"text": "Dikdörtgenler prizmasının hacmi taban alanı ile yüksekliğin çarpımına, yüzey alanı ise açınımdaki 6 yüzün alanları toplamına eşittir.", "correct": True},
                {"text": "Hacim ve alan birbirine eşit birimlerdir.", "correct": False}
            ],
            "conjectures": [
                {"text": "Prizmalarda Hacim = Taban Alanı × Yükseklik (V = a×b×c) temel bağıntıdır; birim küp sayısına denk gelir.", "correct": True},
                {"text": "Küpün hacmi formülle hesaplanamaz.", "correct": False}
            ],
            "sliderLabel": "Taban Eni (a br):",
            "min": 2, "max": 6, "defaultVal": 4, "unit": "br",
            "simType": "prism_net_volume",
            "hasSecondary": True,
            "sliderLabel2": "Taban Boyu (b br):",
            "min2": 2, "max2": 6, "defaultVal2": 3, "unit2": "br"
        }
    ],
    "mini_tasks": [
        {
            "id": 1,
            "tag": "RASYONEL SIRALAMA",
            "question": "-3/5 rasyonel sayısı ile -1/5 rasyonel sayısı arasındaki doğru ilişki hangisidir?",
            "options": [
                {"label": "A) -1/5 > -3/5 (0'a daha yakın olan büyüktür)", "correct": True},
                {"label": "B) -3/5 > -1/5", "correct": False},
                {"label": "C) -3/5 = -1/5", "correct": False}
            ]
        },
        {
            "id": 2,
            "tag": "PRİZMA HACMİ",
            "question": "Ayrıtları 3 cm, 4 cm ve 5 cm olan dikdörtgenler prizmasının hacmi kaç cm³'tür?",
            "options": [
                {"label": "A) 3 x 4 x 5 = 60 cm³", "correct": True},
                {"label": "B) 12 cm³", "correct": False},
                {"label": "C) 94 cm³", "correct": False}
            ]
        },
        {
            "id": 3,
            "tag": "3B GÖRÜNÜM",
            "question": "Bir yapının üstten görünümünde 5 kare vardır. Bu yapı en az kaç eş küple oluşturulabilir?",
            "options": [
                {"label": "A) En az 5 eş küp (Her kare için zeminde 1 küp)", "correct": True},
                {"label": "B) En az 1 küp", "correct": False},
                {"label": "C) En az 10 küp", "correct": False}
            ]
        }
    ],
    "extra_questions": [
        {
            "id": 1,
            "tag": "ARA TATİL • RASYONEL SAYILARDA DÖRT İŞLEM",
            "scenario": "Bir su deposunun 3/4'ü doludur. Depodaki suyun 1/3'ü bahçe sulamasında kullanılıyor.",
            "stem": "Kullanılan su miktarı tüm deponun kaçta kaçıdır?",
            "choices": ["1/4'ü (3/4 x 1/3 = 3/12 = 1/4)", "1/2'si", "5/12'si", "2/3'ü"],
            "correctIndex": 0,
            "explanation": "Deponun 3/4'ünün 1/3'ü: (3/4) x (1/3) = 3/12 = 1/4'tür."
        },
        {
            "id": 2,
            "tag": "ARA TATİL • NEGATİF SAYILARDA İŞLEM",
            "scenario": "Hava sıcaklığı sabah -8 °C iken öğlen 13 °C artmış, gece ise 7 °C düşmüştür.",
            "stem": "Gece ölçülen hava sıcaklığı kaç °C'dir?",
            "choices": ["-2 °C (-8 + 13 - 7 = -2)", "2 °C", "-12 °C", "0 °C"],
            "correctIndex": 0,
            "explanation": "-8 + 13 = +5 °C. 5 - 7 = -2 °C'dir."
        },
        {
            "id": 3,
            "tag": "ARA TATİL • PRİZMA YÜZEY ALANI",
            "scenario": "Ayrıtları 2 cm, 3 cm ve 4 cm olan dikdörtgenler prizması hediye kutusu paketlenecektir.",
            "stem": "Kutunun toplam yüzey alanı kaç cm²'dir?",
            "choices": ["52 cm² (2 x [6 + 8 + 12])", "24 cm²", "48 cm²", "64 cm²"],
            "correctIndex": 0,
            "explanation": "Alan = 2 x (2x3 + 2x4 + 3x4) = 2 x (6 + 8 + 12) = 2 x 26 = 52 cm²."
        },
        {
            "id": 4,
            "tag": "ARA TATİL • KÜP HACMİ VE BİRİM KÜPLER",
            "scenario": "Bir ayrıtı 4 cm olan bir küpün içine bir ayrıtı 1 cm olan birim küpler yerleştirilecektir.",
            "stem": "Küpün içine boşluk kalmayacak şekilde kaç adet birim küp sığar?",
            "choices": ["64 adet (4³ = 64)", "16 adet", "32 adet", "96 adet"],
            "correctIndex": 0,
            "explanation": "Küpün hacmi = 4 x 4 x 4 = 64 cm³'tür. 1 cm³'lük küplerden tam 64 adet sığar."
        },
        {
            "id": 5,
            "tag": "ARA TATİL • DEVİRLİ RASYONEL DÖNÜŞÜMÜ",
            "scenario": "0,444... (0,4 devirli) sayısının rasyonel sayı olarak ifadesi sorulmaktadır.",
            "stem": "Bu devirli sayının rasyonel kesir karşılığı hangisidir?",
            "choices": ["4/9", "4/10", "4/90", "2/5"],
            "correctIndex": 0,
            "explanation": "Tek basamağı devreden ondalıklar paydaya 9 yazılarak kesre dönüştürülür: 0,444... = 4/9."
        },
        {
            "id": 6,
            "tag": "ARA TATİL • ÇOK ADIMLI İŞLEMLER",
            "scenario": "(1 - 1/2) x (1 - 1/3) x (1 - 1/4) işleminin sonucu merak edilmektedir.",
            "stem": "Bu çarpma işleminin sonucu kaçtır?",
            "choices": ["1/4 (1/2 x 2/3 x 3/4 = 1/4)", "1/2", "3/8", "1/12"],
            "correctIndex": 0,
            "explanation": "1/2 x 2/3 x 3/4 = ardışık pay ve paydalar sadeleşir ve geriye 1/4 kalır."
        },
        {
            "id": 7,
            "tag": "ARA TATİL • SAĞ-SOL SİMETRİSİ",
            "scenario": "Bir yapının sağdan görünümünde soldan sağa sütun yükseklikleri sırasıyla 1, 2, 3 küptür.",
            "stem": "Bu yapıya soldan bakıldığında sütun yükseklikleri soldan sağa nasıl görünür?",
            "choices": ["3, 2, 1 küp (Ayna simetrisi)", "1, 2, 3 küp", "3, 3, 3 küp", "2, 2, 2 küp"],
            "correctIndex": 0,
            "explanation": "Sağdan ve soldan görünümler birbirinin ayna simetrisidir; sağdan (1, 2, 3) sırası soldan bakışta (3, 2, 1) olur."
        },
        {
            "id": 8,
            "tag": "ARA TATİL • HAVUZ DOLUM VE HACİM",
            "scenario": "Boyutları 5 m, 3 m ve derinliği 2 m olan dikdörtgenler prizması şeklindeki havuzun tamamı su ile doldurulacaktır.",
            "stem": "Bu havuz kaç metreküp (m³) su alır?",
            "choices": ["30 m³ (5 x 3 x 2)", "25 m³", "40 m³", "60 m³"],
            "correctIndex": 0,
            "explanation": "Hacim = 5 x 3 x 2 = 30 metreküptür."
        },
        {
            "id": 9,
            "tag": "ARA TATİL • RASYONEL KUVVET ALMA",
            "scenario": "(-2/3)³ işleminin sonucu hesaplanacaktır.",
            "stem": "İşlemin sonucu kaçtır?",
            "choices": ["-8/27", "+8/27", "-6/9", "+6/9"],
            "correctIndex": 0,
            "explanation": "Negatif sayının tek kuvveti negatiftir: (-2/3) x (-2/3) x (-2/3) = -8/27'dir."
        },
        {
            "id": 10,
            "tag": "ARA TATİL • MAKSİMUM KÜP SAYISI",
            "scenario": "Önden ve sağdan görünümü 3x3'lük kare olan bir yapıda en fazla kaç eş küp bulunabilir?",
            "choices": ["27 küp (3 x 3 x 3 küp bloğu)", "9 küp", "18 küp", "36 küp"],
            "correctIndex": 0,
            "explanation": "3x3 önden ve 3x3 sağdan silueti veren en dolu yapı 3x3x3 boyutundaki tam dolu küptür: 3³ = 27 eş küp."
        }
    ]
}
