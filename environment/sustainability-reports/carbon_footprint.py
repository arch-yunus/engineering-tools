import os

# Emission factors (kg CO2e per unit) based on typical EPA / GHG Protocol values
FACTOR_NATURAL_GAS_M3 = 1.90    # kg CO2e per m3
FACTOR_DIESEL_LITER = 2.68      # kg CO2e per Liter
FACTOR_PETROL_LITER = 2.31      # kg CO2e per Liter
FACTOR_ELECTRICITY_KWH = 0.45   # kg CO2e per kWh (typical grid average)
FACTOR_FLIGHT_KM = 0.15         # kg CO2e per passenger-km
FACTOR_COMMUTE_KM = 0.12        # kg CO2e per km (average car commute)

def calculate_footprint(nat_gas, diesel, petrol, electricity, flight_km, commute_km):
    # Scope 1: Direct emissions
    s1_nat_gas = nat_gas * FACTOR_NATURAL_GAS_M3
    s1_diesel = diesel * FACTOR_DIESEL_LITER
    s1_petrol = petrol * FACTOR_PETROL_LITER
    scope1_total_kg = s1_nat_gas + s1_diesel + s1_petrol
    
    # Scope 2: Indirect emissions (electricity)
    scope2_total_kg = electricity * FACTOR_ELECTRICITY_KWH
    
    # Scope 3: Other indirect emissions
    s3_flight = flight_km * FACTOR_FLIGHT_KM
    s3_commute = commute_km * FACTOR_COMMUTE_KM
    scope3_total_kg = s3_flight + s3_commute
    
    total_kg = scope1_total_kg + scope2_total_kg + scope3_total_kg
    
    # Convert to Metric Tonnes (tCO2e)
    scope1_t = scope1_total_kg / 1000.0
    scope2_t = scope2_total_kg / 1000.0
    scope3_t = scope3_total_kg / 1000.0
    total_t = total_kg / 1000.0
    
    return {
        "Scope 1 (Doğrudan) tCO2e": scope1_t,
        "  - Doğal Gaz Tüketimi tCO2e": s1_nat_gas / 1000.0,
        "  - Şirket Araçları (Dizel) tCO2e": s1_diesel / 1000.0,
        "  - Şirket Araçları (Benzin) tCO2e": s1_petrol / 1000.0,
        "Scope 2 (Dolaylı Enerji) tCO2e": scope2_t,
        "  - Satın Alınan Elektrik tCO2e": scope2_total_kg / 1000.0,
        "Scope 3 (Diğer Dolaylı) tCO2e": scope3_t,
        "  - İş Seyahatleri (Uçuş) tCO2e": s3_flight / 1000.0,
        "  - Çalışan Ulaşım/Servis tCO2e": s3_commute / 1000.0,
        "Toplam Karbon Ayak İzi tCO2e": total_t
    }

def print_esg_report(results):
    report_lines = []
    report_lines.append("==================================================")
    report_lines.append("        ESG SERA GAZI EMİSYON RAPORU (GHG)")
    report_lines.append("==================================================")
    
    total_t = results["Toplam Karbon Ayak İzi tCO2e"]
    
    for k, v in results.items():
        if "Toplam" in k:
            report_lines.append("-" * 50)
            report_lines.append(f"{k:35}: {v:8.3f} tCO2e")
            report_lines.append("-" * 50)
        elif "  -" in k:
            report_lines.append(f"{k:35}: {v:8.3f} tCO2e")
        else:
            report_lines.append(f"\n{k:35}: {v:8.3f} tCO2e")
            
    # Calculate percentages
    s1 = results["Scope 1 (Doğrudan) tCO2e"]
    s2 = results["Scope 2 (Dolaylı Enerji) tCO2e"]
    s3 = results["Scope 3 (Diğer Dolaylı) tCO2e"]
    
    if total_t > 0:
        report_lines.append("\nKapsam Dağılımı:")
        report_lines.append(f" - Kapsam 1 (Doğrudan)  : %{(s1/total_t)*100:.1f}")
        report_lines.append(f" - Kapsam 2 (Dolaylı)   : %{(s2/total_t)*100:.1f}")
        report_lines.append(f" - Kapsam 3 (Dolaylı)   : %{(s3/total_t)*100:.1f}")
        
    report_lines.append("\nÖNERİLEN AZALTIM EYLEMLERİ:")
    if s1 > 0.5 * total_t:
        report_lines.append(">> Ağırlıklı Kapsam 1: Şirket araç filosunu elektrikli (EV) araçlara dönüştürmeyi ve ısıtmada ısı pompalarına geçmeyi planlayın.")
    if s2 > 0.4 * total_t:
        report_lines.append(">> Ağırlıklı Kapsam 2: Tesis çatılarına Güneş Enerjisi Paneli (GES) kurmayı veya yenilenebilir enerji sertifikalı (I-REC) elektrik satın almayı değerlendirin.")
    if s3 > 0.3 * total_t:
        report_lines.append(">> Ağırlıklı Kapsam 3: Çalışanlara toplu taşıma desteği/servis organizasyonu sağlayın ve video konferans kullanımını artırarak iş seyahatlerini azaltın.")
        
    report_text = "\n".join(report_lines)
    print("\n" + report_text)
    
    # Save option
    save_report = input("\nRaporu dosyaya kaydetmek ister misiniz? (E/H): ").strip().upper()
    if save_report == 'E':
        filepath = os.path.join(os.path.dirname(__file__), "carbon_footprint_report.txt")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(report_text)
        print(f"\n[BAŞARILI] Rapor '{filepath}' konumuna kaydedildi.")

def main():
    print("\n==============================================")
    print("      ESG KARBON AYAK İZİ HESAPLAYICI (GHG)   ")
    print("==============================================")
    print("Bu program, Sera Gazı Protokolü (GHG Protocol)")
    print("standartlarına göre yıllık/aylık karbon emisyonlarını hesaplar.")
    
    try:
        print("\n--- 1. KAPSAM 1 (Doğrudan Emisyon Girişleri) ---")
        nat_gas = float(input("Doğal Gaz Tüketimi (m³): ") or 0)
        diesel = float(input("Şirket Dizel Araç Yakıtı (Litre): ") or 0)
        petrol = float(input("Şirket Benzinli Araç Yakıtı (Litre): ") or 0)
        
        print("\n--- 2. KAPSAM 2 (Dolaylı Enerji Girişleri) ---")
        electricity = float(input("Tesis Elektrik Tüketimi (kWh): ") or 0)
        
        print("\n--- 3. KAPSAM 3 (Diğer Dolaylı Girişler) ---")
        flight_km = float(input("İş Seyahatleri Uçuş Mesafesi (Toplam Yolcu × km): ") or 0)
        commute_km = float(input("Çalışanların Kişisel Araç Ulaşım Mesafesi (Yıllık Toplam km): ") or 0)
        
        results = calculate_footprint(nat_gas, diesel, petrol, electricity, flight_km, commute_km)
        print_esg_report(results)
        
    except ValueError:
        print("[HATA] Lütfen geçerli sayısal değerler girin.")
        
    input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
