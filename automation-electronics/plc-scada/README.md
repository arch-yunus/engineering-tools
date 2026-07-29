# PLC (Programlanabilir Mantıksal Denetleyici) ve SCADA Sistemleri

Endüstriyel otomasyonun temelini PLC cihazları ve bu cihazlardan gelen verileri görselleştiren, kontrol eden SCADA sistemleri oluşturur. PLC'ler milisaniyeler seviyesinde döngülerle (Scan Cycle) fiziksel girişleri okur, kullanıcı programını işler ve çıkışları günceller.

## PLC Programlama Standartları (IEC 61131-3)

IEC 61131-3 standardı, PLC'ler için 5 farklı programlama dilini tanımlar:

1.  **Ladder Diagram (LD - Merdiven Diyagramı):** Elektriksel röle şemalarına dayanan görsel dil. En yaygın kullanılanıdır.
2.  **Structured Text (ST - Yapılandırılmış Metin):** Pascal ve C dillerine benzer, yüksek seviyeli metinsel dil. Karmaşık matematiksel hesaplamalarda tercih edilir.
3.  **Function Block Diagram (FBD):** Fonksiyon bloklarının birbirine bağlanmasıyla oluşturulan görsel dil.
4.  **Instruction List (IL):** Assembly diline benzer düşük seviyeli dil (Modern sistemlerde az tercih edilir).
5.  **Sequential Function Chart (SFC):** Durum makinelerini ve ardışık adımları görselleştirmek için kullanılır.

### Structured Text (ST) Örnek Kodu
Bir motorun aşırı sıcaklık durumunda otomatik durdurulmasını sağlayan ST kodu:

```pascal
VAR
    Motor_Start  : BOOL; // Bobin (0xxxx)
    Temp_Sensor  : INT;  // Analog Giriş (3xxxx)
    Temp_Limit   : INT := 80; // Eşik Değeri
    Motor_Output : BOOL; // Çıkış Bobini
    Alarm_Active : BOOL;
END_VAR

// Program Mantığı
IF Temp_Sensor >= Temp_Limit THEN
    Motor_Output := FALSE;
    Alarm_Active := TRUE;
ELSIF Motor_Start THEN
    Motor_Output := TRUE;
    Alarm_Active := FALSE;
ELSE
    Motor_Output := FALSE;
END_IF;
```

---

## Modbus Protokolü ve Register Yapısı

Modbus, endüstriyel cihazlar arasındaki iletişim için kullanılan en eski ve en popüler açık protokollerden biridir. Register (Kaydedici) yapısı 4 ana gruba ayrılır:

| Tablo Tipi | Adres Aralığı | Erişim Tipi | Veri Tipi | Açıklama |
| :--- | :--- | :--- | :--- | :--- |
| **Discrete Inputs** | 10001 - 19999 | Salt Okunur | 1-bit (Digital) | Sınır anahtarları, buton girişleri |
| **Coils** | 00001 - 09999 | Okuma / Yazma | 1-bit (Digital) | Röle çıkışları, motor start sinyali |
| **Input Registers** | 30001 - 39999 | Salt Okunur | 16-bit (Analog) | Sıcaklık, basınç sensör okumaları |
| **Holding Registers**| 40001 - 49999 | Okuma / Yazma | 16-bit (Analog) | PID parametreleri, set değerleri |

---

## PID Kontrol Döngüsü ve Sıcaklık Regülasyonu

Proses endüstrisinde analog büyüklükleri (sıcaklık, akış, basınç, seviye) kararlı tutmak için **PID (Proportional-Integral-Derivative)** kontrol döngüleri kullanılır.

*   **Proportional (Oransal - Kp):** Anlık hatayla orantılı tepki verir. Hatayı hızlı azaltır ancak kalıcı sapma (offset) bırakabilir.
*   **Integral (İntegral - Ki):** Geçmiş hataları toplayarak kalıcı sapmayı yok eder. Aşırı birikmesi "windup" problemine yol açar (anti-windup koruması gerektirir).
*   **Derivative (Türevsel - Kd):** Hatanın değişim hızına bakarak gelecekteki salınımı sönümler.

---

## Klasördeki Araç

*   **[modbus_simulator.py](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/automation-electronics/plc-scada/modbus_simulator.py):** Belirtilen tüm Modbus register tiplerini (Coil, Discrete Input, Input Register, Holding Register) simüle eden; motor ısınmasını kontrol altında tutmak için gerçekçi bir **PID kapalı çevrim sıcaklık regülasyonu** simülasyonu sunan ve limit güvenlik önlemlerini (E-stop trip vb.) içeren interaktif bir PLC CPU simülatörüdür.
