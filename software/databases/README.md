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

## Klasördeki Araç

*   **[db_manager.py](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/software/databases/db_manager.py):** Yerel bir SQLite veritabanı dosyası (`materials.db`) oluşturan, malzeme mekanik ve fiziksel özelliklerini (Akma Mukavemeti, Elastisite Modülü, Yoğunluk vb.) kaydeden, arayan ve yöneten etkileşimli bir CLI aracıdır.
