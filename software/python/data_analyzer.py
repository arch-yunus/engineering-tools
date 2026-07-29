import math

def calculate_stats(data):
    n = len(data)
    if n == 0:
        return None
    mean = sum(data) / n
    sorted_data = sorted(data)
    if n % 2 == 1:
        median = sorted_data[n // 2]
    else:
        median = (sorted_data[(n // 2) - 1] + sorted_data[n // 2]) / 2.0
    
    variance = sum((x - mean) ** 2 for x in data) / (n - 1) if n > 1 else 0.0
    std_dev = math.sqrt(variance)
    return {
        "N": n,
        "Min": min(data),
        "Max": max(data),
        "Ortalama": mean,
        "Medyan": median,
        "Varyans": variance,
        "Standart Sapma": std_dev
    }

def linear_regression(x, y):
    n = len(x)
    if n != len(y) or n < 2:
        return None
    
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xx = sum(val * val for val in x)
    sum_xy = sum(val_x * val_y for val_x, val_y in zip(x, y))
    
    denom = (n * sum_xx - sum_x * sum_x)
    if denom == 0:
        return None
    
    m = (n * sum_xy - sum_x * sum_y) / denom
    c = (sum_y - m * sum_x) / n
    
    # Calculate R-squared
    y_mean = sum_y / n
    ss_tot = sum((val_y - y_mean) ** 2 for val_y in y)
    ss_res = sum((val_y - (m * val_x + c)) ** 2 for val_x, val_y in zip(x, y))
    
    r_sq = 1 - (ss_res / ss_tot) if ss_tot != 0 else 1.0
    
    return {
        "egim (m)": m,
        "kesim (c)": c,
        "R_kare (R2)": r_sq,
        "denklem": f"y = {m:.4f}x + {c:.4f}"
    }

def unit_converter():
    while True:
        print("\n--- Birim Dönüştürücü ---")
        print("1. Sıcaklık (Celsius <=> Fahrenheit)")
        print("2. Basınç (Bar <=> PSI <=> Pascal)")
        print("3. Uzunluk (İnç <=> Milimetre)")
        print("0. Geri Dön")
        secim = input("Seçiminiz: ").strip()
        
        if secim == '1':
            val = float(input("Değeri girin: "))
            print(f"{val} °C = {val * 1.8 + 32:.2f} °F")
            print(f"{val} °F = {(val - 32) / 1.8:.2f} °C")
        elif secim == '2':
            val = float(input("Değeri girin: "))
            print(f"{val} Bar = {val * 14.5038:.2f} PSI = {val * 100000:.2f} Pa")
            print(f"{val} PSI = {val / 14.5038:.4f} Bar = {val * 6894.76:.2f} Pa")
        elif secim == '3':
            val = float(input("Değeri girin: "))
            print(f"{val} inç = {val * 25.4:.2f} mm")
            print(f"{val} mm = {val / 25.4:.4f} inç")
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")

def data_analysis_flow():
    print("\n--- İstatistik ve Regresyon Analizi ---")
    print("Analiz edilecek sayısal değerleri aralarında boşluk bırakarak girin (Örn: 10 12.5 15 18 20.3):")
    try:
        x_input = input("X Değerleri: ").strip()
        x_data = [float(x) for x in x_input.split()]
        if not x_data:
            print("Veri girilmedi.")
            return
        
        stats = calculate_stats(x_data)
        print("\n--- Betimsel İstatistik Sonuçları ---")
        for k, v in stats.items():
            print(f"{k:15}: {v:.4f}")
            
        y_input = input("\nY Değerlerini girin (Regresyon analizi için X ile aynı sayıda değer olmalı, boş geçilebilir): ").strip()
        if y_input:
            y_data = [float(y) for y in y_input.split()]
            if len(y_data) != len(x_data):
                print("[HATA] X ve Y veri boyutları eşleşmiyor.")
                return
            reg = linear_regression(x_data, y_data)
            if reg:
                print("\n--- Lineer Regresyon Analizi (y = mx + c) ---")
                for k, v in reg.items():
                    if isinstance(v, float):
                        print(f"{k:15}: {v:.6f}")
                    else:
                        print(f"{k:15}: {v}")
            else:
                print("[HATA] Regresyon hesaplanamadı (yetersiz veri veya x değerleri sabit).")
    except ValueError:
        print("[HATA] Lütfen geçerli sayısal değerler girin.")
    input("\nDevam etmek için Enter'a basın...")

def main():
    while True:
        print("\n==============================================")
        print("    VERİ ANALİZİ VE MÜHENDİSLİK HESAPLAYICI    ")
        print("==============================================")
        print("1. İstatistik ve Regresyon Analizi Yap")
        print("2. Birim Dönüştürücü")
        print("0. Çıkış")
        print("==============================================")
        secim = input("Seçiminiz: ").strip()
        if secim == '1':
            data_analysis_flow()
        elif secim == '2':
            unit_converter()
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
            input("Devam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
