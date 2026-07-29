import sqlite3
import os

DB_FILE = "materials.db"

def get_connection():
    db_path = os.path.join(os.path.dirname(__file__), DB_FILE)
    conn = sqlite3.connect(db_path)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL,
            density REAL,               -- g/cm3
            yield_strength REAL,        -- MPa
            elastic_modulus REAL,       -- GPa
            thermal_conductivity REAL   -- W/m-K
        )
    """)
    
    # Check if we need to seed initial materials
    cursor.execute("SELECT COUNT(*) FROM materials")
    if cursor.fetchone()[0] == 0:
        initial_materials = [
            ("Çelik (Structural Steel)", "Metal", 7.85, 250.0, 200.0, 50.0),
            ("Alüminyum (6061-T6)", "Metal", 2.70, 276.0, 68.9, 167.0),
            ("Titanyum (Ti-6Al-4V)", "Metal", 4.43, 880.0, 113.8, 6.7),
            ("Bakır (Pure)", "Metal", 8.96, 70.0, 117.0, 401.0),
            ("Beton (C30/37)", "Yapı Malzemesi", 2.40, 30.0, 32.0, 1.5),
            ("Cam Elyaflı Epoksi (FR4)", "Kompozit", 1.85, 340.0, 24.0, 0.3)
        ]
        cursor.executemany("""
            INSERT INTO materials (name, category, density, yield_strength, elastic_modulus, thermal_conductivity)
            VALUES (?, ?, ?, ?, ?, ?)
        """, initial_materials)
        conn.commit()
    conn.close()

def list_materials():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM materials")
    rows = cursor.fetchall()
    conn.close()
    
    print("\n--- Malzeme Veri Tabanı Kayıtları ---")
    print(f"{'ID':<4} | {'Malzeme Adı':<25} | {'Kategori':<15} | {'Yoğunluk':<8} | {'Akma Muk.':<10} | {'Elast. Mod.':<11} | {'Özgül Muk.(σy/ρ)':<16} | {'Özgül Sert.(E/ρ)'}")
    print("-" * 125)
    for r in rows:
        density = r[3]
        yield_strength = r[4]
        elastic_modulus = r[5]
        m1 = yield_strength / density if density > 0 else 0
        m2 = elastic_modulus / density if density > 0 else 0
        print(f"{r[0]:<4} | {r[1]:<25} | {r[2]:<15} | {r[3]:8.2f} | {r[4]:10.1f} | {r[5]:11.1f} | {m1:16.2f} | {m2:.2f}")
    print("-" * 125)

def search_materials():
    print("\n--- Malzeme Arama ---")
    name_query = input("Malzeme ismi (kısmi arama için boş geçin): ").strip()
    min_yield = input("Minimum Akma Mukavemeti (MPa) (boş geçilebilir): ").strip()
    
    query = "SELECT * FROM materials WHERE 1=1"
    params = []
    
    if name_query:
        query += " AND name LIKE ?"
        params.append(f"%{name_query}%")
    if min_yield:
        try:
            query += " AND yield_strength >= ?"
            params.append(float(min_yield))
        except ValueError:
            print("Geçersiz akma mukavemeti değeri!")
            return
            
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    
    if not rows:
        print("Arama kriterlerine uygun malzeme bulunamadı.")
        return
        
    print("\n--- Arama Sonuçları ---")
    print(f"{'ID':<4} | {'Malzeme Adı':<25} | {'Kategori':<15} | {'Yoğunluk':<8} | {'Akma Muk.':<10} | {'Elast. Mod.':<11} | {'Özgül Muk.(σy/ρ)':<16} | {'Özgül Sert.(E/ρ)'}")
    print("-" * 125)
    for r in rows:
        density = r[3]
        yield_strength = r[4]
        elastic_modulus = r[5]
        m1 = yield_strength / density if density > 0 else 0
        m2 = elastic_modulus / density if density > 0 else 0
        print(f"{r[0]:<4} | {r[1]:<25} | {r[2]:<15} | {r[3]:8.2f} | {r[4]:10.1f} | {r[5]:11.1f} | {m1:16.2f} | {m2:.2f}")
    print("-" * 125)

def add_material():
    print("\n--- Yeni Malzeme Ekleme ---")
    try:
        name = input("Malzeme Adı: ").strip()
        if not name:
            print("İsim boş bırakılamaz!")
            return
        category = input("Kategori (Metal/Plastik/Yapı Malzemesi vb.): ").strip()
        density = float(input("Yoğunluk (g/cm³): ") or 0.0)
        yield_strength = float(input("Akma Mukavemeti (MPa): ") or 0.0)
        elastic_modulus = float(input("Elastisite Modülü (GPa): ") or 0.0)
        thermal_cond = float(input("Isıl İletkenlik (W/m-K): ") or 0.0)
        
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO materials (name, category, density, yield_strength, elastic_modulus, thermal_conductivity)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, category, density, yield_strength, elastic_modulus, thermal_cond))
        conn.commit()
        conn.close()
        print(f"\n[BAŞARILI] '{name}' başarıyla veri tabanına eklendi.")
    except sqlite3.IntegrityError:
        print("\n[HATA] Bu isimde bir malzeme zaten mevcut.")
    except ValueError:
        print("\n[HATA] Lütfen sayısal değerler için geçerli sayılar girin.")

def delete_material():
    list_materials()
    try:
        mat_id = int(input("\nSilmek istediğiniz malzemenin ID numarasını girin: "))
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM materials WHERE id = ?", (mat_id,))
        row = cursor.fetchone()
        if not row:
            print("[HATA] Malzeme bulunamadı.")
            conn.close()
            return
            
        confirm = input(f"'{row[0]}' malzemesini silmek istediğinize emin misiniz? (E/H): ").strip().upper()
        if confirm == 'E':
            cursor.execute("DELETE FROM materials WHERE id = ?", (mat_id,))
            conn.commit()
            print(f"[BAŞARILI] Malzeme silindi.")
        else:
            print("İptal edildi.")
        conn.close()
    except ValueError:
        print("[HATA] Geçersiz ID numarası.")

def main():
    init_db()
    while True:
        print("\n==============================================")
        print("     MALZEME VERİ TABANI YÖNETİCİSİ (SQLite)   ")
        print("==============================================")
        print("1. Tüm Malzemeleri Listele")
        print("2. Malzeme Ara (İsim / Mekanik Özellik)")
        print("3. Yeni Malzeme Ekle")
        print("4. Malzeme Sil")
        print("0. Geri Dön")
        print("==============================================")
        secim = input("Seçiminiz: ").strip()
        
        if secim == '1':
            list_materials()
        elif secim == '2':
            search_materials()
        elif secim == '3':
            add_material()
        elif secim == '4':
            delete_material()
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
