# Python ile Mühendislik ve Veri Analizi

Python, modern mühendislik dünyasında veri analizi, simülasyon, yapay zeka ve otomasyon süreçlerinde en çok tercih edilen dildir. Bu klasör, mühendislerin veri işlemesi ve modelleme yapması için temel kütüphaneleri ve referansları içerir.

## Kütüphane Envanteri

Mühendislik uygulamalarında yaygın olarak kullanılan temel kütüphaneler şunlardır:

1.  **NumPy:** Çok boyutlu diziler (matrisler) ve yüksek performanslı matematiksel fonksiyonlar.
2.  **SciPy:** Optimizasyon, integral, diferansiyel denklemler, sinyal işleme ve istatistik modülleri.
3.  **Pandas:** Yapılandırılmış verileri (CSV, Excel) okuma, filtreleme ve analiz etme (Veri Çerçeveleri - DataFrames).
4.  **Matplotlib & Seaborn:** İki ve üç boyutlu grafik çizimi ve görselleştirme.
5.  **SymPy:** Sembolik matematiksel hesaplamalar ve denklem çözümleri.

---

## Örnek Kurulumlar

Bu kütüphaneleri yerel bilgisayarınıza yüklemek için terminalde aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install numpy scipy pandas matplotlib sympy
```

---

## Örnek Kod Snippet'ı (Lineer Regresyon ve Grafik Çizimi)

Aşağıdaki Python kodu, NumPy ve Matplotlib kullanarak mühendislik deney verilerine eğri uydurma (curve fitting) işlemini gerçekleştirir:

```python
import numpy as np
import matplotlib.pyplot as plt

# Deneysel Veriler (Örn: Gerilme - Gerinim Verileri)
x_strain = np.array([0.0, 0.001, 0.002, 0.003, 0.004, 0.005])
y_stress = np.array([0.0, 210.0, 420.0, 610.0, 800.0, 950.0]) # MPa

# Lineer Regresyon (m: Eğilim/Elastisite Modülü, c: Sapma)
m, c = np.polyfit(x_strain, y_stress, 1)

print(f"Elastisite Modülü (E): {m:.2f} MPa")
print(f"Doğru Denklemi: Stress = {m:.2f} * Strain + {c:.2f}")

# Grafik Çizimi
plt.scatter(x_strain, y_stress, color='red', label='Deney Verileri')
plt.plot(x_strain, m * x_strain + c, color='blue', label='Regresyon Eğrisi')
plt.xlabel('Strain (Gerinim)')
plt.ylabel('Stress (Gerilme - MPa)')
plt.title('Hooke Kanunu / Elastisite Modülü Analizi')
plt.legend()
plt.grid(True)
plt.show()
```

---

## Polinom Eğri Uydurma (Polynomial Curve Fitting)

Deney verileri her zaman doğrusal bir hat izlemez. İkinci derece parabolik davranışlar sergileyen sistemlerde (örneğin aerodinamik sürtünme kuvveti $F_d = \frac{1}{2}\rho C_d A v^2$ veya gerilme-gerinim eğrisindeki plastik deformasyon bölgesi) **İkinci Derece Polinom Regresyonu** ($y = ax^2 + bx + c$) kullanılır.

Bu araç, matris hesaplamalarını saf Python determinant yöntemi (Cramer Kuralı) ile gerçekleştirerek ek kütüphaneler olmadan da hassas eğri uydurma işlemlerini çözer.

---

## Klasördeki Araç

*   **[data_analyzer.py](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/software/python/data_analyzer.py):** Herhangi bir ek kütüphane gerektirmeksizin (saf Python ile) çalışan betimsel istatistik, doğrusal ve ikinci derece **polinom regresyon analizleri** ($y = ax^2 + bx + c$), hız ve sıcaklık/basınç birimleri dönüştürücüsüdür.
