# Yalın Üretim ve Altı Sigma (Lean Six Sigma)

Endüstri mühendisliğinde üretim ve hizmet süreçlerinin verimliliğini artırmak, israfları azaltmak ve hata oranlarını sıfıra yaklaştırmak amacıyla Yalın Üretim ve Altı Sigma metodolojileri birlikte uygulanır.

## OEE (Toplam Ekipman Etkinliği) Nedir?

OEE (Overall Equipment Effectiveness), bir üretim operasyonunun ne kadar etkin yürütüldüğünü ölçen uluslararası bir standarttır. Üç temel bileşenin çarpımı ile hesaplanır:

$$\text{OEE} = \text{Kullanılabilirlik} \times \text{Performans} \times \text{Kalite}$$

1.  **Kullanılabilirlik (Availability):** Makinenin planlanan çalışma süresine kıyasla fiilen ne kadar süre çalıştığıdır. Duruş kayıplarını (arızalar, kurulumlar) kapsar.
    $$\text{Kullanılabilirlik} = \frac{\text{Fiili Çalışma Süresi}}{\text{Net Planlanan Çalışma Süresi}}$$
2.  **Performans (Performance):** Makinenin fiili çalışma süresinde ne kadar hızlı çalıştığıdır. Hız kayıplarını (yavaşlamalar, kısa duruşlar) kapsar.
    $$\text{Performans} = \frac{\text{Üretilen Toplam Adet} \times \text{İdeal Çevrim Süresi}}{\text{Fiili Çalışma Süresi}}$$
3.  **Kalite (Quality):** Üretilen toplam adet içindeki hatasız ürün oranıdır. Iskarta ve hatalı üretim kayıplarını kapsar.
    $$\text{Kalite} = \frac{\text{Üretilen Toplam Adet} - \text{Hatalı Ürün Adedi}}{\text{Üretilen Toplam Adet}}$$

*Dünya standartlarında mükemmel kabul edilen OEE oranı **%85 ve üzeri**dir.*

---

## Altı Sigma (Six Sigma) ve DPMO Hesaplama

Altı Sigma, hata oranlarını azaltarak kaliteyi mükemmelleştirmeyi amaçlayan istatistiksel bir disiplindir. Süreç yeteneği (process capability) seviyesi olan Sigma Seviyesi yükseldikçe hata olasılığı düşer.

*   **DPO (Defects Per Opportunity):** Birim fırsat başına düşen hata oranı.
*   **DPMO (Defects Per Million Opportunities):** Bir milyon fırsatta ortaya çıkan hata sayısı.
    $$\text{DPMO} = \text{DPO} \times 1,000,000 = \frac{\text{Toplam Hata Sayısı}}{\text{Toplam Ürün Adedi} \times \text{Ürün Başına Hata Fırsatı}} \times 1,000,000$$

### Sigma Seviyeleri ve Hata Oranları (1.5 Sigma Sapma / Shift Dahil):
*   **1 Sigma:** 690,000 DPMO (%30.9 Verimlilik)
*   **2 Sigma:** 308,537 DPMO (%69.1 Verimlilik)
*   **3 Sigma:** 66,807 DPMO (%93.3 Verimlilik)
*   **4 Sigma:** 6,210 DPMO (%99.38 Verimlilik)
*   **5 Sigma:** 233 DPMO (%99.977 Verimlilik)
*   **6 Sigma:** 3.4 DPMO (%99.99966 Verimlilik)

---

## Takt Süresi ve Hat Dengeleme (Line Balancing)

*   **Takt Süresi (Takt Time):** Müşteri talebini karşılamak için montaj hattında bir ürünün en fazla ne kadar sürede çıkması gerektiğini gösteren ritim süresidir.
    $$\text{Takt Süresi} = \frac{\text{Net Çalışma Süresi (Saniye)}}{\text{Müşteri Talebi (Adet)}}$$
*   **Hat Dengeleme (Line Balancing):** Montaj hattındaki iş istasyonlarının çevrim sürelerini birbirine yakınlaştırarak darboğazları engelleme ve verimliliği artırma sürecidir.
*   **Hat Dengeleme Verimliliği (Line Balance Efficiency - LBE):**
    $$\text{LBE } \% = \frac{\sum \text{İstasyon Süreleri}}{\text{İstasyon Sayısı} \times \text{En Yüksek İstasyon Süresi}} \times 100$$

---

## Klasördeki Araç

*   **[oee_sigma_calculator.py](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/industrial-engineering/lean-six-sigma/oee_sigma_calculator.py):** Üretim verilerine göre OEE, DPMO ve 1.5 Sigma kaydırılmış Sigma Seviyesini hesaplamanın yanı sıra, müşteri talebine göre **Takt Süresi** ve istasyon sürelerine göre **Montaj Hattı Dengeleme Verimliliği** analizi yapabilen etkileşimli bir CLI hesaplama aracıdır.
