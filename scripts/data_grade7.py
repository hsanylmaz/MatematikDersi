#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
7. Sınıf Matematik Aktif Öğrenme v2.0 Müfredat ve Simülasyon Verisi (Hafta 1-7)
"""

GRADE7_MODULES = [
    # 7. SINIF 1. HAFTA
    {
        "grade": 7,
        "week": 1,
        "title": "Tam Sayılar ve Referans Noktası 0 Atölyesi",
        "date": "14–18 Eylül",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.7.1.1",
        "outcome_text": "Gerçek yaşam ya da matematiksel durumlarda doğal sayı, tam sayı ve rasyonel sayıları yorumlayabilme.",
        "process_items": [
            "Doğal sayıların yetmediği durumları sorgular.",
            "0 referans noktasını ve zıt yönleri (+ / -) modeller.",
            "Yatay ve dikey sayı doğrusunda tam sayıları inceler.",
            "Mutlak değerin başlangıç noktasına uzaklık olduğunu fark eder."
        ],
        "meb_quote": "Sıcaklık/termometre, denizaltı derinliği, asansör ve gelir-gider bağlamlarında 0 referans noktası; yatay/dikey sayı doğrusunda tam sayılar; 100g/200g kahve paketleme hatası ve helikopter-hastane uzaklığı bağlamında mutlak değer (|x|) keşfi.",
        "sim_steps": [
            {
                "tag": "REFERANS NOKTASI 0",
                "title": "Adım 1: Zıt Durumlar ve 0 Başlangıç Noktası",
                "instruction": "Deniz seviyesi, sıcaklık (donma noktası) ve asansör (zemin) için 0 referansını ve artı/eksi yönleri sürgüyle inceleyin. Değerleri gözlem tablosuna kaydedin.",
                "hint": "0 noktası başlangıç (referans) kabul edilir. Referansın üstü veya sağındaki yön pozitif (+), altı veya solundaki yön negatif (-) sayılardır.",
                "hypotheses": [
                    {"text": "0 sayısı ne pozitif ne de negatiftir; başlangıç ve referans noktasıdır.", "correct": True},
                    {"text": "0 daima pozitif bir sayıdır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "0 referans noktasıdır (işaretsizdir); 0'ın üstü pozitif (+), 0'ın altı negatif (-) tam sayılardır.", "correct": True},
                    {"text": "Negatif sayılar 0'dan büyüktür.", "correct": False}
                ],
                "sliderLabel": "Konum / Değer:",
                "min": -8, "max": 8, "defaultVal": -4, "unit": "birim",
                "simType": "integer_depth",
                "hasSecondary": False
            },
            {
                "tag": "MUTLAK DEĞER (|X|)",
                "title": "Adım 2: Başlangıç Noktasına Uzaklık Olarak Mutlak Değer",
                "instruction": "+5 ve -5 noktalarının 0'a olan mesafesini cetvelle ölçün. Sürgüyü değiştirerek farklı sayıların 0'a uzaklıklarını tabloya kaydedin.",
                "hint": "Bir sayının başlangıç noktasına (0'a) olan mesafesine o sayının 'mutlak değeri' denir ve |x| ile gösterilir. Uzaklık asla negatif olamaz!",
                "hypotheses": [
                    {"text": "Bir sayının mutlak değeri başlangıç noktasına olan uzaklığıdır ve daima sıfır veya pozitiftir.", "correct": True},
                    {"text": "Negatif sayıların mutlak değeri de negatiftir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Mutlak değer (|x|) bir sayının 0'a olan uzaklığıdır; |+a| = |-a| = a ve uzaklık asla negatif olamaz.", "correct": True},
                    {"text": "|-7| = -7'dir.", "correct": False}
                ],
                "sliderLabel": "Tam Sayı Seçimi:",
                "min": -10, "max": 10, "defaultVal": -6, "unit": "",
                "simType": "integer_depth",
                "hasSecondary": False
            },
            {
                "tag": "SAYI DOĞRUSUNDA SIRALAMA",
                "title": "Adım 3: Sayı Doğrusunda Büyüklük-Küçüklük Kuralı",
                "instruction": "-8 ile +3 arasındaki tam sayıları sayı doğrusunda inceleyin. Hangi sayının daha sağda olduğunu tabloya kaydedin.",
                "hint": "Sayı doğrusunda sağa doğru gidildikçe sayılar büyür, sola doğru gidildikçe sayılar küçülür.",
                "hypotheses": [
                    {"text": "Sayı doğrusunda sağda yer alan her sayı soldaki sayıdan daima daha büyüktür.", "correct": True},
                    {"text": "-8 sayısı -2 sayısından daha büyüktür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Sayı doğrusunda sağa gidildikçe sayılar büyür; bu nedenle -2 > -8 ve her pozitif tam sayı tüm negatiflerden büyüktür.", "correct": True},
                    {"text": "Negatif sayılarda rakamı büyük olan daima daha büyüktür.", "correct": False}
                ],
                "sliderLabel": "Sayı Konumu:",
                "min": -9, "max": 9, "defaultVal": -3, "unit": "",
                "simType": "integer_depth",
                "hasSecondary": False
            },
            {
                "tag": "ZIT İŞARETLİ SAYILAR",
                "title": "Adım 4: Zıt Sayılar ve Toplamları",
                "instruction": "Bir sayıyı ve onun zıt işaretlisini (+a ve -a) karşılaştırın.",
                "hint": "0'a eşit uzaklıkta bulunan iki zıt sayının toplamı daima 0'dır.",
                "hypotheses": [
                    {"text": "Zıt işaretli iki eş sayının toplamı sıfırdır: (+a) + (-a) = 0.", "correct": True},
                    {"text": "Zıt sayıların toplamı pozitiftir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Bir tam sayının toplama işlemine göre tersi zıt işaretlisidir ve toplamları 0 referansını verir.", "correct": True},
                    {"text": "-5'in tersi yine -5'tir.", "correct": False}
                ],
                "sliderLabel": "Sayı Değeri:",
                "min": 1, "max": 10, "defaultVal": 5, "unit": "",
                "simType": "integer_depth",
                "hasSecondary": False
            }
        ]
    },

    # 7. SINIF 2. HAFTA
    {
        "grade": 7,
        "week": 2,
        "title": "Tam Sayılardan Rasyonel Sayılara Geçiş Atölyesi",
        "date": "21–25 Eylül",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.7.1.1",
        "outcome_text": "Gerçek yaşam ya da matematiksel durumlarda doğal sayı, tam sayı ve rasyonel sayıları yorumlayabilme.",
        "process_items": [
            "2 × ? = 1 sorgulamasıyla tam sayıların yetersizliğini fark eder.",
            "a/b (b≠0) biçimindeki rasyonel sayıları tanımlar.",
            "-a/b = (-a)/b = a/(-b) denkliğini inceler.",
            "Denk rasyonel sayıların sayı doğrusunda aynı noktada çakıştığını gösterir."
        ],
        "meb_quote": "2 × ? = 1 sorgulamasıyla tam sayıların yetmediği durumları keşfetme; 1/2 = 2/4 = 3/6 denk kesirlerin sayı doğrusunda aynı noktada çakışması; -a/b = (-a)/b = a/(-b) denkliği.",
        "sim_steps": [
            {
                "tag": "TAM SAYILARIN YETERSİZLİĞİ",
                "title": "Adım 1: 2 × ? = 1 ve Rasyonel Sayı İhtiyacı",
                "instruction": "2 ile çarpıldığında 1 eden bir tam sayı arayın. Tam sayıların yetmediğini ve rasyonel sayılara (1/2) olan ihtiyacı tabloya kaydedin.",
                "hint": "Hiçbir tam sayının 2 katı 1 etmez. Bu tür durumları ifade etmek için a/b biçimindeki rasyonel sayılar geliştirilmiştir.",
                "hypotheses": [
                    {"text": "2 × ? = 1 denkleminin çözümü bir tam sayı değil, bir rasyonel sayıdır (1/2).", "correct": True},
                    {"text": "Tam sayılar kümesi tüm bölme işlemlerini çözmek için yeterlidir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "a ve b tam sayı (b ≠ 0) olmak üzere a/b biçiminde yazılabilen sayılara RASYONEL SAYILAR (Q) denir.", "correct": True},
                    {"text": "Rasyonel sayıların paydası 0 olabilir.", "correct": False}
                ],
                "sliderLabel": "Çarpan Sürgüsü:",
                "min": 1, "max": 6, "defaultVal": 2, "unit": "",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "EKSİ İŞARETİNİN KONUMU",
                "title": "Adım 2: -a/b = (-a)/b = a/(-b) Denkliği",
                "instruction": "Negatif bir rasyonel sayıda eksi işaretini paya, paydaya veya kesir çizgisinin önüne koyarak sayı doğrusundaki konumunu test edin.",
                "hint": "Zıt işaretli iki tam sayının bölümü daima negatiftir. Bu nedenle eksi işaretinin payda, paydada veya kesir çizgisinin önünde olması sayının değerini değiştirmez.",
                "hypotheses": [
                    {"text": "Eksi işaretinin nerede olduğu sayının sayı doğrusundaki yerini değiştirmez: -a/b = (-a)/b = a/(-b).", "correct": True},
                    {"text": "İşaret paydaya geçerse sayı pozitife döner.", "correct": False}
                ],
                "conjectures": [
                    {"text": "-(a/b) = (-a)/b = a/(-b) özdeştir ve her biri sayı doğrusunda sıfırın solundaki aynı noktayı gösterir.", "correct": True},
                    {"text": "Eksi işareti paya yazılırsa sayı büyür.", "correct": False}
                ],
                "sliderLabel": "Pay Değeri:",
                "min": -5, "max": 5, "defaultVal": -3, "unit": "pay",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "DENK RASYONEL SAYILAR",
                "title": "Adım 3: Denk Rasyonellerin Aynı Noktada Çakışması",
                "instruction": "-1/2, -2/4, -3/6 kesirlerini sayı doğrusunda işaretleyin. Hepsini aynı noktaya denk geldiğini gözlemleyip tabloya kaydedin.",
                "hint": "Bir rasyonel sayının pay ve paydası aynı sıfırdan farklı tam sayı ile çarpılır veya bölünürse değeri değişmez (genişletme ve sadeleştirme).",
                "hypotheses": [
                    {"text": "Denk rasyonel sayılar sayı doğrusunda tam olarak aynı tek bir noktayı temsil eder.", "correct": True},
                    {"text": "Denk kesirler sayı doğrusunda farklı yerlerde durur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Genişletilen veya sadeleştirilen denk rasyonel sayılar sayı doğrusunda aynı noktada çakışır (1/2 = 2/4 = 3/6).", "correct": True},
                    {"text": "Genişletilen kesrin değeri artar.", "correct": False}
                ],
                "sliderLabel": "Genişletme Katı:",
                "min": 1, "max": 5, "defaultVal": 2, "unit": "kat",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "TAM SAYILAR DA RASYONELDİR",
                "title": "Adım 4: Paydası 1 Olan Rasyonel Sayılar",
                "instruction": "Tam sayıları a/1 biçiminde yazarak her tam sayının aslında bir rasyonel sayı olduğunu inceleyin.",
                "hint": "5 = 5/1, -3 = -3/1, 0 = 0/1. Dolayısıyla her tam sayı paydası 1 olan gizli bir rasyonel sayıdır.",
                "hypotheses": [
                    {"text": "Her tam sayı aynı zamanda paydası 1 olan bir rasyonel sayıdır (Z ⊂ Q).", "correct": True},
                    {"text": "Tam sayılar rasyonel sayı sayılamaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Her tam sayı paydasına 1 yazılarak rasyonel sayı biçiminde gösterilebilir (a = a/1).", "correct": True},
                    {"text": "0 rasyonel sayı değildir.", "correct": False}
                ],
                "sliderLabel": "Tam Sayı:",
                "min": -5, "max": 5, "defaultVal": 3, "unit": "",
                "simType": "rational_line",
                "hasSecondary": False
            }
        ]
    },

    # 7. SINIF 3. HAFTA
    {
        "grade": 7,
        "week": 3,
        "title": "Rasyonel Sayıların Ondalık Gösterimleri Atölyesi",
        "date": "28 Eylül–02 Ekim",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.7.1.2",
        "outcome_text": "Gerçek yaşam durumlarında rasyonel sayıların ondalık gösterimlerini yansıtabilme.",
        "process_items": [
            "Bölme işlemini kullanarak her rasyonel sayının bir ondalık gösterimi olduğunu inceler.",
            "Rasyonel sayıların ondalık gösterimlerinden bazılarının devirli olduğuna dair çıkarım yapar."
        ],
        "meb_quote": "Bölme işlemi ve hesap makinesiyle rasyonel sayıların sonlu ve devirli ondalık gösterimlerini keşfetme, payda örüntülerini bulma, 0,999... = 1 tartışması.",
        "sim_steps": [
            {
                "tag": "SONLU ONDALIK DÖNÜŞÜMÜ",
                "title": "Adım 1: Paydayı 10, 100, 1000 Yaparak Ondalık Gösterim",
                "instruction": "-3/4 kesrini 25 ile genişleterek -75/100 = -0,75 yapın. Paydası 10'un kuvveti olabilen kesirleri inceleyip tabloya kaydedin.",
                "hint": "Paydası 2, 4, 5, 8, 20, 25, 50 olan kesirler uygun sayılarla genişletilerek sonlu ondalık sayıya çevrilebilir.",
                "hypotheses": [
                    {"text": "Paydası 10, 100 veya 1000 yapılabilen rasyonel sayılar sonlu ondalık gösterimle ifade edilir.", "correct": True},
                    {"text": "Tüm negatif rasyonel sayılar devirlidir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Paydası genişletilerek 10'un pozitif tam sayı kuvveti yapılan rasyonel sayılar SONLU ondalık gösterimle yazılır.", "correct": True},
                    {"text": "Sonlu sayılar rasyonel sayı değildir.", "correct": False}
                ],
                "sliderLabel": "Pay Değeri:",
                "min": -5, "max": 5, "defaultVal": -3, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": True,
                "sliderLabel2": "Payda:",
                "min2": 2, "max2": 8, "defaultVal2": 4, "unit2": "payda"
            },
            {
                "tag": "BÖLME ALGORİTMASI",
                "title": "Adım 2: Bölme İşlemi ile Devirli Rasyonel Sayılar",
                "instruction": "-2/3 rasyonel sayısını payı paydaya bölerek hesaplayın (-2 ÷ 3 = -0,666... = -0,6̄). Kalanın 0 olmadığını tabloya kaydedin.",
                "hint": "Bölme işleminde kalan hiçbir zaman 0 olmuyor ve aynı rakamlar periyodik tekrar ediyorsa sayı devirli ondalık sayıdır.",
                "hypotheses": [
                    {"text": "Kalanı sıfır olmayan ve periyodik tekrarlayan bölmeler devirli rasyonel sayı üretir.", "correct": True},
                    {"text": "Devirli sayılar rasyonel sayı kümesinde yer almaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Her rasyonel sayı bir ondalık gösterim verir; bu gösterim ya sonlu ya da devirlidir (Örn: -2/3 = -0,6̄).", "correct": True},
                    {"text": "Devirli sayılar tam sayıdır.", "correct": False}
                ],
                "sliderLabel": "Pay:",
                "min": 1, "max": 7, "defaultVal": 5, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": True,
                "sliderLabel2": "Payda:",
                "min2": 3, "max2": 9, "defaultVal2": 9, "unit2": "payda"
            },
            {
                "tag": "İKİ BASAMAKLI DEVİR",
                "title": "Adım 3: İki Basamaklı Devreden Rakamlar",
                "instruction": "4/11 kesrini inceleyin. Virgülden sonra 363636... olarak ikişerli periyotla devrettiğini (0,36̄) gözlemleyin.",
                "hint": "Devreden basamak sayısı kaç taneyse devir çizgisi o basamakların tamamının üzerine çizilir.",
                "hypotheses": [
                    {"text": "Devir çizgisi periyodik olarak tekrar eden tüm basamakların üzerine uzatılmalıdır.", "correct": True},
                    {"text": "Sadece son basamağa çizgi konur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Tekrar eden rakam grubu kaç basamaklı ise devir çizgisi o grubun tamamının üzerine yazılır (4/11 = 0,36̄).", "correct": True},
                    {"text": "Devirli sayılar virgülsüz yazılır.", "correct": False}
                ],
                "sliderLabel": "Pay:",
                "min": 1, "max": 9, "defaultVal": 4, "unit": "pay",
                "simType": "fraction_division",
                "hasSecondary": True,
                "sliderLabel2": "Payda:",
                "min2": 7, "max2": 11, "defaultVal2": 11, "unit2": "payda"
            },
            {
                "tag": "0,999... = 1 TARTIŞMASI",
                "title": "Adım 4: 0,999... Devirli Sayısının 1'e Eşitliği",
                "instruction": "1/9 = 0,111... ; 2/9 = 0,222... örüntüsünü sürdürerek 9/9 = 0,999... = 1 eşitliğini inceleyin.",
                "hint": "1/3 = 0,333... olduğundan 3 × (1/3) = 3 × 0,333... = 0,999... = 1'dir!",
                "hypotheses": [
                    {"text": "0,9̄ devirli sayısı tam olarak 1 doğal sayısına eşittir.", "correct": True},
                    {"text": "0,9̄ sayısı 1'den küçüktür, asla 1 olamaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Matematiksel olarak 0,999... (0,9̄) sayısı tam olarak 1'e eşittir.", "correct": True},
                    {"text": "0,9̄ sayısı 0'a eşittir.", "correct": False}
                ],
                "sliderLabel": "Dokuzda Bir Katı:",
                "min": 1, "max": 9, "defaultVal": 9, "unit": "/9",
                "simType": "fraction_division",
                "hasSecondary": False
            }
        ]
    },

    # 7. SINIF 4. HAFTA
    {
        "grade": 7,
        "week": 4,
        "title": "Rasyonel Sayılarda Karşılaştırma ve Sıralama Atölyesi",
        "date": "05–09 Ekim",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.7.1.2 & MAT.7.1.3",
        "outcome_text": "MAT.7.1.2. Gerçek yaşam durumlarında rasyonel sayıların ondalık gösterimlerini yansıtabilme • MAT.7.1.3. Rasyonel sayıların karşılaştırma ve sıralama ilişkilerini yorumlayabilme.",
        "process_items": [
            "Devirli ve devirsiz ondalık gösterimleri karşılaştırır.",
            "Sayı doğrusunda rasyonel sayıların sağ-sol büyüklük ilişkisini açıklar.",
            "Payda ve pay eşitleme stratejilerini uygular."
        ],
        "meb_quote": "Paydası 1 olan rasyonel sayılardan (tam sayılardan) başlayarak sayı doğrusunda sıralama ('Soldan sağa gidildikçe sayılar büyür' genellemesi); negatiflerde 0'a yakınlık.",
        "sim_steps": [
            {
                "tag": "DEVİRLİ KARŞILAŞTIRMA",
                "title": "Adım 1: Devirli ve Devirsiz Ondalıkları Sıralama",
                "instruction": "0,4 ile 0,4̄ (0,444...) sayılarını basamak basamak karşılaştırıp tabloya kaydedin.",
                "hint": "0,4 = 0,4000... iken 0,4̄ = 0,4444...'tür. Yüzde birler basamağında 4 > 0 olduğundan 0,4̄ > 0,4'tür.",
                "hypotheses": [
                    {"text": "Devirli sayıların basamakları açıldığında daha büyük basamak değeri bulunarak karşılaştırılır.", "correct": True},
                    {"text": "Virgülün hemen sağı aynıysa sayılar eşittir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "0,444... > 0,400 olduğundan 0,4̄ > 0,4'tür; basamakları aynı hizada açarak karşılaştırma yapılır.", "correct": True},
                    {"text": "Devirli sayılar daima devirsizden küçüktür.", "correct": False}
                ],
                "sliderLabel": "Ondalık Değer:",
                "min": 1, "max": 9, "defaultVal": 4, "unit": "onda bir",
                "simType": "decimal_grid",
                "hasSecondary": False
            },
            {
                "tag": "NEGATİFTE 0'A YAKINLIK",
                "title": "Adım 2: Negatif Rasyonellerde 0'a Yakınlık",
                "instruction": "-1/4 ve -3/4 sayılarını sayı doğrusunda inceleyin. 0'a daha yakın olanın neden daha büyük olduğunu tabloya kaydedin.",
                "hint": "Negatif sayılarda 0'a daha yakın olan (daha sağda olan) sayı daha büyüktür: -1/4 > -3/4.",
                "hypotheses": [
                    {"text": "Negatif rasyonel sayılarda sıfıra daha yakın olan (sağdaki) sayı daima daha büyüktür.", "correct": True},
                    {"text": "Sıfırdan uzaklaştıkça negatif sayılar büyür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Sayı doğrusunda sağdaki sayı daima büyüktür; negatiflerde sıfıra daha yakın olan rasyonel sayı büyüktür (-1/4 > -3/4).", "correct": True},
                    {"text": "-3/4 sayısı -1/4 sayısından büyüktür.", "correct": False}
                ],
                "sliderLabel": "Pay (-a/4):",
                "min": -4, "max": -1, "defaultVal": -1, "unit": "pay",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "PAYDA EŞİTLEME",
                "title": "Adım 3: Payda Eşitleyerek Karşılaştırma",
                "instruction": "2/3 ile 3/4 kesirlerini paydalarını 12 yaparak karşılaştırın: 8/12 < 9/12.",
                "hint": "Paydaları eşit pozitif rasyonel sayılarda payı büyük olan daha büyüktür.",
                "hypotheses": [
                    {"text": "Paydalar eşitlendiğinde payı büyük olan pozitif rasyonel sayı daha büyüktür.", "correct": True},
                    {"text": "Payda eşitlendiğinde payı küçük olan daha büyüktür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Pozitif rasyonel sayılarda paydalar eşitlendiğinde payı büyük olan daha büyüktür (8/12 < 9/12 ➔ 2/3 < 3/4).", "correct": True},
                    {"text": "Kesirlerin paydası eşitlenemez.", "correct": False}
                ],
                "sliderLabel": "Pay 1:",
                "min": 1, "max": 5, "defaultVal": 2, "unit": "pay",
                "simType": "rational_line",
                "hasSecondary": True,
                "sliderLabel2": "Pay 2:",
                "min2": 1, "max2": 5, "defaultVal2": 3, "unit2": "pay"
            },
            {
                "tag": "PAY EŞİTLEME",
                "title": "Adım 4: Payları Eşitleyerek Karşılaştırma",
                "instruction": "1/2, 1/3, 1/4 kesirlerini inceleyin. Payları eşit pozitif kesirlerde paydası küçük olanın neden daha büyük parçayı temsil ettiğini tabloya kaydedin.",
                "hint": "Bir bütünü daha az parçaya bölerseniz dilimler daha büyük olur (1/2 > 1/3 > 1/4).",
                "hypotheses": [
                    {"text": "Payları eşit pozitif kesirlerde paydası küçük olan kesir daha büyüktür.", "correct": True},
                    {"text": "Paydası büyük olan dilim daha büyüktür.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Payları eşit pozitif rasyonel sayılarda paydası KÜÇÜK olan daha büyüktür (1/2 > 1/3 > 1/4).", "correct": True},
                    {"text": "1/4 sayısı 1/2'den büyüktür.", "correct": False}
                ],
                "sliderLabel": "Bölünen Parça (Payda):",
                "min": 2, "max": 10, "defaultVal": 3, "unit": "parça",
                "simType": "rational_line",
                "hasSecondary": False
            }
        ]
    },

    # 7. SINIF 5. HAFTA
    {
        "grade": 7,
        "week": 5,
        "title": "Sıralama Stratejileri ve Yoğunluk Özelliği Atölyesi",
        "date": "12–16 Ekim",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.7.1.3",
        "outcome_text": "Rasyonel sayıların karşılaştırma ve sıralama ilişkilerini yorumlayabilme.",
        "process_items": [
            "Rasyonel sayıların karşılaştırma ve sıralama ilişkilerini sembolik olarak ifade eder.",
            "Rasyonel sayıların karşılaştırma ve sıralama ilişkisini sayı doğrusu üzerinde kendi ifadeleriyle açıklar.",
            "İki rasyonel sayı arasında sonsuz rasyonel sayı olduğunu (yoğunluk) fark eder."
        ],
        "meb_quote": "-4 ile -5 veya 3/5 ile 4/5 arasına sayı yerleştirerek 'Herhangi iki rasyonel sayı arasında daima bir rasyonel sayı bulunur' (yoğunluk özelliği) genellemesine ulaşma.",
        "sim_steps": [
            {
                "tag": "YARIMA VE BÜTÜNE YAKINLIK",
                "title": "Adım 1: Yarıma (1/2) ve Bütüne (1) Yakınlık Stratejisi",
                "instruction": "5/8 ile 3/7 kesirlerini yarıma (1/2 = 4/8) göre karşılaştırın: 5/8 yarımdan büyük, 3/7 yarımdan küçüktür (5/8 > 3/7).",
                "hint": "Payda eşitlemeye gerek kalmadan sayıların 0'a, 1/2'ye veya 1'e olan yakınlığına bakarak pratik sıralama yapılabilir.",
                "hypotheses": [
                    {"text": "Rasyonel sayılar 0, 1/2 ve 1 referanslarına olan yakınlıklarıyla pratikçe karşılaştırılabilir.", "correct": True},
                    {"text": "Her sıralamada mutlaka payda eşitlemek şarttır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Referans stratejisiyle (yarımdan büyük/küçük) işlem yapmadan hızlı ve doğru sıralama yapılabilir.", "correct": True},
                    {"text": "Referans noktası sadece 0'dır.", "correct": False}
                ],
                "sliderLabel": "Pay 1 (Pay/8):",
                "min": 1, "max": 7, "defaultVal": 5, "unit": "pay",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "ARAYA SAYI YERLEŞTİRME",
                "title": "Adım 2: İki Rasyonel Sayı Arasına Sayı Yerleştirme",
                "instruction": "3/5 ile 4/5 ardışık gibi görünen kesirleri 2 ile genişletin (6/10 ve 8/10). Aralarına 7/10 rasyonel sayısını yerleştirip tabloya kaydedin.",
                "hint": "Kesirleri 10 ile, 100 ile genişlettikçe aralarına 10'larca, 100'lerce yeni rasyonel sayı sığdırabilirsiniz!",
                "hypotheses": [
                    {"text": "Genişletme yapılarak herhangi iki rasyonel sayı arasına istenildiği kadar yeni rasyonel sayı yerleştirilebilir.", "correct": True},
                    {"text": "Ardışık iki rasyonel sayı arasında başka hiçbir sayı bulunmaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Herhangi iki rasyonel sayı arasında daima en az bir (ve sonsuz sayıda) rasyonel sayı bulunur.", "correct": True},
                    {"text": "Rasyonel sayılar ardışık tamsayılar gibi tek tek sayılabilir.", "correct": False}
                ],
                "sliderLabel": "Genişletme Faktörü:",
                "min": 2, "max": 10, "defaultVal": 2, "unit": "kat",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "YOĞUNLUK ÖZELLİĞİ",
                "title": "Adım 3: Rasyonel Sayıların Yoğunluk Özelliği",
                "instruction": "Sayı doğrusunda iki nokta arasına sürekli yakınlaşarak (zoom yaparak) aradaki sonsuz sayıları keşfedin.",
                "hint": "Tam sayılarda 3 ile 4 arasında başka bir tam sayı yoktur. Ancak rasyonel sayılarda herhangi iki sayı arasında SONSUZ rasyonel sayı vardır (Yoğunluk Özelliği).",
                "hypotheses": [
                    {"text": "Rasyonel sayılar kümesi yoğundur; sayı doğrusundaki herhangi iki nokta arasında sonsuz sayıda rasyonel sayı vardır.", "correct": True},
                    {"text": "Rasyonel sayılar arasında boşluklar vardır ve sonludur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Rasyonel sayılar kümesi YOĞUNDUR; herhangi iki rasyonel sayı arasında sonsuz sayıda rasyonel sayı vardır.", "correct": True},
                    {"text": "İki rasyonel sayı arasında en fazla 1 sayı olabilir.", "correct": False}
                ],
                "sliderLabel": "Aralık Hassasiyeti:",
                "min": 1, "max": 5, "defaultVal": 3, "unit": "kademe",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "ÇOKLU TEMSİL SIRALAMA",
                "title": "Adım 4: Tam Sayı, Kesir ve Ondalık Sıralaması",
                "instruction": "-1,5 < -3/4 < 0,25 < 5/4 çoklu gösterimlerini sayı doğrusunda küçükten büyüğe dizin.",
                "hint": "Farklı gösterimlerdeki sayıları sıralarken hepsini ondalığa veya paydası eşit kesre dönüştürmek kolaylık sağlar.",
                "hypotheses": [
                    {"text": "Farklı gösterimler (ondalık, kesir, tam sayı) ortak bir temsile çevrilerek sayı doğrusunda sıralanabilir.", "correct": True},
                    {"text": "Ondalık sayılar kesirlerle sıralanamaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Rasyonel sayılar temsil türü ne olursa olsun sayı doğrusunda soldan sağa doğru küçükten büyüğe dizilir.", "correct": True},
                    {"text": "Negatif sayılar daima pozitiftir.", "correct": False}
                ],
                "sliderLabel": "Seçilen Sayı Değeri:",
                "min": -2, "max": 2, "defaultVal": 1, "unit": "",
                "simType": "rational_line",
                "hasSecondary": False
            }
        ]
    },

    # 7. SINIF 6. HAFTA
    {
        "grade": 7,
        "week": 6,
        "title": "Rasyonel Sayılarla İşlemler ve Modelleme Atölyesi",
        "date": "19–23 Ekim",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.7.1.4",
        "outcome_text": "Rasyonel sayılar ve işlemler içeren gerçek yaşam problemlerini çözebilme.",
        "process_items": [
            "Sayı ve işlem bileşenlerini belirler.",
            "İstenenler ve seçilen işlemler arasındaki ilişkileri belirler.",
            "Problem bağlamını uygun temsillere (sayı doğrusu, model) dönüştürür.",
            "Stratejiler oluşturur."
        ],
        "meb_quote": "Sayı doğrusu ve sayma pulları modeli; (+2)+(-6) ile (+2)-(+6) eşdeğerliği; negatif sayıların çarpımında örüntü yaklaşımı; en fazla 3 adımlı işlemlerde ayraç ve ana kesir çizgisi işlem önceliği.",
        "sim_steps": [
            {
                "tag": "TOPLAMA VE ÇIKARMA MODELİ",
                "title": "Adım 1: Sayı Doğrusunda Rasyonel Toplama ve Çıkarma",
                "instruction": "(-3/4) + (+5/4) işlemini sayı doğrusunda oklarla modelleyin: -3/4'e gidip sağa 5/4 adım ilerleyin (+2/4 = +1/2).",
                "hint": "Pozitif ekleme sağa, negatif ekleme (veya çıkarma) sola hareketi temsil eder.",
                "hypotheses": [
                    {"text": "Paydaları eşit rasyonel sayılarda paylar toplanır veya çıkarılır, ortak payda aynen yazılır.", "correct": True},
                    {"text": "Paydalar da birbiriyle toplanır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Rasyonel sayılarda toplama/çıkarma için paydalar eşit olmalıdır; paylar işleme girer, ortak payda korunur.", "correct": True},
                    {"text": "Paydalar toplanarak yeni payda bulunur.", "correct": False}
                ],
                "sliderLabel": "2. Adım Uzunluğu (Pay):",
                "min": 1, "max": 7, "defaultVal": 5, "unit": "/4",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "ALAN MODELİYLE ÇARPMA",
                "title": "Adım 2: Alan Modeli ile Rasyonel Çarpma (Kesrin Kesri)",
                "instruction": "(2/3) × (3/4) çarpımını dikdörtgen alan modelinde inceleyin. Yatay 3 parçaya, dikey 4 parçaya bölünen alanda ortak boyalı kareleri (6/12 = 1/2) sayın.",
                "hint": "Çarpma işlemi 'kesrin kesrini' bulmaktır: Paylar kendi arasında, paydalar kendi arasında çarpılır.",
                "hypotheses": [
                    {"text": "Rasyonel sayılar çarpılırken pay ile pay, payda ile payda çarpılır; payda eşitlemeye gerek yoktur.", "correct": True},
                    {"text": "Çarpma yaparken de payda eşitlemek zorunludur.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Rasyonel sayılarda çarpma: (a/b) × (c/d) = (a×c)/(b×d)'dir; modelde iki boyalı bölgenin kesişim alanıdır.", "correct": True},
                    {"text": "Çarpma sonucu daima çarpanlardan büyüktür.", "correct": False}
                ],
                "sliderLabel": "En Payı (n/4):",
                "min": 1, "max": 3, "defaultVal": 2, "unit": "/4",
                "simType": "rational_mult",
                "hasSecondary": True,
                "sliderLabel2": "Boy Payı (m/3):",
                "min2": 1, "max2": 3, "defaultVal2": 2, "unit2": "/3"
            },
            {
                "tag": "NEGATİF ÇARPIM ÖRÜNTÜSÜ",
                "title": "Adım 3: Negatif Sayıların Çarpımında Örüntü",
                "instruction": "3×(-2)=-6, 2×(-2)=-4, 1×(-2)=-2, 0×(-2)=0, (-1)×(-2)=+2, (-2)×(-2)=+4 örüntüsünü sürgüyle inceleyin.",
                "hint": "Çarpan her adımda 1 azaldıkça sonuç 2 artmaktadır. 0'dan sonra bu artış devam ederek negatif × negatif = pozitif sonucunu doğurur!",
                "hypotheses": [
                    {"text": "Aynı işaretli iki sayının çarpımı pozitif (+), zıt işaretli iki sayının çarpımı negatiftir (-).", "correct": True},
                    {"text": "İki negatif sayının çarpımı negatiftir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "İki negatif rasyonel sayının çarpımı daima POZİTİFTİR: (-) × (-) = (+) ve (-) × (+) = (-).", "correct": True},
                    {"text": "Negatif ile negatifin çarpımı negatiftir.", "correct": False}
                ],
                "sliderLabel": "1. Çarpan:",
                "min": -4, "max": 4, "defaultVal": -2, "unit": "",
                "simType": "integer_depth",
                "hasSecondary": False
            },
            {
                "tag": "BÖLME VE TERS ÇEVİRİP ÇARPMA",
                "title": "Adım 4: Gruplama Modeliyle Rasyonel Bölme",
                "instruction": "(3/2) ÷ (1/4) işlemini modelleyin: 1,5 litrelik şişeden 0,25 litrelik kaç bardak çıkar? (6 bardak).",
                "hint": "Bölme işlemi, birinci kesrin içine ikinci kesirden kaç tane sığdığını bulmaktır. Birinci kesir aynen kalır, ikinci kesir ters çevrilip çarpılır.",
                "hypotheses": [
                    {"text": "Bir kesri diğerine bölmek, birinci kesri ikincinin çarpma işlemine göre tersiyle (takla attırarak) çarpmaktır.", "correct": True},
                    {"text": "Bölmede paylar bölünür, paydalar çıkarılır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Rasyonel sayılarda bölme işlemi: (a/b) ÷ (c/d) = (a/b) × (d/c)'dir (İkinci kesir ters çevrilir ve çarpılır).", "correct": True},
                    {"text": "Bölme işlemi sonucu daima küçülür.", "correct": False}
                ],
                "sliderLabel": "Bölünen Pay:",
                "min": 1, "max": 6, "defaultVal": 3, "unit": "/2",
                "simType": "rational_line",
                "hasSecondary": False
            }
        ]
    },

    # 7. SINIF 7. HAFTA (YENİ MODÜL)
    {
        "grade": 7,
        "week": 7,
        "title": "Rasyonel Sayılarla Gerçek Yaşam Problem Çözme ve Strateji Atölyesi",
        "date": "26–30 Ekim",
        "hours": "5 Ders Saati",
        "theme": "1. TEMA: SAYILAR VE NİCELİKLER (1)",
        "outcome_code": "MAT.7.1.4",
        "outcome_text": "Rasyonel sayılar ve işlemler içeren gerçek yaşam problemlerini çözebilme.",
        "process_items": [
            "Problem durumunu modeller (Verilen / İstenen / İşlem / Temsil).",
            "Çok adımlı işlemlerde ayraç ve işlem önceliğini uygular.",
            "Farklı çözüm stratejilerini karşılaştırır.",
            "Verilen matematiksel duruma uygun gerçek yaşam problemi kurar."
        ],
        "meb_quote": "Gerçek yaşam problemlerinde Verilen / İstenen / İşlem / Temsil (Sayı Doğrusu, Şerit/Kutu Modeli, Alan Modeli) seçimi; en fazla 3 adımlı işlemlerde ayraç ve ana kesir çizgisi işlem önceliği; farklı çözüm stratejilerini karşılaştırma ve problem kurma.",
        "sim_steps": [
            {
                "tag": "VERİLEN-İSTENEN ANALİZİ",
                "title": "Adım 1: Problem Durumunu Parçalara Ayırma",
                "instruction": "Bir depodaki suyun önce 1/3'ü, sonra kalanın 1/2'si kullanılıyor. Kalan su 40 litre olduğuna göre deponun tamamını kutu/şerit modeliyle inceleyin.",
                "hint": "Depoyu 3 kutu çizerek modelleyin: 1 kutu harcandı, geriye 2 kutu kaldı. Kalanın yarısı 1 kutudur. Geriye kalan son 1 kutu 40 litre ise tamamı 3 × 40 = 120 litredir.",
                "hypotheses": [
                    {"text": "Kalanın kesri hesaplanırken önce geriye kalan oran (1 - 1/3 = 2/3) bulunmalıdır.", "correct": True},
                    {"text": "1/3 ile 1/2 doğrudan toplanmalıdır.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Problem çözmede şerit/kutu diyagramı çizmek 'kalanın kesri' tuzaklarını engeller ve adım adım çözümü somutlaştırır.", "correct": True},
                    {"text": "Problemlerde şekil çizmek vakit kaybıdır.", "correct": False}
                ],
                "sliderLabel": "Kalan Kutu Değeri:",
                "min": 20, "max": 60, "defaultVal": 40, "unit": "Litre",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "İŞLEM ÖNCELİĞİ VE PARANTEZ",
                "title": "Adım 2: Çok Adımlı İşlemlerde Öncelik Sıralaması",
                "instruction": "Ana kesir çizgili ve parantezli bir işlemi inceleyin: [1 - (1/2)] ÷ [1 + (1/3)]. Önce pay ve paydadaki işlemler, en son ana bölme yapılır.",
                "hint": "İşlem önceliği sırası: 1) Üslü ifadeler, 2) Parantez / Ayraç içleri, 3) Çarpma ve Bölme, 4) Toplama ve Çıkarma.",
                "hypotheses": [
                    {"text": "Ana kesir çizgisi hem payı hem paydayı kendi içinde bir parantez gibi gruplandırır.", "correct": True},
                    {"text": "İşlemler daima soldan sağa sırayla yapılır, parantez önemsizdir.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Çok adımlı rasyonel işlemlerde önce parantez içleri ve ana kesir çizgisinin alt/üst işlemleri tamamlanır.", "correct": True},
                    {"text": "Toplama işlemi çarpmadan önce yapılır.", "correct": False}
                ],
                "sliderLabel": "İşlem Adımı:",
                "min": 1, "max": 3, "defaultVal": 2, "unit": "adım",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "STRATEJİ KARŞILAŞTIRMA",
                "title": "Adım 3: Cebirsel vs Geometrik Çözüm Stratejileri",
                "instruction": "Bir telin ucundan 1/5'i kesildiğinde orta noktasının ne kadar kaydığını inceleyin. Kesilen parçanın yarısı kadar ( (1/5) ÷ 2 = 1/10 ) kaydığını tabloya kaydedin.",
                "hint": "Bir telin ucundan x kadar kesilirse orta noktası daima kesilen parçanın yarısı (x/2) kadar diğer yöne kayar!",
                "hypotheses": [
                    {"text": "Bir telin ucundan parça kesilirse orta nokta kesilen parçanın yarısı kadar zıt yöne kayar.", "correct": True},
                    {"text": "Orta nokta kesilen parça kadar kayar.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Telin ucundan a birim kesildiğinde orta nokta daima a/2 birim zıt yöne kayar (Kesilenin yarısı kuralı).", "correct": True},
                    {"text": "Orta nokta hiç değişmez.", "correct": False}
                ],
                "sliderLabel": "Kesilen Parça Uzunluğu:",
                "min": 4, "max": 20, "defaultVal": 10, "unit": "cm",
                "simType": "rational_line",
                "hasSecondary": False
            },
            {
                "tag": "TERSİNE PROBLEM KURMA",
                "title": "Adım 4: Verilen Matematiksel Modele Problem Kurma",
                "instruction": "(3/4) × (2/5) işlemini ifade eden bir gerçek yaşam problemi kurgulayın: 'Bir tarlanın 3/4'ünün 2/5'ine domates ekilmiştir.'",
                "hint": "Problem kurarken verilen rasyonel sayılara ve işlemin fiziksel anlamına (parçanın parçası) uygun bağlamlar (tarla, para, yol, pasta) seçilir.",
                "hypotheses": [
                    {"text": "Bir rasyonel çarpma işlemi 'bir miktarın kesir kadarının kesrini' ifade eden problemlerle tam örtüşür.", "correct": True},
                    {"text": "Rasyonel sayılarla gerçek yaşam problemi kurulamaz.", "correct": False}
                ],
                "conjectures": [
                    {"text": "Matematiksel bir işleme gerçek yaşam bağlamı giydirerek problem kurmak, kavramsal anlamayı en üst düzeye çıkarır.", "correct": True},
                    {"text": "Problem kurmak sadece sayı yazmaktır.", "correct": False}
                ],
                "sliderLabel": "Problem Karmaşıklığı:",
                "min": 1, "max": 3, "defaultVal": 2, "unit": "düzey",
                "simType": "rational_mult",
                "hasSecondary": False
            }
        ],
        "mini_tasks": [
            {
                "id": 1,
                "tag": "KALANIN KESRİ PROBLEMİ",
                "question": "Maaşının 2/5'ini ev kirasına, kalan parasının 1/3'ünü mutfak masraflarına ayıran bir memurun geriye 12.000 TL'si kalmıştır. Memurun toplam maaşı kaç TL'dir?",
                "options": [
                    {"label": "A) 30.000 TL (Kalan oran 2/5 = 12.000 TL ➔ Tamamı 30.000 TL)", "correct": True},
                    {"label": "B) 25.000 TL", "correct": False},
                    {"label": "C) 36.000 TL", "correct": False}
                ]
            },
            {
                "id": 2,
                "tag": "ÇOK ADIMLI İŞLEM ÖNCELİĞİ",
                "question": "[ 1 - (1/3) ] ÷ [ 1 + (1/3) ] işleminin sonucu kaçtır?",
                "options": [
                    {"label": "A) (2/3) ÷ (4/3) = (2/3) × (3/4) = 1/2", "correct": True},
                    {"label": "B) 1", "correct": False},
                    {"label": "C) 2/3", "correct": False}
                ]
            },
            {
                "id": 3,
                "tag": "ORTA NOKTA KAYMA STRATEJİSİ",
                "question": "80 cm uzunluğundaki bir çıtanın bir ucundan 1/4'ü kesilip atılıyor. Çıtanın orta noktası ilk durumuna göre kaç santimetre kayar?",
                "options": [
                    {"label": "A) 10 cm (Kesilen parça 20 cm olup orta nokta 20 ÷ 2 = 10 cm kayar)", "correct": True},
                    {"label": "B) 20 cm", "correct": False},
                    {"label": "C) 5 cm", "correct": False}
                ]
            }
        ],
        "extra_questions": [
            {
                "id": 1,
                "tag": "YENİ NESİL • GERÇEK YAŞAM HAVUZ VE DEPO PROBLEMİ",
                "scenario": "Bir su deposunun içinde bir miktar su vardır. Depoya 60 litre su eklendiğinde deponun 3/4'ü dolmaktadır. Başlangıçta depodaki su tüm deponun 1/3'ü kadardı.",
                "stem": "Buna göre bu su deposunun tamamı kaç litre su almaktadır?",
                "choices": [
                    "144 Litre",
                    "120 Litre",
                    "160 Litre",
                    "180 Litre"
                ],
                "correctIndex": 0,
                "explanation": "60 litre su (3/4 - 1/3) oranına karşılık gelir. Payda eşitlersek 9/12 - 4/12 = 5/12. Deponun 5/12'si 60 litre ise; 1/12'si 60 ÷ 5 = 12 litredir. Tamamı 12 × 12 = 144 litredir."
            },
            {
                "id": 2,
                "tag": "YENİ NESİL • ÇOK ADIMLI İŞLEMLER VE MERDİVEN KESİR",
                "scenario": "Bir matematik olimpiyatında tahtaya şu merdivenli kesir yazılmıştır: 2 + [ 1 / (1 + 1/2) ].",
                "stem": "Bu işlemin en sade rasyonel sayı sonucu hangisidir?",
                "choices": [
                    "8/3",
                    "5/3",
                    "7/2",
                    "2"
                ],
                "correctIndex": 0,
                "explanation": "Paydadaki işlem: 1 + 1/2 = 3/2. 1 ÷ (3/2) = 2/3. En dıştaki işlem: 2 + 2/3 = 6/3 + 2/3 = 8/3."
            },
            {
                "id": 3,
                "tag": "YENİ NESİL • KİTAP OKUMA VE KALAN SAYFA MODELİ",
                "scenario": "Zeynep 300 sayfalık bir kitabın 1. gün 2/5'ini, 2. gün kalan sayfaların 3/4'ünü okumuştur.",
                "stem": "Zeynep'in kitabı bitirebilmesi için geriye okunmamış kaç sayfası kalmıştır?",
                "choices": [
                    "45 sayfa",
                    "60 sayfa",
                    "30 sayfa",
                    "75 sayfa"
                ],
                "correctIndex": 0,
                "explanation": "1. gün: 300 × (2/5) = 120 sayfa okundu. Kalan = 300 - 120 = 180 sayfa. 2. gün: 180 × (3/4) = 135 sayfa okundu. Geriye kalan = 180 - 135 = 45 sayfa."
            },
            {
                "id": 4,
                "tag": "YENİ NESİL • TEL KESME VE ORTA NOKTA HAREKETİ",
                "scenario": "Marangoz Metin Usta, 120 cm uzunluğundaki tahta çıtanın sağ ucundan 1/6'sını, sol ucundan ise kalan tahtanın 1/5'ini kesip atıyor.",
                "stem": "Son durumda tahtanın orta noktası ilk duruma göre kaç santimetre ve hangi yöne kaymıştır?",
                "choices": [
                    "Orta nokta hiç kaymamıştır (Her iki uçtan da eşit 20 cm kesildiği için)",
                    "5 cm sağa kaymıştır",
                    "10 cm sola kaymıştır",
                    "2 cm sağa kaymıştır"
                ],
                "correctIndex": 0,
                "explanation": "Sağdan: 120 × (1/6) = 20 cm kesildi (orta noktayı 10 cm sola kaydırır). Kalan tahta 100 cm. Soldan: 100 × (1/5) = 20 cm kesildi (orta noktayı 10 cm sağa kaydırır). Zıt yönlü eşit kaymalar birbirini nötrler (10 - 10 = 0 cm kayar)."
            },
            {
                "id": 5,
                "tag": "YENİ NESİL • NEGATİF RASYONEL ÇARPMA VE KUVVET",
                "scenario": "Bir laboratuvardaki soğutucu cihaz, sıcaklığı her saat önceki saatteki sıcaklığın (-2/3)'si katına ayarlamaktadır. Başlangıç sıcaklığı +54°C'dir.",
                "stem": "Buna göre 3 saat sonra soğutucu odadaki sıcaklık kaç °C olur?",
                "choices": [
                    "-16°C",
                    "+16°C",
                    "-24°C",
                    "+36°C"
                ],
                "correctIndex": 0,
                "explanation": "1. saat: 54 × (-2/3) = -36°C. 2. saat: -36 × (-2/3) = +24°C. 3. saat: +24 × (-2/3) = -16°C. Veya 54 × (-2/3)³ = 54 × (-8/27) = 2 × (-8) = -16°C."
            },
            {
                "id": 6,
                "tag": "YENİ NESİL • GELİR-GİDER VE BÜTÇE DENGELEME",
                "scenario": "Bir esnaf bir ayda elde ettiği gelirin 3/10'unu vergiye, 1/4'ünü çalışan maaşlarına ve 1/5'ini dükkan kirasına harcamıştır. Geriye net 15.000 TL kar kalmıştır.",
                "stem": "Bu esnafın bir aylık toplam geliri kaç TL'dir?",
                "choices": [
                    "60.000 TL",
                    "50.000 TL",
                    "75.000 TL",
                    "45.000 TL"
                ],
                "correctIndex": 0,
                "explanation": "Paydaları 20'de eşitleyelim: 3/10 = 6/20, 1/4 = 5/20, 1/5 = 4/20. Toplam harcama = 6/20 + 5/20 + 4/20 = 15/20 = 3/4. Geriye kalan = 1 - 3/4 = 1/4. Gelirin 1/4'ü 15.000 TL ise tamamı 15.000 × 4 = 60.000 TL'dir."
            },
            {
                "id": 7,
                "tag": "YENİ NESİL • TERSİNE PROBLEM KURMA MUHAKEMESİ",
                "scenario": "Öğretmen tahtaya '[ (3/4) × X ] + 15 = 45' denklemini yazmış ve öğrencilerden buna uygun bir gerçek yaşam problemi kurgulamalarını istemiştir.",
                "stem": "Aşağıdaki öğrenci problemlerinden hangisi tahtadaki matematiksel duruma tam olarak uygundur?",
                "choices": [
                    "Kerem: 'Paramın 3/4'ünün 15 TL fazlası 45 TL olduğuna göre paramın tamamı kaç TL'dir?'",
                    "Banu: 'Paramın 15 TL fazlasının 3/4'ü 45 TL'dir.'",
                    "Can: '3/4 kg elma ile 15 kg armut 45 TL'dir.'",
                    "Deniz: '45 TL'nin 3/4'ü kaçtır?'"
                ],
                "correctIndex": 0,
                "explanation": "Paraya X dersek; paramın 3/4'ü (3/4 × X), 15 TL fazlası (+15) ve sonucu 45 TL'dir (=45). Kerem'in kurgusu birebir denklemi modellemektedir."
            },
            {
                "id": 8,
                "tag": "YENİ NESİL • BENZİN DEPOSU VE YOL PROBLEMİ",
                "scenario": "Bir otomobilin benzin deposunun 5/8'i doludur. Otomobil 240 km yol gittiğinde deponun 1/4'ü boşalmıştır.",
                "stem": "Buna göre tam dolu bir depo benzinle bu otomobil toplam kaç kilometre yol gidebilir?",
                "choices": [
                    "960 km",
                    "800 km",
                    "1200 km",
                    "720 km"
                ],
                "correctIndex": 0,
                "explanation": "Deponun 1/4'ü ile 240 km yol gidiliyorsa, tamamı (4/4'ü) ile 240 × 4 = 960 km yol gidilir."
            },
            {
                "id": 9,
                "tag": "YENİ NESİL • ALAN VE KESİR ÇARPIMI MODELİ",
                "scenario": "Kısa kenarı 3/5 metre, uzun kenarı 5/6 metre olan dikdörtgen şeklindeki bir resim çerçevesinin içine, kenarlarından 1/10 metre içeride kalacak şekilde bir fotoğraf yerleştirilecektir.",
                "stem": "Resim çerçevesinin toplam alanı kaç metrekaredir?",
                "choices": [
                    "1/2 m² ( (3/5) × (5/6) = 15/30 = 1/2 )",
                    "8/11 m²",
                    "2/3 m²",
                    "1/4 m²"
                ],
                "correctIndex": 0,
                "explanation": "Dikdörtgenin alanı = Kısa kenar × Uzun kenar = (3/5) × (5/6) = (3×5)/(5×6) = 15/30 = 1/2 m²."
            },
            {
                "id": 10,
                "tag": "YENİ NESİL • ADIM SAYISI VE MESAFE",
                "scenario": "Ali her adımında 3/4 metre, kardeşi Veli ise her adımında 2/5 metre yol almaktadır. İkisi aynı noktadan aynı yöne doğru 20'şer adım atmıştır.",
                "stem": "20 adım sonunda Ali ile Veli arasındaki mesafe kaç metre olur?",
                "choices": [
                    "7 metre",
                    "5 metre",
                    "8 metre",
                    "6 metre"
                ],
                "correctIndex": 0,
                "explanation": "Ali'nin aldığı yol = 20 × (3/4) = 15 metre. Veli'nin aldığı yol = 20 × (2/5) = 8 metre. Aralarındaki fark = 15 - 8 = 7 metre. Veya 20 × (3/4 - 2/5) = 20 × (15/20 - 8/20) = 20 × (7/20) = 7 metre."
            }
        ]
    }
]
