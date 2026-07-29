import math

def calculate_oee(planned_time, planned_down, unplanned_down, ideal_cycle, total_units, reject_units):
    net_operating_time = planned_time - planned_down
    run_time = net_operating_time - unplanned_down
    
    if net_operating_time <= 0 or run_time <= 0:
        return None, "Çalışma süreleri sıfır veya negatif olamaz."
    if total_units <= 0:
        return None, "Üretilen toplam adet sıfırdan büyük olmalıdır."
        
    availability = run_time / net_operating_time
    
    ideal_time_needed_sec = total_units * ideal_cycle
    actual_run_time_sec = run_time * 60
    
    performance = ideal_time_needed_sec / actual_run_time_sec
    quality = (total_units - reject_units) / total_units if total_units > 0 else 0
    
    oee = availability * performance * quality * 100
    
    return {
        "Net Çalışma Süresi (dk)": net_operating_time,
        "Fiili Çalışma Süresi (dk)": run_time,
        "Kullanılabilirlik (Availability) %": availability * 100,
        "Performans (Performance) %": performance * 100,
        "Kalite (Quality) %": quality * 100,
        "OEE %": oee
    }, None

def probit(p):
    """Normal inverse CDF (Probit function) approximation."""
    if p <= 0.0000001:
        return -5.0
    if p >= 0.9999999:
        return 5.0
        
    q = p if p < 0.5 else 1.0 - p
    t = math.sqrt(-2.0 * math.log(q))
    
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
    yield_pct = (1.0 - dpo) * 100
    
    p_success = max(min(1.0 - dpo, 0.9999999), 0.0000001)
    z_value = probit(p_success)
    sigma_level = z_value + 1.5
    
    return {
        "Toplam Fırsat Sayısı": total_opportunities,
        "Defects Per Opportunity (DPO)": dpo,
        "DPMO (Hata/Milyon Fırsat)": dpmo,
        "Verimlilik (Yield) %": yield_pct,
        "Z-Skoru (Kısa Dönem)": z_value,
        "Sigma Seviyesi (1.5 Shift dahil)": sigma_level
    }, None

def calculate_takt_time(available_time_sec, demand):
    if demand <= 0:
        return None, "Müşteri talebi sıfır veya negatif olamaz."
    if available_time_sec <= 0:
        return None, "Çalışma süresi sıfır veya negatif olamaz."
    return available_time_sec / demand, None

def calculate_line_balancing(station_times):
    if not station_times:
        return None, "İstasyon süreleri boş olamaz."
    k = len(station_times)
    max_cycle_time = max(station_times)
    if max_cycle_time <= 0:
        return None, "En yüksek istasyon süresi sıfırdan büyük olmalıdır."
        
    sum_times = sum(station_times)
    efficiency = (sum_times / (k * max_cycle_time)) * 100
    balance_loss = 100.0 - efficiency
    
    return {
        "İstasyon Sayısı (k)": k,
        "Darboğaz Çevrim Süresi (Cmax - sn)": max_cycle_time,
        "Toplam İş İçeriği (sn)": sum_times,
        "Hat Dengeleme Verimliliği %": efficiency,
        "Denge Kaybı (Balance Loss) %": balance_loss
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
            
    except ValueError:
        print("[HATA] Lütfen geçerli sayısal değerler girin.")
    input("\nDevam etmek için Enter'a basın...")

def run_six_sigma_flow():
    print("\n--- Altı Sigma & DPMO Analizi ---")
    try:
        n_units = int(input("Üretilen/Kontrol Edilen Toplam Ürün Adedi: "))
        opportunities = int(input("Ürün Başına Hata Fırsatı Sayısı: "))
        n_defects = int(input("Tespit Edilen Toplam Hata Sayısı: "))
        
        results, err = calculate_six_sigma(n_units, opportunities, n_defects)
        if err:
            print(f"\n[HATA] {err}")
            return
            
        print("\n--- Altı Sigma Sonuçları ---")
        for k, v in results.items():
            print(f"{k:35}: {v:.4f}" if isinstance(v, float) else f"{k:35}: {v}")
            
    except ValueError:
        print("[HATA] Lütfen geçerli tamsayılar girin.")
    input("\nDevam etmek için Enter'a basın...")

def run_takt_flow():
    print("\n--- Takt Süresi ve Montaj Hattı Dengeleme ---")
    try:
        print("\n1. Takt Süresi Hesapla")
        print("2. Hat Dengeleme Verimliliği Hesapla")
        secim = input("Seçiminiz: ").strip()
        
        if secim == '1':
            avail_time = float(input("Net Çalışma Süresi (Dakika): ")) * 60.0
            demand = float(input("Müşteri Talebi (Adet/Vardiya): "))
            takt, err = calculate_takt_time(avail_time, demand)
            if err:
                print(f"[HATA] {err}")
                return
            print(f"\nHesaplanan Takt Süresi: {takt:.2f} saniye/ürün")
            print("Açıklama: Her bir ürün ortalama bu sürede bir banttan çıkmalıdır.")
            
        elif secim == '2':
            station_str = input("İstasyon sürelerini aralarında boşluk bırakarak saniye cinsinden girin (Örn: 45 60 55 40): ").strip()
            station_times = [float(t) for t in station_str.split()]
            res, err = calculate_line_balancing(station_times)
            if err:
                print(f"[HATA] {err}")
                return
            print("\n--- Hat Dengeleme Sonuçları ---")
            for k, v in res.items():
                print(f"{k:35}: {v:.2f}")
                
    except ValueError:
        print("[HATA] Lütfen geçerli sayısal değerler girin.")
    input("\nDevam etmek için Enter'a basın...")

def main():
    while True:
        print("\n==============================================")
        print("    YALIN ÜRETİM VE KALİTE HESAPLAYICILARI    ")
        print("==============================================")
        print("1. OEE (Toplam Ekipman Etkinliği) Hesapla")
        print("2. Altı Sigma DPMO ve Kalite Seviyesi Analizi")
        print("3. Takt Süresi ve Hat Dengeleme Analizi")
        print("0. Geri Dön")
        print("==============================================")
        secim = input("Seçiminiz: ").strip()
        
        if secim == '1':
            run_oee_flow()
        elif secim == '2':
            run_six_sigma_flow()
        elif secim == '3':
            run_takt_flow()
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
