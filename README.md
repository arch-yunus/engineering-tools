# 🛠️ Engineering Tools (Mühendislik Araçları ve Standartları)

![Engineering Tools Banner](assets/banner.jpg)

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Maintained: Yes](https://img.shields.io/badge/Maintained-Yes-green.svg)
![Contributions: Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

Bu depo, farklı mühendislik disiplinlerinde kullanılan temel yazılımlar, matematiksel modellemeler, otomasyon altyapıları, kalite standartları ve sürdürülebilirlik konularının kapsamlı bir referans rehberi ve **interaktif konsol araçları** koleksiyonudur. Çok disiplinli projeler geliştiren mühendisler, araştırmacılar ve teknik ekipler için bir bilgi bankası ve pratik araç kütüphanesi niteliği taşır.

---

## 📌 İçindekiler
1. [Hakkında](#-hakkında)
2. [Hızlı Başlangıç (Launcher Arayüzü)](#-hızlı-başlangıç-launcher-arayüzü)
3. [Teknoloji, Program ve Dil Kataloğu](#-teknoloji-program-ve-dil-kataloğu)
4. [Mühendislik Branşları ve Araçları](#-mühendislik-branşları-ve-araçları)
    - [Yazılım ve Veri Analizi](#1-yazılım-ve-veri-analizi)
    - [Elektrik-Elektronik ve Otomasyon](#2-elektrik-elektronik-ve-otomasyon)
    - [Makine ve İnşaat Mühendisliği](#3-makine-ve-inşaat-mühendisliği)
    - [Endüstri Mühendisliği](#4-endüstri-mühendisliği)
    - [Kalite Yönetimi ve Gıda Güvenliği](#5-kalite-yönetimi-ve-gıda-güvenliği)
    - [Çevre ve Sürdürülebilirlik](#6-çevre-ve-sürdürülebilirlik)
5. [Proje Klasör Yapısı](#-proje-klasör-yapısı)
6. [Kurulum ve Çalıştırma](#-kurulum-ve-çalıştırma)
7. [Katkıda Bulunma (Contributing)](#-katkıda-bulunma)
8. [Mühendislik Alıntıları ve Kaynakça](#-mühendislik-alıntıları-ve-kaynakça)
9. [Lisans](#-lisans)

---

## 📖 Hakkında
Modern mühendislik projeleri artık tek bir disiplinin sınırları içinde kalmamakta, yazılım, otomasyon, mekanik, kalite ve çevre süreçlerinin entegrasyonuyla şekillenmektedir. Bu deponun amacı, her bir mühendislik alanının temel kavramlarını teorik olarak açıklarken, aynı zamanda mühendislerin günlük işlerinde kullanabileceği **aktif çalışan Python araçlarını** tek bir çatı altında sunmaktır.

---

## 🚀 Hızlı Başlangıç (Launcher Arayüzü)

Projeyi bilgisayarınıza indirdikten sonra, tüm araçları tek bir menüden yönetmek ve çalıştırmak için kök dizinde bulunan merkezi yönlendiriciyi çalıştırabilirsiniz:

```bash
python run_tools.py
```

Bu komut size aşağıdaki gibi interaktif bir konsol arayüzü sunacaktır:
```text
==================================================
     🛠️  MÜHENDİSLİK ARAÇLARI KONSOL ARAYÜZÜ      
==================================================
1. Yazılım ve Bilgisayar Mühendisliği
2. Elektrik-Elektronik ve Otomasyon Mühendisliği
3. Makine ve İnşaat Mühendisliği
4. Endüstri Mühendisliği (Yalın & Altı Sigma)
5. Kalite Standartları ve Güvenlik (ISO & HACCP)
6. Çevre ve Sürdürülebilirlik
0. Çıkış
==================================================
```

---

## 📊 Teknoloji, Program ve Dil Kataloğu

Aşağıdaki tablolarda, görsel envanterimizde yer alan tüm dil, program ve uluslararası kalite standartları kategorilerine göre detaylı şekilde incelenmiştir.

### 💻 Yazılım ve Bilgisayar

| Araç / Dil | Okunuşu | Görseldeki Tanımı | Detaylı İnceleme ve Mühendislikteki Rolü |
| :--- | :--- | :--- | :--- |
| **Python** | Paytın | Yapay zeka, veri analizi, otomasyon ve yazılım geliştirme. | Yüksek seviyeli, genel amaçlı programlama dili. Yapay zeka (TensorFlow, PyTorch), veri analitiği (Pandas, NumPy) ve sistem otomasyonlarında sektör standardıdır. |
| **Java** | Cava | Büyük ölçekli uygulamalar ve Android uygulamaları geliştirme. | Sınıf tabanlı, nesne yönelimli dil. Özellikle büyük kurumsal arka ofis yazılımlarında, dağıtık sistemlerde ve Android mobil uygulama altyapısında kullanılır. |
| **C#** | Si Şarp | Masaüstü programlar, web uygulamaları ve oyun geliştirme. | Microsoft tarafından geliştirilen nesne yönelimli dil. Windows masaüstü araçlarında (WPF, WinForms), kurumsal web platformlarında (ASP.NET) ve Unity ile oyun geliştirmede temeldir. |
| **JavaScript** | Cava Script | Web sitelerinin etkileşimli olmasını sağlar. | Dinamik web tarayıcısı betik dili. Web tabanlı mühendislik panelleri, gösterge tabloları (dashboard), gerçek zamanlı grafik izleme arayüzleri ve IoT görselleştirmelerinde vazgeçilmezdir. |
| **SQL** | Es Kyu El | Veri tabanındaki bilgileri saklamak, düzenlemek ve sorgulamak. | İlişkisel veritabanı yönetim dili. Üretim geçmişi, ürün katalogları, deney test sonuçları ve ERP verilerinin yapılandırılmış şekilde depolanması ve hızlıca çekilmesinde kullanılır. |
| **Git** | Git | Yazılım projelerindeki değişiklikleri takip etmeyi sağlar. | Dağıtık versiyon kontrol sistemi. Kod tabanındaki değişikliklerin geçmişini tutar, farklı mühendislerin aynı kod üzerinde çakışmadan çalışmasını ve geriye dönük hata takibini sağlar. |
| **GitHub** | GitHab | Projeleri internet üzerinde saklar ve ekip halinde çalışmayı kolaylaştırır. | Git tabanlı bulut depolama ve iş birliği platformu. Projelerin sürüm takibini, takım içi kod incelemelerini (Pull Request) ve CI/CD (Sürekli Entegrasyon/Dağıtım) süreçlerini yönetir. |
| **AWS** | Ey Dablyu Es | Uygulamaların ve verilerin bulut sunucularda çalışmasını sağlar. | Amazon Web Services. Sanal sunucular, veri depolama alanları, IoT veri analitiği motorları ve veritabanı servisleri sunarak büyük mühendislik uygulamalarını buluta taşır. |
| **Azure** | Ajur | Bulut hizmetleri sunar, büyük şirketler tarafından kullanılır. | Microsoft bulut platformu. Windows sunucuları, Active Directory entegrasyonu, yapay zeka analiz araçları ve hibrit bulut mimarileri ile kurumsal üretim tesislerinde veri merkezi rolü oynar. |

### ⚡ Elektrik-Elektronik ve Mekatronik

| Araç / Standart | Okunuşu | Görseldeki Tanımı | Detaylı İnceleme ve Mühendislikteki Rolü |
| :--- | :--- | :--- | :--- |
| **PLC** | Pi El Si | Fabrikalardaki makineleri ve üretim hatlarını kontrol eder. | Programlanabilir Mantıksal Denetleyici. Endüstriyel ortamlar için tasarlanmış, gerçek zamanlı çalışan mikroişlemci tabanlı donanım. Motorlar, valfler, sensörler ve aktüatörleri milisaniyeler içinde kontrol eder. |
| **SCADA** | Skada | Fabrikadaki tüm sistemlerin tek ekrandan izlenmesini ve yönetilmesini sağlar. | Denetimsel Kontrol ve Veri Toplama Sistemi. Fabrika sahasındaki PLC'lerden veri toplayıp operatörlere grafiksel ekranlar üzerinden tesis sıcaklıklarını, basınçlarını, motor durumlarını izleten ve müdahale ettiren yazılım katmanı. |
| **EPLAN** | İ Plan | Elektrik projelerinin ve devre şemalarının çizilmesini sağlar. | Elektriksel CAD programı. Fabrika panoları, kablolar, klemensler, röleler ve otomatik kumanda şemalarının uluslararası (IEC/ANSI) standartlara uygun çizilmesini ve parça listelerinin (BOM) üretilmesini sağlar. |

### 🏗️ Makine ve İnşaat

| Araç / Süreç | Okunuşu | Görseldeki Tanımı | Detaylı İnceleme ve Mühendislikteki Rolü |
| :--- | :--- | :--- | :--- |
| **AutoCAD** | Oto Ked | Teknik çizim ve proje hazırlamak için kullanılır. | 2 boyutlu ve temel 3 boyutlu bilgisayar destekli tasarım (CAD) yazılımı. Mimari kat planları, inşaat detay çizimleri ve mekanik parça kesitleri için evrensel vektörel standarttır. |
| **SolidWorks** | Solid Vörks | 3 boyutlu makine parçaları ve ürünler tasarlar. | Parametrik 3D katı modelleme yazılımı. Makine parçaları, dişliler, sac metal tasarımları, mekanik montaj simülasyonları yapar ve imalat için teknik resimleri otomatik oluşturur. |
| **CATIA** | Katia | Otomobil, uçak ve karmaşık ürünlerin tasarımında kullanılır. | Üst seviye CAD/CAM/CAE yazılımı. Havacılık, savunma ve otomotiv sektörlerinde kompleks kavisli yüzey tasarımları (surfacing), yapısal analizler ve geniş montaj hiyerarşileri için kullanılır. |
| **CNC** | Si En Si | Bilgisayar kontrollü üretim makinelerini çalıştırmayı sağlar. | Bilgisayarlı Sayısal Kontrol. Torna, freze, lazer kesim ve punch makinelerinin insan gücü yerine G-kodu direktifleriyle hareket ettirilerek mikron hassasiyetinde parça işlemesini sağlayan üretim altyapısı. |
| **Primavera** | Primavera | Büyük projelerin zaman planını ve iş programını oluşturur. | Oracle Primavera P6. Havalimanı, baraj, otoyol gibi büyük ölçekli ve çok paydaşlı inşaat projelerinde kritik yol analizi (CPM), kaynak optimizasyonu, maliyet bütçeleme ve ilerleme takibi yapar. |
| **MS Project** | Em Es Projekt | Projelerin hangi tarihte başlayıp biteceğini planlar. | Microsoft Project. Gantt şemaları, iş kırılım yapıları (WBS) ve kaynak atamaları oluşturarak proje yöneticilerinin teslim tarihlerini, gecikmeleri ve görev bağımlılıklarını izlemesini sağlar. |

### 📊 Endüstri Mühendisliği

| Metot / Araç | Okunuşu | Görseldeki Tanımı | Detaylı İnceleme ve Mühendislikteki Rolü |
| :--- | :--- | :--- | :--- |
| **SAP** | Es Ey Pi | Şirketlerin tüm iş süreçlerini tek sistemden yönetir. | Kurumsal ERP yazılımı. Satış, finans, malzeme tedariği, depo yönetimi, üretim planlama ve insan kaynakları modülleriyle devasa işletmelerin verilerini birbirine entegre eden pazar lideri sistem. |
| **ERP** | İ Ar Pi | Şirketin tüm iş süreçlerini tek bir çatı altında toplar. | Kurumsal Kaynak Planlaması (Enterprise Resource Planning). Şirketlerin fiziki, beşeri ve finansal kaynaklarını verimli kullanmak üzere tüm departmanları ortak bir veri tabanında birleştiren yönetim felsefesidir. |
| **Power BI** | Pavir Bi Ay | Verileri grafiklere ve raporlara dönüştürür. | Microsoft İş Zekası (BI) aracı. Excel, SQL ve buluttaki karmaşık üretim ve finans verilerini alarak yöneticiler için interaktif görsel raporlar, KPI takipleri ve analiz panelleri oluşturur. |
| **Lean** | Lin | İsrafı azaltarak işleri daha verimli hale getirmeyi amaçlar. | Yalın Üretim. Toyota üretim sistemine dayanan, süreçlerdeki israfları (Muda: Aşırı üretim, bekleme, taşıma, gereksiz işlem vb.) yok ederek kaliteyi, hızı ve müşteri değerini artırmayı amaçlayan felsefe. |
| **Six Sigma** | Siks Sigma | Hataları azaltıp kaliteyi artırmak için kullanılan bir yöntemdir. | İstatistiksel kalite iyileştirme metodolojisi. Süreçlerdeki varyasyonu azaltarak milyonda en fazla 3.4 hata (DPMO) hedefleyen, DMAIC (Tanımla, Ölç, Analiz Et, İyileştir, Kontrol Et) çevrimini kullanan sistem. |

### 🧪 Kimya ve Gıda

| Standart / Sistem | Okunuşu | Görseldeki Tanımı | Detaylı İnceleme ve Mühendislikteki Rolü |
| :--- | :--- | :--- | :--- |
| **HACCP** | Hasıp | Gıdanın güvenli üretilmesini sağlayan sistem. | Tehlike Analizi ve Kritik Kontrol Noktaları. Hammaddeden tüketime kadar gıda güvenliğini tehdit eden biyolojik, kimyasal ve fiziksel risklerin belirlenmesi ve Kritik Kontrol Noktalarında önleyici tedbirlerle engellenmesi sistemidir. |
| **GMP** | Ci Em Pi | İlaç ve gıda üretiminin kalite standartlarına uygun yapılmasını sağlar. | İyi Üretim Uygulamaları (Good Manufacturing Practices). İnsan sağlığını doğrudan etkileyen gıda, ilaç ve kozmetik üretim tesislerinin hijyen, tasarım, personel ve dokümantasyon standartlarını belirleyen asgari yasal kurallar. |
| **ISO** | Ay So | Kalite yönetim sistemleri uluslararası standartlardır. | Uluslararası Standartlar Teşkilatı. Ürünlerin, hizmetlerin ve sistemlerin kalitesini, güvenliğini ve verimliliğini küresel düzeyde ortak kurallarla tescilleyen bağımsız kuruluştur. |
| **ISO 22000** | Ay So Yirmi İki Bin | Gıda güvenliği yönetim sistemi standardı. | Çiftlikten sofraya tüm gıda zincirinde geçerli, HACCP ilkelerini de kapsayan, hijyen ve gıda güvenliği yönetimini sertifikalandıran küresel kalite standardıdır. |

### 🌿 Çevre ve Diğer Alanlar

| Standart / Süreç | Okunuşu | Görseldeki Tanımı | Detaylı İnceleme ve Mühendislikteki Rolü |
| :--- | :--- | :--- | :--- |
| **ISO 14001** | Ay So On Dört Bin Bir | Çevre yönetim sistemi standardı. | Kuruluşların çevresel etkilerini (atık yönetimi, karbon ayak izi, enerji tüketimi) sistematik bir yaklaşımla kontrol etmesini, azaltmasını ve yasal çevre mevzuatlarına uymasını sağlayan standarttır. |
| **ÇED** | Çevresel Etki Değerlendirmesi | Projelerin çevreye etkisini analiz eden rapor sürecidir. | Fabrika, baraj, otoyol gibi yatırımların inşaat ve işletme aşamalarında çevreye vereceği zararlı etkilerin analiz edildiği, bu etkileri önlemek adına gerekli önlemlerin belirlendiği resmi yasal izin ve raporlama süreci. |

---


## ⚙️ Mühendislik Branşları ve Araçları

### 1. Yazılım ve Veri Analizi

> 💬 *"First, solve the problem. Then, write the code."* — John Johnson  
> 💬 *"Talk is cheap. Show me the code."* — Linus Torvalds

*   **Betimsel İstatistik ve Lineer Regresyon:** Herhangi bir kütüphaneye bağımlı olmadan çalışan veri analiz aracı.
*   **Birim Dönüştürücü:** Sıcaklık (C/F), Basınç (Bar/PSI/Pascal) ve Uzunluk (İnç/mm) arası dönüşümler.
*   **Malzeme Veri Tabanı Yöneticisi:** SQLite tabanlı, mühendislik malzemelerinin mekanik ve fiziksel özelliklerini saklayan, sorgulayan ve yöneten veritabanı CRUD aracı.
*   **Kılavuzlar:** Python kütüphaneleri (NumPy, Pandas, SciPy, Matplotlib) ve ilişkisel SQL veritabanı kavramları.
*   *Dizin:* [software/](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/software/)

### 2. Elektrik-Elektronik ve Otomasyon

> 💬 *"Automation is good, so long as you know exactly where to put the machine."* — Eliyahu M. Goldratt

*   **PLC Register ve Modbus Simülatörü:** Coils, Discrete Inputs, Input Registers ve Holding Registers yapılarını simüle eden, motor hızı, sıcaklık ve termodinamik dengeleri çevrimsel (Scan Cycle) işleyen interaktif simülatör.
*   **Kılavuzlar:** IEC 61131-3 PLC programlama dilleri, Structured Text (ST) örnekleri ve Modbus protokol detayları.
*   *Dizin:* [automation-electronics/](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/automation-electronics/)

### 3. Makine ve İnşaat Mühendisliği

> 💬 *"Scientists study the world as it is; engineers create the world that has never been."* — Theodore von Kármán  
> 💬 *"Design is not just what it looks like and feels like. Design is how it works."* — Steve Jobs

*   **CNC G-Kodu Jeneratörü:** Dikdörtgen ve daire profilleri için kesim parametrelerine (ilerleme hızı, spindle devri, takım çapı, emniyetli Z) göre CNC makineleri için G-Kodu üreten CAM aracı.
*   **CPM Proje Planlayıcı:** Görevler, süreler ve bağımlılıkları analiz ederek Erken/Geç Başlangıç ve Bitiş zamanlarını hesaplayan, bollukları (slack) bulan ve Kritik Yol'u (Critical Path) çıkaran planlama motoru.
*   **Kılavuzlar:** CAD/CAM dosya standartları (STEP, DXF, STL) ve Proje Yönetimi teorisi.
*   *Dizin:* [mechanical-civil/](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/mechanical-civil/)

### 4. Endüstri Mühendisliği

> 💬 *"Without data, you're just another person with an opinion."* — W. Edwards Deming  
> 💬 *"If you can't describe what you are doing as a process, you don't know what you are doing."* — W. Edwards Deming

*   **OEE Hesaplayıcı:** Kullanılabilirlik, Performans ve Kalite oranlarını hesaplayarak dünya standartlarında verimlilik analizi yapar.
*   **Altı Sigma Analizi:** Hatalı ürün ve fırsat sayılarına göre DPMO ve 1.5 Sigma kaydırılmış Sigma Seviyesini hesaplayan istatistiksel kalite aracı.
*   **Kılavuzlar:** Yalın Üretim prensipleri (5S, Kaizen, Kanban) ve Six Sigma kalitesi.
*   *Dizin:* [industrial-engineering/](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/industrial-engineering/)

### 5. Kalite Yönetimi ve Gıda Güvenliği

> 💬 *"Quality is not an act, it is a habit."* — Aristotle  
> 💬 *"Do it right the first time."* — Philip Crosby

*   **ISO Denetim Asistanı:** ISO 9001 ve ISO 22000 (HACCP) maddelerine göre iç denetim gerçekleştiren, minör/majör uygunsuzlukları ve denetçi bulgularını raporlayan, uyum yüzdesi çıkaran ve denetim raporunu metin olarak dışa aktaran asistan.
*   **Kılavuzlar:** QMS, HACCP prensipleri ve GMP (İyi Üretim Uygulamaları).
*   *Dizin:* [quality-standards/](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/quality-standards/)

### 6. Çevre ve Sürdürülebilirlik

> 💬 *"We do not inherit the Earth from our ancestors; we borrow it from our children."* — Native American Proverb  
> 💬 *"The greatest threat to our planet is the belief that someone else will save it."* — Robert Swan

*   **Sera Gazı (GHG) Karbon Ayak İzi Hesaplayıcı:** Tesis veya projeler için Kapsam 1 (Doğal gaz, yakıt tüketimi), Kapsam 2 (Elektrik) ve Kapsam 3 (Uçuşlar, ulaşım) emisyonlarını hesaplayan ve emisyon dağılımına göre azaltım önerileri sunan ESG hesaplayıcı.
*   **Kılavuzlar:** ISO 14001, ESG gereksinimleri ve sera gazı protokolü.
*   *Dizin:* [environment/](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/environment/)

---

## 📂 Proje Klasör Yapısı

Depo, disiplinlerin kolayca genişletilebileceği modüler bir yapıya sahiptir:

```text
engineering-tools/
│
├── run_tools.py                    # Merkezi CLI Menü Yönlendirici
│
├── software/
│   ├── python/                     # Veri analizi aracı ve kılavuz
│   ├── databases/                  # SQLite malzeme DB yöneticisi ve SQL kılavuzu
│   └── cloud/                      # AWS/Azure ve Docker kılavuzu
│
├── automation-electronics/
│   └── plc-scada/                  # PLC & Modbus simülatörü ve kılavuz
│
├── mechanical-civil/
│   ├── cad-cam/                    # CNC G-kodu üreteci ve komut kılavuzu
│   └── project-management/         # CPM (Kritik Yol) proje planlayıcı ve teorisi
│
├── industrial-engineering/
│   └── lean-six-sigma/             # OEE & Altı Sigma hesaplayıcı ve Yalın kılavuzu
│
├── quality-standards/
│   └── iso-standards/              # ISO 9001 & ISO 22000 denetim aracı ve kılavuz
│
├── environment/
│   └── sustainability-reports/     # Karbon Ayak İzi Hesaplayıcı ve ESG kılavuzu
│
└── README.md                       # Genel tanıtım ve kullanım kılavuzu
```

---

## 🛠 Kurulum ve Çalıştırma

Bu projede kullanılan tüm araçlar saf Python standart kütüphaneleri (SQLite3, Math, Subprocess vb.) kullanılarak geliştirilmiştir. Dolayısıyla **herhangi bir ek paket kurulumu (pip install vb.) yapmadan** doğrudan çalıştırabilirsiniz.

1. Depoyu bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/arch-yunus/engineering-tools.git
   ```
2. Proje dizinine gidin:
   ```bash
   cd engineering-tools
   ```
3. Launcher arayüzünü çalıştırın:
   ```bash
   python run_tools.py
   ```

---

## 🤝 Katkıda Bulunma

Geliştirmeye ve yeni mühendislik araçları eklemeye her zaman açığız! Katkıda bulunmak için şu adımları izleyebilirsiniz:

1. Bu depoyu forklayın (`Fork`).
2. Kendi çalışma dalınızı oluşturun (`git checkout -b feature/YeniArac`).
3. Değişikliklerinizi yapın ve commit'leyin (`git commit -m 'Yeni araç eklendi: MATLAB Analiz Modülü'`).
4. Dalınızı (branch) kendi deponuza itin (`git push origin feature/YeniArac`).
5. Bir Çekme İsteği (Pull Request) oluşturun.

---

## 📚 Mühendislik Alıntıları ve Kaynakça

### 💬 Alıntıların Mühendislik Analizi

*   **John Johnson & Linus Torvalds (Yazılım):** Johnson'ın *"Önce problemi çöz, sonra kod yaz"* uyarısı, mühendislikte algoritma tasarımının kodlamadan önce gelmesi gerektiğini belirtir. Torvalds'ın *"Laf ucuzdur, bana kodu göster"* felsefesi ise teorik fikirlerin çalışan somut bir prototiple kanıtlanması gerekliliğine (Proof of Concept) vurgu yapar.
*   **Eliyahu M. Goldratt (Otomasyon):** Kısıtlar Teorisi'nin (Theory of Constraints) kurucusu Goldratt, otomasyonun tek başına kurtarıcı olmadığını, eğer sistemdeki darboğaz (bottleneck) doğru yönetilmiyorsa otomasyonun sadece verimsizliği hızlandıracağını söyler.
*   **Theodore von Kármán (Tasarım/Mekanik):** *"Bilim insanları olanı inceler, mühendisler ise daha önce hiç var olmamışı yaratır."* Bu söz, mühendisliğin özünde yatan yaratıcılık, tasarım ve sentez kabiliyetini tanımlar.
*   **W. Edwards Deming (Kalite/Veri):** *"Veri olmadan sadece fikri olan başka bir insansınız."* Deming'in bu yaklaşımı, Altı Sigma ve istatistiksel kalite kontrolünün temelini oluşturur. Kararların hissiyatla değil, veri analiziyle alınması gerektiğini savunur.
*   **Philip Crosby (Üretim):** *"İşi ilk seferinde doğru yapın."* Crosby'nin "Sıfır Hata" (Zero Defects) yaklaşımı, sonradan düzeltme maliyetinin, hatayı ilk başta önleme maliyetinden kat kat yüksek olduğunu vurgular.

### 📖 Resmi Standartlar ve Akademik Referanslar

Bu projedeki araçların ve rehberlerin oluşturulmasında aşağıdaki uluslararası standartlar ve dokümanlar referans alınmıştır:

1.  **Python Standart Kütüphanesi:** Saf Python algoritmaları ve matematiksel işlemler için resmi dokümanlar.
    *   [Python Documentation Portal](https://docs.python.org/3/)
2.  **SQL ve SQLite İlişkisel Veritabanı:**
    *   [SQLite SQL Syntax & Specification](https://www.sqlite.org/lang.html)
3.  **Modbus Protokol Standartları:** `modbus_simulator.py` aracı için referans alınan protokol kılavuzu.
    *   [Modbus Organization Specifications](https://modbus.org/specs.php)
4.  **CNC ve G-Kodu Standartları:** CNC tornalama ve frezeleme yörüngeleri.
    *   *NIST RS274NGC G-Code Standard (Version 3)*: [NIST Internal Report](https://www.nist.gov/)
5.  **Kritik Yol Metodu (CPM) ve Proje Yönetimi:**
    *   *PMBOK Guide (A Guide to the Project Management Body of Knowledge)*, Project Management Institute (PMI).
6.  **OEE ve Yalın Altı Sigma Formülleri:**
    *   Deming, W. E. (1986). *Out of the Crisis*. Massachusetts Institute of Technology.
    *   Nakajima, S. (1988). *Introduction to TPM: Total Productive Maintenance*. Productivity Press.
7.  **Sera Gazı Protokolü (GHG Protocol):** Karbon ayak izi emisyon faktörleri hesaplama metodolojisi.
    *   [Greenhouse Gas Protocol Corporate Standard](https://ghgprotocol.org/)
    *   *EPA Greenhouse Gas Emission Factors Hub*: [EPA.gov](https://www.epa.gov/climateleadership/center-corporate-climate-leadership)
8.  **ISO Standartları Kaydı:**
    *   *ISO 9001:2015 - Quality Management Systems*: [ISO Catalogue](https://www.iso.org/standard/62085.html)
    *   *ISO 22000:2018 - Food Safety Management Systems*: [ISO Catalogue](https://www.iso.org/standard/65464.html)
    *   *ISO 14001:2015 - Environmental Management Systems*: [ISO Catalogue](https://www.iso.org/standard/60857.html)

---

## 📜 Lisans

Bu proje **MIT Lisansı** ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/LICENSE) dosyasına göz atabilirsiniz.