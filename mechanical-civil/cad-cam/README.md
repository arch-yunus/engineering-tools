# Bilgisayar Destekli Tasarım ve Üretim (CAD / CAM)

CAD (Computer-Aided Design) ve CAM (Computer-Aided Manufacturing) teknolojileri, mekanik parçaların bilgisayar ortamında tasarlanıp ardından CNC (Computer Numerical Control) tezgâhlarında üretilmesi sürecini kapsar.

## CAD/CAM Dosya Formatları ve Standartlar

Tasarım programları (SolidWorks, AutoCAD, CATIA vb.) arasında veri paylaşımı sağlamak amacıyla uluslararası standart dosya formatları kullanılır:

*   **STEP (.stp, .step):** 3D katı model paylaşımı için en popüler nötr dosya formatıdır (ISO 10303 standardı). Geometri ve montaj yapısını korur.
*   **IGES (.igs, .iges):** Daha eski bir standarttır. Katı modellerden ziyade yüzey modelleri ve tel kafes yapıları aktarmakta kullanılır.
*   **DXF (.dxf):** AutoCAD tarafından geliştirilen 2D çizimlerin aktarımı için kullanılan vektörel dosya formatıdır. CNC lazer/plazma kesim tezgahlarında yaygın olarak tercih edilir.
*   **STL (.stl):** 3D yazıcılar (katmanlı üretim) için tasarımları üçgensel ağ yüzeylerine (mesh) bölen standart formattır. Renk veya malzeme bilgisi içermez.

---

## G-Kodu (G-Code) Standart Komutları

G-Kodu, CNC makinelerinin (freze, torna, 3D yazıcı vb.) eksen hareketlerini, spindle (fener mili) hızlarını ve takım değişimlerini kontrol eden programlama dilidir.

| Komut | Açıklama | Örnek |
| :--- | :--- | :--- |
| **G00** | Belirtilen koordinata en yüksek hızla (kesim yapmadan) ilerleme | `G00 X50.0 Y20.0 Z5.0` |
| **G01** | Belirtilen ilerleme hızı (F) ile doğrusal kesim/ilerleme | `G01 Z-2.0 F400` |
| **G02** | Saat yönünde (CW) dairesel interpolasyon (kesim) | `G02 X10 Y0 I-10 J0 F800` |
| **G03** | Saat yönünün tersinde (CCW) dairesel interpolasyon (kesim) | `G03 X0 Y10 R10 F800` |
| **G21** | Metrik ölçü birimlerini kullan (milimetre) | `G21` |
| **G90** | Mutlak koordinat sistemine göre hareket et | `G90` |
| **M03** | Mili (Spindle) saat yönünde çalıştır (S: Hız/RPM belirtir) | `M03 S12000` |
| **M05** | Mili (Spindle) durdur | `M05` |
| **M30** | Programı sonlandır ve başlangıca dön | `M30` |

---

## Klasördeki Araç

*   **[gcode_generator.py](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/mechanical-civil/cad-cam/gcode_generator.py):** Belirtilen ölçülere göre CNC dik işlem merkezleri için dairesel veya dikdörtgen profil dış hat kesim G-Kodlarını otomatik üreten ve `.nc` uzantılı dosya olarak kaydeden bir CAM kod jeneratörüdür.
