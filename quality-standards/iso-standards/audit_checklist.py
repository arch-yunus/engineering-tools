import os

ISO_9001_QUESTIONS = [
    ("Madde 4.1 - Kuruluşun Bağlamı", "Kuruluş, amacını ve stratejik yönünü etkileyen iç ve dış hususları belirlemiş mi?"),
    ("Madde 5.2 - Kalite Politikası", "Üst yönetim, kuruluşun amacına uygun bir kalite politikası oluşturmuş, yayınlamış ve duyurmuş mu?"),
    ("Madde 6.1 - Risk ve Fırsatlar", "Risk ve fırsatları belirlemek ve bunlara yönelik aksiyonları planlamak için bir süreç tanımlanmış mı?"),
    ("Madde 7.2 - Yetkinlik", "Çalışanların yaptıkları işlerin kalite performansını etkileyen yetkinlik ihtiyaçları (eğitim, tecrübe) belirlenmiş ve kayıt altına alınmış mı?"),
    ("Madde 8.2 - Müşteri İletişimi", "Müşteri geri bildirimleri, şikayetleri ve taleplerini yönetmek için etkin bir süreç işletiliyor mu?"),
    ("Madde 9.3 - Yönetimin Gözden Geçirmesi", "Üst yönetim, kalite yönetim sisteminin uygunluğunu ve etkinliğini düzenli aralıklarla gözden geçiriyor mu?"),
    ("Madde 10.2 - Uygunsuzluk ve Düzeltici Faaliyet", "Uygunsuzluk ortaya çıktığında (şikayetler dahil) kök neden analizi yapılıp düzeltici faaliyetler başlatılıyor mu?")
]

ISO_22000_HACCP_QUESTIONS = [
    ("Madde 5.2 - Gıda Güvenliği Politikası", "Üst yönetim, gıda güvenliği politikasını tanımlamış ve tüm kademelere iletmiş mi?"),
    ("Madde 7.4 - İletişim", "Tedarikçiler, müşteriler ve resmi kurumlar ile gıda güvenliğini etkileyen konularda dış iletişim süreçleri etkin çalışıyor mu?"),
    ("Madde 8.2 - Ön Gereksinim Programları (PRP)", "Üretim ortamındaki sanitasyon, temizlik ve hijyen standartlarını korumak için Ön Gereksinim Programları (PRP) kurulmuş ve sürdürülüyor mu?"),
    ("Madde 8.5 - Tehlike Analizi", "Hammadde kabulünden sevkiyata kadar tüm süreç adımlarında biyolojik, kimyasal ve fiziksel tehlikeler analiz edilmiş mi?"),
    ("Madde 8.5.4 - KKN (Kritik Kontrol Noktaları)", "Kritik Kontrol Noktaları ve Operasyonel Ön Gereksinim Programları (oPRP) belirlenmiş, kritik limitler ve izleme yöntemleri tanımlanmış mı?"),
    ("Madde 8.9 - Uygun Olmayan Ürün Kontrolü", "Kritik limit aşıldığında üretilen gıdaların karantinaya alınması ve imhası için bir prosedür mevcut mu?"),
    ("Madde 8.4 - İzlenebilirlik", "Hammaddeden son ürüne kadar tüm ürünlerin geriye dönük izlenebilirliği (parti/lot takibi) doğrulanabiliyor mu?")
]

def run_audit(standard_name, questions):
    print(f"\n==================================================")
    print(f"      {standard_name} DENETİM SÜRECİ BAŞLADI")
    print(f"==================================================")
    print("Her soru için şu derecelendirmeyi kullanın:")
    print(" 2 - Tam Uygun (Conformity)")
    print(" 1 - Minör Uygunsuzluk (Minor Non-Conformity)")
    print(" 0 - Majör Uygunsuzluk (Major Non-Conformity)")
    print("-" * 50)
    
    audit_results = []
    total_score = 0
    max_possible_score = len(questions) * 2
    
    for i, (clause, question) in enumerate(questions):
        print(f"\n[{i+1}/{len(questions)}] {clause}")
        print(f"Gereksinim: {question}")
        
        # Get valid score
        while True:
            score_input = input("Skor (2 / 1 / 0): ").strip()
            if score_input in ['0', '1', '2']:
                score = int(score_input)
                break
            print("Lütfen sadece 2, 1 veya 0 değerlerinden birini girin.")
            
        comment = input("Bulgu / Denetçi Notu: ").strip()
        audit_results.append({
            "clause": clause,
            "question": question,
            "score": score,
            "comment": comment
        })
        total_score += score
        
    compliance_pct = (total_score / max_possible_score) * 100
    
    # Generate Report Text
    report_lines = []
    report_lines.append("==================================================")
    report_lines.append(f"          DENETİM RAPORU: {standard_name}")
    report_lines.append("==================================================")
    report_lines.append(f"Toplam Skor: {total_score} / {max_possible_score}")
    report_lines.append(f"Uyum Oranı  : %{compliance_pct:.2f}")
    report_lines.append(f"Denetim Sonucu: " + ("UYGUN (BAŞARILI)" if compliance_pct >= 80 and not any(r['score'] == 0 for r in audit_results) else "UYGUNSUZ / TAKİP DENETİMİ GEREKLİ"))
    report_lines.append("-" * 50)
    
    report_lines.append("\nBULGU DETAYLARI:")
    for i, res in enumerate(audit_results):
        status = "TAM UYGUN" if res['score'] == 2 else ("MİNÖR UYGUNSUZLUK" if res['score'] == 1 else "MAJÖR UYGUNSUZLUK")
        report_lines.append(f"\n{i+1}. {res['clause']}")
        report_lines.append(f"   Durum: {status} ({res['score']} Puan)")
        if res['comment']:
            report_lines.append(f"   Denetçi Notu: {res['comment']}")
            
    report_text = "\n".join(report_lines)
    print("\n" + report_text)
    
    # Export option
    save_report = input("\nRaporu dosyaya kaydetmek ister misiniz? (E/H): ").strip().upper()
    if save_report == 'E':
        filename = standard_name.replace(" ", "_").replace(":", "").replace("/", "_").lower() + "_report.txt"
        filepath = os.path.join(os.path.dirname(__file__), filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(report_text)
        print(f"\n[BAŞARILI] Rapor '{filepath}' konumuna kaydedildi.")
        
    return compliance_pct

def main():
    while True:
        print("\n==============================================")
        print("    ISO VE GIDA GÜVENLİĞİ DENETİM ASİSTANI    ")
        print("==============================================")
        print("Bu program, kalite standartları denetimlerinde")
        print("kontrol listelerini yürütmek ve raporlamak içindir.")
        print("\nStandart Seçimi:")
        print("1. ISO 9001:2015 Kalite Yönetim Sistemi Denetimi")
        print("2. ISO 22000 & HACCP Gıda Güvenliği Denetimi")
        print("0. Geri Dön")
        print("==============================================")
        secim = input("Seçiminiz: ").strip()
        
        if secim == '1':
            run_audit("ISO 9001-2015 QMS", ISO_9001_QUESTIONS)
        elif secim == '2':
            run_audit("ISO 22000-HACCP FSMS", ISO_22000_HACCP_QUESTIONS)
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
