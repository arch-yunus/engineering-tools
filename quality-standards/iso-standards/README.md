# Kalite Yönetim Sistemleri ve Gıda Güvenliği Standartları

Mühendislik ve üretim süreçlerinin sürdürülebilir, güvenli ve yüksek kalitede yürümesini sağlamak amacıyla global standartlar uygulanır. Bu standartlara uyum, bağımsız denetim kuruluşları tarafından düzenli olarak denetlenir ve sertifikalandırılır.

## Temel Kalite ve Güvenlik Standartları

### 1. ISO 9001:2015 (Kalite Yönetim Sistemi - QMS)
Sektör bağımsız olarak tüm kuruluşların müşteri memnuniyetini artırmak, süreçlerini sürekli iyileştirmek ve kalite hedeflerini tutturmak için uyguladığı temel yönetim sistemidir.
*   **Temel Felsefe:** PUKÖ Döngüsü (Planla - Uygula - Kontrol Et - Önlem Al) ve Risk Tabanlı Düşünme.

### 2. ISO 22000:2018 (Gıda Güvenliği Yönetim Sistemi - FSMS)
Tarladan sofraya tüm gıda zincirinde yer alan kuruluşların, gıdaların tüketim anında güvenli olmasını sağlamak için tehlikeleri kontrol altına aldığı standarttır.

### 3. HACCP (Tehlike Analizi ve Kritik Kontrol Noktaları)
Gıda güvenliği için biyolojik, kimyasal ve fiziksel risklerin bilimsel yöntemlerle analiz edildiği ve kontrol altına alındığı sistematik yaklaşımdır. ISO 22000 standardının kalbini oluşturur.
*   **KKN (Kritik Kontrol Noktası):** Hatanın önlenmesi veya kabul edilebilir seviyeye indirilmesi için kontrolün uygulanabildiği ve kritik limitlerin (örnek sıcaklık, pH) izlendiği son proses adımıdır.

### 4. GMP (Good Manufacturing Practices - İyi Üretim Uygulamaları)
Gıda, ilaç, kozmetik ve tıbbi cihazların kalitesinin korunması için altyapı, tesis hijyeni ve personel kontrolüne odaklanan asgari üretim koşulları rehberidir.

---

## HACCP'in 7 Temel İlkesi

1.  **Tehlike Analizi Yapılması:** Potansiyel gıda güvenliği tehlikelerinin belirlenmesi.
2.  **Kritik Kontrol Noktalarının (KKN) Belirlenmesi:** Risklerin kontrol altına alınacağı noktaların tespiti.
3.  **Kritik Limitlerin Belirlenmesi:** KKN'ler için sınır değerlerin (örn: Fırın sıcaklığı $\ge 72^\circ\text{C}$) tanımlanması.
4.  **İzleme Sisteminin Kurulması:** KKN'lerin ölçülmesi ve izlenmesi (örn: Sıcaklık sensörü).
5.  **Düzeltici Faaliyetlerin Belirlenmesi:** Limit aşıldığında yapılacak işlemler (örn: Ürünü karantinaya al).
6.  **Doğrulama Prosedürlerinin Oluşturulması:** Sistemin doğru çalıştığının laboratuvar analizleri veya iç denetimle teyit edilmesi.
7.  **Dokümantasyon ve Kayıt Tutma:** Tüm süreçlerin kayıt altına alınması.

---

## Klasördeki Araç

*   **[audit_checklist.py](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/quality-standards/iso-standards/audit_checklist.py):** ISO 9001 ve ISO 22000/HACCP gereksinim maddelerini temel alarak interaktif iç denetim gerçekleştiren, uygunsuzlukları ve denetçi bulgularını kaydeden ve denetim raporunu `.txt` formatında dışa aktaran bir denetim asistanı aracıdır.
