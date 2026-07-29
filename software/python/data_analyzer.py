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

def det3x3(m):
    return (m[0][0]*(m[1][1]*m[2][2] - m[1][2]*m[2][1]) -
            m[0][1]*(m[1][0]*m[2][2] - m[1][2]*m[2][0]) +
            m[0][2]*(m[1][0]*m[2][1] - m[1][1]*m[2][0]))

def quadratic_regression(x, y):
    n = len(x)
    if n != len(y) or n < 3:
        return None
        
    sum_x = sum(x)
    sum_x2 = sum(val**2 for val in x)
    sum_x3 = sum(val**3 for val in x)
    sum_x4 = sum(val**4 for val in x)
    sum_y = sum(y)
    sum_xy = sum(val_x * val_y for val_x, val_y in zip(x, y))
    sum_x2y = sum((val_x**2) * val_y for val_x, val_y in zip(x, y))
    
    # Normal Equations matrix
    A = [
        [sum_x4, sum_x3, sum_x2],
        [sum_x3, sum_x2, sum_x],
        [sum_x2, sum_x, n]
    ]
    
    detA = det3x3(A)
    if abs(detA) < 1e-9:
        return None
        
    # Replace columns with B vector
    B = [sum_x2y, sum_xy, sum_y]
    
    A1 = [
        [B[0], sum_x3, sum_x2],
        [B[1], sum_x2, sum_x],
        [B[2], sum_x, n]
    ]
    A2 = [
        [sum_x4, B[0], sum_x2],
        [sum_x3, B[1], sum_x],
        [sum_x2, B[2], n]
    ]
    A3 = [
        [sum_x4, sum_x3, B[0]],
        [sum_x3, sum_x2, B[1]],
        [sum_x2, sum_x, B[2]]
    ]
    
    a = det3x3(A1) / detA
    b = det3x3(A2) / detA
    c = det3x3(A3) / detA
    
    # Calculate R-squared
    y_mean = sum_y / n
    ss_tot = sum((val_y - y_mean) ** 2 for val_y in y)
    ss_res = sum((val_y - (a * val_x**2 + b * val_x + c)) ** 2 for val_x, val_y in zip(x, y))
    r_sq = 1 - (ss_res / ss_tot) if ss_tot != 0 else 1.0
    
    return {
        "a (x^2)": a,
        "b (x)": b,
        "c (sabit)": c,
        "R_kare (R2)": r_sq,
        "denklem": f"y = {a:.4f}x^2 + {b:.4f}x + {c:.4f}"
    }

def unit_converter():
    while True:
        print("\n--- Birim Dönüştürücü ---")
        print("1. Sıcaklık (Celsius <=> Fahrenheit)")
        print("2. Basınç (Bar <=> PSI <=> Pascal)")
        print("3. Uzunluk (İnç <=> Milimetre)")
        print("4. Hız (m/s <=> km/h <=> mph)")
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
        elif secim == '4':
            val = float(input("Değeri girin (m/s): "))
            print(f"{val} m/s = {val * 3.6:.2f} km/h = {val * 2.23694:.2f} mph")
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")

def data_analysis_flow():
    print("\n--- İstatistik ve Regresyon Analizi ---")
    print("Analiz edilecek sayısal değerleri aralarında boşluk bırakarak girin (Örn: 1 2 3 4 5):")
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
                
            print("\nRegresyon Modeli Seçin:")
            print("1. Doğrusal Regresyon (y = mx + c)")
            print("2. İkinci Derece Polinom Regresyonu (y = ax^2 + bx + c)")
            reg_choice = input("Seçiminiz: ").strip()
            
            if reg_choice == '1':
                reg = linear_regression(x_data, y_data)
                if reg:
                    print("\n--- Lineer Regresyon Analizi ---")
                    for k, v in reg.items():
                        print(f"{k:15}: {v:.6f}" if isinstance(v, float) else f"{k:15}: {v}")
                else:
                    print("[HATA] Regresyon hesaplanamadı.")
            elif reg_choice == '2':
                reg = quadratic_regression(x_data, y_data)
                if reg:
                    print("\n--- Polinom Regresyon Analizi ---")
                    for k, v in reg.items():
                        print(f"{k:15}: {v:.6f}" if isinstance(v, float) else f"{k:15}: {v}")
                else:
                    print("[HATA] Polinom regresyon hesaplanamadı (yetersiz veri veya tekil matris).")
                    
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
