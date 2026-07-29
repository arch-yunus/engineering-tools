# SQL ve Mühendislikte Veri Tabanı Yönetimi

Mühendislik projelerinde veri tabanları; malzeme kütüphaneleri, envanter takibi, sensör logları ve CAD bileşen kataloglarının yönetimi gibi kritik alanlarda kullanılır. SQL (Structured Query Language), ilişkisel veri tabanlarındaki verileri sorgulamak, eklemek ve güncellemek için kullanılan standart dildir.

## Mühendislik Veri Tabanı Mimarisi

Mühendislik verileri genellikle ilişkisel bir yapıda tutulur. Örneğin bir **Malzeme Kataloğu** ve buna bağlı **Deney Testleri** şu şekilde tasarlanabilir:

```
[materials] (Malzemeler)
  - id (PK)
  - name (Malzeme Adı)
  - category (Kategori)
  - density (Yoğunluk)

[tension_tests] (Çekme Testleri)
  - test_id (PK)
  - material_id (FK -> materials.id)
  - operator (Testi Yapan)
  - max_stress (Maksimum Mukavemet)
  - test_date (Tarih)
```

---

## Örnek SQL Sorguları

### 1. Tablo Oluşturma (DDL)
```sql
CREATE TABLE materials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    density REAL,
    yield_strength REAL
);
```

### 2. Arama ve Filtreleme (DML)
Akma mukavemeti 250 MPa'dan büyük olan çelik malzemeleri seçmek için:
```sql
SELECT name, yield_strength 
FROM materials 
WHERE yield_strength > 250.0 AND category = 'Metal';
```

### 3. İlişkili Tabloları Birleştirme (JOIN)
Her bir malzemenin yapılan çekme testleriyle birleştirilerek raporlanması:
```sql
SELECT m.name, t.operator, t.max_stress
FROM materials m
INNER JOIN tension_tests t ON m.id = t.material_id;
```

---

## Ashby Malzeme Seçim İndeksleri

Makine ve yapı tasarımında, minimum ağırlıkla maksimum mukavemet veya sertlik sağlamak için **Ashby Malzeme Seçim İndeksleri** kullanılır.

*   **Özgül Mukavemet (Specific Strength - $M_1$):** Malzemenin akma mukavemetinin yoğunluğuna oranıdır. Hafif ve yüksek mukavemet gerektiren uçak, uzay araçları gibi tasarımlarda yüksek olması istenir.
    $$M_1 = \frac{\sigma_y}{\rho}$$
*   **Özgül Sertlik (Specific Stiffness - $M_2$):** Malzemenin elastisite modülünün yoğunluğuna oranıdır. Eğilmeye karşı direnç ve hafiflik istenen şasiler, köprü kirişlerinde kritik seçim indeksidir.
    $$M_2 = \frac{E}{\rho}$$

---

## Klasördeki Araç

*   **[db_manager.py](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/software/databases/db_manager.py):** Yerel bir SQLite veritabanı dosyası (`materials.db`) oluşturan; malzeme kategorilerini, yoğunluğunu, akma sınırını ve elastisite değerlerini yönetirken aynı zamanda mekanik hafiflik kararları için **Ashby Özgül Mukavemet ve Özgül Sertlik indekslerini** dinamik hesaplayan bir veri tabanı yönetim aracıdır.
