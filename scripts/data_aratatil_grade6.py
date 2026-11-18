# 6. Sınıf 1. Ara Tatil Özel Pekiştirme Modülü Verisi
GRADE6_ARATATIL_1 = {
    "grade": 6,
    "week": 9.5,
    "file_id": "6hafta-aratatil-1",
    "week_label": "1. ARA TATİL",
    "footer_label": "1. Ara Tatil (Pekiştirme)",
    "title": "1. Ara Tatil Sayılar, Kesirler ve Olasılık Keşif Kampı",
    "date": "16–20 Kasım",
    "hours": "Ara Tatil Özel",
    "theme": "ARA TATİL ÖZEL: PEKİŞTİRME & KEŞİF KAMPI",
    "outcome_code": "MAT.6.ARA-1",
    "outcome_text": "1-9. Haftalar arası çarpanlar, katlar, bölünebilme, deneysel olasılık, ondalık gösterimler, kesir-bölme ve problem çözme konularını pekiştirebilme.",
    "process_items": [
        "Doğal sayıların çarpanlarını ve katlarını alan modelleri ile belirler.",
        "Bölünebilme kurallarını inceler ve genellemeler yapar.",
        "Deneysel olasılıkta göreli sıklık kavramını çözümler.",
        "Kesir, ondalık ve yüzde dönüşümlerini problem çözmede uygular."
    ],
    "meb_quote": "Ara tatil döneminde öğrencilerin 1. ve 6. temada edindikleri çarpanlar, bölünebilme, deneysel olasılık ve kesir-ondalık-yüzde problemlerini pekiştirmeleri; 100'lük kareli alan modelleri ve dinamik veri tablolarını içeren bütüncül aktif öğrenme laboratuvarı.",
    "sim_steps": [
        {
            "tag": "ÇARPANLAR VE ALAN MODELİ",
            "title": "Görev 1: 24 Birimkarelik Dikdörtgen ile Çarpanları Keşfetme",
            "instruction": "Genişlik sürgüsünü (1-24) hareket ettirerek 24 birimkarelik dikdörtgenler oluşturun. Tam bölünen genişlik ve boy çiftlerini tabloya kaydedin.",
            "hint": "Genişlik x Boy = 24 olduğunda genişlik 24'ün bir çarpanıdır.",
            "hypotheses": [
                {"text": "Bir doğal sayının çarpanları aynı zamanda o sayıyı kalansız bölen tam sayılardır.", "correct": True},
                {"text": "Her doğal sayı sadece 2 çarpana sahiptir.", "correct": False}
            ],
            "conjectures": [
                {"text": "Bir sayının çarpanları ile bölenleri aynı kümedir; 24'ün çarpanları 1, 2, 3, 4, 6, 8, 12, 24'tür.", "correct": True},
                {"text": "24 sayısı tek sayıdır.", "correct": False}
            ],
            "sliderLabel": "Dikdörtgen Genişliği:",
            "min": 1, "max": 12, "defaultVal": 4, "unit": "br",
            "simType": "factor_rect",
            "hasSecondary": False
        },
        {
            "tag": "BÖLÜNEBİLME KURALLARI",
            "title": "Görev 2: 2, 3, 5 ve 9 ile Bölünebilme Sınaması",
            "instruction": "Sürgüyle bir sayı belirleyin (ör. 120). Son basamak ve rakamlar toplamını inceleyip bölünebilme durumlarını gözlem tablosuna kaydedin.",
            "hint": "Son basamak çift ise 2'ye, 0 veya 5 ise 5'e; rakamlar toplamı 3'ün katı ise 3'e, 9'un katı ise 9'a tam bölünür.",
            "hypotheses": [
                {"text": "3 ve 9 ile bölünebilmede rakamlar toplamı, 2 ve 5 ile bölünebilmede ise sadece son basamak belirleyicidir.", "correct": True},
                {"text": "Tüm tek sayılar 5 ile tam bölünür.", "correct": False}
            ],
            "conjectures": [
                {"text": "Bölünebilme kuralları bölme işlemi yapmadan pratik kontrol sağlar; rakamları toplamı 9'un katı olan sayılar 3'e de daima tam bölünür.", "correct": True},
                {"text": "3'e bölünen her sayı 9'a da tam bölünür.", "correct": False}
            ],
            "sliderLabel": "İncelenen Sayı:",
            "min": 12, "max": 180, "defaultVal": 90, "unit": "",
            "simType": "divisibility_test",
            "hasSecondary": False
        },
        {
            "tag": "DENEYSEL OLASILIK",
            "title": "Görev 3: Göreli Sıklık ve Olasılık Spektrumu (0-1)",
            "instruction": "Olay sayısını (0-20) değiştirerek 20 denemedeki göreli sıklığı (% oranını) inceleyin ve tabloya kaydedin.",
            "hint": "Olasılık değeri 0 (İmkansız Olay) ile 1 (Kesin Olay) arasında değer alır.",
            "hypotheses": [
                {"text": "Deneme sayısı arttıkça göreli sıklık olayın teorik olasılık değerine yaklaşır.", "correct": True},
                {"text": "Bir olayın olasılığı 1'den büyük veya negatif olabilir.", "correct": False}
            ],
            "conjectures": [
                {"text": "Deneysel olasılık (Göreli Sıklık) = İstenen Durum / Toplam Deneme oranıyla bulunur ve 0 ile 1 aralığındadır.", "correct": True},
                {"text": "Olasılık değeri %150 olabilir.", "correct": False}
            ],
            "sliderLabel": "Başarılı Olay Sayısı (n):",
            "min": 0, "max": 20, "defaultVal": 10, "unit": "defa",
            "simType": "probability_fraction",
            "hasSecondary": True,
            "sliderLabel2": "Toplam Deneme Sayısı:",
            "min2": 10, "max2": 50, "defaultVal2": 20, "unit2": "defa"
        },
        {
            "tag": "ALIŞVERİŞ VE YÜZDE PROBLEMİ",
            "title": "Görev 4: % İndirim, Ondalık Çarpan ve Net Tutar",
            "instruction": "Etiket fiyatını ve indirim oranını (%10-%50) değiştirerek sağlanan tasarrufu ve ödenecek tutarı tabloya kaydedin.",
            "hint": "%25 indirim = 1/4 = 0,25 tasarruf demektir.",
            "hypotheses": [
                {"text": "%20 indirimli fiyat etiket fiyatının %80'ine (0,80 katına) eşittir.", "correct": True},
                {"text": "%20 indirim fiyattan 20 TL çıkarmak demektir.", "correct": False}
            ],
            "conjectures": [
                {"text": "Kesir, ondalık ve yüzde aynı matematiksel miktarın farklı gösterimleridir; problem çözmede birbirine dönüştürülerek işlem kolaylığı sağlar.", "correct": True},
                {"text": "İndirim hesaplanırken yüzdeler doğrudan çıkarılır.", "correct": False}
            ],
            "sliderLabel": "Etiket Fiyatı (₺):",
            "min": 100, "max": 800, "defaultVal": 400, "unit": "₺",
            "simType": "fraction_discount_problem",
            "hasSecondary": True,
            "sliderLabel2": "İndirim Oranı (%):",
            "min2": 10, "max2": 50, "defaultVal2": 25, "unit2": "%"
        }
    ],
    "mini_tasks": [
        {
            "id": 1,
            "tag": "BÖLÜNEBİLME",
            "question": "34A sayısı hem 2'ye hem de 3'e kalansız bölünebilen 3 basamaklı bir sayıdır. A yerine yazılabilecek en büyük rakam kaçtır?",
            "options": [
                {"label": "A) 8 (3+4+8=15, 3'ün katı ve çift)", "correct": True},
                {"label": "B) 6", "correct": False},
                {"label": "C) 9", "correct": False}
            ]
        },
        {
            "id": 2,
            "tag": "OLASILIK SPEKTRUMU",
            "question": "Bir torbadan rastgele çekilen topun mavi olma olasılığı 0,65 ise, mavi olmama olasılığı kaçtır?",
            "options": [
                {"label": "A) 1 - 0,65 = 0,35", "correct": True},
                {"label": "B) 0,65", "correct": False},
                {"label": "C) 0,45", "correct": False}
            ]
        },
        {
            "id": 3,
            "tag": "YÜZDE VE KESİR",
            "question": "500 TL'lik bir mont %30 indirimle kaç TL'ye satılır?",
            "options": [
                {"label": "A) 500 - 150 = 350 TL", "correct": True},
                {"label": "B) 470 TL", "correct": False},
                {"label": "C) 400 TL", "correct": False}
            ]
        }
    ],
    "extra_questions": [
        {
            "id": 1,
            "tag": "ARA TATİL • ASAL SAYILAR",
            "scenario": "Kerem, 1 ile 30 arasındaki asal sayıları bir kağıda yazıyor.",
            "stem": "Kerem'in listesinde kaç adet asal sayı bulunur?",
            "choices": ["10 tane (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)", "9 tane", "11 tane", "8 tane"],
            "correctIndex": 0,
            "explanation": "1-30 arasındaki asal sayılar: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29 olmak üzere tam 10 tanedir."
        },
        {
            "id": 2,
            "tag": "ARA TATİL • ORTAK BÖLEN (EBOB)",
            "scenario": "Uzunlukları 36 metre ve 48 metre olan iki top kumaş, hiç parça artmayacak şekilde eşit uzunlukta en büyük parçalara kesilecektir.",
            "stem": "Bir parçanın uzunluğu en fazla kaç metre olabilir?",
            "choices": ["12 metre (36 ve 48'in EBOB'u)", "6 metre", "8 metre", "24 metre"],
            "correctIndex": 0,
            "explanation": "36 ve 48'in en büyük ortak böleni 12'dir. Parçalar en fazla 12 metre olabilir."
        },
        {
            "id": 3,
            "tag": "ARA TATİL • ORTAK KAT (EKOK)",
            "scenario": "İki zilden biri 15 dakikada bir, diğeri 20 dakikada bir çalmaktadır. Saat 09.00'da birlikte çalan bu iki zil ilk kez saat kaçta tekrar birlikte çalar?",
            "stem": "İki zilin tekrar birlikte çalacağı saat kaçtır?",
            "choices": ["Saat 10.00 (EKOK(15, 20) = 60 dakika sonra)", "Saat 09.35", "Saat 10.30", "Saat 11.00"],
            "correctIndex": 0,
            "explanation": "EKOK(15, 20) = 60 dakikadır (1 saat). 09.00 + 1 saat = 10.00'da tekrar birlikte çalarlar."
        },
        {
            "id": 4,
            "tag": "ARA TATİL • DEVİRLİ ONDALIK",
            "scenario": "1/3 kesrinin payı paydasına bölündüğünde 0,333... şeklinde sonsuza uzanan bir örüntü elde edilmektedir.",
            "stem": "Bu tür ondalık gösterimlere ne ad verilir ve nasıl gösterilir?",
            "choices": ["Devirli Ondalık Gösterim (3'ün üzerinde çizgi ile)", "Sonlu Ondalık", "Basit Kesir", "Tam Sayı"],
            "correctIndex": 0,
            "explanation": "Bölme işlemi bittiğinde tekrarlayan rakamların üzerine devir çizgisi konur; buna Devirli Ondalık Gösterim denir."
        },
        {
            "id": 5,
            "tag": "ARA TATİL • DENEYSEL VE TEORİK OLASILIK",
            "scenario": "Bir madeni para 50 defa havaya atılmış ve 28 defa tura gelmiştir.",
            "stem": "Tura gelme olayının deneysel olasılığı kaçtır?",
            "choices": ["28/50 = 0,56 (%56)", "1/2 = 0,50", "22/50 = 0,44", "28/100 = 0,28"],
            "correctIndex": 0,
            "explanation": "Deneysel olasılık yapılan deneydeki gerçekleşme oranıdır: 28 / 50 = 0,56 (%56)."
        },
        {
            "id": 6,
            "tag": "ARA TATİL • KESİRLE ÇARPMA MODELİ",
            "scenario": "Bir tarlanın 2/3'ünün 3/4'üne buğday ekilmiştir.",
            "stem": "Buğday ekili alan tüm tarlanın kaçta kaçıdır?",
            "choices": ["1/2 (2/3 x 3/4 = 6/12 = 1/2)", "5/7", "8/9", "1/4"],
            "correctIndex": 0,
            "explanation": "Kesrin kesri bulunurken çarpma işlemi yapılır: (2/3) x (3/4) = 6/12 = 1/2'dir."
        },
        {
            "id": 7,
            "tag": "ARA TATİL • ALIŞVERİŞTE KDV HESABI",
            "scenario": "KDV hariç fiyatı 800 TL olan bir akıllı saate %20 KDV eklenecektir.",
            "stem": "Akıllı saatin KDV dahil satış fiyatı kaç TL olur?",
            "choices": ["960 TL (800 + 160)", "920 TL", "1000 TL", "880 TL"],
            "correctIndex": 0,
            "explanation": "KDV tutarı = 800 x 0,20 = 160 TL. Satış fiyatı = 800 + 160 = 960 TL'dir."
        },
        {
            "id": 8,
            "tag": "ARA TATİL • ÇÖZÜMLEME",
            "scenario": "45,208 ondalık gösteriminin çözümlenmesi istenmiştir.",
            "stem": "Bu sayının çözümlenmiş hali hangisidir?",
            "choices": [
                "(4 x 10) + (5 x 1) + (2 x 0,1) + (8 x 0,001)",
                "(4 x 10) + (5 x 1) + (2 x 0,01) + (8 x 0,001)",
                "(4 x 100) + (5 x 10) + (2 x 0,1)",
                "(4 x 10) + (5 x 1) + (28 x 0,01)"
            ],
            "correctIndex": 0,
            "explanation": "Onlar=4, Birler=5, Onda birler=2, Yüzde birler=0, Binde birler=8. Doğru açılım A seçeneğidir."
        },
        {
            "id": 9,
            "tag": "ARA TATİL • BÖLÜNEBİLME VE KALAN",
            "scenario": "Bir sepetteki elmalar 6'şar 6'şar ve 8'er 8'er sayıldığında her seferinde 3 elma artmaktadır.",
            "stem": "Sepetteki elma sayısı 50'den fazla olduğuna göre en az kaç elma vardır?",
            "choices": ["51 elma (EKOK(6,8) = 24 ➔ 48 + 3 = 51)", "54 elma", "57 elma", "63 elma"],
            "correctIndex": 0,
            "explanation": "EKOK(6, 8) = 24'tür. 24'ün katları: 24, 48, 72... 50'den büyük en küçük sayı için 48 + 3 = 51 elma olmalıdır."
        },
        {
            "id": 10,
            "tag": "ARA TATİL • YÜZDE İNDİRİMİ VE GERİYE DOĞRU ÇALIŞMA",
            "scenario": "%25 indirim yapıldıktan sonra 300 TL'ye satılan bir ceketin indirimden önceki fiyatı sorulmaktadır.",
            "stem": "Bu ceketin indirimden önceki etiket fiyatı kaç TL'dir?",
            "choices": ["400 TL (%75'i 300 TL ise tamamı 400 TL)", "375 TL", "425 TL", "350 TL"],
            "correctIndex": 0,
            "explanation": "%25 indirimli fiyat etiket fiyatının %75'idir. %75'i 300 TL ise %1'i 4 TL, %100'ü 400 TL'dir."
        }
    ]
}
