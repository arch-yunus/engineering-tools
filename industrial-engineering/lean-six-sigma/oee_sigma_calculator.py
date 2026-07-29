import math

def calculate_oee(planned_time, planned_down, unplanned_down, ideal_cycle, total_units, reject_units):
    net_operating_time = planned_time - planned_down
    run_time = net_operating_time - unplanned_down
    
    if net_operating_time <= 0 or run_time <= 0:
        return None, "Çalışma süreleri sıfır veya negatif olamaz."
    if total_units <= 0:
        return None, "Üretilen toplam adet sıfırdan büyük olmalıdır."
        
    availability = run_time / net_operating_time
    
    # ideal_cycle is in seconds, run_time is in minutes
    # Total time needed at ideal speed / actual run time
    ideal_time_needed_sec = total_units * ideal_cycle
    actual_run_time_sec = run_time * 60
    
    performance = ideal_time_needed_sec / actual_run_time_sec
    # Performance shouldn't exceed 1.0 significantly in real world, but can mathematically. We'll show the raw math.
    
    quality = (total_units - reject_units) / total_units if total_units > 0 else 0
    
    oee = availability * performance * quality * 100
    
    return {
        "Net Calisma Suresi (dk)": net_operating_time,
        "Fiili Calisma Suresi (dk)": run_time,
        "Kullanilabilirlik (Availability) %": availability * 100,
        "Performans (Performance) %": performance * 100,
        "Kalite (Quality) %": quality * 100,
        "OEE %": oee
    }, None

def erfc_inv(x):
    """Approximation of inverse complementary error function."""
    # Simple and robust Winitzki approximation of erfi / erf_inv
    # Since we need normal inverse: Probit(p) = sqrt(2) * erf_inv(2p - 1)
    # Let's approximate Probit(p) directly.
    pass

def probit(p):
    """Approximation of the normal inverse CDF (Probit function) for Six Sigma."""
    if p <= 0.0000001:
        return -5.0
    if p >= 0.9999999:
        return 5.0
        
    # Coefficients for rational approximation (Wichura algorithm / simple approximation)
    # Using a simple rational approximation for standard normal inverse CDF
    # For p < 0.5, we mirror it.
    q = p if p < 0.5 else 1.0 - p
    
    # Rational approximation
    t = math.sqrt(-2.0 * math.log(q))
    # Approximation constants
    c0 = 2.515517
    c1 = 0.802853
    c2 = 0.010328
    d1 = 1.432788
    d2 = 0.189269
    d3 = 0.001308
    
    x = t - ((c2 * t + c1) * t + c0) / (((d3 * t + d2) * t + d1) * t + 1.0)
    
    if p < 0.5:
        return -x
    else:
        return x

def calculate_six_sigma(n_units, opportunities, n_defects):
    total_opportunities = n_units * opportunities
    if total_opportunities <= 0:
        return None, "Toplam fırsat sayısı sıfır veya negatif olamaz."
        
    dpo = n_defects / total_opportunities
    dpmo = dpo * 1000000
    
    # Yield is percentage of defect-free opportunities
    yield_pct = (1.0 - dpo) * 100
    
    # Sigma level calculation with standard 1.5 sigma shift
    # Sigma Level = Z + 1.5
    # Z is probit(1 - DPO)
    p_success = 1.0 - dpo
    # Bound p_success to avoid math domain errors
    p_success = max(min(p_success, 0.9999999), 0.0000001)
    
    z_value = probit(p_success)
    sigma_level = z_value + 1.5
    
    return {
        "Toplam Firsat Sayisi": total_opportunities,
        "Defects Per Opportunity (DPO)": dpo,
        "DPMO (Hata/Milyon Firsat)": dpmo,
        "Verimlilik (Yield) %": yield_pct,
        "Z-Skoru (Kisa Donem)": z_value,
        "Sigma Seviyesi (1.5 Shift dahil)": sigma_level
    }, None

def run_oee_flow():
    print("\n--- OEE (Toplam Ekipman Etkinliği) Hesaplama ---")
    try:
        planned_time = float(input("Planlanan Toplam Süre (Dakika, örn: 8 saat = 480): "))
        planned_down = float(input("Planlanan Duruşlar (Dakika, mola, temizlik vb.): "))
        unplanned_down = float(input("Planlanmayan Duruşlar (Dakika, arıza, ayar, hammadde beklemeleri): "))
        ideal_cycle = float(input("İdeal Çevrim Süresi (1 adet üretmek için gereken saniye): "))
        total_units = float(input("Üretilen Toplam Adet (Hatalı + Sağlam): "))
        reject_units = float(input("Hatalı/Iskarta Üretim Adedi: "))
        
        results, err = calculate_oee(planned_time, planned_down, unplanned_down, ideal_cycle, total_units, reject_units)
        
        if err:
            print(f"\n[HATA] {err}")
            return
            
        print("\n--- OEE Hesaplama Sonuçları ---")
        for k, v in results.items():
            print(f"{k:35}: {v:.2f}")
            
        # OEE Benchmarks
        oee_val = results["OEE %"]
        print("\nDünya Standartlarında OEE Değerlendirmesi:")
        if oee_val >= 85:
            print(">> %85+ OEE: DÜNYA SINIFI (World Class) Üretim Seviyesi! Mükemmel.")
        elif oee_val >= 75:
            print(">> %75-%85 OEE: İYİ. Kabul edilebilir endüstriyel standart.")
        elif oee_val >= 60:
            print(">> %60-%75 OEE: ORTA. İyileştirme (Kaizen) potansiyeli yüksek.")
        else:
            print(">> %60 Altı OEE: DÜŞÜK. Büyük kayıplar mevcut, acil eylem planı gerekli.")
            
    except ValueError:
        print("[HATA] Lütfen geçerli sayısal değerler girin.")
    input("\nDevam etmek için Enter'a basın...")

def run_six_sigma_flow():
    print("\n--- Altı Sigma & DPMO Analizi ---")
    try:
        n_units = int(input("Üretilen/Kontrol Edilen Toplam Ürün Adedi: "))
        opportunities = int(input("Ürün Başına Hata Fırsatı Sayısı (Örn: Devre kartındaki lehim noktası sayısı): "))
        n_defects = int(input("Tespit Edilen Toplam Hata (Defect) Sayısı: "))
        
        results, err = calculate_six_sigma(n_units, opportunities, n_defects)
        if err:
            print(f"\n[HATA] {err}")
            return
            
        print("\n--- Altı Sigma Sonuçları ---")
        for k, v in results.items():
            print(f"{k:35}: {v:.4f}" if isinstance(v, float) else f"{k:35}: {v}")
            
        sigma_lvl = results["Sigma Seviyesi (1.5 Shift dahil)"]
        print(f"\nEşdeğer Sigma Derecesi: {sigma_lvl:.2f} Sigma")
        if sigma_lvl >= 6.0:
            print(">> Sınıfının En İyisi (Six Sigma)! 1 milyon fırsatta en fazla 3.4 hata.")
        elif sigma_lvl >= 4.0:
            print(">> 4-5 Sigma Seviyesi: Ortalama üzeri endüstriyel kalite.")
        elif sigma_lvl >= 3.0:
            print(">> 3 Sigma Seviyesi: Ortalama kalite (1 milyonda 66,807 hata). İyileştirilmeli.")
        else:
            print(">> 3 Sigma Altı Seviyesi: Yüksek hata oranı! Süreç kontrol dışı.")
            
    except ValueError:
        print("[HATA] Lütfen geçerli tamsayılar girin.")
    input("\nDevam etmek için Enter'a basın...")

def main():
    while True:
        print("\n==============================================")
        print("    YALIN ÜRETİM VE KALİTE HESAPLAYICILARI    ")
        print("==============================================")
        print("1. OEE (Toplam Ekipman Etkinliği) Hesapla")
        print("2. Altı Sigma DPMO ve Kalite Seviyesi Analizi")
        print("0. Geri Dön")
        print("==============================================")
        secim = input("Seçiminiz: ").strip()
        
        if secim == '1':
            run_oee_flow()
        elif secim == '2':
            run_six_sigma_flow()
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
