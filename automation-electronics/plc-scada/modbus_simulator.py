import time
import random

class PLCSimulator:
    def __init__(self):
        # Modbus register tables
        # 0xxxx (Coils - Read/Write Bits)
        self.coils = {
            1: False, # Motor Start/Stop
            2: False, # Cooling Valve Open/Close (Manual Mode)
            3: False  # Alarm Buzzer On/Off
        }
        
        # 1xxxx (Discrete Inputs - Read-Only Bits)
        self.discrete_inputs = {
            101: False, # Emergency Stop Button pressed
            102: False  # Overheat Limit Switch tripped
        }
        
        # 3xxxx (Input Registers - Read-Only 16-bit integers/floats)
        self.input_registers = {
            3001: 25.0, # Temperature Sensor (°C)
            3002: 120,  # System Pressure (kPa)
            3003: 0     # Motor Speed (RPM)
        }
        
        # 4xxxx (Holding Registers - Read/Write 16-bit integers)
        self.holding_registers = {
            4001: 75,   # Temperature Setpoint (°C)
            4002: 1500  # Max Motor Speed Limit (RPM)
        }
        
        # PID Variables
        self.pid_active = True # Default PID control enabled
        self.pid_kp = 2.5
        self.pid_ki = 0.4
        self.pid_kd = 1.5
        self.pid_integral = 0.0
        self.pid_prev_error = 0.0
        self.pid_valve_output = 0.0 # 0 to 100%
        
        self.cycle_count = 0

    def print_registers(self):
        print("\n=== PLC MODBUS REGİSTER TABLOSU ===")
        print("\n[COILS (0xxxx) - Bobinler (Okunabilir/Yazılabilir Dijital)]")
        print(f"  0001 - Motor Start/Stop     : {'ON' if self.coils[1] else 'OFF'}")
        print(f"  0002 - Manuel Soğutma Valfi : {'ON' if self.coils[2] else 'OFF'} (PID Aktifken Geçersizdir)")
        print(f"  0003 - Alarm Buzzer         : {'ON' if self.coils[3] else 'OFF'}")
        
        print("\n[DISCRETE INPUTS (1xxxx) - Ayrık Girişler (Salt Okunur Dijital)]")
        print(f"  0101 - Acil Stop Butonu     : {'BASILI' if self.discrete_inputs[101] else 'NORMAL'}")
        print(f"  0102 - Aşırı Isı Sınırı     : {'TRİP' if self.discrete_inputs[102] else 'NORMAL'}")
        
        print("\n[INPUT REGISTERS (3xxxx) - Giriş Kaydedicileri (Salt Okunur Analog)]")
        print(f"  3001 - Sistem Sıcaklığı     : {self.input_registers[3001]:.2f} °C")
        print(f"  3002 - Hat Basıncı          : {self.input_registers[3002]} kPa")
        print(f"  3003 - Motor Hızı           : {self.input_registers[3003]} RPM")
        
        print("\n[HOLDING REGISTERS (4xxxx) - Tutma Kaydedicileri (Okunabilir/Yazılabilir Analog)]")
        print(f"  4001 - Sıcaklık Set Değeri  : {self.holding_registers[4001]} °C")
        print(f"  4002 - Maks. Hız Limiti     : {self.holding_registers[4002]} RPM")
        
        print("\n[PID CONTROL STATUS (Sıcaklık Regülasyonu)]")
        print(f"  PID Modu                    : {'OTOMATİK' if self.pid_active else 'MANUEL'}")
        print(f"  Oransal Soğutma Valfi (CO)  : %{self.pid_valve_output:.1f}")
        print(f"  Hata (PV-SP Error)          : {self.pid_prev_error:.2f} °C")
        print(f"  Kazançlar                   : Kp={self.pid_kp:.1f}, Ki={self.pid_ki:.1f}, Kd={self.pid_kd:.1f}")
        print("====================================")

    def scan_cycle(self):
        """Simulates one PLC scan cycle and physical system behaviors."""
        self.cycle_count += 1
        
        # Check Emergency Stop logic
        if self.discrete_inputs[101]:
            # If Emergency stop is pressed, instantly stop motor and trigger alarm
            self.coils[1] = False
            self.input_registers[3003] = 0
            self.coils[3] = True
            print("\n[ALARM] ACİL STOP BASILI! Motor durduruldu, alarm aktif.")
        
        # Physical system simulation
        # Motor speed logic
        if self.coils[1] and not self.discrete_inputs[101]:
            # Ramp speed up to Max Motor Speed Limit
            target_speed = self.holding_registers[4002]
            current_speed = self.input_registers[3003]
            if current_speed < target_speed:
                self.input_registers[3003] = min(current_speed + 300, target_speed)
        else:
            # Ramp speed down to 0
            current_speed = self.input_registers[3003]
            if current_speed > 0:
                self.input_registers[3003] = max(current_speed - 400, 0)
                
        # Temperature thermodynamics simulation
        temp = self.input_registers[3001]
        motor_speed = self.input_registers[3003]
        
        # Heat generation (motor speed increases temperature)
        if motor_speed > 0:
            temp += (motor_speed / 400.0) + random.uniform(0.1, 0.4)
        else:
            temp -= random.uniform(0.1, 0.3) if temp > 25.0 else 0.0 # natural cooling
            
        # Cooling controller logic
        if self.pid_active:
            # PV: Temp, SP: Setpoint
            error = temp - self.holding_registers[4001]
            
            # Accumulate integral with anti-windup clamping
            self.pid_integral = max(min(self.pid_integral + error, 150.0), -150.0)
            
            # Calculate derivative
            derivative = error - self.pid_prev_error
            self.pid_prev_error = error
            
            # PID Formula
            u = (self.pid_kp * error) + (self.pid_ki * self.pid_integral) + (self.pid_kd * derivative)
            self.pid_valve_output = max(min(u, 100.0), 0.0) # Clamp u(t) to [0, 100]
            
            # 100% opening drops temperature by 4.5 °C per scan cycle
            cooling_effect = (self.pid_valve_output / 100.0) * 4.5
            temp -= cooling_effect
        else:
            # Manual mode
            self.pid_valve_output = 100.0 if self.coils[2] else 0.0
            if self.coils[2]:
                temp -= 4.0 # Static cooling
            self.pid_prev_error = temp - self.holding_registers[4001]
            self.pid_integral = 0.0
            
        # Keep temperature realistic
        temp = max(temp, 20.0)
        self.input_registers[3001] = round(temp, 2)
        
        # Overheat safety limit check (using 85°C as critical safety limit)
        if temp >= 85.0:
            self.discrete_inputs[102] = True
            self.coils[3] = True # Alarm ON
            self.coils[1] = False # Shut off motor
            print(f"\n[ALARM] TEHLİKELİ SICAKLIK (>=85°C) LİMİTİ AŞILDI! Sıcaklık: {temp}°C")
        else:
            self.discrete_inputs[102] = False
            # Alarm automatically goes off if limit clear and e-stop clear
            if not self.discrete_inputs[101] and temp < self.holding_registers[4001]:
                self.coils[3] = False
                
        # Pressure fluctuation simulation
        if motor_speed > 0:
            self.input_registers[3002] = 120 + int(motor_speed / 15) + random.randint(-5, 5)
        else:
            self.input_registers[3002] = 100 + random.randint(-2, 2)

def main():
    plc = PLCSimulator()
    print("PLC Simülatörüne Hoş Geldiniz.")
    while True:
        plc.print_registers()
        print("\nİşlemler:")
        print("1. Bobin Durumu Değiştir (Write Coil - Manuel Mod için)")
        print("2. Set Değeri Değiştir (Write Holding Register)")
        print("3. Acil Stop Butonuna Bas/Bırak")
        print("4. PID Otomatik/Manuel Kontrol Modu Değiştir")
        print("5. PID Kazanç Ayarlarını Güncelle (Kp, Ki, Kd)")
        print("6. Sistem Döngüsünü Çalıştır (1 Çevrim - Scan Cycle)")
        print("7. Sürekli Çalıştır (Gerçek Zamanlı Simülasyon)")
        print("0. Geri Dön")
        
        secim = input("\nSeçiminiz: ").strip()
        
        if secim == '1':
            try:
                addr = int(input("Bobin Adresi (1: Motor, 2: Manuel Soğutma Valfi): "))
                if addr not in [1, 2]:
                    print("Hatalı adres!")
                    continue
                val = input("Değer (1/0 veya True/False): ").strip().upper()
                plc.coils[addr] = val in ['1', 'TRUE', 'T', 'ON']
                print("[BAŞARILI] Bobin yazıldı.")
            except ValueError:
                print("Lütfen sayısal bir adres girin.")
                
        elif secim == '2':
            try:
                addr = int(input("Register Adresi (4001: Sıcaklık Set, 4002: Maks Hız): "))
                if addr not in [4001, 4002]:
                    print("Hatalı adres!")
                    continue
                val = int(input("Değer: "))
                plc.holding_registers[addr] = val
                print("[BAŞARILI] Holding register yazıldı.")
            except ValueError:
                print("Lütfen sayısal bir değer girin.")
                
        elif secim == '3':
            plc.discrete_inputs[101] = not plc.discrete_inputs[101]
            print(f"\n[BİLGİ] Acil Stop butonu durumu değiştirildi: {'BASILI' if plc.discrete_inputs[101] else 'SERBEST'}")
            plc.scan_cycle()
            
        elif secim == '4':
            plc.pid_active = not plc.pid_active
            print(f"\n[BİLGİ] Sıcaklık regülasyon modu değiştirildi: {'OTOMATİK (PID)' if plc.pid_active else 'MANUEL (Coil 2)'}")
            
        elif secim == '5':
            try:
                kp = float(input(f"Oransal Kazanç (Kp) [Şu an: {plc.pid_kp}]: ") or plc.pid_kp)
                ki = float(input(f"İntegral Kazanç (Ki) [Şu an: {plc.pid_ki}]: ") or plc.pid_ki)
                kd = float(input(f"Türevsel Kazanç (Kd) [Şu an: {plc.pid_kd}]: ") or plc.pid_kd)
                plc.pid_kp, plc.pid_ki, plc.pid_kd = kp, ki, kd
                print("[BAŞARILI] PID katsayıları güncellendi.")
            except ValueError:
                print("[HATA] Geçersiz katsayı değeri.")
                
        elif secim == '6':
            print("\nScan Cycle tetiklendi...")
            plc.scan_cycle()
            
        elif secim == '7':
            print("\nReal-time Simülasyon başladı. Durdurmak için Ctrl+C'ye basın...")
            try:
                while True:
                    plc.scan_cycle()
                    plc.print_registers()
                    time.sleep(1.5)
            except KeyboardInterrupt:
                print("\nSimülasyon durduruldu.")
                
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
            
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
