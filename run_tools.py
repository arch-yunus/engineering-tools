import os
import sys
import subprocess

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_script(path):
    abs_path = os.path.join(os.path.dirname(__file__), path)
    if not os.path.exists(abs_path):
        print(f"\n[HATA] '{path}' dosyası bulunamadı. Lütfen dosyanın varlığından emin olun.")
        input("\nDevam etmek için Enter'a basın...")
        return
    try:
        # Run using current python interpreter to avoid path/env issues
        subprocess.run([sys.executable, abs_path])
    except KeyboardInterrupt:
        print("\n\n[BİLGİ] İşlem kullanıcı tarafından iptal edildi.")
        input("\nDevam etmek için Enter'a basın...")
    except Exception as e:
        print(f"\n[HATA] Çalıştırılırken bir hata oluştu: {e}")
        input("\nDevam etmek için Enter'a basın...")

def menu_software():
    while True:
        clear_screen()
        print("==================================================")
        print("          YAZILIM VE BİLGİSAYAR ARAÇLARI          ")
        print("==================================================")
        print("1. Veri Analizi ve Birim Dönüştürücü (Python)")
        print("2. Mühendislik Malzeme Veritabanı Yöneticisi (SQL)")
        print("0. Ana Menüye Dön")
        print("==================================================")
        secim = input("Seçiminiz: ").strip()
        if secim == '1':
            run_script("software/python/data_analyzer.py")
        elif secim == '2':
            run_script("software/databases/db_manager.py")
        elif secim == '0':
            break
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")
            input("Devam etmek için Enter'a basın...")

def menu_automation():
    while True:
        clear_screen()
        print("==================================================")
        print("        ELEKTRİK-ELEKTRONİK VE OTOMASYON          ")
        print("==================================================")
        print("1. PLC Modbus Kaydedici ve Register Simülatörü")
        print("0. Ana Menüye Dön")
        print("==================================================")
        secim = input("Seçiminiz: ").strip()
        if secim == '1':
            run_script("automation-electronics/plc-scada/modbus_simulator.py")
        elif secim == '0':
            break
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")
            input("Devam etmek için Enter'a basın...")

def menu_mechanical_civil():
    while True:
        clear_screen()
        print("==================================================")
        print("            MAKİNE VE İNŞAAT ARAÇLARI             ")
        print("==================================================")
        print("1. CNC G-Kodu Jeneratörü (CAD/CAM)")
        print("2. Kritik Yol Metodu (CPM) Proje Planlayıcı")
        print("0. Ana Menüye Dön")
        print("==================================================")
        secim = input("Seçiminiz: ").strip()
        if secim == '1':
            run_script("mechanical-civil/cad-cam/gcode_generator.py")
        elif secim == '2':
            run_script("mechanical-civil/project-management/cpm_calculator.py")
        elif secim == '0':
            break
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")
            input("Devam etmek için Enter'a basın...")

def menu_industrial():
    while True:
        clear_screen()
        print("==================================================")
        print("          ENDÜSTRİ MÜHENDİSLİĞİ ARAÇLARI          ")
        print("==================================================")
        print("1. OEE (Toplam Ekipman Etkinliği) ve Altı Sigma Hesaplayıcı")
        print("0. Ana Menüye Dön")
        print("==================================================")
        secim = input("Seçiminiz: ").strip()
        if secim == '1':
            run_script("industrial-engineering/lean-six-sigma/oee_sigma_calculator.py")
        elif secim == '0':
            break
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")
            input("Devam etmek için Enter'a basın...")

def menu_quality():
    while True:
        clear_screen()
        print("==================================================")
        print("          KALİTE VE STANDARTLAR ARAÇLARI          ")
        print("==================================================")
        print("1. ISO 9001 & ISO 22000 (HACCP) Denetim Asistanı")
        print("0. Ana Menüye Dön")
        print("==================================================")
        secim = input("Seçiminiz: ").strip()
        if secim == '1':
            run_script("quality-standards/iso-standards/audit_checklist.py")
        elif secim == '0':
            break
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")
            input("Devam etmek için Enter'a basın...")

def menu_environment():
    while True:
        clear_screen()
        print("==================================================")
        print("             ÇEVRE VE SÜRDÜRÜLEBİLİRLİK           ")
        print("==================================================")
        print("1. Kapsam 1, 2, 3 Karbon Ayak İzi Hesaplayıcı")
        print("0. Ana Menüye Dön")
        print("==================================================")
        secim = input("Seçiminiz: ").strip()
        if secim == '1':
            run_script("environment/sustainability-reports/carbon_footprint.py")
        elif secim == '0':
            break
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")
            input("Devam etmek için Enter'a basın...")

def main():
    while True:
        clear_screen()
        print("==================================================")
        print("     🛠️  MÜHENDİSLİK ARAÇLARI KONSOL ARAYÜZÜ      ")
        print("==================================================")
        print("1. Yazılım ve Bilgisayar Mühendisliği")
        print("2. Elektrik-Elektronik ve Otomasyon Mühendisliği")
        print("3. Makine ve İnşaat Mühendisliği")
        print("4. Endüstri Mühendisliği (Yalın & Altı Sigma)")
        print("5. Kalite Standartları ve Güvenlik (ISO & HACCP)")
        print("6. Çevre ve Sürdürülebilirlik")
        print("0. Çıkış")
        print("==================================================")
        secim = input("Seçiminiz: ").strip()

        if secim == '1':
            menu_software()
        elif secim == '2':
            menu_automation()
        elif secim == '3':
            menu_mechanical_civil()
        elif secim == '4':
            menu_industrial()
        elif secim == '5':
            menu_quality()
        elif secim == '6':
            menu_environment()
        elif secim == '0':
            print("\nProgramdan çıkılıyor. İyi çalışmalar!")
            break
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")
            input("Devam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
